
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

    tab1, tab2, tab3 = st.tabs(
        [
            "New Uzbekistan University",
            "Departments",
            "Explanation for database",
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
                    left: 50px;
                }
                
                .school_of_humanities{
                    width: 620px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 330px;
                    left: 50px;
                }
                
                .school_of_engineering{
                    width: 410px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 30px;
                    right: 70px;
                }    
                
                .school_of_management{
                    width: 205px;
                    height: 230px;
                    # border: 1px solid #D9D9D9;
                    position: absolute;
                    top: 330px;
                    right: 275px;
                }
                
                .unit_rectangle {
                    position: absolute;
                    top: 0px;
                    height: 100%;
                    width: 200px;
                    border-top-left-radius: 15px;
                    border-top-right-radius: 15px;
                    transition: all 0.3s ease;
                }
                
                .unit_rectangle:hover {
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
                
                .img_style{
                    position: absolute;
                    top: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    height: 60%;
                    width: auto;
                    border-top-left-radius: 10px;
                    border-top-right-radius: 10px;
                }
                
         

                
            </style>
            
            <div class = "school_of_computing">
                <div class="unit_rectangle" style="left: 0px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/8759/8759068.png" />
                        <div style="
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Software Engineering
                        </div>
                </div>
                <div class="unit_rectangle" style = "left: 210px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/2092/2092629.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Cyber Security
                        </div>
                </div>
                <div class="unit_rectangle" style = "left: 420px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/4616/4616790.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                AI & Robotics
                        </div>                
                </div>
            </div>
            
            <div class = "school_of_humanities">
                <div class="unit_rectangle" style = "left: 0px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/3310/3310764.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            width: 100%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Economics and <br> Data Science
                        </div>                 
                </div>
                <div class="unit_rectangle" style = "left: 210px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/1739/1739422.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            width: 100%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Applied<br>Mathematics
                        </div>                  
                </div>
                <div class="unit_rectangle" style = "left: 420px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/2083/2083161.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            width: 100%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Pedagogy<br>STEAM specialization
                        </div>                  
                </div>
            </div>
            
            <div class = "school_of_engineering">
                <div class="unit_rectangle" style = "left: 0px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/2861/2861645.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            width: 100%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Mechanical<br>Engineering
                        </div>                       
                </div>
                <div class="unit_rectangle" style = "left: 210px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/6912/6912706.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            width: 100%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Chemical<br>Engineering
                        </div>                       
                </div>
            </div>
            
            <div class = "school_of_management">
                <div class="unit_rectangle" style = "left: 0px">
                    <img class="img_style" src="https://cdn-icons-png.flaticon.com/512/11495/11495742.png" />
                        <div style = "
                            position: absolute;
                            top: 85%;
                            left: 50%;
                            width: 100%;
                            transform: translate(-50%, -50%);
                            font-size: 18px;
                            font-weight: 600;
                            font-family: 'Arial', sans-serif;
                            color: black;
                            text-align: center;
                            white-space: nowrap;
                        ">
                                Industrial<br>Management
                        </div>                       
                </div>
            </div>
            <div class = "text_settings" style = "top: -9px; left: 63px">School of Computing</div>
            <div class = "text_settings" style = "top: 285px; left: 63px">School of Humanities, Natural & Social Science</div>
            <div class = "text_settings" style = "top: -9px; left: 740px">School of Engineering</div>
            <div class = "text_settings" style = "top: 285px; left: 740px">School of Management</div>
            """,
            unsafe_allow_html=True
        )

    with tab3:
        st.markdown("""
                <style>
                    .rectangle-for-df-explanation{
                        width: 100%;
                        height: 140px;
                        # border: 1px solid black;
                        position: absolute;
                        top: 0px;
                        left: 0px;
                    }

                    .text-settings-of-rectangle-for-df-explanation {
                        position: absolute;
                        font-size: 15px;
                        line-height: 1.6;
                        color: #1e1e1e;
                        font-family:'Arial', sans-serif;
                        font-weight: 400;
                        text-align: justify;
                    }

                </style>
                <div class = "rectangle-for-df-explanation">
                    <div class = "text-settings-of-rectangle-for-df-explanation">
                    This database presents detailed information about students who were required to take resit exams at New Uzbekistan University during the 2024/2025 academic year. It was constructed by intelligently combining two separate sources:
                    the original exam schedule database, and the student performance database. The merged dataset consists of 12 well-structured columns, representing information such as student ID, full name, major, exam date, time, room, subject, and more.
                    The data types are primarily strings, integers, and Python dictionaries — the latter of which are used to structure multi-session exam data within a single field.
                    This enriched dataset serves as the foundation for analyzing academic performance, identifying failure trends, and supporting institutional decisions on exam planning and academic support.
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                    .rectangle-for-df-columns{
                        width: 400px;
                        height: 1000px;
                        # border: 1px solid black;
                        position: absolute;
                        top: 150px;
                        left: 0px;
                    }

                    .text-settings-of-rectangle-for-df-columns {
                        position: absolute;
                        font-size: 15px;
                        line-height: 1.6;
                        color: #1e1e1e;
                        font-family:'Arial', sans-serif;
                        font-weight: 400;
                        text-align: justify;
                    }

                </style>
                <div class = "rectangle-for-df-columns">
                    <div class="text-settings-of-rectangle-for-df-columns">
                        <b>ID</b> – Unique identifier for each student. <i>Type:</i> <span style="color:green;">Integer</span>. For example: <code>230055</code><br><br>
                        <b>FULLNAME</b> – Full name of the student. <i>Type:</i> <span style="color:green;">String</span>. For example: <code>Abdulloh Abdullayev</code><br><br>
                        <b>STUDY_YEAR</b> – Current year of study (1 to 4). <i>Type:</i> <span style="color:green;">Integer</span>. For example: <code>2</code><br><br>
                        <b>EMAIL</b> – University email address of the student. <i>Type:</i> <span style="color:green;">String</span>. For example: <code>abdulloh.a@newuu.uz</code><br><br>
                        <b>STATUS</b> – Indicates if the student failed or passed. <i>Type:</i> <span style="color:green;">String</span>. Values: <code>'FAILED'</code>, <code>'PASSED'</code><br><br>
                        <b>SCHOOL</b> – Name of the school the student belongs to. <i>Type:</i> <span style="color:green;">String</span>. For example: <code>School of Computing</code><br><br>
                        <b>EDUCATION_PROGRAM</b> – Student’s specific program. <i>Type:</i> <span style="color:green;">String</span>. For example: <code>Software Engineering</code><br><br>
                        <b>MONDAY</b> – Dictionary showing resit exam schedule for Monday. <i>Type:</i> <span style="color:green;">Dictionary</span>. <br>
                        For example: <code>{'M1': ['Room A', '08:30', 'MATH 106']}</code><br><br>
                        <b>TUESDAY</b> – Resit schedule data for Tuesday. <i>Type:</i> <span style="color:green;">Dictionary</span>.<br>
                        Example: <code>{'T2': ['Room B', '13:00', 'PHYS 101']}</code><br><br>
                        <b>WEDNESDAY</b> – Resit schedule data for Wednesday. <i>Type:</i> <span style="color:green;">Dictionary</span>.<br>
                        Example: <code>{}</code> (if no exam that day)<br><br>
                        <b>THURSDAY</b> – Resit schedule data for Thursday. <i>Type:</i> <span style="color:green;">Dictionary</span><br>
                        Example: <code>{'T1': ['Room C', '10:00', 'HUM 102']}</code><br><br>
                        <b>FRIDAY</b> – Resit schedule data for Friday. <i>Type:</i> <span style="color:green;">Dictionary</span><br>
                        Example: <code>{'F3': ['Room D', '14:00', 'CS 201']}</code><br>
                    </div>

                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
            <style>
                .rectangle-for-representor {
                    width: 800px;
                    height: 250px;
                    # border: 1px solid black;
                    position: absolute;
                    top: 134px;
                    left: 410px;
                }

                .text-settings-of-rectangle-for-representor {
                    font-size: 15px;
                    line-height: 1.6;
                    color: #1e1e1e;
                    font-family:'Arial', sans-serif;
                    font-weight: 400;
                    text-align: justify;
                }
                .text-settings-of-rectangle-for-representor b {
                    color: black;
                }
            </style>
            <div class="rectangle-for-representor">
                <div class="text-settings-of-rectangle-for-representor">
                    This dashboard is built upon a custom database representing students who had resit exams at the New Uzbekistan University. The database was constructed by merging the official <b>exam schedule</b> dataset with the <b>students' academic status</b> records. As a result, the final dataset contains 12 columns, including structured information about student identity, academic programs, and detailed exam data for each weekday.<br>
                    All elements in the dataset are either of type <b>string</b>, <b>integer</b>, or <b>dictionary</b>, providing both categorical and nested data. For example, the <code>MONDAY</code> column may include a dictionary that holds multiple exam sessions for that day per student.
                    <br>To analyze, I will use line <b>graphs</b>, <b>bar charts</b>, <b>donut charts</b>, and apply <b>descriptive statistics</b> along with custom <b>Python</b> code to uncover meaningful patterns and insights from the data.
                </div>
            </div>
            
            <div style = "
                position: absolute;
                right: 90px;
                top: 340px;
                font-size: 30px;
                font-weight: bold;
                font-family: Arial;
            ">Main Explanation of Database with Charts</div>
            
        """, unsafe_allow_html=True)

        with st.container():
            col1, col2 = st.columns([3.4, 6.6])  # 30% and 70%
            with col1:
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
                st.write("   ")
            with col2:
                st.write("  ")

        with st.container():
            col3, col4 = st.columns([3.4, 6.4])  # 40% and 60%
            with col3:
                st.write("          ")
            with col4:
                st.write("          ")
                st.write("          ")
                st.write("          ")
                st.write("          ")
                st.write("          ")

                gender, courses = st.columns(2)

                with gender:
                    import streamlit as st
                    import plotly.graph_objects as go
                    import pandas as pd
                    import plotly.express as px
                    # Data
                    labels = ['Men', 'Women']
                    values = [381, 91]

                    fig = go.Figure(data=[go.Pie(
                        labels=labels,
                        values=values,
                        hole=0.6,  # this makes it a donut
                        hoverinfo='label+percent+value',
                        textinfo='label+percent'
                    )])

                    fig.update_layout(
                        title_text="Resit Exam Students by Gender",
                        width=350,
                        height=350
                    )

                    st.plotly_chart(fig)

                with courses:

                    labels = ['Freshmen', 'Sophomore', "Junior", "Senior"]
                    values = [178, 167, 72, 55]

                    fig = go.Figure(data=[go.Pie(
                        labels=labels,
                        values=values,
                        hole=0.6,
                        hoverinfo='label+percent+value',
                        textinfo='label+percent'
                    )])

                    fig.update_layout(
                        title_text="Resit Exam Students by Study Year",
                        width=350,
                        height=350
                    )

                    st.plotly_chart(fig)

                data = {
                    'Major': [
                        'Software Engineering', 'Economics and Data Science', 'Industrial Management',
                        'Mechanical Engineering', 'Cyber Security', 'Chemical and Materials Engineering',
                        'AI and Robotics', 'Pedagogy', 'Applied Mathematics'
                    ],
                    'Students': [140, 102, 60, 49, 32, 30, 21, 19, 19]
                }

                df = pd.DataFrame(data)

                fig = px.bar(
                    df,
                    x='Major',
                    y='Students',
                    title='Number of Resit Exam Students by Major',
                    text='Students',
                    color='Major',
                    color_discrete_sequence=px.colors.qualitative.Set3
                )

                fig.update_layout(
                    xaxis=dict(showticklabels=False),
                    height=400,
                    width=1000
                )

                st.plotly_chart(fig)