from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pandas.core.tools.numeric import to_numeric
import inspect
from bs4.element import NavigableString, Tag
import numpy as np

"""
	CONFIGURATION 
"""
url = "https://coldstorage.com.sg/search?q=" 
headers = {'User-Agent': 'Mozilla/5.0'} 

# Takes in a search query and returns a list of items on NTUC Fairprice
# 	that matches the query with their `title`, `price` and `link`

# EXAMPLE:
#	INPUT: 
# 		"chicken breast whole"
#	OUTPUT: 
		# {
		# 	"Aw's Market Chicken Breast Whole": {
		# 		'price': 5.0, 
		# 		'link': '/product/aw-s-market-chicken-breast-whole-400-g-90018633'	
		# 	}, 
		# 	"Aw's Market Duck Breast Whole": {
		# 		'price': 9.45, 
		# 		'link': '/product/aw-s-market-duck-breast-whole-800-g-90018554'}
		#	}
		#}
def search(keywords):
	# a function to generate the search-query URL
	def generateURL(url, keywords):
		queryURL = url
		cleanedKeywords = keywords.replace(' ', '+')
		queryURL = queryURL + cleanedKeywords

		return queryURL
	
	req = Request(generateURL(url, keywords), headers=headers)
	page = urlopen(req)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	matches = soup.find_all('div', { 'class': 'product_box' })

	# initialize the array to be returned
	result = []

	""" 
		Step 1: Get links to the food products
	"""
	links = []
	for elem in matches:
		links.append(elem.findChildren("a", recursive = False)[0].attrs['href'])

	details = []
	prices = []
	titles = []
	measurements = []
	for elem in matches:
		detailsList = elem.find("div", { "class": "product_detail" })
		
		for detail in detailsList:
			if(isinstance(detail, Tag)):
				details.append(detail)
	
	splitArr = np.array_split(details, (len(details) / 3))

	for detail in splitArr:
		# Step 2: Get the price of the food product 
		prices.append(detail[0]
						.select('div[class*="price_now"]')[0]
						.attrs['data-price']
					)

		# Step 3: Get the title of the food product
		titles.append(detail[1].find('div', { "class": "product_name" }).text.replace('\n', '').strip())

		# Step 4: Get the measurement of the food product
		measurements.append(detail[2].text.replace('\nSize: ', '').replace(' ', ''))
	
	# Step 5: Combine the attributes into a single object and add it to the result array
	for i in range(0, int(len(details) / 3)):
		result.append({
			'title': titles[i],
			'price': prices[i],
			'measurement': measurements[i],
			'link': links[i],
			'supermarket': 'cold-storage'
		})
	
	return result


