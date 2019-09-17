import bs4
import textme
from datetime import datetime
from selenium import webdriver

URL = 'https://www.cricbuzz.com/cricket-team/india/2/schedule'

options = webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.get(URL)
html = browser.page_source
soup = bs4.BeautifulSoup(html, "html.parser")

element = soup.find('div', 
            class_ = 'cb-col-100 cb-col cb-series-brdr cb-series-matches ng-scope')

date = element.div.span.text
