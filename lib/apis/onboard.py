
from urllib2 import Request, urlopen, URLError
from urllib import urlencode

class onboardClient():
	"""Instantiates a client for use with the Onboard API. Requires an API token in string form."""
	def __init__(self, token):
		"""Constructor for Onboard Client"""
		if token: self._token = token
		else: raise ValueError("No token entered")

	def __get(self, url):
		"""Gets a specified URL with the correct headers; uses XML format"""
		request = Request(url, headers={"Accept": "application/xml", "apikey" : self.token})
		contents = urlopen(request).read()

		return contents

# property information methods, limited search parameter options as shown in the Onboard API docs

	def propertyId(self, postalCode = 91711, minBeds = 0, maxBeds = 100): 
		"""Returns XML list of properties which fit the criteria within the search engine geoId"""
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/id?postalcode=%s&minBeds=%s&maxBeds=%s" % (postalCode, minBeds, maxBeds)
		return self.__get(response)

	def propertyDetail(self, id):
		"""Returns detail on a specific property defined by its Onboard ID"""
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/detail?id=%s" % id
		return self.__get(response)

	def propertyZip(self, postalCode = 91711, propertyType = "RESIDENTIAL(NEC)"):
		"""Returns list of properties within a zip, optional propertyType"""
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/address?postalcode=%s&propertytype=%s&orderby=publisheddate&page=1&pagesize=100" % (postalCode, propertyType)
		return self.__get(response)

	def propertySnapshot(self, postalCode, minLotSize=0, maxLotSize=100000):
		"""Returns properties within postal code which fit the lot size criteria."""
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/snapshot?postalcode=%s&minLotSize1=%s&maxLotSize1=%s" % (cityName, minLotSize, maxLotSize)
		return self.__get(response)

	def propertyZipSnapshot(self, postalCode, minAvmValue=0, maxAvmValue=1000000):
		"""Returns list of properties within postal code which fit your valuation criteria."""
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/snapshot?postalcode=%s&minavmvalue=%s&maxavmvalue=%s" % (postalCode, minAvmValue, maxAvmValue)
		return self.__get(response)

	#sales information methods

	def saleSnapshot(self, postalCode, maxSaleAmount, startDate, endDate, minSaleAmount = 0):
		"""Returns list of properties within geographical area which fit your criteria. startDate and endDate must be in YYYY-MM-DD format."""

		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/sale/snapshot?postalcode=%s&minsaleamt=%s&maxsaleamt=%s&startsalesearchdate=%s&endsalesearchdate=%s"
		return self.__get(response)

	#mutable request- can use (almost) any available 'advanced' search parameters for the property resource in Onboard's API
	#available parameters shown on keyList, explanations available through Onboard's docs.
	def propertyDetailMutable(self, d = {}):
		"""Creates an API call according to the key-value pairs assigned to the parameter ``d.`` See RE/docs/api.md for full list of acceptable key names."""
		#list of acceptable key names for d
		keyList = ['minSaleAmt','maxSaleAmt', 'minTaxAmt','maxTaxAmt','minApprTtlValue','maxApprTtlValue',
			'minAssdTtlValue', 'maxAssdTtlValue', 'minAVMValue', 'maxAVMValue','radius','cityName','startSaleTransDate',
			'endSaleTransDate','lotSize1', 'lotSize2', 'minMktLandValue', 'maxMktLandValue','minMktTtlValue', 
			'maxMktTtlValue', 'GeoID', 'ID', 'postalCode', 'address', 'startSaleSearchDate', 'endSaleSearchDate', 
			'propertyType', 'minBathsTotal', 'maxBathsTotal','minBeds', 'maxBeds','universalSize']

		# possible to do more efficiently than worst-case O(n^2)?
		# remove unacceptable keys
		for k in d.keys():
			if k not in keyList:
				print "Parameter Removed: '%s'" % k
				d.pop(k)

		#urlencode is pretty dope tbh
		#encode response to HTTPS call
		string = "?" + urlencode(d)
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/detail%s" % string
		return self.__get(response)
