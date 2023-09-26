import pandas as pd

class StudentCSVLoader:
    def __init__(self, path):
        df = pd.read_csv(path)
        self.students = []

        self.read_student_from_csv(df)

    def read_student_from_csv(self, df):
        columns = df.columns.values
        for i, row in df.iterrows():        
            self.students.append(
                Student(
                    name=row[columns[0]],
                    classroom=row[columns[1]],
                    tests_done=[]
                )
            )
        
        self.students.sort(key=lambda e: e.classroom)

class TestDone:
    def __init__(self, date='', test=''):
        self.date = date
        self.test = test
    
    def to_json(self):
        return {
            'date': self.date,
            'tests': self.test,
        }

class Student:
    def __init__(self, name, classroom, tests_done):
        self.name = name
        self.classroom = classroom
        self.tests_done = tests_done
    
    def to_json(self):
        return {
            'name': self.name,
            'classroom': self.classroom,
            'tests': self.tests.to_json(),
        }

    def __str__(self):
        return f'Student(name:{self.name}, classroom:{self.classroom}, tests_done:{self.tests_done})'

if __name__ == '__main__':
    loader = StudentCSVLoader('/home/eduarte/Documents/Dulcinéia/Apps e Programas/arquivos de configuração diagnóstico planilhas/data/new_students.csv')
    for s in loader.students:
        print(s)
    
    