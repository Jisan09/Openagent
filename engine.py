import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = "Your API key"

def openagent(engine: int, prompt: str):
    data = SimpleDirectoryReader(input_dir=f"./data/chapter{engine}/").load_data()
    index = VectorStoreIndex.from_documents(data)
    chat_engine = index.as_chat_engine(chat_mode='react', verbose=True)
    chat_engine.chat(prompt)

engine = input("Enter the engine number: ") or 2
prompt = input("Enter the prompt: ") or "what did jisan said"

openagent(engine, prompt)