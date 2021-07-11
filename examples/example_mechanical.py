# Examples from https://realpython.com/python-web-scraping-practical-introduction/

import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)

# print(page)

"""	
	page has a .soup attribute that represents a 
	BeautifulSoup object:
""" 	
# print(type(page.soup))

"""	
	to inspect HTML:
""" 
print(page.soup)

