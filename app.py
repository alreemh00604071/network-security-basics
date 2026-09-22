import streamlit as st
import ipaddress
import hashlib

st.set_page_config(
    page_title="Intertec | Network Security",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# DESIGN
# =========================
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at 85% 10%, #dbeafe 0%, transparent 28%),
        radial-gradient(circle at 65% 80%, #ede9fe 0%, transparent 30%),
        linear-gradient(135deg, #f8fbff 0%, #eef5ff 50%, #faf7ff 100%);
}

/* MAIN PAGE */
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    animation: pageLoad 0.6s ease;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #eaf3ff 0%,
        #f1efff 55%,
        #e8f4ff 100%
    );
    border-right: 1px solid #cbdcf7;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}

/* HEADINGS */
h1 {
    color: #102a56;
    font-weight: 800;
}

h2, h3 {
    color: #173b72;
}

/* HERO */
.hero {
    padding: 30px 35px;
    border-radius: 24px;
    margin-bottom: 24px;

    background:
        radial-gradient(circle at 90% 20%, #2563eb 0%, transparent 35%),
        linear-gradient(120deg, #071b46, #123d85 55%, #6039d9);

    box-shadow: 0 15px 35px rgba(30, 64, 175, 0.20);
    color: white;

    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    right: -70px;
    bottom: -140px;
    border-radius: 50%;
    background: rgba(255,255,255,0.10);
}

.hero-small {
    color: #bfdbfe;
    font-size: 17px;
    margin-bottom: 5px;
}

.hero-title {
    color: white;
    font-size: 38px;
    font-weight: 800;
    margin: 0;
}

.hero-text {
    color: #dbeafe;
    font-size: 18px;
    margin-top: 8px;
}

/* STATUS CARDS */
.status-card {
    padding: 20px;
    border-radius: 20px;
    min-height: 130px;
    border: 1px solid rgba(255,255,255,0.8);
    box-shadow: 0 8px 22px rgba(30,64,175,0.10);
    transition: 0.25s ease;
}

.status-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 30px rgba(30,64,175,0.18);
}

.green-card {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
}

.blue-card {
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
}

.purple-card {
    background: linear-gradient(135deg, #f5f3ff, #ede9fe);
}

.orange-card {
    background: linear-gradient(135deg, #fff7ed, #ffedd5);
}

.status-title {
    font-size: 14px;
    font-weight: 700;
    color: #334155;
}

.status-number {
    font-size: 30px;
    font-weight: 800;
    color: #172554;
    margin-top: 7px;
}

/* TOOL CARDS */
.tool-card {
    padding: 22px;
    border-radius: 20px;
    margin-bottom: 15px;
    min-height: 155px;

    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(219,234,254,0.95);

    box-shadow: 0 8px 24px rgba(15, 46, 90, 0.08);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.tool-card:hover {
    transform: translateY(-7px) scale(1.01);
    box-shadow: 0 15px 35px rgba(37,99,235,0.16);
}

.tool-title {
    font-size: 19px;
    font-weight: 800;
    color: #102a56;
}

.tool-text {
    color: #475569;
    margin-top: 8px;
}

/* BUTTONS */
.stButton > button {
    width: 100%;
    border: 0;
    border-radius: 13px;
    padding: 0.65rem 1rem;

    background: linear-gradient(
        90deg,
        #1677ff,
        #6d4aff
    );

    color: white;
    font-weight: 700;

    box-shadow: 0 6px 18px rgba(37,99,235,0.20);

    transition: 0.25s ease;
}

.stButton > button:hover {
    color: white;
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 10px 25px rgba(109,74,255,0.30);
}

/* INPUTS */
div[data-baseweb="input"] {
    border-radius: 12px;
}

/* INFO BOXES */
div[data-testid="stAlert"] {
    border-radius: 15px;
}

/* PAGE ANIMATION */
@keyframes pageLoad {
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


# =========================
# SIDEBAR
# =========================

st.sidebar.image("intertec_systems_logo.jpg", width=150)

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


# =========================
# DASHBOARD
# =========================

if option == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">

        <div class="hero-small">
            INTERTEC SYSTEMS LLC
        </div>

        <div class="hero-title">
            🛡️ Network Security Suite
        </div>

        <div class="hero-text">
            Monitor. Analyze. Protect.
        </div>

        <br>

        <div style="color:#bfdbfe;">
            Network Security • Traffic Analysis • Secure Infrastructure
        </div>

    </div>
    """, unsafe_allow_html=True)

    # STATUS CARDS
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="status-card green-card">
            <div class="status-title">🧰 SECURITY TOOLS</div>
            <div class="status-number">7</div>
            <div>Available tools</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="status-card blue-card">
            <div class="status-title">📡 TRAFFIC ANALYSIS</div>
            <div class="status-number">Wireshark</div>
            <div>TCP • DNS • TLS</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="status-card purple-card">
            <div class="status-title">🛡️ FIREWALL</div>
            <div class="status-number">Demo</div>
            <div>pfSense rules</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="status-card orange-card">
            <div class="status-title">🔎 NETWORK SCAN</div>
            <div class="status-number">Nmap</div>
            <div>Local testing completed</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("## 🔐 Security Tools")

    # ROW 1
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🔎 Network Scan</div>
            <div class="tool-text">
                Identify open ports and running services using Nmap.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-title">📡 Traffic Monitoring</div>
            <div class="tool-text">
                Review TCP, DNS and TLS traffic using Wireshark.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🛡️ Firewall</div>
            <div class="tool-text">
                Demonstrate secure firewall rules using pfSense.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ROW 2
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-title">⚠️ Vulnerability Check</div>
            <div class="tool-text">
                Review potential security risks and recommendations.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🌐 IP Tools</div>
            <div class="tool-text">
                Validate IPv4 and IPv6 addresses.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🔑 Password & Hash Tools</div>
            <div class="tool-text">
                Check password strength and generate SHA-256 hashes.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "📄 Security Report — Review the project findings "
        "and security recommendations."
    )


# =========================
# NETWORK SCAN
# =========================

elif option == "🔎 Network Scan":

    st.title("🔎 Network Scan")

    st.info(
        "Nmap is used to identify open ports and running services."
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

    st.caption(
        "Real Nmap testing was completed locally. "
        "Only scan systems you own or have permission to test."
    )


# =========================
# TRAFFIC MONITORING
# =========================

elif option == "📡 Traffic Monitoring":

    st.title("📡 Traffic Monitoring")

    st.info(
        "Wireshark was used locally to capture and review network traffic."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="status-card blue-card">
            <div class="status-title">TCP</div>
            <div class="status-number">tcp</div>
            <div>Connection traffic</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="status-card green-card">
            <div class="status-title">DNS</div>
            <div class="status-number">dns</div>
            <div>DNS queries</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="status-card purple-card">
            <div class="status-title">TLS</div>
            <div class="status-number">tls</div>
            <div>Encrypted traffic</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Show Wireshark Filters"):
        st.code("""tcp
dns
tls""")


# =========================
# FIREWALL
# =========================

elif option == "🛡️ Firewall":

    st.title("🛡️ Firewall Security")

    st.warning("pfSense section — Demonstration")

    st.success("✅ ALLOW HTTPS — Port 443")
    st.success("✅ ALLOW DNS — Port 53")
    st.error("🚫 BLOCK Telnet — Port 23")

    st.info(
        "This demonstrates how firewall rules can allow "
        "required services and block insecure services."
    )


# =========================
# VULNERABILITY CHECK
# =========================

elif option == "⚠️ Vulnerability Check":

    st.title("⚠️ Vulnerability Check")

    st.write(
        "Review potential network security findings "
        "and recommended controls."
    )

    if st.button("🔍 Run Demo Check"):

        st.warning(
            "Port 445 — File sharing service may be exposed."
        )
        st.write(
            "🛡️ Recommendation: Restrict access to trusted devices."
        )

        st.warning(
            "Telnet Port 23 — Unencrypted remote access."
        )
        st.write(
            "🛡️ Recommendation: Block Telnet and use SSH."
        )

        st.warning(
            "HTTP Port 80 — Unencrypted web traffic."
        )
        st.write(
            "🛡️ Recommendation: Use HTTPS/TLS."
        )

        st.info(
            "These are demonstration findings. "
            "Further testing is required to confirm vulnerabilities."
        )


# =========================
# IP TOOLS
# =========================

elif option == "🌐 IP Tools":

    st.title("🌐 IP Address Analyzer")

    st.write(
        "Validate an IPv4 or IPv6 address and identify its type."
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

                if address.is_private:
                    st.metric(
                        "Network Type",
                        "Private"
                    )
                else:
                    st.metric(
                        "Network Type",
                        "Public"
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


# =========================
# PASSWORD TOOLS
# =========================

elif option == "🔑 Password & Hash Tools":

    st.title("🔑 Password & Hash Tools")

    st.write(
        "Check password strength and generate a SHA-256 hash."
    )

    st.warning(
        "Use a sample password only. "
        "Do not enter your real password."
    )

    password = st.text_input(
        "Sample Password",
        type="password"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("🔐 Check Password Strength"):

            if not password:

                st.warning(
                    "Enter a sample password first."
                )

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
                    st.error(
                        "🔴 Password Strength: Weak"
                    )

                elif score <= 4:
                    st.warning(
                        "🟠 Password Strength: Medium"
                    )

                else:
                    st.success(
                        "🟢 Password Strength: Strong"
                    )

    with c2:

        if st.button("🔑 Generate SHA-256 Hash"):

            if not password:

                st.warning(
                    "Enter a sample password first."
                )

            else:

                hashed_password = hashlib.sha256(
                    password.encode()
                ).hexdigest()

                st.success(
                    "SHA-256 Hash Generated"
                )

                st.code(hashed_password)


# =========================
# SECURITY REPORT
# =========================

elif option == "📄 Security Report":

    st.title("📄 Security Report")

    st.markdown("""
    <div class="hero">
        <div class="hero-small">
            INTERTEC SYSTEMS LLC
        </div>

        <div class="hero-title">
            Network Security Basics
        </div>

        <div class="hero-text">
            Security findings and recommendations
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🔎 Network Scan")
    st.write(
        "Nmap — Identify open ports and running services."
    )

    st.subheader("📡 Traffic Monitoring")
    st.write(
        "Wireshark — Review TCP, DNS and TLS traffic."
    )

    st.subheader("🛡️ Firewall")
    st.write(
        "pfSense — Firewall rule demonstration."
    )

    st.subheader("🌐 IP Tools")
    st.write(
        "Validate IPv4 and IPv6 addresses."
    )

    st.subheader("🔑 Password Security")
    st.write(
        "Password strength and SHA-256 demonstration."
    )

    st.subheader("🛡️ Security Recommendations")

    st.success("Use HTTPS/TLS for secure communication.")
    st.success("Block Telnet and use SSH.")
    st.success("Restrict unnecessary open ports.")
    st.success("Apply appropriate firewall rules.")
    st.success("Monitor network traffic regularly.")
    st.success("Use strong passwords.")

    st.info(
        "Nmap and Wireshark testing was completed locally. "
        "The online Nmap and pfSense sections are demonstrations."
    )
