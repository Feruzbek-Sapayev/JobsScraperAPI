import requests

def get_jobs():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get("https://remoteok.com/api", headers=headers)
    response.raise_for_status()

    data = response.json()
    jobs = data[1:]
    job_list = []
    for job in jobs:
        print(job)
        break
        job_list.append({
            "job_id": job.get("id"),
            "title": job.get("position"),
            "description": job.get("description"),
            "company": job.get("company"),
            "company_logo": job.get("company_logo"),
            "position": job.get("position"),
            "link": job.get("url"),
            "tags": job.get("tags"),
            "location": job.get("location"),
            "date": job.get("date"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
        })
    return job_list

if __name__ == "__main__":
    jobs = get_jobs()
    for j in jobs:
        print(j)
    print(len(jobs))

