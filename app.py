import streamlit as st
import ipaddress
import hashlib

st.set_page_config(
    page_title="Network Security Basics",
    page_icon="🔐",
    layout="wide"
)

# ---------- HEADER ----------
st.title("🔐 Network Security Basics Dashboard")
st.write(
    "A simple and user-friendly dashboard for network security "
    "tools, testing, and recommendations."
)

# ---------- SIDEBAR ----------
st.sidebar.title("🛡️ Security Tools")

option = st.sidebar.radio(
    "Select a Tool",
    [
        "🏠 Home",
        "🔎 Network Scan",
        "📡 Traffic Monitoring",
        "🛡️ Firewall",
        "⚠️ Vulnerability Check",
        "🌐 IP Tools",
        "🔑 Password & Hash Tools",
        "📄 Security Report"
    ]
)

# ---------- HOME ----------
if option == "🏠 Home":
    st.header("Welcome 👋")

    st.write(
        "This dashboard demonstrates basic network security tools "
        "and security recommendations."
    )

    st.subheader("Available Security Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        🔎 **Network Scan**

        Identify open ports and running services using Nmap.
        """)

        st.info("""
        🛡️ **Firewall**

        Review basic firewall rules and secure network access.
        """)

        st.info("""
        🌐 **IP Tools**

        Validate IPv4 and IPv6 addresses.
        """)

        st.info("""
        📄 **Security Report**

        Review security findings and recommendations.
        """)

    with col2:
        st.info("""
        📡 **Traffic Monitoring**

        Review network traffic concepts using Wireshark.
        """)

        st.info("""
        ⚠️ **Vulnerability Check**

        Review potential security risks and recommendations.
        """)

        st.info("""
        🔑 **Password & Hash Tools**

        Check password strength and generate SHA-256 hashes.
        """)

# ---------- NETWORK SCAN ----------
elif option == "🔎 Network Scan":
    st.header("🔎 Network Scan")

    st.write("**Tool:** Nmap")
    st.write("**Purpose:** Identify open ports and running services.")

    target = st.text_input(
        "Enter Target IP Address",
        "127.0.0.1"
    )

    if st.button("Start Demo Scan"):
        st.success("Demo scan completed.")

        st.code(
            f"""Target: {target}

Example Scan Results:

135/tcp   open   msrpc
445/tcp   open   microsoft-ds
902/tcp   open   vmware-auth
912/tcp   open   vmware-auth

Note: This online version displays demonstration results."""
        )

    st.caption(
        "Real Nmap testing was performed locally. "
        "Only scan systems you own or have permission to test."
    )

# ---------- TRAFFIC MONITORING ----------
elif option == "📡 Traffic Monitoring":
    st.header("📡 Traffic Monitoring")

    st.write("**Tool:** Wireshark")
    st.write("**Purpose:** Capture and analyze network packets.")

    if st.button("Show Traffic Information"):
        st.success("Traffic monitoring information displayed.")

        st.subheader("Useful Wireshark Filters")

        st.code(
            """tcp
dns
tls"""
        )

        st.write(
            "These filters can be used to review TCP connections, "
            "DNS queries, and encrypted TLS traffic."
        )

# ---------- FIREWALL ----------
elif option == "🛡️ Firewall":
    st.header("🛡️ Firewall Security")

    st.write("**Tool:** pfSense")
    st.write("**Status:** Demonstration")

    if st.button("Show Firewall Rules"):
        st.success("Firewall rules displayed.")

        st.write("✅ **ALLOW HTTPS — Port 443**")
        st.write("✅ **ALLOW DNS — Port 53**")
        st.write("🚫 **BLOCK Telnet — Port 23**")

        st.info(
            "These rules demonstrate how a firewall can allow "
            "required services and block insecure services."
        )

# ---------- VULNERABILITY CHECK ----------
elif option == "⚠️ Vulnerability Check":
    st.header("⚠️ Vulnerability Check")

    st.write("Review potential security findings.")

    if st.button("Show Security Findings"):

        st.warning(
            "Open Port 445 — File sharing service may be exposed."
        )
        st.write(
            "Recommendation: Restrict access to trusted devices."
        )

        st.warning(
            "Telnet Port 23 — Unencrypted remote access."
        )
        st.write(
            "Recommendation: Block Telnet and use SSH."
        )

        st.warning(
            "HTTP Port 80 — Unencrypted web traffic."
        )
        st.write(
            "Recommendation: Use HTTPS/TLS."
        )

        st.info(
            "These are potential security findings for demonstration. "
            "Further testing is required to confirm a vulnerability."
        )

# ---------- IP TOOLS ----------
elif option == "🌐 IP Tools":
    st.header("🌐 IP Tools")

    st.write(
        "Enter an IP address to validate it and identify its version."
    )

    ip_input = st.text_input(
        "Enter IP Address",
        "192.168.1.1"
    )

    if st.button("Check IP Address"):
        try:
            address = ipaddress.ip_address(ip_input.strip())

            st.success("Valid IP Address ✅")

            st.write(f"**IP Address:** {address}")
            st.write(f"**Version:** IPv{address.version}")

            if address.is_private:
                st.write("**Network Type:** Private")
            else:
                st.write("**Network Type:** Public")

        except ValueError:
            st.error(
                "Invalid IP Address. Please enter a valid IPv4 "
                "or IPv6 address."
            )

# ---------- PASSWORD & HASH ----------
elif option == "🔑 Password & Hash Tools":
    st.header("🔑 Password & Hash Tools")

    st.write(
        "Check password strength and generate a SHA-256 hash."
    )

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Check Password Strength"):
            if password == "":
                st.warning("Please enter a password first.")

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
                    st.error("Password Strength: Weak 🔴")

                elif score <= 4:
                    st.warning("Password Strength: Medium 🟠")

                else:
                    st.success("Password Strength: Strong 🟢")

    with col2:
        if st.button("Generate SHA-256 Hash"):
            if password == "":
                st.warning("Please enter a password first.")

            else:
                hashed_password = hashlib.sha256(
                    password.encode()
                ).hexdigest()

                st.success("SHA-256 Hash Generated")
                st.code(hashed_password)

    st.caption(
        "For this demonstration, the password is processed only "
        "to calculate the displayed result."
    )

# ---------- SECURITY REPORT ----------
elif option == "📄 Security Report":
    st.header("📄 Network Security Basics Report")

    st.subheader("🔎 Network Scan")
    st.write("Tool: Nmap")
    st.write("Identify open ports and running services.")

    st.subheader("📡 Traffic Monitoring")
    st.write("Tool: Wireshark")
    st.write("Filters used: TCP, DNS and TLS.")

    st.subheader("🛡️ Firewall")
    st.write("Tool: pfSense — Demonstration")
    st.write("Allow HTTPS, allow DNS and block Telnet.")

    st.subheader("🌐 IP Tools")
    st.write("Validate IPv4 and IPv6 addresses.")

    st.subheader("🔑 Password & Hash Tools")
    st.write(
        "Check password strength and generate SHA-256 hashes."
    )

    st.subheader("Security Recommendations")

    st.write("• Use HTTPS/TLS.")
    st.write("• Block Telnet and use SSH.")
    st.write("• Restrict unnecessary open ports.")
    st.write("• Use firewall rules.")
    st.write("• Monitor network traffic regularly.")
    st.write("• Use strong passwords.")

    st.success("Security report generated successfully.")
