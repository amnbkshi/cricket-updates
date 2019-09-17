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
            class_ = 'cb-col-100 cb-col cb-series-matches ng-scope')

date = element.div.span.text #split by - for test matches
#datetime.strptime(date, '%b %d, %a')

team = element.find('a', class_='text-hvr-underline').span.text
venue = element.find('div', class_="text-gray cb-ovr-flo").text
time = element.find('div', class_="cb-font-12 text-gray").select('span + span')[0].text
