import os
import openai

def generate_llm_feedback(text, role):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"You're a resume reviewer. Provide feedback for the following resume content for the role of {role}:\n\n{text}\n\nBe concise and professional."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"LLM feedback not available: {e}"
