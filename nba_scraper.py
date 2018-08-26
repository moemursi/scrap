from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
    def __init__(self):
        self.name = ""
        self.link = ""


def get_player():

    driver = webdriver.PhantomJS(executable_path=r'/Users/me/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

    url = 'https://stats.nba.com/players/list'
    base_url ='https://stats.nba.com'
    driver.get(url)

    print(driver.page_source)

    soup = BeautifulSoup(driver.page_source,'html.parser')

    div = soup.find('div' , class_ = 'stats-player-list')

    players = []
    for a in div.find_all('a'):
        name = a.text
        link = base_url+a['href']
        new_player = Player()
        new_player.name = name
        new_player.link = link
        players.append(new_player)
    for player in players:
        print("Name :: " + player.name )
        print("Link :: " + player.link)
    #print(div)
    driver.quit()

    return players

get_player()