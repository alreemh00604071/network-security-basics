import streamlit as st

st.set_page_config(
    page_title="Network Security Basics",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Network Security Basics Dashboard")
st.write("Simple dashboard for network security tools and recommendations.")

option = st.sidebar.radio(
    "Select Security Tool",
    [
        "Home",
        "Network Scan",
        "Traffic Monitoring",
        "Firewall",
        "Vulnerability Check",
        "Security Report"
    ]
)

if option == "Home":
    st.header("Welcome")
    st.write("This dashboard demonstrates basic network security concepts.")
    st.info("Select a security tool from the menu.")

elif option == "Network Scan":
    st.header("🔎 Network Scan")
    st.write("Tool: Nmap")
    st.write("Purpose: Identify open ports and running services.")

    target = st.text_input("Enter Target IP Address", "127.0.0.1")

    if st.button("Start Demo Scan"):
        st.success("Demo scan completed.")
        st.code(
            f"""Target: {target}

Example Scan Results:
135/tcp  open  msrpc
445/tcp  open  microsoft-ds
902/tcp  open  vmware-auth
912/tcp  open  vmware-auth

Note: This online version displays demonstration results."""
        )

elif option == "Traffic Monitoring":
    st.header("📡 Traffic Monitoring")
    st.write("Tool: Wireshark")
    st.write("Purpose: Capture and analyze network packets.")

    if st.button("Show Traffic Information"):
        st.write("Useful Wireshark Filters:")
        st.code("tcp\ndns\ntls")
        st.success("Traffic monitoring information displayed.")

elif option == "Firewall":
    st.header("🛡️ Firewall Security")
    st.write("Tool: pfSense")
    st.write("Status: Demo")

    if st.button("Show Firewall Rules"):
        st.write("✅ ALLOW HTTPS — Port 443")
        st.write("✅ ALLOW DNS — Port 53")
        st.write("⛔ BLOCK Telnet — Port 23")

elif option == "Vulnerability Check":
    st.header("⚠️ Vulnerability Check")
    st.write("Review potential security findings.")

    if st.button("Show Security Findings"):
        st.warning("Open Port 445 — File sharing service may be exposed.")
        st.info("Recommendation: Restrict access to trusted devices.")

        st.warning("Telnet Port 23 — Unencrypted remote access.")
        st.info("Recommendation: Block Telnet and use SSH.")

        st.warning("HTTP Port 80 — Unencrypted web traffic.")
        st.info("Recommendation: Use HTTPS/TLS.")

        st.caption(
            "These are potential security findings for demonstration. "
            "Further testing is required to confirm a vulnerability."
        )

elif option == "Security Report":
    st.header("📄 Security Report")

    if st.button("Generate Security Report"):
        st.subheader("Network Security Basics Report")

        st.write("**Network Scan:** Nmap")
        st.write("Identify open ports and running services.")

        st.write("**Traffic Monitoring:** Wireshark")
        st.write("Filters used: TCP, DNS and TLS.")

        st.write("**Firewall:** pfSense Demo")
        st.write("Allow HTTPS, allow DNS and block Telnet.")

        st.write("**Security Recommendations:**")
        st.write("- Use HTTPS/TLS.")
        st.write("- Block Telnet and use SSH.")
        st.write("- Restrict unnecessary open ports.")
        st.write("- Use firewall rules.")
        st.write("- Monitor network traffic regularly.")

        st.success("Security report generated successfully.")
