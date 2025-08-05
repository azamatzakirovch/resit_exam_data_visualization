def data():
    import pandas as pd
    import ast
    df = pd.read_csv('new_students_data.csv')

    df['MONDAY'] = df['MONDAY'].apply(ast.literal_eval)
    df['TUESDAY'] = df['TUESDAY'].apply(ast.literal_eval)
    df['WEDNESDAY'] = df['WEDNESDAY'].apply(ast.literal_eval)
    df['THURSDAY'] = df['THURSDAY'].apply(ast.literal_eval)
    df['FRIDAY'] = df['FRIDAY'].apply(ast.literal_eval)

    return df