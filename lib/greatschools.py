#greatschools.py

from urllib2 import Request, urlopen, URLError
from urllib import urlencode, quote

class greatschoolsClient():
	def __init__(self, token):
		if token: self._token = token
		else: raise ValueError("No token value added")

	def __get(self, url):
		request = Request(url)
		contents = urlopen(request).read()
		return contents

#parameter debugging checks: need work
	def checkLevelParameter(self, string):
		levelList = ["elementary-schools", "middle-schools", "high-schools"]
		if string not in levelList:
			raise ValueError("Please use one of elementary-schools, middle-schools, or high-schools in the 'level' parameter.") 

	def checkSchoolTypeParameter(self, string):
		schoolTypeList = ["public", "charter", "private"]
		if string not in levelList:
			raise ValueError("Please use one of public, charter, or private in 'schoolType' parameter.")
		# also allowed are any items in the list separated by hyphens; gonna come back to this one later

#these methods will return only the HTTP response; need to decode from XML to be legible
	def schoolsBrowse(self, state = "CA", city = "San Francisco", schoolType = "", level = ""):
		#make sure parameters for schoolType and level make sense
		checkLevelParameter(level)
		checkSchoolTypeParameter(schoolType)

		#properly encode parameters
		s = quote(state)
		#custom replace function for city because greatschools does it... their own special way
		c = city.replace("-", "_").replace(" ", "-")
		st = quote(schoolType)
		l = quote(level)

		#put together request url
		request = "http://api.greatschools.org/schools/%s/%s?key=%s" % (s, c, self._token)
		return self.__get(request)

	def schoolsNearby(self, state, d = {}):
		#define allowable key values for d
		keyList = ["zip", "city", "address", "lat", "lon", "schoolType", "levelCode", "radius", "limit"]
		for k in d.keys():
			if k not in keyList:
				print "Parameter Removed: '%s'" % k
				d.pop(k)

		#for some reason in this endpoint you can urlencode as per usual
		params = "&" + urlencode(d)
		request = "http://api.greatschools.org/schools/nearby?key=%s%s" % (self._token, params)
		return self.__get(request)
