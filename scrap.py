import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'/Users/me/Downloads/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://python.org');
html_doc = driver.page_source
print(html_doc)
driver.quit()