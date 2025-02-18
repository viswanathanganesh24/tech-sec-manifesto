import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", page_title="Manifesto", page_icon="📜")
st.markdown(
    """
    <style>
    .stApp {
        background: none;
        background-attachment: fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

page = option_menu(menu_title=None, default_index=0, options=["Home", "Vision", "Initiatives", "Events", "Tech Room", "Contact"], icons=["house", "lightbulb-fill", "building-up", "calendar-date-fill", "clipboard-check", "telephone-fill"], orientation="horizontal")

if page == "Home":
    st.title("My Manifesto")
    st.subheader("Viswanathan Ganesh: Technical Affairs Secretary")

    st.markdown(
            """
            <style>
            .stApp img {
                display: block;
                margin: 0 auto; /* Center the image */
                border-radius: 50%; /* Make the image circular */
                width: 350px; /* Set the desired width */
                height: 350px; /* Set the desired height */
                object-fit: cover; /* Ensure the image fits within the circle */
                object-position: 15% 5%;
                border: 10px solid white; /* Optional: Add a white border around the circle */
                box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.2); /* Optional: Add a shadow for better aesthetics */
                background-color: #ffffff;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    st.image("viswa.png")
    st.markdown("""<div style="font-size: 20px; line-height: 1.2;">
                        <p>I am excited to present my vision for the role of Technical Affairs Secretary at Alakananda hostel.
                        My goal is to transform our hostel into a vibrant, tech-driven community that offers numerous opportunities for technical growth and innovation.
                        With my experience as a Coordinator at Envisage Game Development, Manager at Oceana Sponsorship and Fundraising, and Deputy Coordinator at XRIG, I bring a wealth of leadership and organizational skills to this position.</p>
                        </div>""", unsafe_allow_html=True)
elif page == "Vision":
    st.title("🎯 Vision & Credentials")
    st.header("My Vision", divider="grey")
    st.markdown(
            """
            <div style="font-size: 20px; line-height: 1.2;">
                <ul>
                    <li><b>Tech-Driven Community</b>: Transform Alakananda into a vibrant tech hub</li>
                    <li><b>Opportunity Creation</b>: Regular technical events and skill development programs</li>
                    <li><b>Infrastructure Upgrade</b>: Modernize hostel facilities and digital systems</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.header("Leadership Experience", divider="grey")
    st.markdown(
        """
        <div style="font-size: 20px; line-height: 1.2;">
            <ul>
                <li><b>Envisage</b>: Game Development Coordinator</li>
                <li><b>Oceana</b>: Sponsorship & Fundraising Manager</li>
                <li><b>XRIG</b>: Deputy Coordinator</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif page == "Initiatives":
    st.title("🚀 Initiatives")

    initiatives = {
        "Alakananda Website Development": 0,
        "Digital Complaint System": 0,
        "LAN Upgrades & Fixing": 0,
        "CCTV Installation": 0,
        "Iron Box Upgrade & Ironing Table Installation": 0
    }

    for initiative, progress in initiatives.items():
        st.header(initiative, divider="grey")
        if initiative == "Alakananda Website Development":
            st.markdown(
                """
                <div style="font-size: 20px; line-height: 1.2;">
                    <ul>
                        <li><b>Central announcement board</b>: Transform Alakananda into a vibrant tech hub</li>
                        <li><b>Event calendar</b>: Regular technical events and skill development programs</li>
                        <li><b>Hall of Fame section</b>: Modernize hostel facilities and digital systems</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif initiative == "Digital Complaint System":
            st.markdown(
                """
                <div style="font-size: 20px; line-height: 1.2;">
                    <ul>
                        <li><b>QR-based logging</b></li>
                        <li><b>Real-time tracking</b></li>
                        <li><b>Priority tagging</b></li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif initiative == "LAN Upgrades & Fixing":
            st.markdown("""
                <div style="font-size: 20px; line-height: 1.2;">
                    <ul>
                        <p>Repair damaged LAN ports and install Wi-Fi extenders for seamless internet connectivity in all wings.</p>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True)
        elif initiative == "CCTV Installation":
            st.markdown("""
                <div style="font-size: 20px; line-height: 1.2;">
                    <ul>
                        <p>Install CCTV cameras in common rooms for the safety of common equipments and things.</p>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True)
        elif initiative == "Iron Box Upgrade & Ironing Table Installation":
            st.markdown("""
                <div style="font-size: 20px; line-height: 1.2;">
                    <ul>
                        <p>Upgrading Iron boxes and adding foldable Ironing Tables to the inventory, which will be available in the Tech Room for the use of students.</p>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True)

elif page == "Events":
    st.title("🎉 Events & Activities")

    tab1, tab2, tab3 = st.tabs(["Competitions", "Learning Sessions", "Tech-Pilots"])

    with tab1:
        st.header("🏆 Intra/Inter Technical Competitions")
        st.markdown(
            """
            <div style="font-size: 20px; line-height: 1.2;">
                <ul>
                    <li><b>Gaming Nights</b> (BGMI, Free Fire, Valorant, CS2)</li>
                    <li><b>Hackathons & CADathons</b></li>
                    <li><b>Tech Quizzes & Debates</b></li>
                    <li><b>₹5000+</b> Prize Pools</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tab2:
        st.header("🎓 Skill Development")
        st.markdown(
            """
            <div style="font-size: 20px; line-height: 1.2;">
                <ul>
                    <li>Full Stack Development</li>
                    <li>Cybersecurity Workshops</li>
                    <li>AI/ML Fundamentals</li>
                    <li>Game Development Workshops</li>
                    <li>Senior Fundae Sessions</li>
                    <li>CAD Modelling</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tab3:
        st.header("👥 Tech-Pilots Community")
        st.markdown(
            """
            <div style="font-size: 20px; line-height: 1.2;">
                <ul>
                    <li>Interest-based groups</li>
                    <li>Tech Room resources</li>
                    <li>Innovation challenges</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

elif page == "Tech Room":
    st.title("💻 Tech Room 2.0")

    st.header("Facility Upgrade Plan")
    st.markdown(
        """
        <div style="font-size: 20px; line-height: 1.2;">
            <ul>
                <li>Power Tools Upgrade</li>
                <li>Iron Boxes & Ironing Tables</li>
                <li>Survey based inventory upgrade</li>
                <li>Entry log</li>
                <li>Weekly maintenance log</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif page == "Contact":
    st.title("📞 Connect With Me")
    st.markdown(
        """
        <div style="font-size: 20px; line-height: 1.2;">
           <h1>Viswanathan Ganesh</h1>
           <p>Technical Affairs Secretary Candidate</p>
           <p>📱 +91 73582 82650</p>  
           <p>📧 na23b077@smail.iitm.ac.in</p> 
        </div>
        """,
        unsafe_allow_html=True
    )
    st.link_button("Instagram", "https://instagram.com/viswanathan_ganesh_", )
    st.link_button("LinkedIn", "https://www.linkedin.com/in/viswanathan-ganesh-0b2185297/")

