from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

def show_initial_data():
    console.print("\n[bold cyan]Here is some initial data:[/bold cyan]")
    table=Table(title="Football Teams")
    table.add_column("Team Name", style="red", no_wrap=True)
    table.add_column("Country", style="purple")
    table.add_column("League", justify="right")
    
    table.add_row("Liverpool", "England", "EPL")
    table.add_row("Arsenal", "England", "EPL")
    table.add_row("Chelsea", "England", "EPL")
    table.add_row("FC Barcelona", "Spain", "La Liga")

    console.print(table)

def get_team_data():
    team_name=console.input("Enter the team name")
    team_country=console.input("Enter the team's country")
    team_league=console.input("Enter the team's league")

    return{"team name":team_name, "country":team_country, "league":team_league}

def confirm_data_and_write(football_teams):
    file_path = "teams_data.txt"
    with open(file_path, "w") as file:
        for team in football_teams:
            file.write(f"{team}\n")
    console.print(f"\n[bold blue]Teams saved successfully to {file_path}[/bold blue]")
    return True
    
def main():
    show_initial_data()
    football_teams=[]
    while True:
        football_team=get_team_data()
        football_teams.append(football_team)
        add_more=console.input("\nWould you like to add another team? (y/n): ").lower()
        if add_more=="n":
            break
    
    while not confirm_data_and_write(football_teams):
        football_teams.clear()
        console.print("\nRe-enter all the teams.\n")
        football_teams.append(get_team_data())

if __name__ == "__main__":
    main()
