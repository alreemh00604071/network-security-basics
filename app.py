import streamlit as st
import ipaddress
import hashlib
import glob
from pathlib import Path


st.code(
                    hashed_password
                )


    if st.button(
        "⬅ Back to Dashboard",
        key="back_password"
    ):
        go_to(
            "🏠 Dashboard"
        )
        st.rerun()


# =========================================================
# SECURITY REPORT
# =========================================================

elif st.session_state.page == "📄 Security Report":

    hero(
        "📄 Security Report",
        "Project findings and security recommendations."
    )

    c1, c2 = st.columns(2)

    with c1:

        card(
            "🔎",
            "Network Scan",
            "Nmap was used locally to identify open ports and running services.",
            "card-blue"
        )

        card(
            "🛡️",
            "Firewall",
            "pfSense firewall rules are presented as a demonstration.",
            "card-pink"
        )

        card(
            "🔑",
            "Password Security",
            "Password strength and SHA-256 hashing demonstration.",
            "card-purple"
        )


    with c2:

        card(
            "📡",
            "Traffic Monitoring",
            "Wireshark was used locally with TCP, DNS and TLS filters.",
            "card-green"
        )

        card(
            "🌐",
            "IP Tools",
            "IPv4 and IPv6 address validation.",
            "card-cyan"
        )

        card(
            "⚠️",
            "Security Findings",
            "Potential risks are reviewed with security recommendations.",
            "card-orange"
        )


    st.markdown(
        "## 🛡️ Security Recommendations"
    )

    st.success(
        "✅ Use HTTPS/TLS for secure communication."
    )

    st.success(
        "✅ Block Telnet and use SSH."
    )

    st.success(
        "✅ Restrict unnecessary open ports."
    )

    st.success(
        "✅ Apply appropriate firewall rules."
    )

    st.success(
        "✅ Monitor network traffic regularly."
    )

    st.success(
        "✅ Use strong passwords."
    )


    st.info(
        "Nmap and Wireshark testing was completed locally. The online Nmap and pfSense sections are demonstrations."
    )


    st.markdown(
        """
        <div class="footer-box">

        <b>INTERTEC SYSTEMS LLC</b>

        <br><br>

        Network Security Basics Project

        <br>

        Monitor • Analyze • Protect

        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button(
        "⬅ Back to Dashboard",
        key="back_report"
    ):
        go_to(
            "🏠 Dashboard"
        )
        st.rerun()
