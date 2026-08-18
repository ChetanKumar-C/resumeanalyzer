import streamlit as st
import plotly.graph_objects as go
import time
from textwrap import dedent


# ============================================================
# PAGE CONFIG
# ============================================================

def html(content):
    st.markdown(
        dedent(content),
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="ResumateAI",
    page_icon="✦",
    layout="wide"
)


# ============================================================
# DARK PROFESSIONAL THEME
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 80% 10%,
            rgba(124, 58, 237, 0.16),
            transparent 28%
        ),
        radial-gradient(
            circle at 10% 45%,
            rgba(37, 99, 235, 0.08),
            transparent 25%
        ),
        #05060d;
    color: white;
}


/* Remove Streamlit default spacing */

.block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}


/* Hide default Streamlit elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* ============================================================
   NAVBAR
============================================================ */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px 5px 20px;

    border-bottom:
        1px solid rgba(255,255,255,0.07);

    margin-bottom: 35px;
}

.logo {
    font-size: 23px;
    font-weight: 800;
    color: white;
}

.logo span {
    background:
        linear-gradient(
            90deg,
            #c084fc,
            #8b5cf6,
            #22d3ee
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nav-text {
    color: #85899d;
    font-size: 13px;
    margin-left: 28px;
}

.nav-active {
    color: white;
}

.nav-button {
    background:
        linear-gradient(
            100deg,
            #7c3aed,
            #6366f1
        );

    padding: 10px 18px;

    border-radius: 9px;

    font-size: 12px;

    font-weight: 700;

    color: white;
}


/* ============================================================
   HERO
============================================================ */

.badge {
    display: inline-block;

    padding: 8px 14px;

    border-radius: 30px;

    background:
        rgba(124,58,237,0.10);

    border:
        1px solid rgba(139,92,246,0.30);

    color: #c4b5fd;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 1px;
}

.hero-title {
    font-size: 55px;

    line-height: 1.08;

    font-weight: 800;

    letter-spacing: -2px;

    margin-top: 22px;

    margin-bottom: 20px;
}

.gradient {
    background:
        linear-gradient(
            90deg,
            #c084fc,
            #8b5cf6,
            #6366f1,
            #22d3ee
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text {
    color: #9297aa;

    font-size: 15px;

    line-height: 1.8;

    max-width: 580px;
}


/* ============================================================
   FEATURE MINI CARDS
============================================================ */

.mini-card {
    background:
        rgba(15,17,31,0.75);

    border:
        1px solid rgba(255,255,255,0.07);

    border-radius: 12px;

    padding: 14px;

    min-height: 100px;
}

.mini-icon {
    font-size: 20px;
}

.mini-title {
    color: #f3f4f6;

    font-size: 12px;

    font-weight: 700;

    margin-top: 7px;
}

.mini-text {
    color: #6f7488;

    font-size: 9px;

    line-height: 1.5;

    margin-top: 4px;
}


/* ============================================================
   RESUME VISUAL
============================================================ */

.visual {
    height: 390px;

    display: flex;

    justify-content: center;

    align-items: center;

    position: relative;
}

.resume {
    width: 220px;

    height: 300px;

    background:
        linear-gradient(
            145deg,
            #19162e,
            #0b0e1b
        );

    border:
        1px solid rgba(168,85,247,0.45);

    border-radius: 16px;

    padding: 25px;

    transform:
        rotate(5deg);

    box-shadow:
        0 30px 80px rgba(0,0,0,0.5),
        0 0 50px rgba(124,58,237,0.18);
}

.avatar {
    width: 45px;
    height: 45px;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #a855f7,
            #2563eb
        );

    margin-bottom: 20px;
}

.line {
    height: 6px;

    background:
        linear-gradient(
            90deg,
            #8b5cf6,
            #2563eb
        );

    border-radius: 10px;

    margin-bottom: 11px;

    opacity: 0.7;
}

.line-long {
    width: 95%;
}

.line-medium {
    width: 70%;
}

.line-short {
    width: 45%;
}

.floating {
    position: absolute;

    background:
        rgba(12,14,27,0.92);

    border:
        1px solid rgba(139,92,246,0.30);

    border-radius: 11px;

    padding: 11px 14px;

    font-size: 10px;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.35);

    z-index: 5;
}

.float-one {
    top: 40px;
    left: 20px;

    color: #c4b5fd;
}

.float-two {
    top: 90px;
    right: 20px;

    color: #5eead4;
}

.float-three {
    bottom: 65px;
    left: 15px;

    color: #67e8f9;
}

.float-four {
    bottom: 40px;
    right: 20px;

    color: #d8b4fe;
}


/* ============================================================
   MAIN INPUT CARD
============================================================ */

.input-card {
    background:
        linear-gradient(
            145deg,
            rgba(18,21,38,0.98),
            rgba(8,10,19,0.98)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 28px;

    margin-top: 20px;

    box-shadow:
        0 25px 70px rgba(0,0,0,0.25);
}

.section-heading {
    font-size: 17px;

    font-weight: 800;

    color: #f5f5f5;
}

.section-subtitle {
    color: #73788c;

    font-size: 11px;

    margin-top: 5px;

    margin-bottom: 22px;
}


/* ============================================================
   UPLOAD AREA
============================================================ */

[data-testid="stFileUploaderDropzone"] {

    background:
        rgba(7,9,18,0.85) !important;

    border:
        1px dashed rgba(139,92,246,0.50) !important;

    border-radius: 14px !important;

    min-height: 165px !important;
}

[data-testid="stFileUploaderDropzone"]:hover {

    border-color:
        #a855f7 !important;

    background:
        rgba(20,14,40,0.85) !important;
}


/* ============================================================
   TEXT AREA
============================================================ */

textarea {

    background:
        rgba(7,9,18,0.85) !important;

    color: #e5e7eb !important;

    border:
        1px solid rgba(255,255,255,0.08) !important;

    border-radius: 14px !important;

    font-size: 12px !important;

    line-height: 1.6 !important;
}

textarea:focus {

    border-color:
        #8b5cf6 !important;

    box-shadow:
        0 0 20px rgba(139,92,246,0.12) !important;
}


/* ============================================================
   ANALYZE BUTTON
============================================================ */

[data-testid="stButton"] button {

    width: 100%;

    height: 52px;

    border: none;

    border-radius: 11px;

    background:
        linear-gradient(
            100deg,
            #7c3aed,
            #a855f7,
            #6366f1,
            #2563eb
        );

    color: white;

    font-size: 14px;

    font-weight: 700;

    box-shadow:
        0 12px 35px rgba(124,58,237,0.25);
}

[data-testid="stButton"] button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 18px 45px rgba(124,58,237,0.40);
}


/* ============================================================
   BENEFIT BAR
============================================================ */

.benefit {
    background:
        rgba(13,15,28,0.90);

    border:
        1px solid rgba(255,255,255,0.07);

    border-radius: 14px;

    padding: 17px;

    text-align: center;
}

.benefit-icon {
    font-size: 20px;
}

.benefit-title {
    color: #e5e7eb;

    font-size: 11px;

    font-weight: 700;

    margin-top: 5px;
}

.benefit-text {
    color: #666b7e;

    font-size: 9px;

    margin-top: 3px;
}


/* ============================================================
   RESULTS
============================================================ */

.result-box {
    background:
        linear-gradient(
            145deg,
            rgba(17,20,37,0.98),
            rgba(7,9,18,0.98)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 25px;

    margin-top: 30px;
}

.metric {
    background:
        rgba(10,13,25,0.85);

    border:
        1px solid rgba(255,255,255,0.07);

    border-radius: 13px;

    padding: 17px;

    text-align: center;
}

.metric-label {
    color: #6d7285;

    font-size: 9px;

    font-weight: 700;

    letter-spacing: 1px;
}

.metric-value {
    font-size: 27px;

    font-weight: 800;

    margin-top: 5px;
}

.purple {
    color: #c084fc;
}

.blue {
    color: #67e8f9;
}

.green {
    color: #5eead4;
}

.red {
    color: #fca5a5;
}


/* ============================================================
   RESULT INNER CARDS
============================================================ */

.inner-card {
    background:
        rgba(10,13,25,0.75);

    border:
        1px solid rgba(255,255,255,0.07);

    border-radius: 14px;

    padding: 20px;

    min-height: 150px;
}

.inner-title {
    color: #e5e7eb;

    font-size: 13px;

    font-weight: 700;

    margin-bottom: 14px;
}

.skill-good {
    display: inline-block;

    padding: 6px 10px;

    border-radius: 20px;

    margin: 3px;

    background:
        rgba(16,185,129,0.08);

    border:
        1px solid rgba(16,185,129,0.20);

    color: #5eead4;

    font-size: 10px;
}

.skill-bad {
    display: inline-block;

    padding: 6px 10px;

    border-radius: 20px;

    margin: 3px;

    background:
        rgba(239,68,68,0.08);

    border:
        1px solid rgba(239,68,68,0.20);

    color: #fca5a5;

    font-size: 10px;
}

.insight {
    color: #9da2b4;

    font-size: 11px;

    padding: 9px 0;

    border-bottom:
        1px solid rgba(255,255,255,0.05);
}


/* ============================================================
   FOOTER
============================================================ */

.footer {
    text-align: center;

    color: #4f5467;

    font-size: 10px;

    padding-top: 50px;
}


/* ============================================================
   MOBILE
============================================================ */

@media(max-width: 800px) {

    .hero-title {
        font-size: 40px;
    }

    .nav-text {
        display: none;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================

html("""
<div class="navbar">

    <div class="logo">
        ✦ Resumate<span>AI</span>
    </div>

    <div>
        <span class="nav-text nav-active">Home</span>
        <span class="nav-text">How it Works</span>
        <span class="nav-text">Features</span>
        <span class="nav-text">About</span>
    </div>

    <div class="nav-button">
        ✦ Get Started
    </div>

</div>
""")


# ============================================================
# HERO
# ============================================================

left, right = st.columns([1.15, 1], gap="large")


with left:

    html("""
    <div style="padding-top:45px;">

        <div class="badge">
            ✦ &nbsp; GENAI POWERED RESUME ANALYSIS
        </div>

        <div class="hero-title">
            Build a Resume<br>
            That <span class="gradient">Gets You Hired.</span>
        </div>

        <div class="hero-text">
            Analyze your resume, match it with job requirements,
            identify missing skills, and get AI-powered
            recommendations to improve your chances of landing
            your dream job.
        </div>

    </div>
    """)

    st.write("")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="mini-card">
            <div class="mini-icon">◎</div>
            <div class="mini-title">ATS Score</div>
            <div class="mini-text">
                See how your resume performs against ATS systems.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="mini-card">
            <div class="mini-icon">✓</div>
            <div class="mini-title">Job Match</div>
            <div class="mini-text">
                Compare your resume with job requirements.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="mini-card">
            <div class="mini-icon">✦</div>
            <div class="mini-title">AI Insights</div>
            <div class="mini-text">
                Get personalized improvement recommendations.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# HERO VISUAL
# ============================================================

with right:

    html("""
    <div class="visual">

        <div class="floating float-one">
            ✦ AI Powered
        </div>

        <div class="floating float-two">
            <b style="font-size:18px;">98%</b><br>
            Accuracy
        </div>

        <div class="floating float-three">
            ✦ Smart<br>
            Analysis
        </div>

        <div class="floating float-four">
            ⚡ Instant<br>
            Results
        </div>

        <div class="resume">

            <div class="avatar"></div>

            <div class="line line-long"></div>
            <div class="line line-medium"></div>

            <br>

            <div class="line line-long"></div>
            <div class="line line-medium"></div>
            <div class="line line-short"></div>

            <br>

            <div class="line line-long"></div>
            <div class="line line-long"></div>
            <div class="line line-medium"></div>
            <div class="line line-short"></div>

        </div>

    </div>
    """)


# ============================================================
# INPUT SECTION
# ============================================================

html("""
<div class="input-card">

    <div class="section-heading">
        📄 Analyze Your Resume
    </div>

    <div class="section-subtitle">
        Upload your resume and provide the job description
        to receive an AI-powered analysis.
    </div>

</div>
""")


col1, col2 = st.columns(2, gap="large")


# ============================================================
# RESUME
# ============================================================

with col1:

    st.markdown("""
    <div class="section-heading">
        📄 Resume
    </div>

    <div class="section-subtitle">
        Upload your latest resume (PDF or DOCX)
    </div>
    """, unsafe_allow_html=True)

    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        label_visibility="collapsed"
    )

    if resume:
        st.success(
            f"✓ {resume.name} uploaded successfully"
        )


# ============================================================
# JOB DESCRIPTION
# ============================================================

with col2:

    st.markdown("""
    <div class="section-heading">
        💼 Job Description
    </div>

    <div class="section-subtitle">
        Paste the job description you're applying for
    </div>
    """, unsafe_allow_html=True)

    job_description = st.text_area(
        "Job Description",
        placeholder=(
            "Example:\n\n"
            "We are looking for a Python Developer "
            "with experience in SQL, REST APIs, "
            "Django and cloud technologies..."
        ),
        height=165,
        label_visibility="collapsed"
    )


st.markdown("""
<div style="
    color:#606679;
    font-size:10px;
    margin-top:5px;
">
    🔒 Your resume data is handled securely and confidentially.
</div>
""", unsafe_allow_html=True)


st.write("")


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze = st.button(
    "✦  Analyze My Resume  →",
    use_container_width=True
)


# ============================================================
# BENEFITS
# ============================================================

st.write("")

b1, b2, b3, b4 = st.columns(4)


with b1:
    st.markdown("""
    <div class="benefit">
        <div class="benefit-icon">🛡️</div>
        <div class="benefit-title">Secure & Private</div>
        <div class="benefit-text">
            Your data stays confidential
        </div>
    </div>
    """, unsafe_allow_html=True)


with b2:
    st.markdown("""
    <div class="benefit">
        <div class="benefit-icon">⚡</div>
        <div class="benefit-title">Instant Analysis</div>
        <div class="benefit-text">
            Get results in seconds
        </div>
    </div>
    """, unsafe_allow_html=True)


with b3:
    st.markdown("""
    <div class="benefit">
        <div class="benefit-icon">📊</div>
        <div class="benefit-title">Detailed Insights</div>
        <div class="benefit-text">
            Understand your resume
        </div>
    </div>
    """, unsafe_allow_html=True)


with b4:
    st.markdown("""
    <div class="benefit">
        <div class="benefit-icon">✦</div>
        <div class="benefit-title">Improve & Grow</div>
        <div class="benefit-text">
            Increase your chances
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MOCK ANALYSIS
# ============================================================

def analyze_resume():

    time.sleep(2)

    return {

        "ats": 87,
        "match": 91,

        "matched": [
            "Python",
            "SQL",
            "Machine Learning",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Data Analysis",
            "Git",
            "Statistics",
            "Matplotlib"
        ],

        "missing": [
            "AWS",
            "Docker",
            "REST APIs",
            "Django"
        ],

        "strengths": [
            "Strong technical foundation",
            "Good problem solving abilities",
            "Relevant projects and experience",
            "Well structured resume"
        ],

        "improvements": [
            "Add measurable achievements",
            "Include relevant certifications",
            "Improve professional summary",
            "Add cloud or deployment experience"
        ]

    }


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if resume is None:

        st.error(
            "Please upload your resume first."
        )

    elif not job_description.strip():

        st.error(
            "Please enter the job description first."
        )

    else:

        with st.spinner(
            "✦ AI is analyzing your resume..."
        ):

            result = analyze_resume()


        # ====================================================
        # RESULT HEADER
        # ====================================================

        st.markdown("""
        <div class="result-box">

            <div class="section-heading">
                📊 Your Resume Analysis
            </div>

            <div class="section-subtitle">
                AI-powered insights based on your resume
                and target job description.
            </div>

        </div>
        """, unsafe_allow_html=True)


        # ====================================================
        # METRICS
        # ====================================================

        m1, m2, m3, m4 = st.columns(4)


        with m1:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-label">ATS SCORE</div>
                <div class="metric-value purple">
                    {result["ats"]}/100
                </div>
            </div>
            """, unsafe_allow_html=True)


        with m2:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-label">JOB MATCH</div>
                <div class="metric-value blue">
                    {result["match"]}%
                </div>
            </div>
            """, unsafe_allow_html=True)


        with m3:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-label">SKILLS MATCHED</div>
                <div class="metric-value green">
                    {len(result["matched"])}
                </div>
            </div>
            """, unsafe_allow_html=True)


        with m4:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-label">SKILLS MISSING</div>
                <div class="metric-value red">
                    {len(result["missing"])}
                </div>
            </div>
            """, unsafe_allow_html=True)


        st.write("")


        # ====================================================
        # GAUGE + SUMMARY
        # ====================================================

        g1, g2 = st.columns([1, 2], gap="large")


        with g1:

            fig = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=result["ats"],

                    number={
                        "font": {
                            "color": "white",
                            "size": 40
                        }
                    },

                    title={
                        "text": "ATS SCORE",
                        "font": {
                            "color": "#777c91",
                            "size": 11
                        }
                    },

                    gauge={

                        "axis": {
                            "range": [0, 100]
                        },

                        "bar": {
                            "color": "#a855f7"
                        },

                        "bgcolor": "#111426",

                        "borderwidth": 1,

                        "bordercolor": "#292d45"

                    }

                )

            )

            fig.update_layout(

                height=280,

                paper_bgcolor="rgba(0,0,0,0)",

                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=10
                )

            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )


        with g2:

            st.markdown("""
            <div class="inner-card">

                <div class="inner-title">
                    ⭐ Overall Assessment
                </div>

                <div style="
                    font-size:27px;
                    font-weight:800;
                    color:#5eead4;
                    margin-bottom:12px;
                ">
                    Excellent
                </div>

                <div style="
                    color:#85899c;
                    font-size:12px;
                    line-height:1.8;
                ">

                    Your resume demonstrates a strong technical
                    foundation and has a high level of alignment
                    with the target position.

                    <br><br>

                    You already match most important requirements.
                    Adding the missing skills and improving measurable
                    achievements could make your profile even stronger.

                </div>

            </div>
            """, unsafe_allow_html=True)


        # ====================================================
        # SKILLS
        # ====================================================

        st.markdown("""
        <div style="
            font-size:17px;
            font-weight:800;
            color:#f3f4f6;
            margin-top:30px;
            margin-bottom:12px;
        ">
            🛠 Skills Analysis
        </div>
        """, unsafe_allow_html=True)


        s1, s2 = st.columns(2, gap="large")


        with s1:

            skills = ""

            for skill in result["matched"]:

                skills += (
                    f'<span class="skill-good">'
                    f'{skill}'
                    f'</span>'
                )


            st.markdown(f"""
            <div class="inner-card">

                <div class="inner-title">
                    🟢 Matched Skills
                </div>

                {skills}

            </div>
            """, unsafe_allow_html=True)


        with s2:

            missing = ""

            for skill in result["missing"]:

                missing += (
                    f'<span class="skill-bad">'
                    f'{skill}'
                    f'</span>'
                )


            st.markdown(f"""
            <div class="inner-card">

                <div class="inner-title">
                    🔴 Missing Skills
                </div>

                {missing}

            </div>
            """, unsafe_allow_html=True)


        # ====================================================
        # INSIGHTS
        # ====================================================

        st.markdown("""
        <div style="
            font-size:17px;
            font-weight:800;
            color:#f3f4f6;
            margin-top:30px;
            margin-bottom:12px;
        ">
            💡 Resume Insights
        </div>
        """, unsafe_allow_html=True)


        i1, i2 = st.columns(2, gap="large")


        with i1:

            strength_html = ""

            for item in result["strengths"]:

                strength_html += f"""
                <div class="insight">
                    <span style="color:#86efac;">
                        ✓
                    </span>
                    &nbsp; {item}
                </div>
                """


            st.markdown(f"""
            <div class="inner-card">

                <div class="inner-title">
                    🟢 Resume Strengths
                </div>

                {strength_html}

            </div>
            """, unsafe_allow_html=True)


        with i2:

            improve_html = ""

            for item in result["improvements"]:

                improve_html += f"""
                <div class="insight">
                    <span style="color:#fcd34d;">
                        •
                    </span>
                    &nbsp; {item}
                </div>
                """


            st.markdown(f"""
            <div class="inner-card">

                <div class="inner-title">
                    ⚠ Areas to Improve
                </div>

                {improve_html}

            </div>
            """, unsafe_allow_html=True)


        # ====================================================
        # FOOTER
        # ====================================================

        st.markdown("""
        <div class="footer">

            ✦ <b>ResumateAI</b>

            <br><br>

            AI-powered resume intelligence

            <br>

            Analyze • Match • Improve • Get Hired

        </div>
        """, unsafe_allow_html=True)