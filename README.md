# 🤖 Q&A CLI Chatbot using google/flan-t5-base

This is a simple Command Line Interface (CLI) chatbot built using Hugging Face's `google/flan-t5-base` model. The chatbot is designed for **single-turn factual question answering**, ideal for lightweight environments with CPU support.

---

## 🚀 Features

- 💬 Responds to factual questions (e.g., capital cities, math, general knowledge)
- ✅ Uses `transformers` library and runs locally
- 🧠 Powered by instruction-tuned model `google/flan-t5-base`
- 💻 Works efficiently even on machines without GPU
- 🔒 No internet required after first-time model download

---

## 🧠 Model Details

- **Model:** [`google/flan-t5-base`](https://huggingface.co/google/flan-t5-base)
- **Type:** Sequence-to-sequence model tuned for instructions and tasks
- **Memory:** ❌ No multi-turn memory (each question is answered independently)
- **Speed:** ✅ Fast and CPU-friendly

---

## 📦 Requirements

Install dependencies (if not already):

```bash
pip install transformers torch
