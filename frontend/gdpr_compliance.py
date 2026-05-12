"""
================================================================================
GDPR & AI Act Compliance Module - CareerMatch AI
================================================================================

Compliance with GDPR (EU Reg. 2016/679), EU AI Act (EU Reg. 2024/1689)
and ePrivacy Directive.

Features:
- Consent banner (consent gate)
- Full Privacy Policy
- AI Act transparency disclosure
- Data deletion (right to erasure)
- Contact form
- Language toggle (EN/IT)

================================================================================
"""

import streamlit as st
from datetime import datetime
from i18n import get_t

def _t(key):
    """Wrapper to use global translation in GDPR module."""
    t = get_t()
    return t(key)


# CareerMatch AI specific model data
AI_MODELS = [
    ("Skill Matching", "Random Forest (150 trees)", "Skill classification"),
    ("Semantic Analysis", "TF-IDF + LSA", "Professional context"),
    ("Skill Clustering", "K-Means + Hierarchical", "Skill grouping"),
    ("Topic Discovery", "LDA (Latent Dirichlet Allocation)", "JD theme identification"),
    ("Fuzzy Matching", "FuzzyWuzzy (85% threshold)", "Typo tolerance"),
]


# =============================================================================
# CSS STYLES
# =============================================================================

def get_compliance_css():
    return """
    <style>
        .gdpr-banner {
            background: linear-gradient(135deg, rgba(0, 119, 181, 0.15), rgba(0, 160, 220, 0.08));
            border: 1px solid rgba(0, 160, 220, 0.3);
            border-radius: 12px;
            padding: 2rem;
            margin: 1rem 0 2rem 0;
        }
        .gdpr-banner h3 { color: #00A0DC; margin-bottom: 1rem; }
        .gdpr-banner p { color: #c9d1d9; line-height: 1.6; }
        .privacy-section {
            background: rgba(13, 17, 23, 0.6);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .privacy-section h4 { color: #00A0DC; margin-bottom: 0.75rem; }
        .ai-transparency-box {
            background: linear-gradient(135deg, rgba(56, 132, 244, 0.1), rgba(0, 200, 160, 0.08));
            border-left: 4px solid #3884F4;
            border-radius: 0 10px 10px 0;
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .ai-transparency-box h4 { color: #3884F4; margin-bottom: 0.5rem; }
        .delete-warning {
            background: rgba(229, 57, 53, 0.1);
            border: 1px solid rgba(229, 57, 53, 0.3);
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
        }
        .compliance-badge {
            display: inline-block;
            background: rgba(0, 200, 83, 0.15);
            color: #00C853;
            border: 1px solid rgba(0, 200, 83, 0.3);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .contact-form {
            background: rgba(13, 17, 23, 0.6);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
        }
    </style>
    """


# =============================================================================
# LANGUAGE TOGGLE
# =============================================================================

def render_language_toggle():
    """Renders a compact language toggle."""
    col1, col2 = st.columns([6, 1])
    with col2:
        lang = st.selectbox(
            "Lang",
            options=["en", "it"],
            format_func=lambda x: "EN" if x == "en" else "IT",
            key="gdpr_lang",
            label_visibility="collapsed",
        )


# =============================================================================
# CONSENT BANNER (GDPR Art. 6-7)
# =============================================================================

def render_consent_banner():
    if st.session_state.get("gdpr_consent_given", False):
        return True

    st.markdown(get_compliance_css(), unsafe_allow_html=True)
    st.markdown("<br>" * 2, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        render_language_toggle()

        st.markdown(f"""
        <div class="gdpr-banner">
            <h3>{_t("consent_title")}</h3>
            <p>{_t("consent_intro")}</p>
            <p style="margin-top: 1rem;">
                <strong>{_t("consent_data_label")}</strong> {_t("consent_data_value")}
            </p>
            <p>
                <strong>{_t("consent_purpose_label")}</strong> {_t("consent_purpose_value")}
            </p>
            <p>
                <strong>{_t("consent_retention_label")}</strong> {_t("consent_retention_value")}
            </p>
            <p style="margin-top: 0.5rem; font-size: 0.85rem; color: #8b949e;">
                {_t("consent_details")}
            </p>
        </div>
        """, unsafe_allow_html=True)

        consent_data = st.checkbox(_t("checkbox_gdpr"), key="gdpr_consent_checkbox")
        consent_ai = st.checkbox(_t("checkbox_ai"), key="ai_act_consent_checkbox")

        st.markdown("<br>", unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            if st.button(_t("btn_accept"), type="primary", use_container_width=True,
                        disabled=not (consent_data and consent_ai)):
                st.session_state["gdpr_consent_given"] = True
                st.session_state["gdpr_consent_timestamp"] = datetime.now().isoformat()
                st.rerun()

        if not (consent_data and consent_ai):
            st.caption(_t("consent_warning"))

    return False


# =============================================================================
# PRIVACY POLICY PAGE
# =============================================================================

def render_privacy_policy_page():
    st.markdown(get_compliance_css(), unsafe_allow_html=True)

    render_language_toggle()

    st.markdown(f"""
    <div class="hero-gradient" style="text-align: center; padding: 2.5rem; margin-bottom: 2rem;">
        <h1 style="margin-bottom: 0.5rem;">{_t("page_title")}</h1>
        <p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 1rem;">{_t("page_subtitle")}</p>
        <div>
            <span class="compliance-badge">GDPR Compliant</span>
            <span class="compliance-badge" style="margin-left: 8px;">AI Act Compliant</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- SIMPLIFIED COMPLIANCE SECTIONS ---
    st.markdown(f"## {_t('privacy_heading')}")

    with st.expander(f"🏢 {_t('controller_title')}", expanded=True):
        st.markdown(_t('controller_body'), unsafe_allow_html=True)
        
    with st.expander(f"📁 {_t('data_title')}", expanded=False):
        st.markdown(_t('data_body'), unsafe_allow_html=True)
        
    with st.expander(f"⚖️ {_t('legal_title')}", expanded=False):
        headers = _t("legal_headers")
        rows = _t("legal_rows")
        for purpose, basis in rows:
            st.markdown(f"**{purpose}**  \n*Basis: {basis}*")
            st.markdown("---")
            
    with st.expander(f"⏱️ {_t('retention_title')}", expanded=False):
        st.markdown(_t('retention_body'), unsafe_allow_html=True)

    with st.expander(f"🛡️ {_t('rights_title')}", expanded=False):
        for r in _t("rights_items"):
            st.markdown(f"- {r}", unsafe_allow_html=True)
        st.info(_t("rights_note"))

    with st.expander(f"🌍 {_t('transfer_title')}", expanded=False):
        st.markdown(_t('transfer_body'), unsafe_allow_html=True)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # --- AI ACT TRANSPARENCY ---
    render_ai_transparency()

    st.divider()

    # --- DATA DELETION ---
    st.markdown(f"## {_t('exercise_rights')}")
    render_delete_my_data_button()

    st.divider()

    # --- CONTACT FORM ---
    render_contact_form()

    st.divider()

    st.markdown(f"""
    <p style='color: #6e7681; font-size: 0.8rem; text-align: center;'>
        {_t("footer").format(date=datetime.now().strftime('%d/%m/%Y'))}
    </p>
    """, unsafe_allow_html=True)


# =============================================================================
# AI ACT TRANSPARENCY (Art. 52)
# =============================================================================

def render_ai_transparency():
    st.markdown(f"## {_t('ai_heading')}")
    st.info("Risk Classification: **LIMITED / MINIMAL RISK** (Art. 52 AI Act)")
    
    with st.expander("🤖 AI Models Used & Purpose", expanded=True):
        for model, algo, purpose in AI_MODELS:
            st.markdown(f"**{model}**")
            st.markdown(f"- *Algorithm:* {algo}")
            st.markdown(f"- *Purpose:* {purpose}")
            st.markdown("---")
            
    with st.expander("⚖️ AI Decisions & Human Oversight", expanded=False):
        st.markdown(_t("ai_decisions"), unsafe_allow_html=True)
        st.markdown(_t("ai_oversight"), unsafe_allow_html=True)
        st.markdown(_t("ai_limitations"), unsafe_allow_html=True)


# =============================================================================
# DELETE MY DATA (GDPR Art. 17)
# =============================================================================

def render_delete_my_data_button():
    st.markdown(f"""
    <div class="delete-warning">
        <strong>{_t("delete_title")}</strong><br>
        <span style="font-size: 0.9rem; color: #c9d1d9;">{_t("delete_body")}</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        confirm = st.checkbox(_t("delete_confirm"), key="delete_confirm_checkbox")
        if st.button(_t("delete_btn"), type="primary", use_container_width=True,
                     disabled=not confirm):
            keys_to_clear = list(st.session_state.keys())
            for key in keys_to_clear:
                if key != "page":
                    del st.session_state[key]
            st.success(_t("delete_success"))
            st.info(_t("delete_info"))


# =============================================================================
# CONTACT FORM
# =============================================================================

def render_contact_form():
    st.markdown(f"## {_t('contact_heading')}")
    st.markdown(f"""
    <div class="contact-form">
        <p>{_t("contact_body")}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("gdpr_contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(_t("contact_name"))
        with col2:
            email = st.text_input(_t("contact_email"))

        subject = st.selectbox(_t("contact_subject"), options=_t("contact_subject_options"))
        message = st.text_area(_t("contact_message"), height=120)

        submitted = st.form_submit_button(_t("contact_submit"), use_container_width=True)
        if submitted:
            if name and email and message:
                st.success(_t("contact_success"))
            else:
                st.warning(_t("contact_error"))


# =============================================================================
# SIDEBAR COMPLIANCE WIDGET
# =============================================================================

def render_sidebar_compliance_badge():
    st.markdown(f"""
    <div style='margin-top: 1rem; padding: 8px; background: rgba(0, 200, 83, 0.08);
         border: 1px solid rgba(0, 200, 83, 0.2); border-radius: 8px; text-align: center;'>
        <span style='color: #00C853; font-size: 0.7rem; font-weight: 600;'>
            {_t("sidebar_badge")}
        </span>
    </div>
    """, unsafe_allow_html=True)
