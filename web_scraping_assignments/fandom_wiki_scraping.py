import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os

url= "https://halloweenspecials.fandom.com/wiki/List_of_Halloween_television_episodes"
response= requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')

tables=soup.find_all('table', class_='wikitable')
data = []
for table in tables:
    headers=[header.text.strip() for header in table.find_all('td')]
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if cells:
            data.append([cell.get_text(strip=True) for cell in cells])

df = pd.DataFrame(data)

# Define the current working directory
cwd = os.getcwd()

# Save the DataFrame to the CSV file in the current directory
csv_filename = 'halloween_episodes.csv'
csv_path = os.path.join(cwd, csv_filename)
# Print the path to the CSV file
print(f"CSV file saved at: {csv_path}")
df.to_csv(csv_path, index=False)

# Print the path to the CSV file
print(f"CSV file saved at: {csv_path}")