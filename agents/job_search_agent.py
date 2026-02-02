import requests
from config import SERPAPI_KEY, GOOGLE_JOBS_ENGINE, DEFAULT_LOCATION


class JobSearchAgent:
    def __init__(self):
        self.base_url = "https://serpapi.com/search"

    def search_jobs(self, keywords: str, location: str = None):
        """
        Search jobs using Google Jobs (aggregates LinkedIn, Indeed, etc.)
        """
        params = {
            "engine": GOOGLE_JOBS_ENGINE,
            "q": keywords,
            "location": location or DEFAULT_LOCATION,
            "api_key": SERPAPI_KEY
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        jobs = []
        for idx, job in enumerate(data.get("jobs_results", []), start=1):
            jobs.append({
                "id": idx,
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "paid": self._is_paid(job),
                "description": job.get("description", ""),
                "apply_link": job.get("related_links", [{}])[0].get("link"),
                "source": job.get("via")  # LinkedIn / Indeed / etc.
            })

        return jobs

    def _is_paid(self, job):
        """
        Heuristic: internships mentioning stipend/salary
        """
        text = (job.get("description") or "").lower()
        keywords = ["stipend", "salary", "paid", "ctc", "per month"]
        return any(k in text for k in keywords)
