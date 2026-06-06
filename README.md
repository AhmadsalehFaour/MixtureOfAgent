# 🧠 MoA: Mixture of Agents

<p align="center">
  <img src="https://img.shields.io/badge/AI-Mixture_of_Agents-blue?style=for-the-badge&logo=openai" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Models-HuggingFace-orange?style=for-the-badge&logo=huggingface" />
  <img src="https://img.shields.io/badge/Docker-Ready-green?style=for-the-badge&logo=docker" />
</p>

---
<img width="2816" height="1536" alt="Gemini_Generated_Image_1tnwh51tnwh51tnw" src="https://github.com/user-attachments/assets/13c9faa4-8853-4854-b9fd-e25e72769217" />

## 🎯 Project Idea

**MoA (Mixture of Agents)** is an application that combines multiple AI models (Proposers & Aggregator) to generate a unified, more accurate response.  
Users can enter any question, receive two answers from different models, and then the **Aggregator agent** merges them into a simplified final answer.

---

## 📊 Why is this field important?

```
  +----------------------+       +----------------------+
  |   🤖 Proposer 1      |       |   🤖 Proposer 2      |
  | (LLM / Transformer)  |       | (LLM / Seq2Seq)      |
  +----------+-----------+       +-----------+----------+
             |                           |
             +------------+--------------+
                          |
                  🔀 Aggregator Agent
                          |
                 ✅ Final Unified Response
```

- 🧩 **Model integration**: leverage the strengths of each model.  
- 📚 **More accurate answers**: reduce bias and mistakes from a single model.  
- 👨‍👩‍👧‍👦 **Accessible to everyone**: outputs are simplified, even for kids.  
- 🚀 **High flexibility**: supports both local (Ollama) and remote (HuggingFace) execution.  

---

## ⚙️ Core Components

- **`main.py`**: Streamlit-powered interactive UI.  
- **`logic.py`**: Logic for generating and aggregating answers.  
- **`utils.py`**: Logging and prompt saving.  
- **`models.py`**: Load models (local & remote).  
- **`docker-compose.yml` + `Dockerfile`**: Run the project in containers.  
- **`.env`**: Environment variables (e.g., HF_TOKEN).  
- **`requirements.txt`**: Dependencies (Torch, Transformers, Streamlit).  
- **`FUTURE_ENHANCEMENTS.md`**: Roadmap for upcoming features.  

---

## 🚀 Getting Started

### 1️⃣ Run locally
```bash
git clone https://github.com/AhmadsalehFaour/moa.git
cd moa
pip install -r requirements.txt
streamlit run main.py
```

### 2️⃣ Run with Docker
```bash
docker-compose up --build
```

---

## 🌍 Modes

- 🛰️ **Remote Mode** → Cloud models (Falcon, Flan-T5).  
- 💻 **Local Mode** → Local Ollama models (llama3, qwen, deepseek).  


---

## 🧮 Future Roadmap

- Support **LangChain** and **RAG** for external knowledge.  
- **Multilingual interface**.  
- Export sessions to **CSV / JSON**.  
- Deployment to **HuggingFace Spaces**.  

---

## 👨‍💻 Contributors

- **Mixture of Agents** development team.  
- Open contributions from the community via Pull Requests.  

---

## 📜 License

This project is open-source under the **MIT License**.
