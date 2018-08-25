import time
from selenium import webdriver
from bs4 import BeautifulSoup
letters = [
           "a","b","c","d","e","f","g","h","i","k",
           "l","m","n","o","p","q","r","s","t","u",
           "v","w","x","y","z"]
def scap(letters):
    #driver = webdriver.Chrome(executable_path=r'/Users/me/Downloads/chromedriver')  # Optional argument, if not specified will search path.
    driver = webdriver.PhantomJS(executable_path=r'/Users/me/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.get('https://druginfo.nlm.nih.gov/drugportal/drug/names/{}'.format(letters))
    html_doc = driver.page_source

    soup = BeautifulSoup(html_doc,'html.parser')
    soup.prettify()
    table = soup.find('table',{'border':'1'})
    first = table.find('tr')
    sibling = first.findNextSiblings()
    all_child = table.findChildren()
    #tr_tags = soup.find_all('td')
    for child in sibling:
        print(child.get_text())
    driver.quit()
for letter in letters:
  scap(letter)
#print(all_child)
#for child in all_child:
    #print(child.get_text())
#
# for tr in tr_tags:
#     print(tr)
