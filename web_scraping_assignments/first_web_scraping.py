from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
links = soup.find_all('a')
for link in links:
	print(link.get('href'))
	print(link.get_text())
links = soup.find_all('a', class_='sister')
link = soup.find_all('a', id='link1')
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
	print(paragraph.get_text())
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
	print(paragraph.name)
	print(paragraph.attrs)
	paragraphs = soup.find_all('p')
for paragraph in paragraphs:
	print(paragraph.get('class'))
	print(paragraph['class'])
	paragraphs = soup.find_all('p')
for paragraph in paragraphs:
	print(paragraph.next_sibling)
	paragraphs = soup.find_all('p')
for paragraph in paragraphs:
	print(paragraph.parent)
	from bs4 import BeautifulSoup
soup = BeautifulSoup(open("top_100_ebooks.html"), features="html.parser")

print(soup.prettify())
titles = soup.find_all('li')
for title in titles:
	print(title.get_text())
from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.gutenberg.org/browse/scores/top")
print("Status code:", response.status_code)
print("Headers:",response.headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
response = requests.get("https://www.gutenberg.org/browse/scores/top")
soup = BeautifulSoup(response.text, "html.parser")
top_100_ebooks = soup.find(id="books-last1")
list_of_books = top_100_ebooks.find_next('ol').find_all('li')
for book in list_of_books:
	print(book.get_text())
response = requests.get("https://www.gutenberg.org/browse/scores/top")
soup = BeautifulSoup(response.text, "html.parser")
top_lists = soup.find_all("h2")

data = []
for top_list in top_lists:
	top_list_name = top_list.get_text()
	top_list_items = top_list.find_next('ol').find_all('li')
	for item in top_list_items:
		data.append({"list": top_list_name, "title": item.get_text()})
response = requests.get("https://www.gutenberg.org/browse/scores/top")
soup = BeautifulSoup(response.text, "html.parser")
top_lists = soup.find_all("h2")

books = []
authors = []

for top_list in top_lists:
	top_list_name = top_list.get_text()
	top_list_items = top_list.find_next('ol').find_all('li')
	for item in top_list_items:
		if "EBooks" in top_list_name:
			books.append({"list": top_list_name, "title": item.get_text()})
		else:
			authors.append({"list": top_list_name, "author": item.get_text()})
			response = requests.get("https://www.gutenberg.org/browse/scores/top")
soup = BeautifulSoup(response.text, "html.parser")
top_lists = soup.find_all("h2")

books = []
authors = []

for top_list in top_lists:
	top_list_name = top_list.get_text()
	top_list_items = top_list.find_next('ol').find_all('li')
	for item in top_list_items:
		if "EBooks" in top_list_name:
			books.append({"top_list": top_list_name, "book_title": item.get_text(), "book_link": item.find('a').get('href')})
		else:
			authors.append({"top_list": top_list_name, "author_name": item.get_text(), "author_link": item.find('a').get('href')})

import csv

with open('top_100_ebooks.csv', 'w') as file:
	writer = csv.writer(file)
	# Write the headers
	writer.writerow(['top_list', 'book_title', 'book_link'])
	for book in books:
		writer.writerow([book['top_list'], book['book_title'], book['book_link']])

with open('top_100_authors.csv', 'w') as file:
	writer = csv.writer(file)
	# Write the headers
	writer.writerow(['top_list', 'author_name', 'author_link'])
	for author in authors:
		writer.writerow([author['top_list'], author['author_name'], author['author_link']])
def check_page_exists(url):
	response = requests.get(url)
	if response.status_code == 200:
		return True
	else:
		return False
import requests
import csv
from bs4 import BeautifulSoup

# Ensure books and authors lists are initialized
books = []
authors = []

# Assuming top_list and top_list_name are defined earlier in the code
top_list_items = top_list.find_next('ol').find_all('li')
for item in top_list_items:
    if "EBooks" in top_list_name:
        books.append({"top_list": top_list_name, "book_title": item.get_text(), "book_link": item.find('a').get('href')})
    else:
        authors.append({"top_list": top_list_name, "author_name": item.get_text(), "author_link": item.find('a').get('href')})

# Write books to CSV
with open('top_100_ebooks.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['top_list', 'book_title', 'book_link'])
    for book in books:
        writer.writerow([book['top_list'], book['book_title'], book['book_link']])

# Write authors to CSV
with open('top_100_authors.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['top_list', 'author_name', 'author_link'])
    for author in authors:
        writer.writerow([author['top_list'], author['author_name'], author['author_link']])

# Function to check if a page exists
def check_page_exists(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False
for book in books:
	book['webpage_exists'] = check_page_exists(book['book_link'])

for author in authors:
	author['webpage_exists'] = check_page_exists(author['author_link'])
def check_gutenberg_page_exists(url):
	gutenberg_url = "https://www.gutenberg.org" + url
	response = requests.get(gutenberg_url)
	if response.status_code == 200:
		return True
	else:
		return False

response = requests.get("https://lotr.fandom.com/wiki/Main_Page")
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")