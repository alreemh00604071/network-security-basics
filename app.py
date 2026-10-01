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
# SESSION STATE
# =========================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"

# =========================================================
# HELPERS
# =========================================================
def find_project_logo():
    preferred = [
        "network_security_suite_logo.png",
        "network_security_suite_logo.jpg",
        "network_security_suite_logo.jpeg",
    ]

    for filename in preferred:
        if Path(filename).exists():
            return filename

    matches = sorted(
        glob.glob("network_security_suite_logo*")
    )

    return matches[0] if matches else None


def hero(title, subtitle):

    st.markdown(
        f"""
        <div class="hero">

            <div class="hero-company">
                INTERTEC SYSTEMS LLC
            </div>

            <div class="hero-title">
                {title}
            </div>

            <div class="hero-subtitle">
                {subtitle}
            </div>

            <div class="hero-tags">
                🛡️ Network Security
                &nbsp;&nbsp;
                📡 Traffic Analysis
                &nbsp;&nbsp;
                🔐 Secure Infrastructure
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def card(
    icon,
    title,
    text,
    color
):

    st.markdown(
        f"""
        <div class="card {color}">

            <div class="card-title">
                {icon} {title}
            </div>

            <div class="card-text">
                {text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# DESIGN
# =========================================================
st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 88% 10%,
                rgba(59,130,246,.20),
                transparent 25%
            ),

            radial-gradient(
                circle at 70% 80%,
                rgba(139,92,246,.16),
                transparent 30%
            ),

            linear-gradient(
                135deg,
                #f8fbff 0%,
                #eef5ff 50%,
                #faf7ff 100%
            );
    }


    .block-container {
        padding-top: 1.3rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }


    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #eaf3ff 0%,
                #eef2ff 50%,
                #f5f3ff 100%
            );

        border-right: 1px solid #dbeafe;
    }


    section[data-testid="stSidebar"] img {
        background: white;

        padding: 8px;

        border-radius: 18px;

        box-shadow:
            0 8px 22px
            rgba(15,46,90,.10);
    }


    h1, h2, h3 {
        color: #102a56;
    }


    .stButton > button {

        width: 100%;

        min-height: 46px;

        border: 0;

        border-radius: 14px;

        color: white;

        font-weight: 700;

        background:
            linear-gradient(
                90deg,
                #1677ff,
                #7047eb
            );

        box-shadow:
            0 7px 18px
            rgba(37,99,235,.22);

        transition:
            transform .25s ease,
            box-shadow .25s ease;
    }


    .stButton > button:hover {

        color: white;

        transform:
            translateY(-3px);

        box-shadow:
            0 13px 27px
            rgba(109,74,255,.30);
    }


    div[data-testid="stMetric"] {

        background:
            rgba(255,255,255,.90);

        border:
            1px solid
            rgba(255,255,255,.95);

        border-radius: 20px;

        padding: 20px;

        box-shadow:
            0 10px 27px
            rgba(30,64,175,.12);
    }


    div[data-testid="stAlert"] {
        border-radius: 17px;
    }


    div[data-baseweb="input"] {
        border-radius: 14px;
    }


    .hero {

        position: relative;

        overflow: hidden;

        padding:
            32px 36px;

        margin-bottom:
            24px;

        border-radius:
            25px;

        background:

            radial-gradient(
                circle at 88% 25%,
                rgba(59,130,246,.75),
                transparent 27%
            ),

            linear-gradient(
                115deg,
                #071b46 0%,
                #123d85 58%,
                #7047eb 100%
            );

        box-shadow:
            0 16px 38px
            rgba(30,64,175,.25);
    }


    .hero::before {

        content: "";

        position: absolute;

        width: 230px;

        height: 230px;

        border-radius: 50%;

        right: -65px;

        bottom: -140px;

        background:
            rgba(255,255,255,.11);
    }


    .hero::after {

        content: "";

        position: absolute;

        width: 120px;

        height: 120px;

        border-radius: 50%;

        right: 70px;

        top: -60px;

        background:
            rgba(255,255,255,.08);
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


    .card {

        background:
            rgba(255,255,255,.82);

        border:
            1px solid
            rgba(255,255,255,.95);

        border-radius:
            20px;

        padding:
            21px;

        min-height:
            145px;

        margin-bottom:
            15px;

        box-shadow:
            0 8px 24px
            rgba(15,46,90,.09);

        transition:
            all .25s ease;
    }


    .card:hover {

        transform:
            translateY(-6px);

        box-shadow:
            0 16px 32px
            rgba(37,99,235,.17);
    }


    .card-blue {
        background:
            linear-gradient(
                135deg,
                #eff6ff,
                #dbeafe
            );
    }


    .card-green {
        background:
            linear-gradient(
                135deg,
                #ecfdf5,
                #d1fae5
            );
    }


    .card-purple {
        background:
            linear-gradient(
                135deg,
                #f5f3ff,
                #ede9fe
            );
    }


    .card-orange {
        background:
            linear-gradient(
                135deg,
                #fff7ed,
                #ffedd5
            );
    }


    .card-pink {
        background:
            linear-gradient(
                135deg,
                #fff1f2,
                #fce7f3
            );
    }


    .card-cyan {
        background:
            linear-gradient(
                135deg,
                #ecfeff,
                #cffafe
            );
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


    .footer-box {

        margin-top:
            25px;

        padding:
            22px;

        border-radius:
            20px;

        color:
            white;

        background:
            linear-gradient(
                100deg,
                #102a56,
                #164e9c,
                #6339d7
            );

        box-shadow:
            0 10px 25px
            rgba(30,64,175,.18);
    }


    .lock-note {

        color:
            #64748b;

        font-size:
            14px;

        margin-top:
            -4px;

        margin-bottom:
            10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    logo = find_project_logo()

    if logo:

        c1, c2, c3 = st.columns(
            [1, 1.5, 1]
        )

        with c2:

            st.image(
                logo,
                width=220
            )


    hero(
        "🛡️ Network Security Suite",
        "Secure access for Guest and Staff."
    )


    st.subheader(
        "🔐 Login"
    )


    role = st.selectbox(
        "Select Access Type",
        [
            "Guest",
            "Staff"
        ]
    )


    if role == "Guest":

        st.info(
            "Guest access includes Dashboard, "
            "Network Scan, Traffic Monitoring, "
            "and Security Report."
        )


        if st.button(
            "Continue as Guest"
        ):

            st.session_state.logged_in = True

            st.session_state.role = "Guest"

            st.session_state.page = "🏠 Dashboard"

            st.rerun()


    else:

        st.info(
            "Staff access includes all security "
            "tools and protected sections."
        )


        password = st.text_input(
            "Staff Password",
            type="password"
        )


        if st.button(
            "Login as Staff"
        ):

            if password == "Staff123":

                st.session_state.logged_in = True

                st.session_state.role = "Staff"

                st.session_state.page = "🏠 Dashboard"

                st.rerun()

            else:

                st.error(
                    "Incorrect staff password."
                )


    st.stop()


# =========================================================
# ROLE-BASED PAGES
# =========================================================

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

        st.session_state.page = page

    else:

        st.session_state.page = "🏠 Dashboard"


# =========================================================
# SIDEBAR
# =========================================================

project_logo = find_project_logo()


if project_logo:

    st.sidebar.image(
        project_logo,
        width=190
    )

else:

    st.sidebar.markdown(
        "### 🛡️ Network Security Suite"
    )


st.sidebar.markdown(
    "## 🛡️ Security Console"
)


st.sidebar.success(
    f"Logged in as: {st.session_state.role}"
)


option = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(
        st.session_state.page
    )
)


if option != st.session_state.page:

    st.session_state.page = option

    st.rerun()


if st.sidebar.button(
    "🚪 Logout"
):

    st.session_state.logged_in = False

    st.session_state.role = None

    st.session_state.page = "🏠 Dashboard"

    st.rerun()


st.sidebar.divider()


if Path(
    "intertec_systems_logo.jpg"
).exists():

    st.sidebar.image(
        "intertec_systems_logo.jpg",
        width=150
    )


st.sidebar.caption(
    "INTERTEC SYSTEMS LLC"
)


st.sidebar.caption(
    "Network Security Basics Project"
)


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "🏠 Dashboard":

    hero(
        "🛡️ Network Security Suite",
        "Monitor. Analyze. Protect."
    )


    st.markdown(
        "### ⚡ Quick Access"
    )


    q1, q2, q3, q4 = st.columns(4)


    # -----------------------------------------------------
    # SECURITY TOOLS
    # -----------------------------------------------------

    with q1:

        st.metric(
            "🧰 Security Tools",
            "7",
            "Available"
        )


        if st.session_state.role == "Staff":

            if st.button(
                "🧰 View Tools",
                key="quick_tools"
            ):

                go_to(
                    "🧰 Security Tools"
                )

                st.rerun()

        else:

            st.markdown(
                """
                <div class="lock-note">
                    🔒 Staff access only
                </div>
                """,
                unsafe_allow_html=True
            )


    # -----------------------------------------------------
    # WIRESHARK
    # -----------------------------------------------------

    with q2:

        st.metric(
            "📡 Traffic Analysis",
            "Wireshark",
            "Local testing"
        )


        if st.button(
            "📡 Open Wireshark",
            key="quick_wireshark"
        ):

            go_to(
                "📡 Traffic Monitoring"
            )

            st.rerun()


    # -----------------------------------------------------
    # FIREWALL
    # -----------------------------------------------------

    with q3:

        st.metric(
            "🛡️ Firewall",
            "pfSense",
            "Demo"
        )


        if st.session_state.role == "Staff":

            if st.button(
                "🛡️ Open pfSense",
                key="quick_firewall"
            ):

                go_to(
                    "🛡️ Firewall"
                )

                st.rerun()

        else:

            st.markdown(
                """
                <div class="lock-note">
                    🔒 Staff access only
                </div>
                """,
                unsafe_allow_html=True
            )


    # -----------------------------------------------------
    # NMAP
    # -----------------------------------------------------

    with q4:

        st.metric(
            "🔎 Network Scan",
            "Nmap",
            "Local testing"
        )


        if st.button(
            "🔎 Open Nmap",
            key="quick_nmap"
        ):

            go_to(
                "🔎 Network Scan"
            )

            st.rerun()


    st.write("")


    st.markdown(
        "## 🛡️ Security Tools"
    )


    # -----------------------------------------------------
    # FIRST ROW
    # -----------------------------------------------------

    c1, c2, c3 = st.columns(3)


    with c1:

        card(
            "🔎",
            "Network Scan",
            "Identify open ports and running services using Nmap.",
            "card-blue"
        )


        if st.button(
            "Open Network Scan →",
            key="card_nmap"
        ):

            go_to(
                "🔎 Network Scan"
            )

            st.rerun()


    with c2:

        card(
            "📡",
            "Traffic Monitoring",
            "Review TCP, DNS and TLS network traffic using Wireshark.",
            "card-green"
        )


        if st.button(
            "Open Traffic Monitoring →",
            key="card_wireshark"
        ):

            go_to(
                "📡 Traffic Monitoring"
            )

            st.rerun()


    with c3:

        card(
            "🛡️",
            "Firewall",
            "Review secure firewall rules using a pfSense demonstration.",
            "card-pink"
        )


        if st.session_state.role == "Staff":

            if st.button(
                "Open Firewall →",
                key="card_firewall"
            ):

                go_to(
                    "🛡️ Firewall"
                )

                st.rerun()

        else:

            st.caption(
                "🔒 Staff access only"
            )


    # -----------------------------------------------------
    # SECOND ROW
    # -----------------------------------------------------

    c4, c5, c6 = st.columns(3)


    with c4:

        card(
            "⚠️",
            "Vulnerability Check",
            "Review potential security risks and recommendations.",
            "card-orange"
        )


        if st.session_state.role == "Staff":

            if st.button(
                "Run Vulnerability Check →",
                key="card_vulnerability"
            ):

                go_to(
                    "⚠️ Vulnerability Check"
                )

                st.rerun()

        else:

            st.caption(
                "🔒 Staff access only"
            )


    with c5:

        card(
            "🌐",
            "IP Tools",
            "Validate IPv4 and IPv6 addresses and identify their type.",
            "card-purple"
        )


        if st.session_state.role == "Staff":

            if st.button(
                "Open IP Tools →",
                key="card_ip"
            ):

                go_to(
                    "🌐 IP Tools"
                )

                st.rerun()

        else:

            st.caption(
                "🔒 Staff access only"
            )


    with c6:

        card(
            "🔑",
            "Password & Hash Tools",
            "Check password strength and generate SHA-256 hashes.",
            "card-cyan"
        )


        if st.session_state.role == "Staff":

            if st.button(
                "Open Password Tools →",
                key="card_password"
            ):

                go_to(
                    "🔑 Password & Hash Tools"
                )

                st.rerun()

        else:

            st.caption(
                "🔒 Staff access only"
            )


    st.markdown(
        """
        <div class="footer-box">

            <b>
                🔐 Network Security Basics
            </b>

            <br><br>

            Learn to detect security risks,
            analyze network traffic,
            protect network services,
            and apply security recommendations.

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SECURITY TOOLS - STAFF ONLY
# =========================================================

elif st.session_state.page == "🧰 Security Tools":

    if st.session_state.role != "Staff":

        st.error(
            "Staff access only."
        )

        st.stop()


    hero(
        "🧰 Security Tools",
        "Choose a network security tool to open."
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        card(
            "🔎",
            "Network Scan",
            "Identify open ports and running services using Nmap.",
            "card-blue"
        )


        if st.button(
            "Open Network Scan →",
            key="tools_nmap"
        ):

            go_to(
                "🔎 Network Scan"
            )

            st.rerun()


    with c2:

        card(
            "📡",
            "Traffic Monitoring",
            "Review TCP, DNS and TLS traffic using Wireshark.",
            "card-green"
        )


        if st.button(
            "Open Traffic Monitoring →",
            key="tools_wireshark"
        ):

            go_to(
                "📡 Traffic Monitoring"
            )

            st.rerun()


    with c3:

        card(
            "🛡️",
            "Firewall",
            "Review secure firewall rules using a pfSense demonstration.",
            "card-pink"
        )


        if st.button(
            "Open Firewall →",
            key="tools_firewall"
        ):

            go_to(
                "🛡️ Firewall"
            )

            st.rerun()


    c4, c5, c6 = st.columns(3)


    with c4:

        card(
            "⚠️",
            "Vulnerability Check",
            "Review potential security risks and recommendations.",
            "card-orange"
        )


        if st.button(
            "Open Vulnerability Check →",
            key="tools_vulnerability"
        ):

            go_to(
                "⚠️ Vulnerability Check"
            )

            st.rerun()


    with c5:

        card(
            "🌐",
            "IP Tools",
            "Validate IPv4 and IPv6 addresses and identify their type.",
            "card-purple"
        )


        if st.button(
            "Open IP Tools →",
            key="tools_ip"
        ):

            go_to(
                "🌐 IP Tools"
            )

            st.rerun()


    with c6:

        card(
            "🔑",
            "Password & Hash Tools",
            "Check password strength and generate SHA-256 hashes.",
            "card-cyan"
        )


        if st.button(
            "Open Password Tools →",
            key="tools_password"
        ):

            go_to(
                "🔑 Password & Hash Tools"
            )

            st.rerun()


    if st.button(
        "📄 Open Security Report",
        key="tools_report"
    ):

        go_to(
            "📄 Security Report"
        )

        st.rerun()


# =========================================================
# NETWORK SCAN
# =========================================================

elif st.session_state.page == "🔎 Network Scan":

    hero(
        "🔎 Network Scan",
        "Identify open ports and running services."
    )


    st.info(
        "Tool: Nmap — "
        "Nmap testing was completed locally."
    )


    target = st.text_input(
        "Target IP Address",
        "127.0.0.1"
    )


    if st.button(
        "▶ Start Demo Scan"
    ):

        st.success(
            "✅ Demo scan completed."
        )


        st.code(
            f"""Nmap Security Scan

Target: {target}

PORT       STATE    SERVICE
135/tcp    open     msrpc
445/tcp    open     microsoft-ds
902/tcp    open     vmware-auth
912/tcp    open     vmware-auth

Scan Status: Completed
"""
        )


        st.warning(
            "Open ports should be reviewed "
            "to confirm that they are required."
        )


    st.warning(
        "⚠️ Only scan systems you own "
        "or have permission to test."
    )


# =========================================================
# TRAFFIC MONITORING
# =========================================================

elif st.session_state.page == "📡 Traffic Monitoring":

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
            "Review TCP connections, ports and communication.",
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


    st.markdown(
        "### 📡 Wireshark Filters"
    )


    filter_type = st.selectbox(
        "Select traffic type",
        [
            "TCP",
            "DNS",
            "TLS",
            "TCP SYN",
            "Large TCP Packets"
        ]
    )


    filters = {

        "TCP":
            "tcp",

        "DNS":
            "dns",

        "TLS":
            "tls",

        "TCP SYN":
            "tcp.flags.syn == 1",

        "Large TCP Packets":
            "tcp.len > 10000"

    }


    if st.button(
        "🔍 Show Filter"
    ):

        st.success(
            f"{filter_type} filter:"
        )


        st.code(
            filters[
                filter_type
            ]
        )


    st.markdown(
        "### 🧪 Wireshark Capture Results"
    )


    r1, r2, r3 = st.columns(3)


    with r1:

        st.metric(
            "🔵 TCP Packets",
            "189",
            "66.5% displayed"
        )


    with r2:

        st.metric(
            "🟢 DNS Packets",
            "20",
            "1.2% displayed"
        )


    with r3:

        st.metric(
            "🟣 TLS Packets",
            "610",
            "18.5% displayed"
        )


    st.markdown(
        "### 📊 Capture Summary"
    )


    st.table(
        {

            "Protocol":
                [
                    "TCP",
                    "DNS",
                    "TLS"
                ],

            "Displayed Packets":
                [
                    189,
                    20,
                    610
                ],

            "Total Packets at Screenshot":
                [
                    284,
                    1619,
                    3289
                ],

            "Displayed Percentage":
                [
                    "66.5%",
                    "1.2%",
                    "18.5%"
                ]

        }
    )


    st.info(
        "These values are based on "
        "Wireshark screenshots from local testing. "
        "The screenshots were taken at different times."
    )


# =========================================================
# FIREWALL - STAFF ONLY
# =========================================================

elif st.session_state.page == "🛡️ Firewall":

    if st.session_state.role != "Staff":

        st.error(
            "Staff access only."
        )

        st.stop()


    hero(
        "🛡️ Firewall Security",
        "Manage and review network access rules."
    )


    st.warning(
        "Tool: pfSense — Demonstration"
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        card(
            "✅",
            "HTTPS",
            "ALLOW — TCP Port 443",
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
            "BLOCK — TCP Port 23",
            "card-pink"
        )


    st.markdown(
        "### 🔥 Firewall Rule Tester"
    )


    service = st.selectbox(
        "Select Service",
        [
            "HTTPS",
            "DNS",
            "SSH",
            "HTTP",
            "Telnet"
        ]
    )


    firewall_rules = {

        "HTTPS":
            (
                "443",
                "ALLOW"
            ),

        "DNS":
            (
                "53",
                "ALLOW"
            ),

        "SSH":
            (
                "22",
                "ALLOW"
            ),

        "HTTP":
            (
                "80",
                "REVIEW"
            ),

        "Telnet":
            (
                "23",
                "BLOCK"
            )

    }


    if st.button(
        "🛡️ Check Firewall Rule"
    ):

        port, action = (
            firewall_rules[
                service
            ]
        )


        st.write(
            f"**Service:** {service}"
        )


        st.write(
            f"**Port:** {port}"
        )


        if action == "ALLOW":

            st.success(
                "✅ ALLOW"
            )


        elif action == "BLOCK":

            st.error(
                "🚫 BLOCK"
            )


        else:

            st.warning(
                "⚠️ REVIEW"
            )


    st.info(
        "Firewall rules help control "
        "network access and reduce security risks."
    )


# =========================================================
# VULNERABILITY CHECK - STAFF ONLY
# =========================================================

elif st.session_state.page == "⚠️ Vulnerability Check":

    if st.session_state.role != "Staff":

        st.error(
            "Staff access only."
        )

        st.stop()


    hero(
        "⚠️ Vulnerability Check",
        "Review potential network security risks."
    )


    st.write(
        "Run a basic demonstration security check."
    )


    if st.button(
        "🔍 Run Demo Vulnerability Check"
    ):

        st.warning(
            "⚠️ Port 445 — "
            "File sharing service may be exposed."
        )


        st.success(
            "Recommendation: "
            "Restrict access to trusted devices."
        )


        st.warning(
            "⚠️ Telnet Port 23 — "
            "Unencrypted remote access."
        )


        st.success(
            "Recommendation: "
            "Block Telnet and use SSH."
        )


        st.warning(
            "⚠️ HTTP Port 80 — "
            "Unencrypted web traffic."
        )


        st.success(
            "Recommendation: "
            "Use HTTPS/TLS."
        )


        st.info(
            "These are demonstration findings. "
            "Further testing is required "
            "to confirm vulnerabilities."
        )


# =========================================================
# IP TOOLS - STAFF ONLY
# =========================================================

elif st.session_state.page == "🌐 IP Tools":

    if st.session_state.role != "Staff":

        st.error(
            "Staff access only."
        )

        st.stop()


    hero(
        "🌐 IP Address Analyzer",
        "Validate and analyze IPv4 and IPv6 addresses."
    )


    ip_input = st.text_input(
        "Enter IP Address",
        "192.168.1.1"
    )


    if st.button(
        "🌐 Analyze IP"
    ):

        try:

            address = (
                ipaddress.ip_address(
                    ip_input.strip()
                )
            )


            st.success(
                "✅ Valid IP Address"
            )


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


            st.write(
                "**Loopback:**",
                (
                    "Yes"
                    if address.is_loopback
                    else "No"
                )
            )


            st.write(
                "**Multicast:**",
                (
                    "Yes"
                    if address.is_multicast
                    else "No"
                )
            )


        except ValueError:

            st.error(
                "❌ Invalid IP address. "
                "Enter a valid IPv4 or IPv6 address."
            )


# =========================================================
# PASSWORD & HASH TOOLS - STAFF ONLY
# =========================================================

elif st.session_state.page == "🔑 Password & Hash Tools":

    if st.session_state.role != "Staff":

        st.error(
            "Staff access only."
        )

        st.stop()


    hero(
        "🔑 Password & Hash Tools",
        "Test password strength and SHA-256 hashing."
    )


    st.warning(
        "⚠️ Use a sample password only. "
        "Do not enter your real password."
    )


    password = st.text_input(
        "Sample Password",
        type="password"
    )


    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "🔐 Check Password Strength"
        ):

            if not password:

                st.warning(
                    "Enter a sample password first."
                )

            else:

                score = 0


                if len(password) >= 8:

                    score += 1


                if any(
                    c.isupper()
                    for c in password
                ):

                    score += 1


                if any(
                    c.islower()
                    for c in password
                ):

                    score += 1


                if any(
                    c.isdigit()
                    for c in password
                ):

                    score += 1


                if any(
                    not c.isalnum()
                    for c in password
                ):

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

        if st.button(
            "🔑 Generate SHA-256 Hash"
        ):

            if not password:

                st.warning(
                    "Enter a sample password first."
                )

            else:

                hashed_password = (
                    hashlib.sha256(
                        password.encode()
                    ).hexdigest()
                )


                st.success(
                    "✅ SHA-256 Hash Generated"
                )


                st.code(
                    hashed_password
                )


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
        "Nmap and Wireshark testing was completed locally. "
        "The online Nmap and pfSense sections "
        "are demonstrations."
    )


    st.markdown(
        """
        <div class="footer-box">

            <b>
                INTERTEC SYSTEMS LLC
            </b>

            <br><br>

            Network Security Basics Project

            <br>

            Monitor • Analyze • Protect

        </div>
        """,
        unsafe_allow_html=True
    )
