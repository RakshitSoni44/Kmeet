from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List

from agents.job_search_agent import JobSearchAgent
from agents.filter_agent import FilterAgent
from agents.cv_analyzer_agent import CVAnalyzerAgent
from agents.cv_suggestion_agent import CVSuggestionAgent

from utils.file_loader import load_cv_text
from models.schemas import JobSearchRequest, Job

app = FastAPI(
    title="Job & Internship Search – Agentic AI",
    description="Search jobs, apply filters, and get AI-powered CV suggestions",
    version="1.0.0"
)

# Initialize agents
job_search_agent = JobSearchAgent()
filter_agent = FilterAgent()
cv_analyzer_agent = CVAnalyzerAgent()
cv_suggestion_agent = CVSuggestionAgent()

# Temporary in-memory cache (replace with DB later)
cached_jobs: List[dict] = []


@app.post("/search-jobs", response_model=List[Job])
def search_jobs(request: JobSearchRequest):
    """
    1. Search jobs using keywords
    2. Apply filters (location, paid/unpaid)
    3. Return filtered job list
    """
    global cached_jobs

    jobs = job_search_agent.search_jobs(
        keywords=request.keywords,
        location=request.location
    )

    filtered_jobs = filter_agent.apply_filters(
        jobs=jobs,
        location=request.location,
        paid_only=request.paid_only
    )

    cached_jobs = filtered_jobs
    return filtered_jobs


@app.post("/cv-suggestions")
def generate_cv_suggestions(
    job_id: int,
    cv: UploadFile = File(...)
):
    """
    1. User selects a job
    2. Uploads CV
    3. AI generates job-specific CV bullet points
    """
    if not cached_jobs:
        raise HTTPException(
            status_code=400,
            detail="No jobs found. Please search jobs first."
        )

    job = next((job for job in cached_jobs if job["id"] == job_id), None)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Selected job not found."
        )

    cv_text = load_cv_text(cv.file)
    cv_insights = cv_analyzer_agent.analyze(cv_text)
    suggestions = cv_suggestion_agent.generate(job, cv_insights)

    return {
        "job_title": job["title"],
        "company": job["company"],
        "suggested_cv_points": suggestions
    }


@app.get("/")
def health_check():
    return {"status": "Job Agent API is running"}
