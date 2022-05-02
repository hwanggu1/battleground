import requests
import sys
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
file_name = sys.argv[1]

#print(sys.argv[1])

URL = 'https://pubg.op.gg/user/'+file_name
res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup)

soup = str(soup)

html_file = open(file_name+'.html', 'w', encoding='utf-8', errors='ignore')
html_file.write(soup)
html_file.close()