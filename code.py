from urllib import request
servicekey = 'L%2Bx%2FuV2N4A5xeGN%2FJxtJ3idEtmvq7HMZeioTgu2kROPGZeUz0oSiz5zQiqUj94Oco4%2FcC%2BJNatV8hJf5mL%2BSuQ%3D%3D'
url = 'http://api.data.go.kr/openapi/tn_pubr_prkplce_info_api'
pagenum = '0'
type = 'json'
rows = '100'
queryParams = '?' + 'serviceKey=' + servicekey
queryParams += '&pagenum=' + pagenum
queryParams += '&numOfRows=' + rows
queryParams += '&type=' +type
req = request.Request(url + queryParams)
req.get_method = lambda: 'GET'
response_body = request.urlopen(req).read()
print(response_body)
