API Reference
=============

## onboardClient(): ##

> 	OnboardClient gives you methods to use with the Onboard API. The 
	methods defined are not all-inclusive of every available API call, but instead represent what may be necessary for this project.

*	**__get**
	*Parameters*: url  
	*Description*: Private method that returns an urllib2 request to the url. Simple.
*	**propertyId**
     *Parameters*:
     *Description*:
*	**propertyDetail**
    *Parameters*:
    *Description*:
*	**propertyZip**
    *Parameters*:
    *Description*:
*	**propertySnapshot**
    *Parameters*:
    *Description*:
*	**propertyZipSnapshot**
    *Parameters*:
    *Description*:
*	**saleSnapshot**
    *Parameters*:
    *Description*:
*	**propertyDetailMutable**
    *Parameters*: d
    *Description*: Creates an API call according to the key-value pairs assigned to the parameter ``d``. Acceptable key names include: 
> 'minSaleAmt','maxSaleAmt', 'minTaxAmt', 'maxTaxAmt', 'minApprTtlValue', 'maxApprTtlValue', 'minAssdTtlValue', 'maxAssdTtlValue', 'minAVMValue', 'maxAVMValue', 'radius', 'cityName', 'startSaleTransDate', 'endSaleTransDate', 'lotSize1', 'lotSize2', 'minMktLandValue', 'maxMktLandValue','minMktTtlValue', 'maxMktTtlValue', 'GeoID', 'ID', 'postalCode', 'address', 
> 'startSaleSearchDate', 'endSaleSearchDate', 'propertyType', 'minBathsTotal', 'maxBathsTotal', 'minBeds', 'maxBeds', 'universalSize'


>All Onboard API documentation is available on their [website](https://developer.onboard-apis.com/docs). 

> From their developer site: "The data provided in the Onboard Property API is from CoreLogic and derived from county public records. It includes the most up-to-date data publicly available from the counties that publish it." I do not personally guarantee the accuracy or efficacy of this information.


## zillowClient(): ##
> Instantiates a client for use with the Zillow API. 
> 

## greatSchoolsClient():##
> Instantiates a client for use with the GreatSchools API. For direct access to Greatschools data, apply for an API key with Greatschools [here](https://www.greatschools.org/api/registration.page). Otherwise, please use data files within the github folder.