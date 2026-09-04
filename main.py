import html
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

emp_web_page = response.text
soup = BeautifulSoup(emp_web_page, 'html.parser')

titles = [
    html.unescape(
        title.getText().split(")")[-1]
        if ")" in title.getText()
        else title.getText().split(":")[-1]
    )
    for title in soup.find_all(name='h3', class_='title')][::-1]
n_count = [html.unescape(title.getText().split(")")[0] if ")" in title.getText() else title.getText().split(":")[0])
           for title in soup.find_all(name='h3', class_='title')][::-1]
with open("movies.txt", "w", encoding="utf-8") as file:
    for i in range(len(n_count)):
        file.write(f"{n_count[i]}. {titles[i]}\n")
