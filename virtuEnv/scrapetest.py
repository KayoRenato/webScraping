from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as err:
    return 'HTTPErrror'
  except URLError as err:
    return 'URLErrror'
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.notag
  except AttributeError as err:
    return 
  return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
  print('Tag was not found!')
else:
  print(title)
