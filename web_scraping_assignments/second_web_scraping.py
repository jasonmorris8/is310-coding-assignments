from bs4 import BeautifulSoup
import requests
response = requests.get("https://lotr.fandom.com/wiki/Main_Page")
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
response = requests.get("https://lotr.fandom.com/wiki/Main_Page", timeout=5)
import time

start = time.time()
response = requests.get("https://lotr.fandom.com/wiki/Main_Page")
end = time.time()
print(end - start)
response = requests.get("https://lotr.fandom.com/wiki/Category:Canon_characters_in_The_Rings_of_Power")
soup = BeautifulSoup(response.text, "html.parser")
characters = soup.find_all('a', class_='category-page__member-link')

for character in characters:
	print(character.get_text())
import re

response = requests.get("https://lotr.fandom.com/wiki/Galadriel")
soup = BeautifulSoup(response.text, "html.parser")
languages = soup.find_all('a', attrs={'data-tracking-label': re.compile(r'lang-')})
for language in languages:
	print(language.get('data-tracking-label'))
	print(language.get_text())
import csv
def get_character_languages(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	languages = soup.find_all('a', attrs={'data-tracking-label': re.compile(r'lang-')})
	return [{"language": language.get('data-tracking-label'), "language_name": language.get_text()} for language in languages]

response = requests.get("https://lotr.fandom.com/wiki/Category:Canon_characters_in_The_Rings_of_Power")

soup = BeautifulSoup(response.text, "html.parser")
canon_characters = soup.find_all('a', class_='category-page__member-link')

canon_characters_data = []

for character in canon_characters:
	character_data = {"character": character.get_text(), "character_link": character.get('href')}
	character_data['languages'] = get_character_languages("https://lotr.fandom.com" + character_data['character_link'])
	character_data['langauges_count'] = len(character_data['languages'])
	canon_characters_data.append(character_data)

with open('lotr_canon_characters.csv', 'w') as file:
	writer = csv.writer(file)
	writer.writerow(['character', 'character_link', 'languages', 'languages_count'])
	for character in canon_characters_data:
		writer.writerow([character['character'], character['character_link'], character['languages'], character['langauges_count']])
import re
import requests
from bs4 import BeautifulSoup
import rich
from rich.console import Console
from rich.table import Table

console = Console()

def get_character_languages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    languages = soup.find_all('a', attrs={'data-tracking-label': re.compile(r'lang-')})
    return [{"language": language.get('data-tracking-label'), "language_name": language.get_text()} for language in languages]

def fetch_characters(url, category):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    characters = soup.find_all('a', class_='category-page__member-link')
    characters_data = []

    for character in characters:
        console.print(f"Processing {character.get_text()}...")
        character_data = {
            "character": character.get_text(),
            "character_link": character.get('href'),
            "category": category
        }
        character_data['languages'] = get_character_languages("https://lotr.fandom.com" + character_data['character_link'])
        character_data['languages_count'] = len(character_data['languages'])
        characters_data.append(character_data)
    
    return characters_data
# Fetch characters from the given URLs
canon_characters_data = fetch_characters("https://lotr.fandom.com/wiki/Category:Canon_characters_in_The_Rings_of_Power", "Canon")
new_characters_data = fetch_characters("https://lotr.fandom.com/wiki/Category:Characters_created_for_The_Rings_of_Power", "New")

# Combine and sort characters by language count
all_characters_data = canon_characters_data + new_characters_data
sorted_characters = sorted(all_characters_data, key=lambda x: x['languages_count'], reverse=True)

# Display the sorted characters in a table
table = Table(title="Translations of LOTR Canon Characters VS New Characters")
table.add_column("Character", style="cyan")
table.add_column("Language Count", style="magenta")
table.add_column("Category", style="green")

for character in sorted_characters:
    table.add_row(character['character'], str(character['languages_count']), character['category'])

console.print(table)