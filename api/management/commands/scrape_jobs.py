from django.core.management.base import BaseCommand
import requests
from django.utils.dateparse import parse_datetime
from api.models import Job
from bs4 import BeautifulSoup

BASE_URL = "https://remoteok.com/api"

def parse_text(text):
    soup = BeautifulSoup(text, "html.parser")
    parse_text = soup.get_text(separator=" ", strip=True)
    return parse_text


class Command(BaseCommand):
    help = "Scrape jobs from RemoteOK API"

    def handle(self, *args, **kwargs):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()

        data = response.json()[1:]

        for item in data:
            title=item.get("position")
            company_logo = item.get("company_logo")
            defaults={
                "title": title,
                # "description": parse_text(item.get("description")),
                "description": item.get("description"),
                "company": item.get("company"),
                "position": item.get("position"),
                "url": item.get("url"),
                "tags": ", ".join(item.get("tags", [])),
                "location": item.get("location"),
                "salary_min": item.get("salary_min"),
                "salary_max": item.get("salary_max"),
                "posted_at": parse_datetime(item.get("date")),
            }
            if company_logo != "":
                defaults["company_logo"] = company_logo

            if title:
                Job.objects.update_or_create(
                    job_id = item.get("id"),
                    defaults=defaults
                )
        self.stdout.write(self.style.SUCCESS(f"{Job.objects.count()} jobs scraped successfully"))
