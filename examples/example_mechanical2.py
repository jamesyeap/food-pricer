# Examples from https://realpython.com/python-web-scraping-practical-introduction/

import mechanicalsoup

""" 
	STEP 1

	You create a Browser instance and use it to request the 
		URL http://olympus.realpython.org/login. 

	You assign the HTML content of the page to the 
		login_html variable using the .soup property.
"""
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

"""
	STEP 2

	login_html.select("form") returns a list of all <form> elements 
		on the page. 

	Since the page has only one <form> element, 
		you can access the form by retrieving the element at 
		index 0 of the list. The next two lines select the 
		username and password inputs and set their value to 
		"zeus" and "ThunderDude", respectively.
"""

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

"""
	STEP 3

	You submit the form with browser.submit(). 

	Notice that you pass two arguments to this method, 
		the form object and the URL of the login_page, which you 
		access via login_page.url.
"""
profiles_page = browser.submit(form, login_page.url)