from dotenv import load_dotenv
load_dotenv()
from unsloth import FastLanguageModel

max_seq_length = 2048 # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "lora_model", # YOUR MODEL YOU USED FOR TRAINING
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

from transformers import TextStreamer
def query(user_input):
    FastLanguageModel.for_inference(model) # Enable native 2x faster inference
    inputs = tokenizer(
    [
        alpaca_prompt.format(
            user_input, # instruction
            "", # input
            "", # output - leave this blank for generation!
        )
    ], return_tensors = "pt").to("cuda")

    text_streamer = TextStreamer(tokenizer)
    _ = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 2048)

query(
'''
Please help me change the following code style strictly accoording to the PEP 8 standard. :
class Solution:
    def intToRoman(self, num: int) -> str:
        thousand = {1:'M', 2:'MM', 3:'MMM'}
        hundred = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
        ten = {1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
        one = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        res = ''
        if num // 1000 != 0:
            res += thousand[num // 1000]
            num %= 1000
        if num // 100 != 0:
            res += hundred[num // 100]
            num %= 100
        if num // 10 != 0:
            res += ten[num // 10]
            num %= 10
        if num != 0:
            res += one[num]
        return res
'''
)