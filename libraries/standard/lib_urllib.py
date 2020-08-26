from urllib.request import urlopen
from urllib.parse import urlparse, urlencode

start_dt = '201001'
end_dt = '202012'

savename = 'temperature_from_' + start_dt + '_to_' + end_dt + '.csv'

values = {
    'fileType': 'csv',
    'pgmNo': '70',
    'menuNo': '432',
    'serviceSe': 'F00101',
    'stdrMg': '99999',
    'startDt': start_dt,
    'endDt': end_dt,
    'taElement': 'MIN',
    'taElement': 'AVG',
    'taElement': 'MAX',
    'stnGroupSns': '',
    'selectType': '1',
    'mddlClssCd': 'SFC01',
    'dataFormCd': 'F00513',
    'dataTypeCd': 'standard',
    'startDay': '20000701',
    'startYear': '2010',
    'endDay': '20200821',
    'endYear': '2020',
    'startMonth': '01',
    'endMonth': '12',
    'sesnCd': '0',
    'txtStnNm': '서울',
    'stnId': '108',
    'areaId':'', 
    'gFontSize':''
}

# print(f'Before urlencode : {values}')
params = urlencode(values)
# print(f"After urlencode : {params}")
# print("------------------------------------------")

API = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do"
url = API + "?" + params

response = urlopen(url)
data = response.read()

# print("Before decode response :", data)
text = data.decode("cp949")
# print("After decode response :", text)

with open(savename, mode ="wb") as f:
	f.write(data)
