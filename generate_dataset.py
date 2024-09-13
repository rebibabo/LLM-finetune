import jieba
import json
from openai import OpenAI
from typing import List, Literal, Tuple
from rouge_chinese import Rouge
from loguru import logger
from html_splitter import HTMLSplitter
from prompt import controdictary_prompt, non_annotated_prompt

class Generator:
    client = OpenAI()
    rouge = Rouge()
    Q_ref: List[str] = []
    A_ref: List[str] = []
    QA_pairs: List[Tuple[str, str]] = []

    def __init__(self, 
        model_name: str = 'gpt-4o-mini-2024-07-18', 
        rouge_type: Literal['rouge-1', 'rouge-2', 'rouge-l'] = 'rouge-l',
        rouge_metric: Literal['f', 'p', 'r'] ='r',
        min_rouge_score: int = 0.7,
        max_tokens: int = 2000,
        temperature: float = 1.2,
        top_p: float = 1,
        seed: int = 42
    ):
        self.model = model_name
        self.seed = seed
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.rouge_type = rouge_type
        self.rouge_metric = rouge_metric
        self.min_rouge_score = min_rouge_score

    def _repetitive(self, hypothesis: str, reference: str) -> bool:
        scores = self.rouge.get_scores(hypothesis, reference)
        score = scores[0][self.rouge_type][self.rouge_metric]
        return score > self.min_rouge_score, score

    def _insert(self, question: str, answer: str) -> int:
        q_hyp = ' '.join(jieba.cut(question))
        a_hyp = ' '.join(jieba.cut(answer))
        for i, (q_ref, a_ref) in enumerate(zip(self.Q_ref, self.A_ref)):
            q_rep, q_score = self._repetitive(q_hyp, q_ref)
            a_rep, a_score = self._repetitive(a_hyp, a_ref)
            if q_rep and a_rep:
                logger.warning(f"Two QAs are repetitive, q_score: {q_score:.4f}, a_score: {a_score:.4f}")
                if a_rep > 0.9:
                    response = self.query(controdictary_prompt.format(q1=question, q2=self.QA_pairs[i][0]))
                    if not response.isdigit():
                        logger.warning(f"Invalid response: {response}")
                        return 0
                    score = int(response)
                    if score >= 70:
                        logger.warning(f"Two questions are controdictary")
                        del self.Q_ref[i]
                        del self.A_ref[i]
                        del self.QA_pairs[i]
                return 0
            elif q_rep and not a_rep:
                logger.warning(f"One Q is repetitive, q_score: {q_score:.4f}, a_score: {a_score:.4f}")
                del self.Q_ref[i]
                del self.A_ref[i]
                del self.QA_pairs[i]
                return 0
        self.Q_ref.append(q_hyp)
        self.A_ref.append(a_hyp)
        self.QA_pairs.append((question, answer))
        return 1
        
    def query(self, 
        user_input: str, 
        system_prompt: str = '', 
    ) -> str:

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=self.max_tokens,  
            temperature=self.temperature,
            seed=self.seed,
        )

        return completion.choices[0].message.content
    
    def generate(self, 
        non_annatated_data: List[str], 
        times: int = 3, 
        save_path: str = 'output.jsonl'
    ):
        with open(save_path, 'w', encoding='utf-8') as f:
            for paragraph in non_annatated_data:
                for _ in range(times):
                    response = self.query(non_annotated_prompt.format(paragraph=paragraph))
                    QA = self.parse_response(response)
                    for q, a in QA:
                        if self._insert(q, a):
                            logger.info(f"Question: {q}")
                            logger.info(f"Answer: {a}")
                            if '#question' in q or '#answer' in a:
                                logger.warning(f"Invalid question or answer: {q}, {a}")
                                continue
                            lines = q.split('\n')
                            if len(lines) > 1:
                                instruction = lines[0]
                                input_ = '\n'.join(lines[1:])
                            else:
                                instruction = q
                                input_ = ''
                            f.write(json.dumps({'instruction': instruction, 'input': input_,'output': a}, ) + '\n')
                            f.flush()
        
    def parse_response(self, response: str) -> Tuple[str, str]:
        QA = []
        lines = response.split('\n')
        i = 0

        while i < len(lines):
            if lines[i].startswith('#question'):
                question = ':'.join(lines[i].split(':')[1:]).strip()
                while i + 1 < len(lines) and not lines[i + 1].startswith('#answer'):
                    i += 1
                    question += '\n' + lines[i]
                i += 1
                if i >= len(lines):
                    break
                answer = ':'.join(lines[i].split(':')[1:]).strip()
                while i + 1 < len(lines) and not lines[i + 1].startswith('#question'):
                    i += 1
                    answer += '\n' + lines[i]
                QA.append((question, answer))
            i += 1

        return QA

    
if __name__ == '__main__':
    html_splitter = HTMLSplitter.from_md("pep")
    non_annatated_data = html_splitter.split()
    generator = Generator()
    generator.generate(non_annatated_data)