import requests
query = input("Enter any domain to get the latest news: ")
api = "" # paste your api key
url = f"https://newsapi.org/v2/top-headlines?country=us&category={query}&apiKey={api}"
print(url)
r = requests.get(url)
data = r.json()
# with open("News_API/news.txt", "w") as f:
#     f.write(str(data))
print(data.get("totalResults"))
articles = data["articles"]
for index, article in enumerate(articles, start=1):
    print(f"{index}. {article["title"]}")
    print(article["author"])
    print(article.get("url")) # article.get("url")
    # Safer version
    author = article.get("description", "Anonymous") # Returns 'Anonymous' if missing
    print(author)
    print("******************************************")
