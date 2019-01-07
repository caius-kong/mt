# -*- coding: utf-8 -*-
import os, requests, uuid, json

deploy_languages = ['zh']

if 'TRANSLATOR_TEXT_KEY' in os.environ:
    subscriptionKey = os.environ['TRANSLATOR_TEXT_KEY']
else:
    print('Environment variable for TRANSLATOR_TEXT_KEY is not set.')
    exit()

base_url = 'https://api.cognitive.microsofttranslator.com'

headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# 获取支持的语言
# request = requests.get(base_url + '/languages?api-version=3.0', headers=headers)
# response = request.json()
# print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))

## 翻译文本
# 最多可以有 25 个元素
body = [{
    'text': 'Cisco ICS doesnt support upgrade from the installed version.'
}]
# to是必选参数，其他都可选。category指定部署的自定义翻译，默认general; textType指定是否作为html翻译，默认plain
to_params = ''
for lang in deploy_languages:
    to_params += '&to=' + lang
params = '&from=en%s&textType=html&category=0c9c6bb9-6d48-4855-9aab-5cf2e501acef-TECH' % to_params
request = requests.post(base_url + '/translate?api-version=3.0'+params, headers=headers, json=body)
response = request.json()
print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))



