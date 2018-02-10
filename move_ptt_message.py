#有寫網誌了
import requests
from bs4 import BeautifulSoup

#所要擷取的網站網址
url = 'https://www.ptt.cc/bbs/movie/M.1496375334.A.C6B.html'
#建立回應
response = requests.get(url)
#印出網站原始碼
#print(response.text)

#將原始碼做整理
soup = BeautifulSoup(response.text, 'lxml')
#使用find_all()找尋特定目標
articles = soup.find_all('div', 'push')

#寫入檔案中
with open('movie_message.txt','w') as f:
	for article in articles:
		#去除掉冒號和左右的空白
		messages = article.find('span','f3 push-content').getText().replace(':','').strip()
		print(messages)
		f.write(messages + "\n")
