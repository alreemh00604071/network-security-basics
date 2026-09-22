import streamlit as st
import ipaddress
import hashlib

# =========================================================
# PAGE SETUP
# =========================================================
st.set_page_config(
    page_title="Intertec | Network Security",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# DESIGN
# =========================================================
st.markdown("""
<style>

/* PAGE */
.stApp {
    background:
        radial-gradient(circle at 85% 10%, rgba(59,130,246,.20), transparent 25%),
        radial-gradient(circle at 70% 80%, rgba(139,92,246,.16), transparent 30%),
        linear-gradient(135deg, #f8fbff 0%, #eef5ff 50%, #faf7ff 100%);
}

.block-container {
    padding-top: 1.3rem;
    padding-bottom: 3rem;
    max-width: 1250px;
    animation: fadeUp .55s ease;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #eaf3ff 0%, #eef2ff 50%, #f5f3ff 100%);
    border-right: 1px solid #dbeafe;
}

section[data-testid="stSidebar"] img {
    background: white;
    padding: 8px;
    border-radius: 18px;
    box-shadow: 0 8px 22px rgba(15, 46, 90, .10);
}

/* TITLES */
h1, h2, h3 {
    color: #102a56;
}

/* BUTTONS */
.stButton > button {
    width: 100%;
    min-height: 44px;
    border: 0;
    border-radius: 14px;
    color: white;
    font-weight: 700;
    background: linear-gradient(90deg, #1677ff, #7047eb);
    box-shadow: 0 7px 18px rgba(37,99,235,.22);
    transition: all .25s ease;
}

.stButton > button:hover {
    color: white;
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(109,74,255,.32);
}

/* METRICS */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,.80);
    border: 1px solid rgba(255,255,255,.95);
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 9px 25px rgba(30,64,175,.10);
    transition: all .25s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 30px rgba(37,99,235,.18);
}

/* NORMAL STREAMLIT BOXES */
div[data-testid="stAlert"] {
    border-radius: 17px;
}

/* INPUT */
div[data-baseweb="input"] {
    border-radius: 14px;
}

/* HERO */
.hero {
    position: relative;
    overflow: hidden;
    padding: 32px 36px;
    margin-bottom: 24px;
    border-radius: 25px;
    background:
        radial-gradient(circle at 88% 25%, rgba(59,130,246,.75), transparent 27%),
        linear-gradient(115deg, #071b46 0%, #123d85 58%, #7047eb 100%);
    box-shadow: 0 16px 38px rgba(30,64,175,.25);
}

.hero::before {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    right: -65px;
    bottom: -140px;
    background: rgba(255,255,255,.11);
}

.hero-company {
    color: #bfdbfe;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero-title {
    color: white;
    font-size: 40px;
    line-height: 1.15;
    font-weight: 800;
    margin-top: 8px;
}

.hero-subtitle {
    color: #dbeafe;
    font-size: 19px;
    margin-top: 8px;
}

.hero-tags {
    color: #bfdbfe;
    font-size: 14px;
    margin-top: 22px;
}

/* CARDS */
.card {
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(255,255,255,.95);
    border-radius: 20px;
    padding: 21px;
    min-height: 145px;
    margin-bottom: 15px;
    box-shadow: 0 8px 24px rgba(15,46,90,.09);
    transition: all .25s ease;
}

.card:hover {
    transform: translateY(-7px);
    box-shadow: 0 16px 32px rgba(37,99,235,.17);
}

.card-blue {
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
}

.card-green {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
}

.card-purple {
    background: linear-gradient(135deg, #f5f3ff, #ede9fe);
}

.card-orange {
    background: linear-gradient(135deg, #fff7ed, #ffedd5);
}

.card-pink {
    background: linear-gradient(135deg, #fff1f2, #fce7f3);
}

.card-cyan {
    background: linear-gradient(135deg, #ecfeff, #cffafe);
}

.card-title {
    color: #102a56;
    font-size: 19px;
    font-weight: 800;
    margin-bottom: 8px;
}

.card-text {
    color: #475569;
    font-size: 15px;
    line-height: 1.55;
}

/* FOOTER */
.footer-box {
    margin-top: 25px;
    padding: 22px;
    border-radius: 20px;
    color: white;
    background: linear-gradient(100deg, #102a56, #164e9c, #6339d7);
    box-shadow: 0 10px 25px rgba(30,64,175,.18);
}

/* ANIMATION */
@keyframes fadeUp {
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


# =========================================================
# HELPER FUNCTIONS
# =========================================================
def hero(title, subtitle):
    html = (
        '<div class="hero">'
        '<div class="hero-company">INTERTEC SYSTEMS LLC</div>'
        f'<div class="hero-title">{title}</div>'
        f'<div class="hero-subtitle">{subtitle}</div>'
        '<div class="hero-tags">'
        '🛡️ Network Security &nbsp;&nbsp; '
        '📡 Traffic Analysis &nbsp;&nbsp; '
        '🔐 Secure Infrastructure'
        '</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def card(icon, title, text, color):
    html = (
        f'<div class="card {color}">'
        f'<div class="card-title">{icon} {title}</div>'
        f'<div class="card-text">{text}</div>'
        '</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.image("intertec_systems_logo.jpg", width=145)

st.sidebar.markdown("## 🛡️ Security Console")

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
st.sidebar.markdown("### 🔐 Network Security")
st.sidebar.caption("INTERTEC SYSTEMS LLC")
st.sidebar.caption("Network Security Basics Project")


# =========================================================
# DASHBOARD
# =========================================================
if option == "🏠 Dashboard":

    hero(
        "🛡️ Network Security Suite",
        "Monitor. Analyze. Protect."
    )

    # STATUS
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🧰 Security Tools", "7", "Available")

    with c2:
        st.metric("📡 Traffic Analysis", "Wireshark", "Local testing")

    with c3:
        st.metric("🛡️ Firewall", "pfSense", "Demo")

    with c4:
        st.metric("🔎 Network Scan", "Nmap", "Local testing")

    st.write("")
    st.markdown("## 🛡️ Security Tools")

    # FIRST ROW
    c1, c2, c3 = st.columns(3)

    with c1:
        card(
            "🔎",
            "Network Scan",
            "Identify open ports and running services using Nmap.",
            "card-blue"
        )

    with c2:
        card(
            "📡",
            "Traffic Monitoring",
            "Review TCP, DNS and TLS network traffic using Wireshark.",
            "card-green"
        )

    with c3:
        card(
            "🛡️",
            "Firewall",
            "Review secure firewall rules using a pfSense demonstration.",
            "card-pink"
        )

    # SECOND ROW
    c4, c5, c6 = st.columns(3)

    with c4:
        card(
            "⚠️",
            "Vulnerability Check",
            "Review potential security risks and recommendations.",
            "card-orange"
        )

    with c5:
        card(
            "🌐",
            "IP Tools",
            "Validate IPv4 and IPv6 addresses and identify their type.",
            "card-purple"
        )

    with c6:
        card(
            "🔑",
            "Password & Hash Tools",
            "Check password strength and generate SHA-256 hashes.",
            "card-cyan"
        )

    st.markdown(
        '<div class="footer-box">'
        '<b>🔐 Network Security Basics</b><br>'
        'Learn to detect risks, protect network services, '
        'and apply security recommendations.'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# NETWORK SCAN
# =========================================================
elif option == "🔎 Network Scan":

    hero(
        "🔎 Network Scan",
        "Review open ports and running services."
    )

    st.info(
        "Tool: Nmap — Real Nmap testing was completed locally."
    )

    target = st.text_input(
        "Target IP Address",
        "127.0.0.1"
    )

    if st.button("▶ Start Demo Scan"):

        st.success("Demo scan completed.")

        st.code(
            f"""Target: {target}

135/tcp   open   msrpc
445/tcp   open   microsoft-ds
902/tcp   open   vmware-auth
912/tcp   open   vmware-auth"""
        )

    st.warning(
        "Only scan systems you own or have permission to test."
    )


# =========================================================
# TRAFFIC MONITORING
# =========================================================
elif option == "📡 Traffic Monitoring":

    hero(
        "📡 Traffic Monitoring",
        "Analyze network traffic using Wireshark."
    )

    st.info(
        "Wireshark testing was completed locally."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        card(
            "🔵",
            "TCP",
            "Review TCP connections and communication.",
            "card-blue"
        )

    with c2:
        card(
            "🟢",
            "DNS",
            "Review DNS queries and domain requests.",
            "card-green"
        )

    with c3:
        card(
            "🟣",
            "TLS",
            "Review encrypted TLS network traffic.",
            "card-purple"
        )

    if st.button("📡 Show Wireshark Filters"):
        st.code("tcp\ndns\ntls")


# =========================================================
# FIREWALL
# =========================================================
elif option == "🛡️ Firewall":

    hero(
        "🛡️ Firewall Security",
        "Review secure network access rules."
    )

    st.warning("Tool: pfSense — Demonstration")

    c1, c2, c3 = st.columns(3)

    with c1:
        card(
            "✅",
            "HTTPS",
            "ALLOW — Port 443",
            "card-green"
        )

    with c2:
        card(
            "✅",
            "DNS",
            "ALLOW — Port 53",
            "card-blue"
        )

    with c3:
        card(
            "🚫",
            "Telnet",
            "BLOCK — Port 23",
            "card-pink"
        )

    st.info(
        "These rules demonstrate how a firewall can allow "
        "required services and block insecure services."
    )


# =========================================================
# VULNERABILITY CHECK
# =========================================================
elif option == "⚠️ Vulnerability Check":

    hero(
        "⚠️ Vulnerability Check",
        "Review potential network security risks."
    )

    if st.button("🔍 Run Demo Check"):

        st.warning(
            "Port 445 — File sharing service may be exposed."
        )

        st.success(
            "Recommendation: Restrict access to trusted devices."
        )

        st.warning(
            "Telnet Port 23 — Unencrypted remote access."
        )

        st.success(
            "Recommendation: Block Telnet and use SSH."
        )

        st.warning(
            "HTTP Port 80 — Unencrypted web traffic."
        )

        st.success(
            "Recommendation: Use HTTPS/TLS."
        )

        st.info(
            "These are demonstration findings. "
            "Further testing is required to confirm vulnerabilities."
        )


# =========================================================
# IP TOOLS
# =========================================================
elif option == "🌐 IP Tools":

    hero(
        "🌐 IP Address Analyzer",
        "Validate IPv4 and IPv6 addresses."
    )

    ip_input = st.text_input(
        "Enter IP Address",
        "192.168.1.1"
    )

    if st.button("🌐 Analyze IP"):

        try:
            address = ipaddress.ip_address(ip_input.strip())

            st.success("✅ Valid IP Address")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "IP Version",
                    f"IPv{address.version}"
                )

            with c2:
                network_type = (
                    "Private"
                    if address.is_private
                    else "Public"
                )

                st.metric(
                    "Network Type",
                    network_type
                )

            with c3:
                st.metric(
                    "Status",
                    "Valid"
                )

        except ValueError:
            st.error(
                "❌ Invalid IP address. "
                "Enter a valid IPv4 or IPv6 address."
            )


# =========================================================
# PASSWORD & HASH
# =========================================================
elif option == "🔑 Password & Hash Tools":

    hero(
        "🔑 Password & Hash Tools",
        "Test password strength and SHA-256 hashing."
    )

    st.warning(
        "Use a sample password only — do not enter your real password."
    )

    password = st.text_input(
        "Sample Password",
        type="password"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("🔐 Check Password Strength"):

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
                    st.error("🔴 Password Strength: Weak")

                elif score <= 4:
                    st.warning("🟠 Password Strength: Medium")

                else:
                    st.success("🟢 Password Strength: Strong")

    with c2:

        if st.button("🔑 Generate SHA-256 Hash"):

            if not password:
                st.warning("Enter a sample password first.")

            else:
                hashed_password = hashlib.sha256(
                    password.encode()
                ).hexdigest()

                st.success("SHA-256 Hash Generated")
                st.code(hashed_password)


# =========================================================
# SECURITY REPORT
# =========================================================
elif option == "📄 Security Report":

    hero(
        "📄 Security Report",
        "Project findings and security recommendations."
    )

    c1, c2 = st.columns(2)

    with c1:

        card(
            "🔎",
            "Network Scan",
            "Nmap was used locally to identify open ports "
            "and running services.",
            "card-blue"
        )

        card(
            "🛡️",
            "Firewall",
            "pfSense firewall rules are presented "
            "as a demonstration.",
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

    st.markdown("## 🛡️ Recommendations")

    st.success("✅ Use HTTPS/TLS for secure communication.")
    st.success("✅ Block Telnet and use SSH.")
    st.success("✅ Restrict unnecessary open ports.")
    st.success("✅ Apply appropriate firewall rules.")
    st.success("✅ Monitor network traffic regularly.")
    st.success("✅ Use strong passwords.")

    st.info(
        "Nmap and Wireshark testing was completed locally. "
        "The online Nmap and pfSense sections are demonstrations."
    )
