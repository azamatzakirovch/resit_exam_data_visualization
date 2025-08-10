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
                if session.get(q) and session[q] != '0' and session[q] != 'CW':
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


def get_gender_statistics(exam_day, edu_programs):
    gender_dictionary = {}
    exam_day_sessions = list(df[exam_day][0].keys())
    genders = ['MALE', 'FEMALE']

    def is_available(info):
        if info == '0' or info == 'CW':
            return False
        return True

    for q in edu_programs:
        gender_dictionary[q] = {}

    for q in edu_programs:
        for e in exam_day_sessions:
            gender_dictionary[q][e] = {}

    for k in edu_programs:
        for g in exam_day_sessions:
            for r in genders:
                gender_dictionary[k][g][r] = 0

    for idx, school in df['EDUCATION_PROGRAM'].items():
        if school in edu_programs:
            sessions = gender_dictionary[school]
            for session in exam_day_sessions:
                if df['GENDER'][idx] == 'MALE' and is_available(df[exam_day][idx][session]):
                    sessions[session]['MALE'] += 1
                elif is_available(df[exam_day][idx][session]):
                    sessions[session]['FEMALE'] += 1

    return gender_dictionary


def get_numbers_by_session(examination_day, education_program, session_number):
    if len(education_program) == 0:
        return False

    data_frame = get_gender_statistics(examination_day, education_program)
    male, female = 0, 0
    mini_keys = list(data_frame[education_program[0]].keys())

    if session_number == 1:
        for program in data_frame:
            male = male + data_frame[program][mini_keys[session_number - 1]]['MALE']
            female = female + data_frame[program][mini_keys[session_number - 1]]['FEMALE']

    if session_number == 2:
        for program in data_frame:
            male = male + data_frame[program][mini_keys[session_number - 1]]['MALE']
            female = female + data_frame[program][mini_keys[session_number - 1]]['FEMALE']

    if session_number == 3:
        for program in data_frame:
            male = male + data_frame[program][mini_keys[session_number - 1]]['MALE']
            female = female + data_frame[program][mini_keys[session_number - 1]]['FEMALE']

    if session_number == 4:
        for program in data_frame:
            male = male + data_frame[program][mini_keys[session_number - 1]]['MALE']
            female = female + data_frame[program][mini_keys[session_number - 1]]['FEMALE']

    return [male, female]


def get_mini_keys(day):
    return list(df[day][0].keys())


def get_df_of_counted_students_by_study_year(school):
    students_statistics_by_edu_year = df[df["EDUCATION_PROGRAM"].isin(school)]
    counter = students_statistics_by_edu_year['STUDY_YEAR'].value_counts()
    studyyear = []
    numbers = []
    for z in counter.keys():
        if z == 1:
            studyyear.append("Freshmen")
            numbers.append(counter[z])
        if z == 2:
            studyyear.append("Sophomore")
            numbers.append(counter[z])
        if z == 3:
            studyyear.append("Junior")
            numbers.append(counter[z])
        if z == 4:
            studyyear.append("Senior")
            numbers.append(counter[z])

    return pd.DataFrame(list(zip(studyyear, numbers)), columns=["STUDY YEAR", "IN NUMBERS"])