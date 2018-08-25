from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'/Users/me/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

url = 'https://stats.nba.com/players/list'
base_url ='https://stats.nba.com'
driver.get(url)

print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'html.parser')

div = soup.find('div' , class_ = 'stats-player-list')
for a in div.find_all('a'):
    print(a.text)
    #print(base_url+a['href'])
#print(div)
