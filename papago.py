import requests
from decouple import config
from pprint import pprint
# 1. 네이버 API 설정
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
# 2. URL 설정
naver_url = 'https://openapi.naver.com/v1/papago/n2mt'
# 3. 요청보내기! POST
headers = {'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
        }
data = {
    'source': 'ko',
    'target': 'en',
    'text': '결코 다시 전쟁'
}

# data = {
#     'source': 'en',
#     'target': 'ko',
#     'text': 'War never again! Never again war!'
# }

response = requests.post(naver_url, headers=headers, data=data).json()
pprint(response)
text = response.get('message').get('result').get('translatedText')
print(text)