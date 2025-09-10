import torch
import requests
import os
from dotenv import load_dotenv
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost:11434")

def load_remote_model(model_id, model_type, use_gpu=True):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    if model_type == "causal":
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto" if use_gpu else {"": "cpu"},
            torch_dtype=torch.float16 if use_gpu and torch.cuda.is_available() else torch.float32
        )
    else:
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_id,
            device_map="auto" if use_gpu else {"": "cpu"}
        )
    return pipeline("text-generation" if model_type == "causal" else "text2text-generation",
                    model=model, tokenizer=tokenizer, max_new_tokens=128)

def load_ollama_pipeline(model_name):
    def ollama_pipeline(prompt):
        try:
            response = requests.post(
                f"http://{OLLAMA_HOST}/api/generate",
                json={"model": model_name, "prompt": prompt, "stream": False},
                timeout=20
            )
            response.raise_for_status()
            return [{"generated_text": response.json().get("response", "[No Response]")}]
        except requests.exceptions.RequestException as e:
            return [{"generated_text": f"[Local Model Error: {model_name}] {str(e)}"}]
    return ollama_pipeline

def load_models(mode="remote", local_models=("llama3.1:8b", "qwen2.5:7b", "gemma3:4b")):
    if mode == "local":
        proposer1 = load_ollama_pipeline(local_models[0])
        proposer2 = load_ollama_pipeline(local_models[1])
        aggregator = load_ollama_pipeline(local_models[2])
    else:
        proposer1 = load_remote_model("tiiuae/falcon-rw-1b", "causal", use_gpu=True)
        proposer2 = load_remote_model("google/flan-t5-base", "seq2seq", use_gpu=False)
        aggregator = load_remote_model("google/flan-t5-base", "seq2seq", use_gpu=False)
    return proposer1, proposer2, aggregator, {
        "p1": local_models[0] if mode=="local" else "tiiuae/falcon-rw-1b",
        "p2": local_models[1] if mode=="local" else "google/flan-t5-base",
        "agg": local_models[2] if mode=="local" else "google/flan-t5-base"
    }