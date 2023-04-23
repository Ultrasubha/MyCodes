import requests
from bs4 import BeautifulSoup
#import json
import csv

# Function to scrape links to YouTube channels from search results
def get_youtube_links(query, num_results):
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    search_results = soup.select(".tF2Cxc")

    links = []
    for result in search_results:
        link = result.select_one("a")["href"]
        if "youtube.com/channel/" in link:
            links.append(link)

    return links

# Call the function to get the links
query = "site:youtube.com openinapp.co"
num_results = 10000
links = get_youtube_links(query, num_results)

# Save the links in JSON format
#with open("youtube_links.json", "w") as f:
    #json.dump(links, f)

# Save the links in CSV format
with open("youtube_links.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for link in links:
        writer.writerow([link])

