import google.generativeai as genai
genai.configure(api_key="AIzaSyAVQdTdlkT9iN6egZR2bAU6r8pm-7P_fx0")
model = genai.GenerativeModel('gemini-2.0-flash')
chat_history = []
while True:
    q = input("you: ")
    chat_history.append(f"user: {q}")
    prompt = "\n".join(chat_history) + "\nAI:"
    response = model.generate_content(prompt)
    chat_history.append(f"AI:{response.text}")
    print(f"AI: {response.text}")
    if q.lower() == "exit":
        break