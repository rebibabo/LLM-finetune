echo 'export HF_HOME="/root/autodl-tmp/huggingface"' >> ~/.bashrc
source ~/.bashrc
pip install --upgrade pip
pip install python-dotenv
pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"