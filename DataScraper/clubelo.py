import requests
import csv
from io import StringIO
import pandas as pd
import os
from datetime import datetime

from selenium import webdriver

from bs4 import BeautifulSoup
import time
import urllib.parse

url = 'http://api.clubelo.com/Fixtures'
response = requests.get(url)

if response.status_code != 200:
    print("Unable to retrieve data.\n")

with open("Fixtures.csv", "wb") as f:
    f.write(response.content)

data = StringIO(response.text)
df = pd.read_csv(data, sep=",")


df["Game_ID"] = df["Home"] + " vs " + df["Away"]
df['Home Win%'] = df.apply(lambda x: round((x['GD=1'] + x['GD=2'] + x['GD=3'] + x['GD=4'] + x['GD=5'] + x['GD>5']) * 100, 2) if (x['GD=-1'] + x['GD=0'] + x['GD=1'] + x['GD=2'] + x['GD=3'] + x['GD=4'] + x['GD>5']) > 0 else '', axis=1)
df['Away Win%'] = df.apply(lambda x: round((x['GD<-5'] + x['GD=-5'] + x['GD=-4'] + x['GD=-3'] + x['GD=-2'] + x['GD=-1']) * 100, 2) if (x['GD=-1'] + x['GD=0'] + x['GD=1'] + x['GD=2'] + x['GD=3'] + x['GD=4'] + x['GD>5']) > 0 else '', axis=1)
df['Draw%'] = df.apply(lambda x: round(x['GD=0'] * 100, 2) if x['GD=0'] != 0 else '', axis=1)

# Create a new dataframe with selected columns
new_df = df[['Game_ID', 'Home Win%', 'Away Win%', 'Draw%']]
# Save the new dataframe to an Excel file
new_df.to_excel('Fixtures.xlsx', index=False)
# Convert the CSV to Excel format
writer = pd.ExcelWriter('Fixtures.xlsx', engine='xlsxwriter')
new_df.to_excel(writer, sheet_name='Fixtures', index=False)

#print(new_df.head())

total_games = len(new_df)
print("Total number of games:", total_games)
writer._save()

# Iterate over each unique Game_ID
unique_game_ids = df['Game_ID'].unique()
for game_id in unique_game_ids:
    game_df = df[df['Game_ID'] == game_id].copy()  # Filter DataFrame for the current Game_ID
    game_df.reset_index(drop=True, inplace=True)  # Reset the index of the filtered DataFrame

    # Create a new DataFrame for the current Game_ID
    result_df = pd.DataFrame(index=range(8), columns=range(8))
    result_df.iloc[0, 0] = "Goals"
    result_df.iloc[0, 1] = "#"
    result_df.iloc[0, 2] = "#"
    result_df.iloc[0, 4] = "#"
    result_df.iloc[0, 5] = "#"
    result_df.iloc[0, 6] = "#"
    result_df.iloc[0, 7] = "#"
    result_df.iloc[1, 0] = "#"
    result_df.iloc[2, 0] = "#"
    result_df.iloc[4, 0] = "#"
    result_df.iloc[5, 0] = "#"
    result_df.iloc[6, 0] = "#"
    result_df.iloc[7, 0] = "#"
    
    result_df.iloc[0, 3] = game_df.loc[0, 'Home']  # Home Team
    result_df.iloc[3, 0] = game_df.loc[0, 'Away']  # Away Team

    result_df.iloc[1, 1] = game_df.loc[0, 'R:0-0'] *100 # Draw 0-0
    result_df.iloc[2, 1] = game_df.loc[0, 'R:0-1'] *100 # Home team loses 0-1
    result_df.iloc[3, 1] = game_df.loc[0, 'R:0-2'] *100 # Home team loses 0-2
    result_df.iloc[4, 1] = game_df.loc[0, 'R:0-3'] *100 # Home team loses 0-3
    result_df.iloc[5, 1] = game_df.loc[0, 'R:0-4'] *100 # Home team loses 0-4
    result_df.iloc[6, 1] = game_df.loc[0, 'R:0-5'] *100 # Home team loses 0-5
    result_df.iloc[7, 1] = game_df.loc[0, 'R:0-6'] *100 # Home team loses 0-6

    result_df.iloc[1, 2] = game_df.loc[0, 'R:1-0'] *100 # Home team wins 1-0
    result_df.iloc[1, 3] = game_df.loc[0, 'R:2-0'] *100 # Home team wins 2-0
    result_df.iloc[1, 4] = game_df.loc[0, 'R:3-0'] *100 # Home team wins 3-0
    result_df.iloc[1, 5] = game_df.loc[0, 'R:4-0'] *100 # Home team wins 4-0
    result_df.iloc[1, 6] = game_df.loc[0, 'R:5-0'] *100 # Home team wins 5-0
    result_df.iloc[1, 7] = game_df.loc[0, 'R:6-0'] *100 # Home team wins 6-0

    result_df.iloc[2, 2] = game_df.loc[0, 'R:1-1'] *100 # Draw 1-1
    result_df.iloc[3, 2] = game_df.loc[0, 'R:1-2'] *100 # Home team loses 1-2
    result_df.iloc[4, 2] = game_df.loc[0, 'R:1-3'] *100 # Home team loses 1-3
    result_df.iloc[5, 2] = game_df.loc[0, 'R:1-4'] *100 # Home team loses 1-4
    result_df.iloc[6, 2] = game_df.loc[0, 'R:1-5'] *100 # Home team loses 1-5

    result_df.iloc[2, 3] = game_df.loc[0, 'R:2-1'] *100 # Home team wins 2-1
    result_df.iloc[3, 3] = game_df.loc[0, 'R:2-2'] *100 # Draw 2-2
    result_df.iloc[4, 3] = game_df.loc[0, 'R:2-3'] *100 # Home team loses 2-3
    result_df.iloc[5, 3] = game_df.loc[0, 'R:2-4'] *100 # Home team loses 2-4

    result_df.iloc[2, 4] = game_df.loc[0, 'R:3-1'] *100 # Home team wins 3-1
    result_df.iloc[3, 4] = game_df.loc[0, 'R:3-2'] *100 # Home team wins 3-2
    result_df.iloc[4, 4] = game_df.loc[0, 'R:3-3'] *100 # Draw 3-3

    result_df.iloc[2, 5] = game_df.loc[0, 'R:4-1'] *100 # Home team wins 4-1
    result_df.iloc[3, 5] = game_df.loc[0, 'R:4-2'] *100 # Home team wins 4-2

    result_df.iloc[2, 6] = game_df.loc[0, 'R:5-1'] *100 # Home team wins 5-1

     # Fill NaN values with "#"
    result_df.fillna("#", inplace=True)
    
    # Print the resulting DataFrame for the current Game_ID
    print(f"Table for Game_ID: {game_id}")
    print(result_df)
    print("\n")

    # Extract the team names from the first row of game_df
    teams_participating = []

    for i in range(len(game_df)):
        home_team = game_df.loc[i, 'Home']
        away_team = game_df.loc[i, 'Away']
        
        teams_participating.append(home_team)
        teams_participating.append(away_team)

    # Create a Selenium WebDriver instance
    driver = webdriver.Chrome()

    # Rest of the code...

    print(teams_participating)

    for team in teams_participating:
        encoded_team = urllib.parse.quote(team.replace(" ", ""))
        print(encoded_team)
        
        url = f"http://clubelo.com/{encoded_team}"

        response = requests.get(url)
        time.sleep(2)
        soup = BeautifulSoup(response.content, 'html.parser')

        result1_coordinates = [(615, y) for y in range(63, 364, 20)]
        result2_coordinates = [(625, y) for y in range(63, 364, 20)]

        result1_scores = []
        result2_scores = []

        # Retrieve result 1 scores
        for coordinate in result1_coordinates:
            x, y = coordinate
            try:
                score_element = soup.find("text", {"x": str(x), "y": str(y)})
                score_text = score_element.text.strip()
                result1_scores.append(int(score_text))
            except ValueError:
                result1_scores.append(None)
            except AttributeError:
                pass

        # Retrieve result 2 scores
        for coordinate in result2_coordinates:
            x, y = coordinate
            try:
                score_element = soup.find("text", {"x": str(x), "y": str(y)})
                score_text = score_element.text.strip()
                result2_scores.append(int(score_text))
            except ValueError:
                result2_scores.append(None)
            except AttributeError:
                pass

        # Calculate outcomes
        games_won = 0
        games_lost = 0
        games_draw = 0

        for i in range(len(result1_scores)):
            if result1_scores[i] is not None and result2_scores[i] is not None:
                if result1_scores[i] > result2_scores[i]:
                    games_won += 1
                elif result1_scores[i] == result2_scores[i]:
                    games_draw += 1
                else:
                    games_lost += 1


        print(f"Team: {team}")
        print(f"Games won: {games_won}")
        print(f"Games lost: {games_lost}")
        print(f"Games draw: {games_draw}")
        print("------------------------------")

driver.quit()


















# Delete the files
files_to_delete = [".~lock.Fixtures.csv#", "Fixtures.csv"]
for file_name in files_to_delete:
    if os.path.exists(file_name):
        os.remove(file_name)

#for every team, go to clubelo.com/{team} and scrape latest 10 games to check performance
# performance will be classified like this:
# ELO BASED:
# win against high elo +2.5 , win against lower elo +1.5
# draw against high elo +1, draw against lower elo +0
# lost against higher elo -1.5 , lost against lower elo -2.5
# 
# Same league based:
# win against high pos +2.5 , win against lower pos +1.5
# draw against high pos +1, draw against lower pos +0
# lost against higher pos -1.5 , lost against lower pos -2.5

# if A played again 5 higher elos and B against 1 higher elo, fix




    # pull last games of each team  https://www.whoscored.com/Statistics
    #https://github.com/RamisLao/scraper-whoscored