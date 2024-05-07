import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_gpt(user_input)
        print("Chatbot:", response)
