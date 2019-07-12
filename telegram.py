import requests
from pprint import pprint

from decouple import config  # python 환경변수 관리하는 패키지
# 1. 토큰 및 기본 url 설정
token = config('TELEGRAM_TOKEN')  # .env 설정값 가져오기
base_url = f"https://api.telegram.org/bot{token}/"

# 2. getUpdates 정보 가져오기
responses = requests.get(base_url+"getUpdates").json()
# pprint(responses)

# 3. 나의 chat_id 가져오기
# chat_id = responses['result'][1]['message']['chat']['id']
chat_id = responses.get('result')[0].get('message').get('chat').get('id')
# 715985641

# 4. chat_id에 메시지 보내기
# 4-1. 요청보낼 URL 만들기
text = '안녕?'
api_url = f'{base_url}sendMessage?chat_id={chat_id}&text={text}'

# 4-2. requests로 보내기
requests.get(api_url)