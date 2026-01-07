import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

# ---------- CSS ----------
st.markdown(
    """
    <style>
      /* Global */
      .stApp { background: #f3f4f6; }
      .block-container { padding-top: 1.0rem; padding-bottom: 2rem; }

      /* Top bar */
      .topbar {
        background: #111;
        border-radius: 14px;
        padding: 12px 16px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 10px;
        margin-bottom: 16px;
      }
      .pill {
        background: #1f2937;
        color: #fff;
        border: 1px solid #374151;
        padding: 8px 12px;
        border-radius: 999px;
        font-size: 14px;
        cursor: pointer;
      }
      .pillActive {
        background: #e5e7eb;
        color: #111;
        border: 1px solid #e5e7eb;
      }

      /* Cards */
      .card {
        background: #fff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 12px 12px 6px 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        height: 100%;
      }
      .cardHeader {
        display:flex;
        align-items:center;
        justify-content:space-between;
        margin-bottom: 8px;
      }
      .cardTitle { font-weight: 650; color:#111827; }
      .iconBtn {
        border: 1px solid #e5e7eb;
        background:#fff;
        border-radius: 10px;
        padding: 4px 10px;
        font-size: 12px;
        color:#111;
      }

      /* Scroll areas */
      .scrollArea {
        max-height: 520px;
        overflow-y: auto;
        padding-right: 6px;
      }

      /* List items */
      .item {
        border-top: 1px solid #eef2f7;
        padding: 10px 0;
      }
      .item:first-child { border-top: none; }
      .meta { color:#6b7280; font-size: 12px; }
      .strong { font-weight: 600; color:#111827; }
      .tag {
        display:inline-block;
        border:1px solid #e5e7eb;
        background:#f9fafb;
        padding: 2px 8px;
        border-radius: 999px;
        font-size: 12px;
        margin-right: 6px;
        margin-top: 6px;
      }

      /* Tighten Streamlit default spacing inside our cards */
      div[data-testid="stVerticalBlock"] > div:has(.card) { padding-top: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Top bar (HTML) ----------
active = st.session_state.get("unit", "First Team")

topbar_html = f"""
<div class="topbar">
  <span class="pill {'pillActive' if active=='All Units' else ''}">All Units</span>
  <span class="pill {'pillActive' if active=='First Team' else ''}">First Team</span>
  <span class="pill {'pillActive' if active=='Academy' else ''}">Academy</span>
  <span class="pill">⟲</span>
  <span class="pill">CF</span>
</div>
"""
st.markdown(topbar_html, unsafe_allow_html=True)

# ---------- Layout grid ----------
col_news, col_mid, col_right = st.columns([1.25, 1.15, 1.15], gap="large")

# NEWS (left) ----------
with col_news:
    st.markdown(
        """
        <div class="card">
          <div class="cardHeader">
            <div class="cardTitle">News</div>
            <div>
              <button class="iconBtn">✓</button>
              <button class="iconBtn">⛃</button>
            </div>
          </div>
          <div class="scrollArea">
        """,
        unsafe_allow_html=True,
    )

    # Example items
    news = [
        ("Danny Dispenza", "Conor Chaplin added to Summer 2026s Watchlist", "07/01/2026 15:14"),
        ("Emyr Humphreys", "Stade Reims 1–2 USL Dunkerque", "07/01/2026 15:05"),
        ("Danny Dispenza", "James Wright added to Removed", "07/01/2026 15:02"),
        ("Danny Dispenza", "James Wright removed from Tier 4", "07/01/2026 15:02"),
        ("Conor Froud", "André Luiz added to Conor Froud", "07/01/2026 14:12"),
        ("Conor Froud", "Yassir Zabiri added to Conor Froud", "07/01/2026 13:57"),
    ]
    for author, text, ts in news:
        st.markdown(
            f"""
            <div class="item">
              <div class="meta">{author}</div>
              <div class="strong">{text}</div>
              <div class="meta">{ts}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div></div>", unsafe_allow_html=True)

# MIDDLE column: My Tasks / My Appointments ----------
with col_mid:
    # My Tasks
    st.markdown(
        """
        <div class="card" style="min-height: 290px;">
          <div class="cardHeader">
            <div class="cardTitle">My Tasks</div>
            <button class="iconBtn">⛃</button>
          </div>
          <div style="display:flex;align-items:center;justify-content:center;height:220px;color:#6b7280;">
            No data available
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")  # spacer

    # My Appointments
    st.markdown(
        """
        <div class="card" style="min-height: 290px;">
          <div class="cardHeader">
            <div class="cardTitle">My Appointments</div>
            <button class="iconBtn">⛃</button>
          </div>
          <div style="display:flex;align-items:center;justify-content:center;height:220px;color:#6b7280;">
            No data available
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# RIGHT column: Shortlists / Interesting Matches ----------
with col_right:
    # Shortlists
    st.markdown(
        """
        <div class="card" style="min-height: 290px;">
          <div class="cardHeader">
            <div class="cardTitle">Shortlists</div>
            <button class="iconBtn">⛃</button>
          </div>
          <div class="scrollArea" style="max-height: 220px;">
        """,
        unsafe_allow_html=True,
    )

    shortlists = [
        ("Contract Watchlists", "Danny Dispenza • First Team", "Last change: 31/07/2025"),
        ("Emerging (By Season)", "Danny Dispenza • First Team", "Last change: 02/12/2024"),
        ("Meetings", "Danny Dispenza • First Team", "Last change: 02/12/2024"),
        ("FT Staff Shortlists", "Danny Dispenza • First Team", "Last change: 02/12/2024"),
        ("Emyr Humphreys", "Emyr Humphreys • First Team", "Last change: 29/10/2024"),
    ]
    for title, meta, change in shortlists:
        st.markdown(
            f"""
            <div class="item">
              <div class="strong">{title}</div>
              <div class="meta">{meta}</div>
              <div class="meta">{change}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.write("")  # spacer

    # Interesting Matches
    st.markdown(
        """
        <div class="card" style="min-height: 290px;">
          <div class="cardHeader">
            <div class="cardTitle">Interesting Matches</div>
            <button class="iconBtn">⛃</button>
          </div>
          <div class="scrollArea" style="max-height: 220px;">
        """,
        unsafe_allow_html=True,
    )

    matches = [
        ("07/01/2026 11:00 • Coppa Italia Primavera", "Juventus Primavera 2–1 Frosinone Primavera", ["Shane van Aarle"]),
        ("07/01/2026 11:30 • AFC U23 Asian Cup", "Japan U23 5–0 Syria U23", ["Yuto Ozeki", "Ryunosuke Sato", "Nelson Ishiwatari"]),
        ("07/01/2026 11:30 • AFC U23 Asian Cup", "South Korea U23 0–0 Iran U23", []),
    ]
    for when, result, tags in matches:
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags]) or ""
        st.markdown(
            f"""
            <div class="item">
              <div class="meta">{when}</div>
              <div class="strong">{result}</div>
              {tags_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div></div>", unsafe_allow_html=True)

