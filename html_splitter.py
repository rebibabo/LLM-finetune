import os
import requests
import html2text
from tqdm import tqdm
from loguru import logger
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter

urls = [
    "https://peps.python.org/pep-0008/",
    "https://peps.python.org/pep-0257/",
    "https://peps.python.org/pep-0484/",
]

class HTMLSplitter:
    filenames = []
    htmls = []
    mds = []
    splits = []

    def __init__(self, 
        chunk_size: int = 256,
        chunk_overlap: int = 20,
        paragraph_separator: str = '\n\n'
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.paragraph_separator = paragraph_separator

    @ staticmethod
    def from_url(*urls):
        htmlsplitter = HTMLSplitter()
        for url in urls:
            logger.info(f'Downloading html from {url}')
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                logger.error(f'Failed to download {url}: {e}')
                continue
            html_text = response.content.decode('utf-8')
            htmlsplitter.htmls.append(html_text)
            url = url[:-1] if url.endswith('/') else url
            filename = os.path.basename(url)
            htmlsplitter.filenames.append(filename)
            logger.success(f'Downloaded {filename}')
        return htmlsplitter

    @ staticmethod
    def from_html(html_dir):
        htmlsplitter = HTMLSplitter()
        for file in os.listdir(html_dir):
            if not file.endswith('.html'):
                continue
            file_path = os.path.join(html_dir, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                logger.info(f'Reading html from {file_path}')
                html_text = file.read()
                htmlsplitter.htmls.append(html_text)
                filename = os.path.basename(file_path.replace('.html', ''))
                htmlsplitter.filenames.append(filename)
        return htmlsplitter

    @ staticmethod
    def from_md(md_dir):
        htmlsplitter = HTMLSplitter()
        for file in os.listdir(md_dir):
            if not file.endswith('.md'):
                continue
            file_path = os.path.join(md_dir, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                logger.info(f'Reading md from {file_path}')
                md_text = file.read()
                htmlsplitter.mds.append(md_text)
                filename = os.path.basename(file_path.replace('.md', ''))
                htmlsplitter.filenames.append(filename)
        return htmlsplitter

    def convert_to_md(self):
        for html_text in tqdm(self.htmls, desc='Converting to md'):
            self.mds.append(html2text.html2text(html_text))
        logger.success('Successfully converted to md')

    def save(self, save_dir):
        if not os.path.exists(save_dir):
            logger.info(f'Creating directory {save_dir}')
            os.makedirs(save_dir)
        for i in range(len(self.htmls)):
            with open(os.path.join(save_dir, f'{self.filenames[i]}.html'), 'w', encoding='utf-8') as file:
                file.write(self.htmls[i])
        for i in range(len(self.mds)):
            with open(os.path.join(save_dir, f'{self.filenames[i]}.md'), 'w', encoding='utf-8') as file:
                file.write(self.mds[i])
        logger.success(f'Saved to {save_dir}')

    def split(self):
        node_parser = SentenceSplitter(chunk_size=self.chunk_size, 
                                       chunk_overlap=self.chunk_overlap, 
                                       paragraph_separator=self.paragraph_separator)

        for md in tqdm(self.mds, desc='Splitting md'):
            nodes = node_parser.get_nodes_from_documents(
                [Document(text=md)]
            )

            self.splits.extend([node.text for node in nodes])
        return self.splits

if __name__ == '__main__':
    html_splitter = HTMLSplitter.from_md("pep")
    print(len(html_splitter.split()))  
