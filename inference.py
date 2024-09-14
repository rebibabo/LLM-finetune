from dotenv import load_dotenv
load_dotenv()
from unsloth import FastLanguageModel
import json

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

