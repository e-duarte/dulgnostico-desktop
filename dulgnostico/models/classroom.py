import pandas as pd

class ClassroomCSVLoader:
    def __init__(self, path):
        df = pd.read_csv(path)
        self.classrooms = []

        self.read_classsroom_from_csv(df)

    def read_classsroom_from_csv(self, df):
        columns = df.columns.values
        for i, row in df.iterrows():        
            self.classrooms.append(
                Classroom(
                    classroom=row[columns[0]],
                    grade=row[columns[1]],
                    period=row[columns[2]],
                    teacher=row[columns[3]],
                )
            )

class Classroom:
    def __init__(self, classroom, grade, period, teacher):
        self.classroom = classroom
        self.grade = grade
        self.period = period
        self.teacher = teacher
    
    def to_json(self):
        return {
            'classroom': self.classroom,
            'grade': self.grade,
            'period': self.period,
            'teacher': self.teacher,
        }

    def __str__(self):
        return f'Classrrom(classroom:{self.classroom}, grade:{self.grade}, period:{self.period}, teacher:{self.teacher})'


if __name__ == '__main__':
    path = '/home/eduarte/Documents/Dulcinéia/Apps e Programas/arquivos de configuração diagnóstico planilhas/data/classrooms_dulcineia.csv'
    loader = ClassroomCSVLoader(path)
    print(loader.classrooms[0])