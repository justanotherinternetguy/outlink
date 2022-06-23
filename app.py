import requests
from bs4 import BeautifulSoup
import time
import random

base = requests.get(input("enter ur link: "))
soup_base = BeautifulSoup(base.text, 'html.parser')


for i in range(200):
    outgoing = []
    for link in soup_base.find_all('a'):
        outgoing.append(str(link.get('href')))

    # prune
    pruned = []
    for i in outgoing:
        if i[0:5] == "https":
            pruned.append(i)

    indx = random.randint(0, len(pruned)-1)
    print(pruned[indx], f"index: {indx}")
