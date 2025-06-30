from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

player_country = []
titles = []
names = []
classical = []
rapid = []
blitz = []

for page in range(1, 12, 1):

    website = f"https://www.chess.com/ratings?page={page}"
    driver = webdriver.Chrome()
    driver.get(website)

    player_names = driver.find_elements(
        By.CLASS_NAME, 'master-players-rating-username')
    players_ratings = driver.find_elements(
        By.CLASS_NAME, "master-players-rating-player-rank")
    chess_titles = driver.find_elements(
        By.CLASS_NAME, "user-chess-title")
    countries = driver.find_elements(
        By.CLASS_NAME, 'master-players-rating-user-flag')

    for country in countries:
        player_country.append(country.get_attribute("v-tooltip"))

    for chess_title in chess_titles:
        titles.append(chess_title.find_element(By.TAG_NAME, 'span').text)

    for player_name in player_names:
        names.append(player_name.text)

    for i in range(0, len(players_ratings), 3):
        classical.append(players_ratings[i].text)
        rapid.append(players_ratings[i+1].text)
        blitz.append(players_ratings[i+2].text)

    driver.quit()

player_country = [country.replace(
    'Click here to see our stance on the war in Ukraine', 'Russia') for country in player_country]


df = pd.DataFrame({'Name': names, 'Title': titles, 'Country': player_country,
                  'Classical Rating': classical, 'Rapid Rating': rapid, 'Blitz Rating': blitz})
df.to_csv('chess_ratings.csv', index=False)
print(df)
