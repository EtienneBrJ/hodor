import sys
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level1.php"
repetition = 4096
id = 2696

for i in range(repetition):
    session = requests.session()
    link = session.get(url)
    doc = link.content
    tag = BeautifulSoup(doc, 'html.parser')
    key = tag.find("input", {"name": "key"})
    ke = key.get("value")
    session.post(url, data={'id': id, 'holdthedoor': 'submit', 'key': ke})
    


