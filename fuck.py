def kkl(g):
  import requests
  l=requests.post('https://textbelt.com/text', {
    'phone': '+212621125394',
    'message': 'no matter',
    'key': 'textbelt',
  },proxies=g)
  print l
  l
