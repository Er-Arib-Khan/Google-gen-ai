from serpapi import GoogleSearch
import google.generativeai as genai
genai.configure(api_key="AIzaSyAVQdTdlkT9iN6egZR2bAU6r8pm-7P_fx0")
model = genai.GenerativeModel('gemini-2.0-flash')
SERPAPIAPI_KEY = "108e482531c540efdb6a1dff9a2b45b196a676c3f6dd1f1b7b498f96ab48844a"

def google_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPIAPI_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    # Return snippet if available, else the full results.
    return results.get("snippet", str(results))

def chat_with_gemini(query):
    search_result = google_search(query)
    prompt = f"""I searched google for '{query}' and found the following information:
{search_result}
Based on this, please give me a concise and to the point answer."""
    response = model.generate_content(prompt)
    return response.text

print(chat_with_gemini("what is the current population of the world"))
