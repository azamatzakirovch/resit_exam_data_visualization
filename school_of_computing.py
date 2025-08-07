def school_of_computing():
    import streamlit as st
    from students_and_exam_schedule_data import data
    import plotly.express as px
    import pandas as pd

    df = data()

    def return_the_number_of_students_in_exam_session(exam_day, edu_programs):
        length = len(df)
        new_df = df[['STUDY_YEAR', 'SCHOOL', 'EDUCATION_PROGRAM', exam_day]]
        dictionary = {}
        total_keys = []
        for j in new_df[exam_day][0]:
            total_keys.append(j)

        for key in edu_programs:
            dictionary[key] = {}
            for mini_key in total_keys:
                dictionary[key][mini_key] = 0

        for p in range(length):
            student_edu_program = df['EDUCATION_PROGRAM'][p]
            if student_edu_program in edu_programs:
                session = df[exam_day][p]
                for q in total_keys:
                    if session.get(q) and session[q] != '0':
                        dictionary[student_edu_program][q] = dictionary[student_edu_program][q] + 1

        new_columns = []
        new_rows = []

        for ii in dictionary:
            mini_list = []
            for jj in dictionary[ii]:
                mini_list.append(dictionary[ii][jj])
            new_rows.append(mini_list)
            new_columns.append(ii)

        dct = {}

        for qq in range(len(new_columns)):
            dct[new_columns[qq]] = new_rows[qq]

        final_df = pd.DataFrame(dct)
        final_df.index = total_keys

        return final_df

    def get_education_programs(dep):
        school_and_edu = {
            'School of Computing': ['Software Engineering', 'Cyber Security', 'AI and Robotics'],
            'School of Engineering': ['Chemical and Materials Engineering', 'Mechanical Engineering'],
            'School of Humanities, Natural and Social Sciences': ['Applied Mathematics', 'Economics and Data Science', 'Pedagogy'],
            'School of Management': ['Industrial Management']
        }
        return school_and_edu[dep]

    def get_keys(EXAMINATION_DAY):
        return list(df[EXAMINATION_DAY][0].keys())

    department, education_program, exam_day = st.columns([3, 4, 2])

    with department:
        departments = st.selectbox(
            "Departments of New Uzbekistan University",
            ["School of Computing", "School of Engineering", "School of Humanities, Natural and Social Sciences", "School of Management"]
        )

    with education_program:
        default_data = get_education_programs(departments)
        edu_programs = st.multiselect(
            "Education Programs of Department",
            default_data,
            default=default_data[:1]  # default single item as list
        )

    with exam_day:
        week_day = st.selectbox("Exam Days", ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"])

    dictionary_of_exam_session = return_the_number_of_students_in_exam_session(week_day, edu_programs)

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

    with exam_day:
        st.markdown("""
            <style>
                .rectangle {
                    position: absolute;
                    top: 0px;
                    left: 0px;
                    height: 600px;
                    width: 260px;
                    border: 1px solid black;
                }
            </style>

            <div class="rectangle"></div>
        """, unsafe_allow_html=True)

