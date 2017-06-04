
from urllib2 import Request, urlopen, URLError
from urllib import urlencode

class zillowClient():
	#instantiate and define get method
	def __init__(self, key):
		if key: self._key = key
		else: raise ValueError("No key entered")
	def __get(self, url):
		request = Request(url)
		contents = urlopen(request).read()

		return contents

	#gets neighborhood info
	def getRegionChildren(self, state="CA", d= {}):
		auth = self._key

		#list of acceptable dict values for d
		keyList = ["county", "city", "childtype"]

		#remove any wrong values in d.keys()
		for k in d.keys():
			if k not in keyList:
				print "Parameter Removed: '%s'" % k
				d.pop(k)

		dictvals = "%s" % urlencode(d)

		url = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=%s&state=%s&%s" % (auth, state, dictvals)
		return self.__get(url)
