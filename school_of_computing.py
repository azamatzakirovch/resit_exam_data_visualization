def school_of_computing():
    import streamlit as st
    import plotly.express as px
    import plotly.graph_objects as go
    import methods

    col_department, col_program, col_day = st.columns([3, 4, 2])

    with col_department:
        selected_department = st.selectbox(
            "Departments of New Uzbekistan University",
            ["School of Computing"]
        )

    with col_program:
        available_programs = methods.get_education_programs(selected_department)
        selected_programs = st.multiselect(
            "Education Programs of Department",
            available_programs,
            default=available_programs[:1]
        )

    with col_day:
        selected_day = st.selectbox("Exam Days", ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"])

    if not selected_programs:
        st.error("Please select at least one education program to continue.")
        st.stop()

    exam_data = methods.return_the_number_of_students_in_exam_session(selected_day, selected_programs)

    col_chart, col_info = st.columns([6, 4])

    with col_chart:
        df_sessions = exam_data.reset_index().rename(columns={"index": "Session"})
        df_long = df_sessions.melt(id_vars="Session", var_name="Program", value_name="Students")

        session_list = df_long["Session"].unique().tolist()
        filtered_df = df_long[df_long["Session"].isin(session_list)]

        fig = px.bar(
            filtered_df,
            x="Session",
            y="Students",
            color="Program",
            barmode="group",
            title="Number of Students per Session by Program",
            width=600,
            height=550
        )

        st.plotly_chart(fig, use_container_width=True)

    with col_info:
        gender_diagnosis = methods.get_gender_statistics(selected_day, selected_programs)
        male = 0
        female = 0

        for program in gender_diagnosis:
            for session in gender_diagnosis[program]:
                male = male + gender_diagnosis[program][session]['MALE']
                female = female + gender_diagnosis[program][session]['FEMALE']

        labels = ['Men', 'Women']
        values = [male, female]

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.6,
            hoverinfo='label+percent+value',
            textinfo='label+percent',
        )])

        fig.update_layout(
            title_text="                                        Resit Exam Students by Gender",
            width=650,
            height=250,
            margin=dict(l=100, r=30, t=70, b=0)
        )

        st.plotly_chart(fig)

        session_one, session_two, session_three = st.columns(3)

        with session_one:
            gender_teller_for_one = methods.get_numbers_by_session(selected_day, selected_programs, 1)

            number_of_male_in_session_one = gender_teller_for_one[0]
            number_of_female_in_session_one = gender_teller_for_one[1]
            labels = ['Men', 'Women']
            values = [number_of_male_in_session_one, number_of_female_in_session_one]

            fig = go.Figure(data=[go.Pie(
                labels=labels,
                values=values,
                hole=0.7,
                hoverinfo='label+percent+value',
                textinfo='label+percent',
                showlegend=False,  # remove legend
                domain=dict(x=[0, 1], y=[0, 1])  # controls donut outer size
            )])

            fig.update_layout(
                width=350,
                height=250,
                margin=dict(l=30, r=30, t=20, b=0)
            )

            st.plotly_chart(fig)

        with session_two:
            gender_teller_for_two = methods.get_numbers_by_session(selected_day, selected_programs, 2)
            number_of_male_in_session_two = gender_teller_for_two[0]
            number_of_female_in_session_two = gender_teller_for_two[1]
            labels = ['Men', 'Women']
            values = [number_of_male_in_session_two, number_of_female_in_session_two]

            fig = go.Figure(data=[go.Pie(
                labels=labels,
                values=values,
                hole=0.7,  # keeps the donut style
                hoverinfo='label+percent+value',
                textinfo='label+percent',
                showlegend=False,  # remove legend
                domain=dict(x=[0, 1], y=[0, 1])  # controls donut outer size
            )])

            fig.update_layout(
                width=350,
                height=250,
                margin=dict(l=30, r=30, t=20, b=0)
            )

            st.plotly_chart(fig)

        with session_three:
            gender_teller_for_three = methods.get_numbers_by_session(selected_day, selected_programs, 3)
            number_of_male_in_session_three = gender_teller_for_three[0]
            number_of_female_in_session_three = gender_teller_for_three[1]
            labels = ['Men', 'Women']
            values = [number_of_male_in_session_three, number_of_female_in_session_three]

            fig = go.Figure(data=[go.Pie(
                labels=labels,
                values=values,
                hole=0.7,
                hoverinfo='label+percent+value',
                textinfo='label+percent',
                showlegend=False,
                domain=dict(x=[0, 1], y=[0, 1])
            )])

            fig.update_layout(
                width=350,
                height=250,
                margin=dict(l=30, r=30, t=20, b=0)
            )

            st.plotly_chart(fig)

    statistics_by_study_year, small_information = st.columns([4, 6])

    with statistics_by_study_year:
        students_data = methods.get_df_of_counted_students_by_study_year(selected_programs)

        fig = px.bar(
            students_data,
            x="STUDY YEAR",
            y="IN NUMBERS",
        )

        fig.update_traces(
            width=0.4

        )

        fig.update_layout(
            xaxis_title="Session",
            title="Number of Students by Study Year",
            bargroupgap=0.1,
            width=20,
            height=450,
            margin=dict(l=80, r=30, t=50, b=0),
        )

        st.plotly_chart(fig, use_container_width=True)

    with small_information:
        st.markdown("""
            <style>
                .text-settings {
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
                }
            </style>
            <div class="text-settings">Explanation for charts</div>
        """, unsafe_allow_html=True)

        sessions, gender, study_year = st.columns(3)

        with sessions:
            st.markdown("""
            <p style="font-size:14px;line-height:1.5;margin:0;">
                First chart hows how students are distributed across sessions in the program, 
                providing a clear view of participation at different stages 
                of the academic calendar.
                
                
            </p>
            """, unsafe_allow_html=True)

        with gender:
            st.markdown("""
            <p style="font-size:14px;line-height:1.5;margin:0;">
                Second chart is plays the proportion of <b>male</b> and <b>female</b> students 
                taking resit exams, offering insight into gender representation 
                in this category.
                
                
            </p>
            """, unsafe_allow_html=True)

        with study_year:
            st.markdown("""
            <p style="font-size:14px;line-height:1.5;margin:0;">
                Third chart illustrates how students are spread across different academic years, 
                highlighting overall progression through the program.
                
                
            </p>
            """, unsafe_allow_html=True)

        st.markdown("""
            <style>
                .text-settings-of-summary {
                    position: absolute;
                    top: 20px;
                    left: 50%;
                    width: 100%;
                    transform: translateX(-50%);
                    font-size: 18px;
                    font-weight: 600;
                    font-family: 'Arial', sans-serif;
                    color: black;
                    text-align: center;
                    white-space: nowrap;
                }
            </style>
            <div class="text-settings-of-summary">Summary for School Of Computations department</div>
        """, unsafe_allow_html=True)

        st.markdown("""
                        <style>
                            .text-settings-of-rectangle-for-df-explanation {
                                position: absolute;
                                top: 30px;
                                font-size: 15px;
                                line-height: 1.6;
                                color: #1e1e1e;
                                font-family:'Arial', sans-serif;
                                font-weight: 400;
                                text-align: justify;
                            }

                        </style>
                        <div class = "text-settings-of-rectangle-for-df-explanation">
                            The dashboard presents three key visualizations describing student distribution and demographics. The first chart shows the total number of students across different sessions by program. Notably, the total here is higher than in the third chart because a single student may participate in multiple exam sessions, leading to repeated counting. This explains why the sum in Chart 1 exceeds the total number of unique students.
                            The second chart illustrates the proportion of male and female students taking resit exams. While the exact numbers vary, the visualization makes it clear how gender representation differs within this specific group, potentially pointing to trends in performance or participation in resits.
                            The third chart shows the distribution of students by study year, providing a clear picture of academic progression. Compared to the first chart, this figure represents unique student counts, as each student belongs to a single study year. This distinction is essential when comparing totals between the first and third charts.
                            Together, the three charts give a multi-layered perspective: the first highlights session participation patterns, the second addresses gender balance in resits, and the third reflects the overall academic composition of the student body.
                        </div>
                        """, unsafe_allow_html=True)
