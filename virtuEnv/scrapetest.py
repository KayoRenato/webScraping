from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
  html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as err:
  print(err)
except URLError as err:
  print('The server could not be found!')
else:
  print('It Worked!')