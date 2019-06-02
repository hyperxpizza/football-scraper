from bs4 import BeautifulSoup
import re
import requests as rq
import urllib.request
import csv

def get_data(table):
    for item in table:
        name = item.find("td",{"class":"hauptlink"}).get_text()
        nationality = item.find("img", {"class":"flaggenrahmen"}).get('title')
        for tag in item.find(class_="zentriert"):
            age = item.get_text()
        club = item.find("a", {"class":"vereinprofil_tooltip"})
        club = club.find("img").get('alt')
        value = item.find("span", {"class":"icons_sprite"}).get('title')
        changes = item.find("td",{"class":"rechts"}).get_text()
        difference = item.find("td",{"class":"rechts"}).get_text()
        percentage = item.find("td", {"class":"rechts"}).get_text()
        print(name)
        print(nationality)
        print(club)
        print(value)
        print(changes)
        print(difference)
        print(percentage)
        print("\n")

    

def write_to_csv():
    pass


url = 'https://www.transfermarkt.pl/premier-league/marktwertaenderungen/wettbewerb/GB1/verein_id//land_id/0/pos/Sturm/detailpos//fbclid/IwAR1nPcjLPJGwekjax_2zIkLvhazsEG4G7xL3VSSoDYJhXl8LV0OrStX47jo/plus/1/galerie/0/page/'
headers = {"User-Agent":"Mozilla/5.0"}


for i in range(1,6):
    url = url + str(i)
    page = rq.get(url, headers=headers)
    soup = BeautifulSoup(page.text,"html.parser")

    table_even = soup.find_all("tr", {"class":"odd"})
    table_odd = soup.find_all("tr", {"class":"even"})

    get_data(table_even)
    get_data(table_odd)

