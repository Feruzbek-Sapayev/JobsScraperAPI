import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://remoteok.com"

def get_jobs_from_page(page=1):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"{BASE_URL}/?page={page}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_row in soup.find_all("tr", class_="job"):
        title_tag = job_row.find("h2")
        company_tag = job_row.find("h3")
        link_tag = job_row.find("a", class_="preventLink")

        if not (title_tag and company_tag and link_tag):
            continue

        jobs.append({
            "title": title_tag.get_text(strip=True),
            "company": company_tag.get_text(strip=True),
            "link": BASE_URL + link_tag.get("href"),
        })

    return jobs

def scrape_all_jobs(max_pages=5, delay=1):
    all_jobs = []
    for page in range(1, max_pages + 1):
        jobs = get_jobs_from_page(page)
        if not jobs:
            break  # keyingi sahifa yo‘q bo‘lsa to‘xtaymiz
        all_jobs.extend(jobs)
        print(f"Page {page}: {len(jobs)} jobs found.")
        time.sleep(delay)  # saytni bosmaslik uchun kutish

    return all_jobs

if __name__ == "__main__":
    jobs = scrape_all_jobs(max_pages=10)  # 10 sahifagacha yuklaymiz
    for j in jobs:
        print(j)
    print(f"Total jobs: {len(jobs)}")
