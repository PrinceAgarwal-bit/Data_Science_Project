import streamlit as st

def app():
    # =========================================================
    # CUSTOM CSS
    # =========================================================

    st.markdown(
        """
    <style>

    /* ---------- MAIN APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(99, 102, 241, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(14, 165, 233, 0.08),
                transparent 30%
            ),
            #080b14;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 35px;
        padding-bottom: 60px;
    }


    /* ---------- HIDE STREAMLIT MENU & FOOTER ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Keep header transparent so the sidebar toggle icon stays visible */
    header {
        background-color: transparent !important;
    }


    /* ---------- HERO ---------- */

    .hero-box {
        padding: 55px 30px 60px;
        text-align: center;
    }

    .hero-badge {
        display: inline-block;
        padding: 8px 18px;
        border-radius: 30px;
        background: rgba(99, 102, 241, 0.10);
        border: 1px solid rgba(129, 140, 248, 0.25);
        color: #a5b4fc;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    .hero-title {
        font-size: 64px;
        font-weight: 850;
        line-height: 1.05;
        letter-spacing: -3px;
        color: white;
        margin: 0;
    }

    .gradient {
        background: linear-gradient(
            90deg,
            #818cf8,
            #38bdf8,
            #22d3ee
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-text {
        max-width: 700px;
        margin: 25px auto 0;
        color: #9ca3af;
        font-size: 18px;
        line-height: 1.7;
    }


    /* ---------- SECTION ---------- */

    .section-heading {
        text-align: center;
        color: white;
        font-size: 30px;
        font-weight: 800;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    .section-text {
        text-align: center;
        color: #71717a;
        font-size: 15px;
        margin-bottom: 30px;
    }


    /* ---------- FEATURE CARDS ---------- */

    .card {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 28px;
        min-height: 220px;
        transition: 0.3s ease;
    }

    .card:hover {
        border-color: rgba(129,140,248,0.35);
        background: rgba(255,255,255,0.05);
        transform: translateY(-4px);
    }

    .card-icon {
        font-size: 40px;
        margin-bottom: 15px;
    }

    .card-title {
        color: white;
        font-size: 21px;
        font-weight: 750;
        margin-bottom: 12px;
    }

    .card-text {
        color: #9ca3af;
        font-size: 14px;
        line-height: 1.7;
    }


    /* ---------- INFO BOX ---------- */

    .info-box {
        margin-top: 45px;
        padding: 32px;
        border-radius: 22px;
        background:
            linear-gradient(
                135deg,
                rgba(99,102,241,0.08),
                rgba(14,165,233,0.04)
            );
        border: 1px solid rgba(255,255,255,0.07);
    }

    .info-title {
        color: white;
        font-size: 23px;
        font-weight: 750;
        margin-bottom: 12px;
    }

    .info-text {
        color: #9ca3af;
        font-size: 15px;
        line-height: 1.8;
    }


    /* ---------- TOOL ITEMS ---------- */

    .tool-item {
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.06);
    }

    .tool-item:last-child {
        border-bottom: none;
    }

    .tool-title {
        color: white;
        font-size: 17px;
        font-weight: 700;
    }

    .tool-description {
        color: #71717a;
        font-size: 14px;
        margin-top: 5px;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #a1a1aa;
        font-size: 14px;
        margin-top: 60px;
        padding-top: 30px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }

    .footer-author {
        color: #e4e4e7;
        font-weight: 600;
        margin-top: 8px;
        display: block;
    }

    .footer-highlight {
        color: #818cf8;
        font-weight: 700;
    }

    </style>
    """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # BRAND
    # =========================================================

    st.markdown(
        "<h3 style='text-align:center; color:white;'>"
        "🤖 Data<span style='color:#818cf8;'>Science</span> Fun & Learn"
        "</h3>",
        unsafe_allow_html=True,
    )

    # =========================================================
    # HERO
    # =========================================================

    st.markdown(
        """<div class="hero-box">
        <div class="hero-badge">✨ AI-Powered Data Science Learning</div>
        <div class="hero-title">Data Science<br><span class="gradient">Made Simple & Fun</span></div>
        <div class="hero-text">An AI-powered learning platform designed to make Data Science easier to understand, practice, and explore.</div>
    </div>""",
        unsafe_allow_html=True,
    )

    # =========================================================
    # WHAT IS IT?
    # =========================================================

    st.markdown(
        '<div class="section-heading">🧠 What is Data Science Fun & Learn?</div>'
        '<div class="section-text">Learn complex Data Science concepts through simple, interactive and AI-powered tools.</div>',
        unsafe_allow_html=True,
    )

    # =========================================================
    # FEATURE CARDS (2 COLUMNS)
    # =========================================================

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """<div class="card">
            <div class="card-icon">🗄️</div>
            <div class="card-title">SQL Query Explainer</div>
            <div class="card-text">Understand complicated SQL queries in simple language. The AI breaks down the query and explains what each part does step-by-step.</div>
        </div>""",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """<div class="card">
            <div class="card-icon">🎯</div>
            <div class="card-title">Data Science MCQ Generator</div>
            <div class="card-text">Generate AI-powered multiple-choice questions to test your Data Science knowledge and strengthen your understanding of important concepts.</div>
        </div>""",
            unsafe_allow_html=True,
        )

    # =========================================================
    # WHY THIS PLATFORM?
    # =========================================================

    st.markdown(
        """<div class="info-box">
        <div class="info-title">💡 Why was this platform created?</div>
        <div class="info-text">
            Learning Data Science can be challenging because it combines programming, SQL, statistics, and analytical thinking.<br><br>
            <b style="color:#e4e4e7;">Data Science Fun & Learn</b> brings useful AI-powered learning tools together in one place, helping learners understand concepts more easily and practice them in an engaging way.
        </div>
    </div>""",
        unsafe_allow_html=True,
    )

    # =========================================================
    # TOOLKIT
    # =========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">🚀 AI Learning Toolkit</div>'
        '<div class="section-text">Two AI-powered tools for different parts of your Data Science learning journey.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """<div class="info-box">
        <div class="tool-item">
            <div class="tool-title">🗄️ SQL Query Explainer</div>
            <div class="tool-description">Break down SQL queries and understand their logic step-by-step.</div>
        </div>
        <div class="tool-item">
            <div class="tool-title">🎯 Data Science MCQ Generator</div>
            <div class="tool-description">Generate practice questions and test your Data Science knowledge.</div>
        </div>
    </div>""",
        unsafe_allow_html=True,
    )

    # =========================================================
    # FOOTER
    # =========================================================

    st.markdown(
        """<div class="footer">
        🤖 <b>DataScience Fun & Learn</b><br>
        <span style="color: #71717a;">Learn • Practice • Understand • Improve</span><br><br>
        <span class="footer-author">
            Developed by <span class="footer-highlight">Prince Agarwal</span> | B.Tech CSE 4th Year Project
        </span>
    </div>""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    app()