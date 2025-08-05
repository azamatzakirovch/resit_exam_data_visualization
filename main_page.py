
def main_page():
    import streamlit as st

    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("logo.png", width=200)
    with col2:
        st.markdown(
            """
            <div style="
                position: absolute;
                width: 900px;
                height: 125px;
                top: 30px;
                left: -50px;
            ">
                <div style = "
                    position: absolute;
                    top: 1px;
                    left: 10px;
                    font-size: 50px;
                    color: #2A407A;
                    font-weight: bold;
                ">
                New Uzbekistan University</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                position: absolute;
                width: 900px;
                height: 125px;
                top: 60px;
                left: -50px;
            ">
                <div style = "
                    position: absolute;
                    top: 10px;
                    left: 10px;
                    font-size: 50px;
                    color: #2A407A;
                    font-weight: bold;
                ">
                Resit Exam Analyse</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("""
        <style>
        /* Increase tab height and font */
        .stTabs [data-baseweb="tab"] {
            font-size: 40px !important;
            padding: 16px 24px !important;
        }

        /* Optional: Bold text */
        .stTabs [data-baseweb="tab"] span {
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "New Uzbekistan University",
            "Departments",
            "Explanation for database",
            "Connection"
        ]
    )

    with tab1:

        information_about_newuu = """
        <div 
            style = "
                position: absolute;
                width: 650px;
                height: 400px;
                top: 10px;
                left: 0px;
                # border: 1px solid #D9D9D9;
                border-radius: 10px;
                justify-content: space-between;
            "
        >
            <div style = "
                position: absolute;
                width: 650px;
                top:70px;
                left: 10px;
                font-size: 18px;
                justify-content: space-between;
            ">
                New Uzbekistan University (NewUU) is Uzbekistan's first comprehensive research university, seamlessly integrating education with cutting-edge research. Located in Central Asia, NewUU is shaping the nation's academic landscape with partnerships like MIT's Jameel Abdul Latif World Education Lab (J-WEL) and the Technical University of Munich (TUM) International.
                <br><br>
                Offering diverse programs in Engineering, Computing, Humanities, and Management, NewUU (equips) future leaders and innovators with the skills to drive progress. As a hub for innovation, it fosters knowledge exchange through events like forums, conferences, and hackathons, contributing to (the advancement of) Uzbekistan and Central Asia.
            </div>
        </div>
        """

        video_about_newuu = """
        <div 
            style="
                position: absolute;
                width: 540px;
                height: 400px;
                top: -6px;
                right: 0px;
                border: 1px solid #D9D9D9;
                border-radius: 10px;
                overflow: hidden;
            "
        >
            <iframe 
                width="100%" 
                height="100%" 
                src="https://www.youtube.com/embed/5mS3eSabIog"
                frameborder="0" 
                allowfullscreen
            ></iframe>
        </div>
        """

        idunno = """
        <div style = "
            position: absolute;
            top: 30px;
            left: 10px;
            font-size: 30px;
            font-weight: bold;
        ">
                About University
        </div>
                """

        st.markdown(idunno, unsafe_allow_html=True)
        st.markdown(information_about_newuu, unsafe_allow_html=True)
        st.markdown(video_about_newuu, unsafe_allow_html=True)

    with tab2:
        st.markdown(
            """
            <style>
                .school_of_computing{
                    width: 620px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 30px;
                    left: 0px;
                }
                
                .school_of_humanities{
                    width: 620px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 310px;
                    left: 0px;
                }
                
                .school_of_engineering{
                    width: 410px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 30px;
                    right: 120px;
                }    
                
                .school_of_management{
                    width: 410px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 310px;
                    right: 120px;
                }
                
                .unit_rectangle {
                    position: absolute;
                    top: 0px;
                    height: 100%;
                    width: 200px;
                    border: 1px solid #D9D9D9;
                    border-top-left-radius: 10px;
                    border-top-right-radius: 10px;
                    transition: all 0.3s ease; /* important for smooth animation */
                }
                
                .unit_rectangle:hover {
                    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
                    transform: translateY(-3px);
                    cursor: pointer;
                }

                
                .text_settings{
                    position: absolute;
                    color: black;
                    font-size: 23px;
                    font-weight: bold;
                    font-family: Arial;
                }
            </style>
            
            <div class = "school_of_computing">
                <div class="unit_rectangle" style = "left: 0px"></div>
                <div class="unit_rectangle" style = "left: 210px"></div>
                <div class="unit_rectangle" style = "left: 420px"></div>
            </div>
            
            <div class = "school_of_humanities">
                <div class="unit_rectangle" style = "left: 0px"></div>
                <div class="unit_rectangle" style = "left: 210px"></div>
                <div class="unit_rectangle" style = "left: 420px"></div>
            </div>
            
            <div class = "school_of_engineering">
                <div class="unit_rectangle" style = "left: 0px"></div>
                <div class="unit_rectangle" style = "left: 210px"></div>
            </div>
            
            <div class = "school_of_management">
                <div class="unit_rectangle" style = "left: 0px"></div>
            </div>
            
            <div class = "text_settings" style = "top: -9px; left: 13px">School of Computing</div>
            <div class = "text_settings" style = "top: 270px; left: 13px">School of Humanities, Natural & Social Science</div>
            <div class = "text_settings" style = "top: -9px; left: 690px">School of Engineering</div>
            <div class = "text_settings" style = "top: 270px; left: 690px">School of Management</div>
            

            
            """,
            unsafe_allow_html=True
        )

    with tab3:
        st.write("Settings and preferences go here.")

    with tab4:
        st.write("Settings and others go here.")
