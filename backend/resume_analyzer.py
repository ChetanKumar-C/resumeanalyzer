import os
from typing import List

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from backend.prompts.prompts import (
    RESUME_ANALYSIS_SYSTEM_PROMPT,
    RESUME_ANALYSIS_USER_PROMPT,
)


# =========================================================
# ENVIRONMENT CONFIGURATION
# =========================================================

load_dotenv(".env", override=True)

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN was not found. "
        "Make sure it exists in C:\\Resumeanalyzer\\.env"
    )


# =========================================================
# DATA MODELS
# =========================================================

class Education(BaseModel):
    degree: str = Field(
        description="Degree or qualification"
    )

    institution: str = Field(
        description="Institution name"
    )

    year: str = Field(
        description="Year or duration if available"
    )


class Experience(BaseModel):
    role: str = Field(
        description="Job or internship role"
    )

    organization: str = Field(
        description="Company or organization"
    )

    duration: str = Field(
        description="Employment duration if available"
    )

    description: str = Field(
        description="Short description of the work performed"
    )


class Project(BaseModel):
    name: str = Field(
        description="Project name"
    )

    description: str = Field(
        description="Short description of the project"
    )

    technologies: List[str] = Field(
        default_factory=list,
        description="Technologies used in the project"
    )


class ResumeAnalysis(BaseModel):

    candidate_name: str = Field(
        description=(
            "Candidate's full name. "
            "Return 'Unknown' if unavailable."
        )
    )

    professional_summary: str = Field(
        description=(
            "Concise professional summary based only "
            "on information present in the resume."
        )
    )

    technical_skills: List[str] = Field(
        default_factory=list
    )

    soft_skills: List[str] = Field(
        default_factory=list
    )

    education: List[Education] = Field(
        default_factory=list
    )

    experience: List[Experience] = Field(
        default_factory=list
    )

    projects: List[Project] = Field(
        default_factory=list
    )

    certifications: List[str] = Field(
        default_factory=list
    )

    achievements: List[str] = Field(
        default_factory=list
    )

    strengths: List[str] = Field(
        default_factory=list
    )

    weaknesses: List[str] = Field(
        default_factory=list
    )

    ats_issues: List[str] = Field(
        default_factory=list
    )

    recommendations: List[str] = Field(
        default_factory=list
    )


# =========================================================
# HUGGING FACE MODEL
# =========================================================

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
    temperature=0,
    max_tokens=3000,
    timeout=120,
    max_retries=2,
)


# =========================================================
# STRUCTURED OUTPUT
# =========================================================

structured_llm = llm.with_structured_output(
    ResumeAnalysis
)


# =========================================================
# PROMPT
# =========================================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            RESUME_ANALYSIS_SYSTEM_PROMPT,
        ),
        (
            "human",
            RESUME_ANALYSIS_USER_PROMPT,
        ),
    ]
)


# =========================================================
# LANGCHAIN PIPELINE
# =========================================================

analysis_chain = prompt | structured_llm


# =========================================================
# PUBLIC FUNCTION
# =========================================================

def analyze_resume(
    resume_text: str,
    job_description: str,
) -> ResumeAnalysis:

    resume_text = resume_text.strip()
    job_description = job_description.strip()

    if not resume_text:
        raise ValueError(
            "Resume text cannot be empty."
        )

    if not job_description:
        raise ValueError(
            "Job description cannot be empty."
        )

    result = analysis_chain.invoke(
        {
            "resume_text": resume_text,
            "job_description": job_description,
        }
    )

    return result