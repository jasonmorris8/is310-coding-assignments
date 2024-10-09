import rich
from rich import print
from rich.console import Console
from rich.table import Table
import sys

console=Console()
console.print("Here is some intitial data", style="bold cyan")
table=Table(title="Football Teams")
table.add_column("Team", justify="center", style="bold")
table.add_column("Country", justify="center", style="bold")
table.add_column("Ranking", justify="center", style="bold")

table.add_row("Liverpool", "England", "1")
table.add_row("Real Madrid", "Spain", "2")
table.add_row("Bayern Munich", "Germany", "3")
table.add_row("Juventus", "Italy", "4")
table.add_row("Paris Saint-Germain", "France", "5")

console.print(table)
console.print("\n[bold cyan]Now I want you to enter your favorite football teams:[/bold cyan]")

team_name = input("Enter the name of the team: ")
team_country = input("Enter the country the team is located in: ")
team_ranking = input("Enter the ranking of the team: ")
while True:
    team_name = input("Enter the name of the team (or 'q' to quit): ")
    if team_name.lower() == 'q':
        break
    team_country = input("Enter the country the team is located in: ")
    team_ranking = input("Enter the ranking of the team: ")
    table.add_row(team_name, team_country, team_ranking)
console.print(table)
file_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/jmo/Desktop/is310-coding-assignments/python-libraries/teams_data.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the table data to the file
    file.write(str(table))
