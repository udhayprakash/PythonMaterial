scrapy shell

from scrapy.http import FormRequest

viewstate = response.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first() 
viewstategenerator = response.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first() 
eventvalidation = response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()

data = {'__VIEWSTATE': viewstate,
'__VIEWSTATEGENERATOR': viewstategenerator,
'__EVENTVALIDATION': eventvalidation,
'today': '20170905',
'sortBy': '',
'selPartID': '',
'alertMsg': '',
'ddlShareholdingDay': '04',
'ddlShareholdingMonth': '09',
'ddlShareholdingYear': '2017',
'txtStockCode': '00001',
'txtStockName': '',
'txtParticipantID': '',
'txtParticipantName': '',
'btnSearch.x': '45',
'btnSearch.y': '9'}

page = FormRequest(url='http://www.hkexnews.hk/sdw/search/searchsdw.aspx', formdata=data)

fetch(page)

view(response)