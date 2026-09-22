import streamlit as st
import ipaddress
import hashlib

st.set_page_config(
    page_title="Intertec | Network Security",
    page_icon="🛡️",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .company-name {
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .system-name {
        font-size: 15px;
        color: #666;
        margin-top: 0px;
    }

    .header-line {
        border-bottom: 1px solid #e6e6e6;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    div[data-testid="stMetric"] {
        background: #f7f9fc;
        border: 1px solid #e5e7eb;
        padding: 15px;
        border-radius: 12px;
    }
    /* Colorful background */
.stApp {
    background: linear-gradient(135deg, #f4f8ff 0%, #ffffff 45%, #f3f0ff 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #eaf3ff 0%, #f5f0ff 100%);
    border-right: 1px solid #dbeafe;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #ffffff, #eaf4ff);
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

/* Movement when mouse goes over card */
div[data-testid="stMetric"]:hover {
    transform: translateY(-7px);
    box-shadow: 0 12px 28px rgba(37,99,235,0.18);
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 18px rgba(37,99,235,0.30);
    color: white;
}

/* Titles */
h1, h2, h3 {
    color: #172554;
}

/* Smooth page animation */
.block-container {
    animation: fadeIn 0.7s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- COMPANY HEADER ----------
logo_col, name_col = st.columns([1, 5])

with logo_col:
    st.image("intertec_systems_logo.jpg", width=120)

with name_col:
    st.markdown(
        '<p class="company-name">INTERTEC SYSTEMS LLC</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="system-name">Network Security Basics</p>',
        unsafe_allow_html=True
    )

st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("🛡️ Security Console")

option = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🔎 Network Scan",
        "📡 Traffic Monitoring",
        "🛡️ Firewall",
        "⚠️ Vulnerability Check",
        "🌐 IP Tools",
        "🔑 Password & Hash Tools",
        "📄 Security Report"
    ]
)

st.sidebar.divider()
st.sidebar.caption("INTERTEC SYSTEMS LLC")
st.sidebar.caption("Network Security Basics")

# ---------- DASHBOARD ----------
if option == "🏠 Dashboard":

    st.title("Security Dashboard")
    st.write(
        "Monitor and review basic network security tools from one dashboard."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Security Tools", "7")

    with col2:
        st.metric("Monitoring", "Active")

    with col3:
        st.metric("Environment", "Demo")

    st.subheader("Security Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        🔎 **Network Scan**

        Identify open ports and running services using Nmap.
        """)

        st.info("""
        🛡️ **Firewall**

        Review firewall rules and network access controls.
        """)

        st.info("""
        🌐 **IP Tools**

        Validate IPv4 and IPv6 addresses.
        """)

    with col2:
        st.info("""
        📡 **Traffic Monitoring**

        Review network traffic concepts using Wireshark.
        """)

        st.info("""
        ⚠️ **Vulnerability Check**

        Review potential network security risks.
        """)

        st.info("""
        🔑 **Password & Hash Tools**

        Check password strength and generate SHA-256 hashes.
        """)

# ---------- NETWORK SCAN ----------
elif option == "🔎 Network Scan":

    st.header("🔎 Network Scan")
    st.write("Tool: **Nmap**")
    st.write("Identify open ports and running services.")

    target = st.text_input(
        "Target IP Address",
        "127.0.0.1"
    )

    if st.button("Start Demo Scan"):
        st.success("Demo scan completed.")

        st.code(
f"""Target: {target}

135/tcp   open   msrpc
445/tcp   open   microsoft-ds
902/tcp   open   vmware-auth
912/tcp   open   vmware-auth"""
        )

    st.caption(
        "Real Nmap testing was performed locally. "
        "Only scan systems you own or have permission to test."
    )

# ---------- TRAFFIC ----------
elif option == "📡 Traffic Monitoring":

    st.header("📡 Traffic Monitoring")
    st.write("Tool: **Wireshark**")
    st.write("Review network traffic and common protocols.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TCP", "Monitored")

    with col2:
        st.metric("DNS", "Monitored")

    with col3:
        st.metric("TLS", "Monitored")

    if st.button("Show Wireshark Filters"):
        st.code("""tcp
dns
tls""")

        st.success("Traffic monitoring information displayed.")

# ---------- FIREWALL ----------
elif option == "🛡️ Firewall":

    st.header("🛡️ Firewall")
    st.write("Tool: **pfSense**")
    st.write("Status: **Demonstration**")

    st.subheader("Firewall Rules")

    st.success("✅ ALLOW HTTPS — Port 443")
    st.success("✅ ALLOW DNS — Port 53")
    st.error("🚫 BLOCK Telnet — Port 23")

    st.info(
        "This section demonstrates how firewall rules can "
        "allow required services and block insecure services."
    )

# ---------- VULNERABILITY ----------
elif option == "⚠️ Vulnerability Check":

    st.header("⚠️ Vulnerability Check")
    st.write("Review potential network security findings.")

    if st.button("Run Demo Check"):

        st.warning("Port 445 — File sharing service may be exposed.")
        st.write("Recommendation: Restrict access to trusted devices.")

        st.warning("Telnet Port 23 — Unencrypted remote access.")
        st.write("Recommendation: Block Telnet and use SSH.")

        st.warning("HTTP Port 80 — Unencrypted web traffic.")
        st.write("Recommendation: Use HTTPS/TLS.")

        st.info(
            "These are demonstration findings. "
            "Further testing is required to confirm vulnerabilities."
        )

# ---------- IP TOOLS ----------
elif option == "🌐 IP Tools":

    st.header("🌐 IP Address Analyzer")
    st.write("Validate an IP address and identify its network type.")

    ip_input = st.text_input(
        "IP Address",
        "192.168.1.1"
    )

    if st.button("Analyze IP"):

        try:
            address = ipaddress.ip_address(ip_input.strip())

            st.success("Valid IP Address")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Version", f"IPv{address.version}")

            with col2:
                if address.is_private:
                    st.metric("Network Type", "Private")
                else:
                    st.metric("Network Type", "Public")

            with col3:
                st.metric("Status", "Valid")

        except ValueError:
            st.error("Invalid IP address.")

# ---------- PASSWORD ----------
elif option == "🔑 Password & Hash Tools":

    st.header("🔑 Password & Hash Tools")
    st.write(
        "Check password strength and generate a SHA-256 hash."
    )

    password = st.text_input(
        "Test Password",
        type="password"
    )

    st.caption("Use a sample password only — not your real password.")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Check Strength"):

            if not password:
                st.warning("Enter a sample password first.")

            else:
                score = 0

                if len(password) >= 8:
                    score += 1
                if any(c.isupper() for c in password):
                    score += 1
                if any(c.islower() for c in password):
                    score += 1
                if any(c.isdigit() for c in password):
                    score += 1
                if any(not c.isalnum() for c in password):
                    score += 1

                if score <= 2:
                    st.error("Password Strength: Weak")
                elif score <= 4:
                    st.warning("Password Strength: Medium")
                else:
                    st.success("Password Strength: Strong")

    with col2:

        if st.button("Generate SHA-256"):

            if not password:
                st.warning("Enter a sample password first.")

            else:
                hashed_password = hashlib.sha256(
                    password.encode()
                ).hexdigest()

                st.success("SHA-256 Generated")
                st.code(hashed_password)

# ---------- REPORT ----------
elif option == "📄 Security Report":

    st.header("📄 Security Report")
    st.caption("INTERTEC SYSTEMS LLC | Network Security Basics")

    st.subheader("Network Scan")
    st.write("Nmap — Open port and service identification.")

    st.subheader("Traffic Monitoring")
    st.write("Wireshark — TCP, DNS and TLS traffic analysis.")

    st.subheader("Firewall")
    st.write("pfSense — Firewall rule demonstration.")

    st.subheader("IP Analysis")
    st.write("IPv4 and IPv6 address validation.")

    st.subheader("Password Security")
    st.write("Password strength and SHA-256 demonstration.")

    st.subheader("Security Recommendations")

    st.write("• Use HTTPS/TLS for secure communication.")
    st.write("• Block Telnet and use SSH.")
    st.write("• Restrict unnecessary open ports.")
    st.write("• Apply firewall rules.")
    st.write("• Monitor network traffic regularly.")
    st.write("• Use strong passwords.")

    st.success("Security report ready.")
