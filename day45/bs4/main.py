from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# h3_heading = soup.find("h3", class_="heading")
# print(h3_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.select_one(".titleline title"))