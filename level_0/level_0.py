import sys
import requests

url = "http://158.69.76.135/level0.php"
repetition = 1024
id = 2696

for i in range(repetition):
    requests.post(url, data={'id': id, 'holdthedoor': 'pinging'})
