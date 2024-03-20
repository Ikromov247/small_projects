from bs4 import BeautifulSoup
import requests

link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=link).text
soup = BeautifulSoup(response, "html.parser")

all_h3s = soup.find_all("h3", class_="title")
all_titles = [title.getText() for title in all_h3s][::-1]

titles = "\n".join(all_titles)
with open("movies.txt", "w", encoding="utf-8") as f:
    f.write(titles)