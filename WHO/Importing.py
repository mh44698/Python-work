####  https://www.who.int/data/gho/info/gho-odata-api
#### Deminsion Values
# "https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues"


import requests 
import json

# Code: "USA",
# Title: "United States of America",
# ParentDimension: "REGION",
# Dimension: "COUNTRY",
# ParentCode: "AMR",
# ParentTitle: "Americas"

url = "https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues"
response = requests.get(url)
data = response.text
country = json.loads(data)

# {
# IndicatorCode: "AIR_41",
# IndicatorName: "Ambient air pollution attributable deaths",
# Language: "EN"
# }
url = "https://ghoapi.azureedge.net/api/Indicator"
response = requests.get(url)
data = response.text
indicators = json.loads(data)
#Filtering Data:
#https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=Dim1 eq 'MLE'

https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=IndicatorCode eq 'SA_0000001542'

# {
# Id: 15578243,
# IndicatorCode: "WHOSIS_000001",
# SpatialDimType: "COUNTRY",
# SpatialDim: "RWA",
# TimeDimType: "YEAR",
# TimeDim: 2000,
# Dim1Type: "SEX",
# Dim1: "FMLE",
# Dim2Type: null,
# Dim2: null,
# Dim3Type: null,
# Dim3: null,
# DataSourceDimType: null,
# DataSourceDim: null,
# Value: "48.4",
# NumericValue: 48.38779,
# Low: null,
# High: null,
# Comments: null,
# Date: "2017-03-31T08:14:36.36+02:00"
# }

url = "https://ghoapi.azureedge.net/api/WHOSIS_000001"
response = requests.get(url)
data = response.text
WHOSIS_Data = json.loads(data)




print(country)
print(indicators)
print(WHOSIS_Data)




