CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Availability Badge */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #10B981;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 16px;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10B981;
    }

    /* Hero Gradient Text */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.15;
        background: linear-gradient(135deg, #FFFFFF 30%, #38BDF8 70%, #818CF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.15rem;
        line-height: 1.6;
        margin-bottom: 24px;
    }

    /* Terminal Mockup */
    .terminal-container {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
        overflow: hidden;
        margin-top: 10px;
    }
    .terminal-header {
        background: #1E293B;
        padding: 10px 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .terminal-btn {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .btn-red { background: #EF4444; }
    .btn-yellow { background: #F59E0B; }
    .btn-green { background: #10B981; }
    .terminal-title {
        color: #64748B;
        font-size: 0.75rem;
        font-family: 'Fira Code', monospace;
        margin-left: 8px;
    }
    .terminal-body {
        padding: 18px 20px;
        font-family: 'Fira Code', monospace;
        font-size: 0.88rem;
        color: #E2E8F0;
        line-height: 1.6;
    }
    .t-keyword { color: #F43F5E; }
    .t-func { color: #38BDF8; }
    .t-str { color: #A3E635; }
    .t-comment { color: #64748B; font-style: italic; }

    /* Metric Cards */
    .stat-card {
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px 18px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stat-card:hover {
        border-color: #38BDF8;
        transform: translateY(-5px);
        box-shadow: 0 10px 25px -5px rgba(56, 189, 248, 0.2);
    }
    .stat-num {
        font-size: 2.2rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 4px;
    }
    .stat-desc {
        color: #94A3B8;
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.75px;
    }

    /* Project Cards & Badges */
    .project-card {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 12px;
    }
    .project-title {
        color: #F8FAFC;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .project-desc {
        color: #94A3B8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 14px;
    }
    .tech-pill {
        display: inline-block;
        background: #1E293B;
        color: #38BDF8;
        border: 1px solid #334155;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-family: 'Fira Code', monospace;
        margin-right: 6px;
        margin-bottom: 6px;
    }
</style>
"""