from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib
import requests
import codecs

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup2 = BeautifulSoup(body, 'html.parser')
    texts = soup2.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

url = raw_input("Enter full website to extract the URL's from: ")

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

for link in (a for a in soup.find_all('a') if a is not "#"):
	links = link.get('href')
	html = urllib.urlopen(links).read()
	print(text_from_html(html))
	print(links)
	f = codecs.open("textout.txt", "a", encoding="utf-8") 
	f.write(text_from_html(html))
	f.close()