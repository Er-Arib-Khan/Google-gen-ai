from serpapi import GoogleSearch
params = {
    "q": "python programming",
    "hl": "en",
    "gl": "us",
    "tbm": "nws",
    "api_key": "108e482531c540efdb6a1dff9a2b45b196a676c3f6dd1f1b7b498f96ab48844a",
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results.get("news_results", []):
    print(f"Title: {result.get('title')}")
    print(f"Link: {result.get('link')}")
    print(f"Time: {result.get('published_date', 'N/A')}\n")
          