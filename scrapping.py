from bs4 import BeautifulSoup
import requests
from kafka_me import producer

html_text = requests.get('https://www.nba.com/teams').text


soup = BeautifulSoup(html_text, 'lxml')
teams = soup.find('div', class_="TeamDivisions_wrapper__5_SVo").find_all('a', class_="Anchor_anchor__cSc3P TeamFigure_tfMainLink__OPLFu")

#for team in teams:
    #producer.produce('nba', value=team.text)
   # producer.flush()