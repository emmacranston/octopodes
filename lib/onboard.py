
from urllib2 import Request, urlopen, URLError
from urllib import urlencode

class onboardClient():
	def __init__(self, token):
		if token: self._token = token
		else: raise ValueError("No token entered")

	def __get(self, url):
		request = Request(url, headers={"Accept": "application/json", "apikey" : self.token})
		contents = urlopen(request).read()

		return contents

	# property information methods, limited search parameter options as shown in the Onboard API docs

	def propertyId(self, postalCode = 91711, minBeds = 0, maxBeds = 100): 
		#returns list of properties which fit the criteria within the search engine geoId
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/id?postalcode=%s&minBeds=%s&maxBeds=%s" % (postalCode, minBeds, maxBeds)
		return self.__get(response)

	def propertyDetail(self, id):
		#returns detail on a specific property
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/detail?id=%s" % id
		return self.__get(response)

	def propertyZip(self, postalCode = 91711, propertyType = "RESIDENTIAL(NEC)"):
		#should return list of properties within a zip
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/address?postalcode=%s&propertytype=%s&orderby=publisheddate&page=1&pagesize=100" % (postalCode, propertyType)
		return self.__get(response)

	def propertySnapshot(self, postalCode, minLotSize=0, maxLotSize=100000):
		#returns properties which fit the criteria
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/snapshot?postalcode=%s&minLotSize1=%s&maxLotSize1=%s" % (cityName, minLotSize, maxLotSize)
		return self.__get(response)

	def propertyZipSnapshot(self, postalCode, minAvmValue=0, maxAvmValue=1000000):
		#returns list of properties within postal code which fit the criteria
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/snapshot?postalcode=%s&minavmvalue=%s&maxavmvalue=%s" % (postalCode, minAvmValue, maxAvmValue)
		return self.__get(response)

	#sales information methods

	def saleSnapshot(self, postalCode, minSaleAmount, maxSaleAmount, startDate, endDate):
		#should return list of properties within geographical area which fit the criteria
		response = "https://search.onboard-apis.com/propertyapi/v1.0.0/sale/snapshot?postalcode=%s&minsaleamt=%s&maxsaleamt=%s&startsalesearchdate=%s&endsalesearchdate=%s"
		return self.__get(response)

	#mutable request- can use (almost) any available 'advanced' search parameters for the property resource in Onboard's API
	#available parameters shown on keyList, explanations available through Onboard's docs.
	def propertyDetailMutable(self, d = {}):
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
