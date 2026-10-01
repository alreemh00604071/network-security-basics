import streamlit as st
import ipaddress
import hashlib
import glob
from pathlib import Path

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Intertec | Network Security",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# LOGIN / ACCESS CONTROL
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"

# Demo staff password. You can later set STAFF_PASSWORD in Streamlit Secrets.
try:
    STAFF_PASSWORD = st.secrets.get("STAFF_PASSWORD", "Staff123")
except Exception:
    STAFF_PASSWORD = "Staff123"


def show_login():
    st.markdown("## 🔐 Network Security Suite Login")
    st.write("Please select your access type.")

    role_choice = st.selectbox("Select Role", ["Guest", "Staff"])

    if role_choice == "Guest":
        st.info(
            "Guest access includes Dashboard, Network Scan, "
            "Traffic Monitoring and Security Report."
        )
        if st.button("Continue as Guest", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.role = "Guest"
            st.session_state.page = "🏠 Dashboard"
            st.rerun()
    else:
        st.info("Staff access includes all security tools.")
        password = st.text_input("Enter Staff Password", type="password")
        if st.button("Login as Staff", use_container_width=True):
            if password == STAFF_PASSWORD:
                st.session_state.logged_in = True
                st.session_state.role = "Staff"
                st.session_state.page = "🏠 Dashboard"
                st.rerun()
            else:
                st.error("Incorrect staff password.")


if not st.session_state.logged_in:
    show_login()
    st.stop()


if st.session_state.role == "Staff":
    pages = [
        "🏠 Dashboard",
        "🧰 Security Tools",
        "🔎 Network Scan",
        "📡 Traffic Monitoring",
        "🛡️ Firewall",
        "⚠️ Vulnerability Check",
        "🌐 IP Tools",
        "🔑 Password & Hash Tools",
        "📄 Security Report"
    ]
else:
    pages = [
        "🏠 Dashboard",
        "🔎 Network Scan",
        "📡 Traffic Monitoring",
        "📄 Security Report"
    ]

if st.session_state.page not in pages:
    st.session_state.page = "🏠 Dashboard"


def go_to(page):
    if page in pages:
