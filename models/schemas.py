from pydantic import BaseModel
from typing import List, Optional


class JobSearchRequest(BaseModel):
    keywords: str
    location: Optional[str] = None
    paid_only: Optional[bool] = None


class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    paid: bool
    description: str


class CVSuggestionRequest(BaseModel):
    job_id: int
