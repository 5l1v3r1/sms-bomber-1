import fuck
kl=open('58017.txt','r').read()
for item in kl.split('\n'):
  try:
    k=item.split(' ')[0]
  except:
    k=item
  ko={"http":'http://'+k}
  fuck.kkl(ko)