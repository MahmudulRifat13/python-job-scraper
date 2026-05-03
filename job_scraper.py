import requests
from bs4 import BeautifulSoup
import csv
import time
import random
from datetime import datetime


def scrape_jobs(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("div", class_="card-content")

with open("all_jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location","Links","Time"])

    url="https://realpython.github.io/fake-jobs/"
    base_url="https://realpython.github.io/"
    jobs=scrape_jobs(url)

    count=0

    for j in jobs:
        title = j.find("h2", class_="title is-5").text.strip()
        company = j.find("h3", class_="subtitle is-6 company").text.strip()
        location = j.find("p", class_="location").text.strip()
        link = j.find_all("a")
        apply_link=""
        full_link = ""
        
        for l in link:
            if "Apply" in l.text:
                apply_link = l["href"]

                if apply_link.startswith("https"):
                    full_link = apply_link
                else:
                    full_link = base_url + apply_link

                break

        now = datetime.now().strftime("%Y-%m-%d %H:%M")   
        
        writer.writerow([title, company, location, full_link, now])
        count+=1

        

print("Total jobs found:", count)












#         print(title)
#         print(company)
#         print(location)
#         print(apply_link)
