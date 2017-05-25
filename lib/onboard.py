
from urllib2 import Request, urlopen, URLError

key = 'c90a5d66f14103ee60fa88338ed9ebf2'

def get(url):
	request = Request(url, headers={"Accept": "application/json", "apikey" : key})
	contents = urlopen(request).read()

	return contents

# property information methods, limited search parameter options as shown in the Onboard API docs

def propertyId(postalCode = 91711, minBeds = 0, maxBeds = 100): 
	#returns list of properties which fit the criteria within the search engine geoId
	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/id?postalcode=%s&minBeds=%s&maxBeds=%s" % (postalCode, minBeds, maxBeds)
	return get(response)

def propertyDetail(id):
	#returns detail on a specific property
	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/detail?id=%s" % id
	return get(response)

def propertyZip(postalCode = 91711, propertyType = "RESIDENTIAL(NEC)"):
	#should return list of properties within a zip
	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/address?postalcode=%s&propertytype=%s&orderby=publisheddate&page=1&pagesize=100" % (postalCode, propertyType)
	return get(response)

def propertySnapshot(postalCode, minLotSize=0, maxLotSize=100000):
	#returns properties which fit the criteria
	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/snapshot?postalcode=%s&minLotSize1=%s&maxLotSize1=%s" % (cityName, minLotSize, maxLotSize)
	return get(response)

def propertyZipSnapshot(postalCode, minAvmValue=0, maxAvmValue=1000000):
	#returns list of properties within postal code which fit the criteria
	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/snapshot?postalcode=%s&minavmvalue=%s&maxavmvalue=%s" % (postalCode, minAvmValue, maxAvmValue)
	return get(response)

#sales information methods

def saleSnapshot(postalCode, minSaleAmount, maxSaleAmount, startDate, endDate):
	#should return list of properties within geographical area which fit the criteria
	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/sale/snapshot?postalcode=%s&minsaleamt=%s&maxsaleamt=%s&startsalesearchdate=%s&endsalesearchdate=%s"
	return get(response)

#mutable request

def propertyDetailMutable(d = {}):
	#list of acceptable key names for d
	keyList = ['minSaleAmt','maxSaleAmt', 'minTaxAmt','maxTaxAmt','minApprTtlValue','maxApprTtlValue',
		'minAssdTtlValue', 'maxAssdTtlValue', 'minAVMValue', 'maxAVMValue','radius','cityName','startSaleTransDate',
		'endSaleTransDate','lotSize1', 'lotSize2', 'minMktLandValue', 'maxMktLandValue','minMktTtlValue', 
		'maxMktTtlValue', 'GeoID', 'ID', 'postalCode', 'address', 'startSaleSearchDate', 'endSaleSearchDate', 
		'propertyType', 'minBathsTotal', 'maxBathsTotal','minBeds', 'maxBeds','universalSize']

	#check d's key names against keyList to make sure you don't break shit


	#replace spaces in string values with %20


	#iterates through keys to add values to the search parameter

	string = ""
	i = 1
	for k in d:
		string += "%s=%s" % (k, d[k])
		if i < len(d) : string += "&"
		i += 1

	response = "https://search.onboard-apis.com/propertyapi/v1.0.0/property/detail?%s" % string
	return response

print propertyDetailMutable(d = {'minSaleAmt' : 100000, 'maxSaleAmt' : 500000, 'cityName' : "Burlingame"})
print propertyId()
