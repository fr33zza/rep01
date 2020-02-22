#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

main_url = "https://pl.wikipedia.org/wiki/Dupa_biskupa"
req = requests.get(main_url)
soup = BeautifulSoup(req.text, "html.parser")

# Finding the main title tag.
title = soup.find("h1", class_ = "firstHeading")
print (title.get_text())

# Finding the mid-titles tags and storing them in a list.
mid_titles = [tag.get_text() for tag in soup.find_all("span", class_ = "mw-headline")]

# Now using css selectors to retrieve the article shortcut links
links_tags = soup.select("li.toclevel-1")
for tag in links_tags:
    print (tag.a.get("href"))

# Retrieving the side page links by "blocks" and storing them in a dictionary
side_page_blocks = soup.find("div",
                            id = "mw-panel").find_all("div",
                                                      class_ = "portal")
blocks_links = {}
for num, block in enumerate(side_page_blocks):
    blocks_links[num] = [link.get("href") for link in block.find_all("a", href = True)]

print (blocks_links[0])

