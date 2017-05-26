#greatschools.py

from urllib2 import Request, urlopen, URLError
from urllib import urlencode, quote

class greatschoolsClient():
	def __init__(self, token):
		if token: pass
		else: raise ValueError("No token value added")

	def get(self, url):
		request = Request(url, headers={"Accept": "application/json", "apikey" : key})
		contents = urlopen(request).read()
		return contents

	def checkLevelParameter(self, string):
		levelList = ["elementary-schools", "middle-schools", "high-schools"]
		if string not in levelList:
			raise ValueError("Please use one of elementary-schools, middle-schools, or high-schools in the 'level' parameter.") 

	def checkSchoolTypeParameter(self, string):
		schoolTypeList = ["public", "charter", "private"]
		# also allowed are any items in the list separated by hyphens; gonna come back to this one later

	def browseSchools(self, state = "CA", city = "San Francisco", schoolType = "", level = ""):
		#make sure parameters for schoolType and level make sense
		checkLevelParameter(level)
		checkSchoolTypeParameter(schoolType)

		#properly encode parameters
		s = quote(state)
		c = city.replace("-", "_").replace(" ", "-")
		st = quote(schoolType)
		l = quote(level)

		#put together request url
		request = "http://api.greatschools.org/schools/%s/%s?key=%s" % (s, c, key)
		return request
		#return urlopen(request).read()
