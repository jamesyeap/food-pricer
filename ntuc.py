from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pandas.core.tools.numeric import to_numeric

"""
	CONFIGURATION 
"""
url = "https://www.fairprice.com.sg/search?query=" 
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
def searchFoodProduct(keywords):
	# a function to generate the search-query URL
	def generateURL(url, keywords):
		queryURL = url
		cleanedKeywords = keywords.replace(' ', '%20')
		queryURL = queryURL + cleanedKeywords

		return queryURL
	
	req = Request(generateURL(url, keywords), headers=headers)
	page = urlopen(req)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	matches = soup.select('div[class*="product-container"]')

	# initialize the dictionary to be returned
	result = {}

	for elem in matches:
		matches = elem.findChildren("a", recursive=False) 
		
		for match in matches:
			"""
				Step 1: Find the name of the food product
			"""
			# the image of the food product contain a 'title' attribute
			#	that has the name of the food product
			image = match.findChildren("img")
			linkToProduct = match.attrs['href']

			"""
				Step 2: Find the price of the food product
				
					THE ISSUE OF MULTIPLE PRICES: 
					Sometimes the product may be on discount, 
						so 2 or more prices will be shown. 

					To deal with this, we just return the lowest of 
						all the prices; with the assumption that the lowest 
						price is the discount price offered to the customer.
			"""
			# the span elements of the food product 
			# 	contain its price
			spanList = match.findChildren("span")
			priceList = []

			for span in spanList:
				# check that the string contained inside the span element is referring to the 
				# 	price of the food item (and not a button like "add to cart")
				if ("$" in span.text):
					cleanedPrice = (span.text).replace('$', '')
					priceList.append(to_numeric(cleanedPrice))

			"""
				Step 3: Find the weight/volume of the food product
			"""
			units = [
				'kg', 'KG',
				'g', 'G',
				'ml', 'ML'
				'l', 'L'
			]

			measurement = ""
			for span in spanList:
				if (any(x in span.text for x in units)):
					measurement = span.text
			"""
				Step 4: Add the title, price and link to the food product to the result object
			"""
			result[(image[0].attrs['title'])] = { 
				'price' : min(priceList), 
				'measurement': measurement,
				'link': linkToProduct,
			}
					
	return result

# DOES IT WORK?
print(searchFoodProduct("chicken breast whole"))

	
	
