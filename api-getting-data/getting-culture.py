import requests
import csv
import pyeuropeana.apis as apis
import os
import apikey
# Make a GET request to SWAPI to fetch character data
response = requests.get('https://swapi.dev/api/people/5/')
data = response.json()

# Extract the character results
results = [data]

# Define the CSV file path
#csv_file = '/path/to/your/csv/file.csv'
cwd = os.getcwd()
csv_file = os.path.join(cwd, 'starwars.csv')
# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Name', 'Height', 'Mass', 'Hair Color', 'Skin Color', 'Eye Color', 'Birth Year', 'Gender'])

    # Iterate over each character and write their data to the CSV file
    for character in results:
        writer.writerow([
            character['name'],
            character['height'],
            character['mass'],
            character['hair_color'],
            character['skin_color'],
            character['eye_color'],
            character['birth_year'],
            character['gender']
        ])

print(f"Character data has been imported and saved to {csv_file}.")
# Get the current working directory


# Define the CSV file path relative to the current working directory
csv_file = os.path.join(cwd, 'starwars.csv')

# Fetch Europeana data related to Leia Organa using the API key
europeana_api_key = os.getenv("EUROPEANA_API_KEY")  # Replace with your API key
search_query = 'Leia Organa'

# Make a GET request to Europeana API to fetch data
europeana_url = f'https://www.europeana.eu/api/v2/search.json?wskey={europeana_api_key}&query={search_query}'
response = requests.get(europeana_url)
data = response.json()

# Extract the items from the response
items = data['items']

# Iterate over each item and print its title
for item in items:
    print(item['title'])
    # Define the CSV file path for Europeana data
    europeana_csv_file = os.path.join(cwd, 'europeana.csv')

    # Open the CSV file in write mode
    with open(europeana_csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Title'])

        # Iterate over each item and write its title to the CSV file
        for item in items:
            writer.writerow([item['title']])

    print(f"Europeana data has been imported and saved to {europeana_csv_file}.")