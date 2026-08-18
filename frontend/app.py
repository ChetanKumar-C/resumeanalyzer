import streamlit as st
import plotly.graph_objects as go
import time
import textwrap

# ============================================================
# PAGE CONFIGURATION
# ============================================================
def render_html(html, **kwargs):
    st.html(textwrap.dedent(html))
    
st.set_page_config(
    page_title="ResumateAI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 80% 15%,
            rgba(101, 56, 255, 0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 15% 45%,
            rgba(0, 150, 255, 0.06),
            transparent 25%
        ),
        #05060d;

    color: #ffffff;
}

/* Remove Streamlit padding */

.block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit UI */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ==========================================================
   NAVBAR
========================================================== */

.navbar {
    height: 70px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    border-bottom: 1px solid rgba(255,255,255,0.08);

    margin-bottom: 20px;
}

.logo {
    font-size: 23px;
    font-weight: 800;

    letter-spacing: -0.5px;
}

.logo-ai {
    color: #9b5cff;
}

.logo-star {
    color: #7b5cff;
    margin-left: 4px;
}

.nav-center {
    display: flex;
    gap: 38px;

    color: #a5a8b8;

    font-size: 14px;
}

.nav-active {
    color: #ffffff;

    border-bottom: 2px solid #8b5cf6;

    padding-bottom: 8px;
}

.nav-button {
    background: linear-gradient(
        90deg,
        #7c3aed,
        #2563eb
    );

    padding: 11px 20px;

    border-radius: 10px;

    font-weight: 600;

    font-size: 14px;

    box-shadow:
        0 0 25px rgba(124,58,237,0.3);
}

/* ==========================================================
   HERO
========================================================== */

.hero {
    padding: 70px 0 55px 0;
}

.hero-badge {
    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding: 8px 15px;

    border-radius: 30px;

    background: rgba(124,58,237,0.10);

    border: 1px solid rgba(139,92,246,0.25);

    color: #c4b5fd;

    font-size: 12px;

    font-weight: 600;

    letter-spacing: 0.4px;
}

.hero-title {
    font-size: 55px;

    line-height: 1.08;

    font-weight: 800;

    letter-spacing: -2px;

    margin-top: 20px;

    margin-bottom: 20px;
}

.gradient-text {
    background:
        linear-gradient(
            90deg,
            #a855f7,
            #6366f1,
            #22d3ee
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #9ca3b5;

    font-size: 17px;

    line-height: 1.8;

    max-width: 570px;
}

/* ==========================================================
   HERO FEATURE ITEMS
========================================================== */

.feature-row {
    display: flex;

    gap: 35px;

    margin-top: 35px;
}

.feature-item {
    display: flex;

    gap: 12px;

    align-items: flex-start;

    width: 150px;
}

.feature-icon {
    width: 38px;

    height: 38px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 10px;

    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,0.25),
            rgba(37,99,235,0.12)
        );

    border: 1px solid rgba(139,92,246,0.25);

    font-size: 18px;
}

.feature-title {
    font-size: 13px;

    font-weight: 600;

    margin-bottom: 4px;
}

.feature-description {
    font-size: 11px;

    color: #777c91;

    line-height: 1.5;
}

/* ==========================================================
   HERO VISUAL
========================================================== */

.resume-visual {
    height: 350px;

    position: relative;

    display: flex;

    justify-content: center;

    align-items: center;
}

.resume-glow {
    position: absolute;

    width: 250px;

    height: 250px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(124,58,237,0.35),
            transparent 65%
        );

    filter: blur(15px);
}

.resume-card {
    width: 210px;

    height: 280px;

    transform: rotate(7deg);

    border-radius: 14px;

    background:
        linear-gradient(
            145deg,
            #17152c,
            #0c1020
        );

    border: 1px solid rgba(139,92,246,0.65);

    box-shadow:
        0 0 40px rgba(124,58,237,0.25),
        0 0 90px rgba(37,99,235,0.12);

    padding: 25px;

    z-index: 2;
}

.resume-avatar {
    width: 42px;

    height: 42px;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #8b5cf6,
            #2563eb
        );

    margin-bottom: 20px;
}

.resume-line {
    height: 7px;

    border-radius: 10px;

    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #2563eb
        );

    margin-bottom: 13px;

    opacity: 0.8;
}

.resume-line.small {
    width: 55%;
}

.resume-line.medium {
    width: 75%;
}

.resume-line.full {
    width: 95%;
}

/* Floating badges */

.floating-badge {
    position: absolute;

    padding: 12px 17px;

    border-radius: 12px;

    background:
        rgba(12,15,30,0.88);

    border: 1px solid rgba(139,92,246,0.35);

    backdrop-filter: blur(10px);

    font-size: 12px;

    z-index: 5;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.35);
}

.badge-ai {
    top: 20px;

    left: 20px;

    color: #c4b5fd;
}

.badge-score {
    right: 10px;

    top: 80px;

    color: #5eead4;
}

.badge-smart {
    left: 5px;

    bottom: 45px;

    color: #67e8f9;
}

.badge-result {
    right: 5px;

    bottom: 40px;

    color: #d8b4fe;
}

/* ==========================================================
   INPUT SECTION
========================================================== */

.input-section {
    margin-top: 20px;

    padding: 28px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(18,20,36,0.95),
            rgba(10,12,23,0.95)
        );

    border: 1px solid rgba(255,255,255,0.09);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.25);
}

.input-header {
    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 6px;
}

.input-icon {
    width: 35px;

    height: 35px;

    border-radius: 9px;

    background:
        rgba(124,58,237,0.15);

    border: 1px solid rgba(139,92,246,0.25);

    display: flex;

    align-items: center;

    justify-content: center;
}

.input-title {
    font-size: 16px;

    font-weight: 700;
}

.input-subtitle {
    color: #777c91;

    font-size: 12px;

    margin-bottom: 20px;
}

/* Upload box */

.upload-box {
    min-height: 190px;

    border: 1px dashed rgba(139,92,246,0.45);

    border-radius: 13px;

    background:
        rgba(10,12,24,0.65);

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;
}

.upload-icon {
    font-size: 40px;

    color: #a855f7;

    margin-bottom: 10px;
}

.upload-text {
    font-size: 14px;

    font-weight: 600;
}

.upload-info {
    color: #6f7488;

    font-size: 11px;

    margin-top: 5px;
}

/* ==========================================================
   STREAMLIT FILE UPLOADER
========================================================== */

[data-testid="stFileUploader"] {

    background: transparent !important;

}

[data-testid="stFileUploaderDropzone"] {

    background:
        rgba(10,12,24,0.7) !important;

    border:
        1px dashed rgba(139,92,246,0.45) !important;

    border-radius: 13px !important;

}

[data-testid="stFileUploaderDropzoneInstructions"] {

    color: #a5a8b8 !important;

}

[data-testid="stFileUploaderDropzone"] button {

    background:
        transparent !important;

    color:
        #c4b5fd !important;

    border:
        1px solid rgba(139,92,246,0.6) !important;

    border-radius: 8px !important;

}

/* ==========================================================
   TEXT AREA
========================================================== */

[data-testid="stTextArea"] textarea {

    background:
        rgba(8,10,20,0.85) !important;

    color: #e5e7eb !important;

    border:
        1px solid rgba(255,255,255,0.10) !important;

    border-radius: 12px !important;

}

[data-testid="stTextArea"] textarea:focus {

    border:
        1px solid #8b5cf6 !important;

    box-shadow:
        0 0 15px rgba(139,92,246,0.15) !important;

}

/* ==========================================================
   ANALYZE BUTTON
========================================================== */

.analyze-button button {

    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #a855f7,
            #2563eb
        ) !important;

    color: white !important;

    border: none !important;

    height: 54px !important;

    border-radius: 11px !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 10px 35px rgba(124,58,237,0.25);
}

/* ==========================================================
   SECURITY
========================================================== */

.security-text {

    color: #74798c;

    font-size: 11px;

    margin-top: 10px;
}

/* ==========================================================
   BENEFIT BAR
========================================================== */

.benefit-bar {

    margin-top: 20px;

    padding: 22px;

    border-radius: 15px;

    background:
        rgba(14,16,29,0.9);

    border: 1px solid rgba(255,255,255,0.07);

    display: flex;

    justify-content: space-between;
}

.benefit {

    display: flex;

    gap: 12px;

    align-items: center;

    width: 24%;

    border-right:
        1px solid rgba(255,255,255,0.08);

    padding-left: 15px;
}

.benefit:last-child {

    border-right: none;

}

.benefit-icon {

    font-size: 23px;

}

.benefit-title {

    font-size: 12px;

    font-weight: 700;

}

.benefit-text {

    color: #6f7488;

    font-size: 10px;

    margin-top: 3px;

}

/* ==========================================================
   RESULTS
========================================================== */

.results-container {

    margin-top: 25px;

    padding: 28px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(15,18,34,0.98),
            rgba(8,10,20,0.98)
        );

    border:
        1px solid rgba(255,255,255,0.08);

}

.results-header {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 25px;

}

.results-title {

    font-size: 20px;

    font-weight: 700;

}

.results-subtitle {

    color: #72778a;

    font-size: 11px;

}

/* ==========================================================
   RESULT CARDS
========================================================== */

.result-card {

    background:
        rgba(12,15,28,0.85);

    border:
        1px solid rgba(255,255,255,0.07);

    border-radius: 14px;

    padding: 20px;

    min-height: 150px;

}

.result-card-title {

    font-size: 13px;

    font-weight: 700;

    margin-bottom: 15px;

}

.result-card-icon {

    margin-right: 8px;

}

/* ==========================================================
   SKILLS
========================================================== */

.skill-match {

    display: inline-block;

    padding: 6px 10px;

    margin: 3px;

    border-radius: 20px;

    background:
        rgba(16,185,129,0.10);

    border:
        1px solid rgba(16,185,129,0.20);

    color: #5eead4;

    font-size: 10px;

}

.skill-missing {

    display: inline-block;

    padding: 6px 10px;

    margin: 3px;

    border-radius: 20px;

    background:
        rgba(239,68,68,0.10);

    border:
        1px solid rgba(239,68,68,0.20);

    color: #fca5a5;

    font-size: 10px;

}

/* ==========================================================
   RECOMMENDATIONS
========================================================== */

.recommendation {

    padding: 12px;

    border-bottom:
        1px solid rgba(255,255,255,0.06);

    color: #aeb2c2;

    font-size: 11px;

}

.recommendation-number {

    display: inline-flex;

    width: 23px;

    height: 23px;

    border-radius: 50%;

    align-items: center;

    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #6366f1
        );

    color: white;

    margin-right: 8px;

}

/* ==========================================================
   FOOTER
========================================================== */

.footer {

    text-align: center;

    color: #555a6d;

    font-size: 11px;

    padding-top: 50px;

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================

render_html("""
<div class="navbar">

    <div class="logo">
        ✦ Resumate<span class="logo-ai">AI</span>
    </div>

    <div class="nav-center">

        <div class="nav-active">
            Home
        </div>

        <div>
            How it Works
        </div>

        <div>
            Features
        </div>

        <div>
            About
        </div>

    </div>

    <div class="nav-button">
        ✦ Get Started
    </div>

</div>
""")


# ============================================================
# HERO
# ============================================================

hero_left, hero_right = st.columns([1.1, 1], gap="large")


with hero_left:

    render_html("""
    <div class="hero">

        <div class="hero-badge">
            ✦ GENAI POWERED
        </div>

        <div class="hero-title">

            Build a Resume<br>

            That
            <span class="gradient-text">
                Gets You Hired.
            </span>

        </div>

        <div class="hero-description">

            Analyze your resume, match it with job requirements,
            and get AI-powered recommendations to land your
            dream job.

        </div>

        <div class="feature-row">

            <div class="feature-item">

                <div class="feature-icon">
                    ◎
                </div>

                <div>

                    <div class="feature-title">
                        ATS Score
                    </div>

                    <div class="feature-description">
                        Get an ATS score for your resume
                    </div>

                </div>

            </div>


            <div class="feature-item">

                <div class="feature-icon">
                    ✓
                </div>

                <div>

                    <div class="feature-title">
                        Job Match
                    </div>

                    <div class="feature-description">
                        See how well you match the job
                    </div>

                </div>

            </div>


            <div class="feature-item">

                <div class="feature-icon">
                    ✦
                </div>

                <div>

                    <div class="feature-title">
                        AI Insights
                    </div>

                    <div class="feature-description">
                        Get smart AI recommendations
                    </div>

                </div>

            </div>

        </div>

    </div>
    """)


with hero_right:

    render_html("""
    <div class="resume-visual">

        <div class="resume-glow"></div>

        <div class="floating-badge badge-ai">
            ✦ AI Powered
        </div>

        <div class="floating-badge badge-score">
            98%<br>
            <small>Accuracy</small>
        </div>

        <div class="floating-badge badge-smart">
            ✦ Smart<br>
            Analysis
        </div>

        <div class="floating-badge badge-result">
            ⚡ Instant<br>
            Results
        </div>

        <div class="resume-card">

            <div class="resume-avatar"></div>

            <div class="resume-line full"></div>

            <div class="resume-line medium"></div>

            <br>

            <div class="resume-line full"></div>

            <div class="resume-line medium"></div>

            <div class="resume-line small"></div>

            <br>

            <div class="resume-line full"></div>

            <div class="resume-line full"></div>

            <div class="resume-line medium"></div>

            <div class="resume-line small"></div>

        </div>

    </div>
    """)


# ============================================================
# INPUT SECTION
# ============================================================

render_html("""
<div class="input-section">

    <div class="input-header">

        <div class="input-icon">
            📄
        </div>

        <div class="input-title">
            Upload Your Resume
        </div>

    </div>

    <div class="input-subtitle">
        Upload your latest resume in PDF or DOCX format
    </div>

</div>
""")


input_left, input_right = st.columns(2, gap="large")


with input_left:

    resume = st.file_uploader(
        "Resume",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )

    if resume:

        st.success(
            f"✓ {resume.name} uploaded"
        )


with input_right:

    render_html("""
    <div class="input-header">

        <div class="input-icon">
            💼
        </div>

        <div class="input-title">
            Job Description
        </div>

    </div>

    <div class="input-subtitle">
        Paste the job description you're applying for
    </div>
    """)

    job_description = st.text_area(
        "Job Description",
        placeholder="Paste job description here...",
        height=170,
        label_visibility="collapsed"
    )


render_html("""
<div class="security-text">
    🔒 Your data is secure and confidential
</div>
""")


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.write("")

analyze = st.button(
    "✦  Analyze My Resume        →",
    use_container_width=True
)


# ============================================================
# BENEFITS
# ============================================================

render_html("""
<div class="benefit-bar">

    <div class="benefit">

        <div class="benefit-icon">
            🛡️
        </div>

        <div>

            <div class="benefit-title">
                Secure & Private
            </div>

            <div class="benefit-text">
                Your data stays confidential
            </div>

        </div>

    </div>


    <div class="benefit">

        <div class="benefit-icon">
            ⚡
        </div>

        <div>

            <div class="benefit-title">
                Instant Analysis
            </div>

            <div class="benefit-text">
                Results in seconds
            </div>

        </div>

    </div>


    <div class="benefit">

        <div class="benefit-icon">
            📊
        </div>

        <div>

            <div class="benefit-title">
                Detailed Insights
            </div>

            <div class="benefit-text">
                Actionable recommendations
            </div>

        </div>

    </div>


    <div class="benefit">

        <div class="benefit-icon">
            ✦
        </div>

        <div>

            <div class="benefit-title">
                Improve & Grow
            </div>

            <div class="benefit-text">
                Increase your chances
            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MOCK BACKEND DATA
# ============================================================

def analyze_resume():

    time.sleep(2)

    return {

        "score": 87,

        "match": 91,

        "matched": 12,

        "missing_count": 4,

        "matched_skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Data Analysis",
            "Git",
            "Problem Solving",
            "Statistics",
            "Jupyter",
            "Matplotlib"
        ],

        "missing_skills": [
            "AWS",
            "Docker",
            "REST APIs",
            "Django"
        ],

        "strengths": [
            "Strong technical foundation",
            "Good problem solving abilities",
            "Relevant projects and experience",
            "Well structured sections"
        ],

        "improvements": [
            "Add more quantifiable achievements",
            "Include relevant certifications",
            "Improve professional summary",
            "Add cloud or deployment experience"
        ],

        "recommendations": [
            "Add measurable results to your project descriptions.",
            "Include AWS or cloud deployment experience if applicable.",
            "Highlight REST API development experience.",
            "Improve the professional summary to make it more impactful.",
            "Add relevant certifications to boost credibility."
        ]
    }


# ============================================================
# RESULTS
# ============================================================

if analyze:

    if resume is None:

        st.error("Please upload your resume.")

    elif not job_description.strip():

        st.error("Please enter the job description.")

    else:

        with st.spinner("✦ AI is analyzing your resume..."):

            result = analyze_resume()

        render_html("""
        <div class="results-container">

            <div class="results-header">

                <div>

                    <div class="results-title">
                        📊 Your Resume Analysis
                    </div>

                    <div class="results-subtitle">
                        Here's how your resume performed
                    </div>

                </div>

            </div>

        </div>
        """)

        # ----------------------------------------------------
        # METRICS
        # ----------------------------------------------------

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "ATS SCORE",
                f'{result["score"]}/100'
            )

        with c2:

            st.metric(
                "JOB MATCH",
                f'{result["match"]}%'
            )

        with c3:

            st.metric(
                "SKILLS MATCHED",
                result["matched"]
            )

        with c4:

            st.metric(
                "SKILLS MISSING",
                result["missing_count"]
            )


        # ----------------------------------------------------
        # SCORE GAUGE
        # ----------------------------------------------------

        st.write("")

        gauge_col, summary_col = st.columns([1, 2])


        with gauge_col:

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",

                    value=result["score"],

                    number={
                        "font": {
                            "color": "white",
                            "size": 42
                        }
                    },

                    gauge={

                        "axis": {
                            "range": [0, 100],
                            "tickcolor": "#666"
                        },

                        "bar": {
                            "color": "#a855f7"
                        },

                        "bgcolor": "#111426",

                        "bordercolor": "#292d45",

                        "steps": [
                            {
                                "range": [0, 50],
                                "color": "#171a2b"
                            },
                            {
                                "range": [50, 75],
                                "color": "#1b1e30"
                            },
                            {
                                "range": [75, 100],
                                "color": "#20233a"
                            }
                        ]
                    }
                )
            )

            fig.update_layout(
                height=280,

                paper_bgcolor="rgba(0,0,0,0)",

                font={
                    "color": "white"
                },

                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={"displayModeBar": False}
            )


        with summary_col:

            render_html("""
            <div class="result-card">

                <div class="result-card-title">
                    ⭐ Overall Rating
                </div>

                <h2 style="color:#4ade80;">
                    Excellent
                </h2>

                <p style="color:#85899c; font-size:13px; line-height:1.7;">

                    Your resume is strong and matches the
                    target position well. A few targeted
                    improvements can make it even stronger.

                </p>

            </div>
            """)


        # ----------------------------------------------------
        # SKILLS
        # ----------------------------------------------------

        st.markdown("### 🛠 Skills Analysis")

        skill_col, missing_col = st.columns(2)


        with skill_col:

            skills_html = ""

            for skill in result["matched_skills"]:

                skills_html += (
                    f'<span class="skill-match">'
                    f'{skill}'
                    f'</span>'
                )

            render_html(
                f"""
                <div class="result-card">

                    <div class="result-card-title">
                        🟢 Matched Skills
                    </div>

                    {skills_html}

                </div>
                """
            )


        with missing_col:

            missing_html = ""

            for skill in result["missing_skills"]:

                missing_html += (
                    f'<span class="skill-missing">'
                    f'{skill}'
                    f'</span>'
                )

            render_html(
                f"""
                <div class="result-card">

                    <div class="result-card-title">
                        🔴 Missing Skills
                    </div>

                    {missing_html}

                    <br><br>

                    <span style="color:#85899c;font-size:11px;">
                        💡 Adding these skills can improve
                        your job match.
                    </span>

                </div>
                """
            )


        # ----------------------------------------------------
        # STRENGTHS
        # ----------------------------------------------------

        st.markdown("### 💪 Resume Insights")

        strength_col, improve_col = st.columns(2)


        with strength_col:

            items = ""

            for item in result["strengths"]:

                items += f"""
                <div style="
                    padding:9px 0;
                    color:#a5f3d0;
                    font-size:12px;
                ">
                    ✓ &nbsp; {item}
                </div>
                """

            render_html(
                f"""
                <div class="result-card">

                    <div class="result-card-title">
                        🟢 Resume Strengths
                    </div>

                    {items}

                </div>
                """
            )


        with improve_col:

            items = ""

            for item in result["improvements"]:

                items += f"""
                <div style="
                    padding:9px 0;
                    color:#fcd34d;
                    font-size:12px;
                ">
                    • &nbsp; {item}
                </div>
                """

            render_html(
                f"""
                <div class="result-card">

                    <div class="result-card-title">
                        ⚠ Areas to Improve
                    </div>

                    {items}

                </div>
                """
            )


        # ----------------------------------------------------
        # AI RECOMMENDATIONS
        # ----------------------------------------------------

        st.markdown("### ✦ AI Recommendations")

        recommendation_html = ""

        for index, recommendation in enumerate(
            result["recommendations"],
            1
        ):

            recommendation_html += f"""
            <div class="recommendation">

                <span class="recommendation-number">
                    {index}
                </span>

                {recommendation}

            </div>
            """

        render_html(
            f"""
            <div class="result-card">

                <div class="result-card-title">
                    🤖 Personalized Recommendations
                </div>

                {recommendation_html}

            </div>
            """
        )


        # ----------------------------------------------------
        # DOWNLOAD
        # ----------------------------------------------------

        st.write("")

        report = f"""
RESUMATE AI - RESUME ANALYSIS

ATS SCORE: {result["score"]}/100
JOB MATCH: {result["match"]}%

MATCHED SKILLS:
{chr(10).join("- " + x for x in result["matched_skills"])}

MISSING SKILLS:
{chr(10).join("- " + x for x in result["missing_skills"])}

STRENGTHS:
{chr(10).join("- " + x for x in result["strengths"])}

AREAS TO IMPROVE:
{chr(10).join("- " + x for x in result["improvements"])}

AI RECOMMENDATIONS:
{chr(10).join("- " + x for x in result["recommendations"])}
"""

        st.download_button(
            "⬇ Download Analysis Report",
            report,
            file_name="resumate_analysis.txt",
            mime="text/plain",
            use_container_width=True
        )


# ============================================================
# FOOTER
# ============================================================

render_html("""
<div class="footer">

    ✦ ResumateAI

    <br><br>

    AI-powered resume intelligence

</div>
""")
