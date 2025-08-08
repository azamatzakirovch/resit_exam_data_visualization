def school_of_management():
    import streamlit as st
    import plotly.express as px
    import methods

    department_m, education_program_m, exam_day_m = st.columns([3, 4, 2])

    with department_m:
        departments = st.selectbox(
            "Departments of New Uzbekistan University",
            ["School of Management"]
        )

    with education_program_m:
        default_data_m = methods.get_education_programs(departments)
        edu_programs = st.multiselect(
            "Education Programs of Department",
            default_data_m,
            default=default_data_m[:1]
        )

    with exam_day_m:
        week_day = st.selectbox("Exam Days", ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"])

    dictionary_of_exam_session = methods.return_the_number_of_students_in_exam_session(week_day, edu_programs)

    barchart, explanation = st.columns([7, 3])

    with barchart:
        df_reset = dictionary_of_exam_session.reset_index().rename(columns={"index": "Session"})
        df_melted = df_reset.melt(id_vars="Session", var_name="Program", value_name="Students")

        sessions = df_melted["Session"].unique().tolist()

        filtered_df = df_melted[df_melted["Session"].isin(sessions)]

        # Bar chart
        fig = px.bar(
            filtered_df,
            x="Session",
            y="Students",
            color="Program",
            barmode="group",
            title="Number of Students per Session by Program",
            width=600,
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

    with explanation:
        st.markdown("""
            <style>
                .rectangle {
                    position: absolute;
                    top: 0px;
                    left: 0px;
                    height: 600px;
                    width: 400px;
                    border: 1px solid black;
                }
            </style>

            <div class="rectangle"></div>
        """, unsafe_allow_html=True)