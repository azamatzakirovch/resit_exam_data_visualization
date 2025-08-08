def school_of_computing():
    import streamlit as st
    import plotly.express as px
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

    exam_data = methods.return_the_number_of_students_in_exam_session(selected_day, selected_programs)

    col_chart, col_info = st.columns([7, 3])

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
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

    with col_info:
        st.markdown("""
            <style>
                .rectangle {
                    position: absolute;
                    top: 0px;
                    left: 0px;
                    height: 600px;
                    width: 360px;
                    border: 1px solid black;
                }
            </style>
            <div class="rectangle"></div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .rectangle-1 {
                position: absolute;
                top: 0px;
                left: 0px;
                height: 300px;
                width: 100%;
                border: 1px solid black;
            }
        </style>
        <div class="rectangle-1"></div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .rectangle-2 {
                position: absolute;
                top: 300px;
                left: 0px;
                height: 20px;
                width: 100%;
                # border: 1px solid black;
            }
        </style>
        <div class="rectangle-2"></div>
    """, unsafe_allow_html=True)
