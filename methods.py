from students_and_exam_schedule_data import data
import pandas as pd

df = data()


def return_the_number_of_students_in_exam_session(Exam_day, Edu_programs):
    length = len(df)
    new_df = df[['STUDY_YEAR', 'SCHOOL', 'EDUCATION_PROGRAM', Exam_day]]
    dictionary = {}
    total_keys = []
    for j in new_df[Exam_day][0]:
        total_keys.append(j)

    for key in Edu_programs:
        dictionary[key] = {}
        for mini_key in total_keys:
            dictionary[key][mini_key] = 0

    for p in range(length):
        student_edu_program = df['EDUCATION_PROGRAM'][p]
        if student_edu_program in Edu_programs:
            session = df[Exam_day][p]
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
        'School of Humanities, Natural and Social Sciences': ['Applied Mathematics', 'Economics and Data Science',
                                                              'Pedagogy'],
        'School of Management': ['Industrial Management']
    }
    return school_and_edu[dep]
