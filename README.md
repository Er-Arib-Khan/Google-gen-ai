🧠 Generative AI with Python — Google Meets ChatGPT (Mini Version)
In just one day, I built a Python-powered AI project that combines creativity, memory, and real-time web capabilities — like a mini version of Google meets ChatGPT. Here's what it can do:

🚀 Features
✍️ AI-Generated Poetry

The AI generates creative and seasonal poems using OpenAI's language model.

Example: A beautiful summer poem generated entirely by Python code.

🔁 Chat Memory (Context Retention)

Integrated a memory system that allows the AI to remember previous interactions.

Makes the conversation feel more human and consistent, like chatting with a smart friend who never forgets.

🌐 Real-Time Google Search

Using SerpAPI, the app fetches live search results including titles and URLs.

One-click access to real pages — similar to how Google search works, but integrated with AI chat.

📊 Live Data Access via APIs

Makes real-time API calls to get live data, like the current world population or other public info.

Answers with instant, updated information.

🛠️ Tech Stack
Python

OpenAI API (ChatGPT / GPT model)

SerpAPI (for real-time search)

Flask / Streamlit (optional, for interface)

Requests (for live data APIs)

📁 Project Structure
bash
Copy
Edit
/generative-ai-chat
│
├── poetry_generator.py
├── memory_chatbot.py
├── real_time_search.py
├── live_data_fetcher.py
├── requirements.txt
└── README.md
🧪 How to Run
Clone this repo:

bash
Copy
Edit
git clone https://github.com/your-username/generative-ai-chat.git
cd generative-ai-chat
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API keys (OpenAI & SerpAPI).

Run each script as needed:

bash
Copy
Edit
python poetry_generator.py
python memory_chatbot.py
python real_time_search.py
python live_data_fetcher.py
🔑 API Keys Required
OpenAI API Key

SerpAPI Key

📌 Highlights
This project combines:

Natural Language Generation (NLG)

Conversational Memory

Real-Time Search and Info Retrieval

External API Integration

📚 Future Enhancements
Voice-based interaction

GUI using Streamlit or Flask

PDF or image summarization
