
import streamlit as st
from youtube_analyzer import build_youtube_agent

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Madhu Patel | YouTube Analyzer",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Global */
    .stApp {
        background-color: #f7f8fa;
    }

    .main .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    .sidebar-title {
        font-size: 21px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 4px;
    }

    .sidebar-subtitle {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 28px;
    }

    /* Header */
    .hero {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 32px 36px;
        margin-bottom: 24px;
    }

    .hero-title {
        font-size: 34px;
        font-weight: 750;
        color: #111827;
        margin-bottom: 8px;
        letter-spacing: -0.8px;
    }

    .hero-description {
        font-size: 16px;
        color: #6b7280;
        line-height: 1.6;
        margin: 0;
    }

    /* Section headings */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
        margin-top: 28px;
        margin-bottom: 14px;
    }

    /* Input */
    div[data-testid="stTextInput"] label {
        font-weight: 600;
        color: #374151;
    }

    div[data-testid="stTextInput"] input {
        border: 1px solid #d1d5db;
        border-radius: 9px;
        padding: 13px 14px;
        font-size: 15px;
        background-color: #ffffff;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #111827;
        box-shadow: 0 0 0 1px #111827;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 9px;
        border: none;
        background-color: #111827;
        color: white;
        font-weight: 600;
        padding: 11px 18px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #374151;
        color: white;
    }

    /* Analysis container */
    .analysis-container {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 28px 32px;
        margin-top: 24px;
        line-height: 1.7;
    }

    /* Info cards */
    .info-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
    }

    .info-card-title {
        font-size: 14px;
        font-weight: 600;
        color: #6b7280;
        margin-bottom: 8px;
    }

    .info-card-value {
        font-size: 17px;
        font-weight: 650;
        color: #111827;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 12px;
        padding-top: 40px;
        border-top: 1px solid #e5e7eb;
        margin-top: 50px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "video_url" not in st.session_state:
    st.session_state.video_url = ""


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">Madhu Patel</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Agentic AI Project</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Navigation")

    page = st.radio(
        "Select",
        [
            "Video Analyzer",
            "About"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### Technology")

    st.caption("Agno")
    st.caption("Groq")
    st.caption("YouTube Transcript API")
    st.caption("Streamlit")
    st.caption("Python")


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-title">YouTube Video Analyzer</div>
    <p class="hero-description">
        Analyze YouTube videos using an AI-powered workflow.
        Generate structured summaries, identify important topics,
        and extract meaningful timestamps from video content.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# VIDEO ANALYZER
# ---------------------------------------------------------

if page == "Video Analyzer":

    st.markdown(
        '<div class="section-title">Analyze a Video</div>',
        unsafe_allow_html=True
    )

    video_url = st.text_input(
        "YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=...",
        value=st.session_state.video_url
    )

    analyze_col, clear_col = st.columns([3, 1])

    with analyze_col:
        analyze = st.button(
            "Analyze Video",
            use_container_width=True
        )

    with clear_col:
        clear = st.button(
            "Clear",
            use_container_width=True
        )

    if clear:
        st.session_state.analysis = None
        st.session_state.video_url = ""
        st.rerun()

    # -----------------------------------------------------
    # ANALYSIS
    # -----------------------------------------------------

    if analyze:

        if not video_url.strip():
            st.warning("Please enter a YouTube video URL.")

        elif "youtube.com" not in video_url and "youtu.be" not in video_url:
            st.error("Please enter a valid YouTube URL.")

        else:

            st.session_state.video_url = video_url

            with st.spinner("Analyzing video. Please wait..."):

                try:

                    @st.cache_resource
                    def get_agent():
                        return build_youtube_agent()

                    agent = get_agent()

                    response = agent.run(
                        f"Analyze this video: {video_url}"
                    )

                    st.session_state.analysis = response.content

                except Exception as e:

                    st.error(
                        "Unable to analyze the video. "
                        "Please verify the URL and try again."
                    )

                    with st.expander("Technical details"):
                        st.code(str(e))

    # -----------------------------------------------------
    # DISPLAY RESULT
    # -----------------------------------------------------

    if st.session_state.analysis:

        st.markdown(
            '<div class="section-title">Analysis Report</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="analysis-container">',
            unsafe_allow_html=True
        )

        st.markdown(
            st.session_state.analysis
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.download_button(
            label="Download Report",
            data=st.session_state.analysis,
            file_name="youtube_analysis.txt",
            mime="text/plain"
        )


# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------

elif page == "About":

    st.markdown(
        '<div class="section-title">About the Project</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="analysis-container">

    <h3>AI-Powered YouTube Video Analyzer</h3>

    <p>
    This project analyzes YouTube videos and generates structured
    insights using an AI agent. It combines video transcript
    extraction, language-model reasoning, and a Streamlit interface
    into a single workflow.
    </p>

    <h4>Core Features</h4>

    <ul>
        <li>YouTube video analysis</li>
        <li>Video overview generation</li>
        <li>Topic identification</li>
        <li>Timestamp-based content organization</li>
        <li>Key learning points</li>
        <li>Structured AI-generated reports</li>
        <li>Downloadable analysis reports</li>
    </ul>

    <h4>Developer</h4>

    <p>
    <strong>Madhu Patel</strong><br>
    B.Tech Data Science
    </p>

    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div class="footer">
    Madhu Patel | AI & Data Science | YouTube Video Analyzer
</div>
""", unsafe_allow_html=True)
