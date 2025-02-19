import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def get_chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    user_input = input("Enter your question or prompt: ")
    response = get_chatgpt_response(user_input)
    print("ChatGPT response:", response)

if __name__ == "__main__":
    main()