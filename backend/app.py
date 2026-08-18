from typing import Annotated

from fastapi import (
    FastAPI,
    File,
    Form,
    HTTPException,
    UploadFile,
)

from fastapi.middleware.cors import CORSMiddleware

from backend.resume_parser import (
    ResumeParserError,
    extract_resume_text,
)

from backend.resume_analyzer import (
    analyze_resume,
)


# =========================================================
# APPLICATION CONFIGURATION
# =========================================================

APP_NAME = "AI Resume Analyzer API"
APP_VERSION = "1.0.0"


app = FastAPI(
    title=APP_NAME,
    description=(
        "AI-powered resume analysis, job matching, "
        "ATS evaluation and career recommendations."
    ),
    version=APP_VERSION,
)


# =========================================================
# CORS CONFIGURATION
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
async def root():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
        "message": "AI Resume Analyzer backend is online.",
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "resume-analyzer-backend",
    }


# =========================================================
# RESUME PARSING ENDPOINT
# =========================================================

@app.post("/parse-resume")
async def parse_resume(
    resume: Annotated[
        UploadFile,
        File(description="Resume PDF or DOCX file"),
    ],
):
    """
    Upload a resume and extract its text.

    Supported:
    - PDF
    - DOCX
    """

    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided.",
        )

    try:
        file_bytes = await resume.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty.",
            )

        text = extract_resume_text(
            filename=resume.filename,
            file_bytes=file_bytes,
        )

        return {
            "success": True,
            "filename": resume.filename,
            "characters_extracted": len(text),
            "text": text,
        }

    except ResumeParserError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unexpected error while processing resume.",
        ) from exc

    finally:
        await resume.close()


# =========================================================
# AI RESUME ANALYSIS ENDPOINT
# =========================================================

@app.post("/analyze")
async def analyze_resume_endpoint(
    resume: Annotated[
        UploadFile,
        File(description="Resume PDF or DOCX file"),
    ],
    job_description: Annotated[
        str,
        Form(description="Target job description"),
    ],
):
    """
    Analyze an uploaded resume against a target
    job description using the GenAI engine.
    """

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Resume filename is missing.",
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty.",
        )

    try:
        # -------------------------------------------------
        # READ RESUME
        # -------------------------------------------------

        file_bytes = await resume.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded resume is empty.",
            )

        # -------------------------------------------------
        # EXTRACT TEXT
        # -------------------------------------------------

        resume_text = extract_resume_text(
            filename=resume.filename,
            file_bytes=file_bytes,
        )

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail=(
                    "Could not extract readable text "
                    "from the resume."
                ),
            )

        # -------------------------------------------------
        # AI ANALYSIS
        # -------------------------------------------------

        analysis = analyze_resume(
            resume_text=resume_text,
            job_description=job_description,
        )

        # -------------------------------------------------
        # RESPONSE
        # -------------------------------------------------

        return {
            "success": True,
            "filename": resume.filename,
            "analysis": analysis.model_dump(),
        }

    # -----------------------------------------------------
    # KNOWN RESUME PARSER ERROR
    # -----------------------------------------------------

    except ResumeParserError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    # -----------------------------------------------------
    # VALIDATION ERROR
    # -----------------------------------------------------

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    # -----------------------------------------------------
    # HTTP ERROR
    # -----------------------------------------------------

    except HTTPException:
        raise

    # -----------------------------------------------------
    # UNEXPECTED ERROR
    # -----------------------------------------------------

    except Exception as exc:

        print(
            f"[AI ANALYSIS ERROR] {type(exc).__name__}: {exc}"
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "AI analysis failed. "
                "Check the backend terminal for details."
            ),
        ) from exc

    finally:
        await resume.close()