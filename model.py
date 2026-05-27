from transformers import pipeline

# Use a supported task
chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

def get_response(prompt):
    try:
        result = chatbot(
            prompt,
            max_length=100,
            num_return_sequences=1
        )
        return result[0]["generated_text"]

    except Exception as e:
        return f"Error: {str(e)}"