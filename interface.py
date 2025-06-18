from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def main():
    print("🤖 Welcome to Q&A Bot (FLAN-T5)! Type '/exit' to quit.")
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=100,
            do_sample=False
        )

        reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Bot: {reply.strip()}")

if __name__ == "__main__":
    main()
