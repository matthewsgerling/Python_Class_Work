import requests
from bs4 import BeautifulSoup

url = "https://dmacc.blackboard.com/webapps/blackboard/content/listContent.jsp?course_id=_82063_1&content_id=_4799677_1"
response = requests.get(url)
html = requests.get(url)
f = open("requestsResult.txt", "w+")
f.writelines((str(html)))
f.close()

soup = BeautifulSoup(open("requestsResult.txt"), 'html.parser')
print(soup.prettify())
