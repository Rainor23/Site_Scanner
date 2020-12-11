import requests 
from bs4 import BeautifulSoup 


URL = "http://rainerinfosec.com"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html.parser') 

href_Arr = []
for link in soup.find_all('a', href=True, text=True):
    href_Arr.append(link['href'])
print('Starting search.... \n')
print(f'''URLS found on webpage {URL} \n
============================================== \n''')
print('\n'.join(href_Arr))