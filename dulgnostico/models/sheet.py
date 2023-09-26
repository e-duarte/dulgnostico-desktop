from test import Test, TestVar
import json

class SheetJsonLoader:
    def __init__(self, path):
        with open(path, encoding="utf8") as config_file:
            config = json.load(config_file)
        
        self.read_sheet_from_json(config)

    def read_sheet_from_json(self, data):
        self.sheet = Sheet(
            header=data['header'],
            metadata=SheetMatadata(
                title=data['metadata']['title'],
                subject=data['metadata']['subject'],
                grade=data['metadata']['grade'],
                bimester=data['metadata']['bimester'],
                year=data['metadata']['year'],
            ),
            shared_with=data['shared_with'],
            columns_width=data['columns_width'],
            test=Test(
                test_vars= [
                    TestVar(var['name'], var['values'])
                    for var in data['vars'] 
                ]
            )
        )

class SheetMatadata:
    def __init__(self, title, subject, grade, bimester, year):
        self.title = title
        self.subject = subject
        self.grade = grade
        self.bimester = bimester
        self.year = year
    
    def to_json(self):
        return {
            'title': self.title,
            'subject': self.subject,
            'grade': self.grade,
            'bimester': self.bimester,
            'year': self.year,
        }

class Sheet:
    def __init__(self,  header, metadata, shared_with, columns_width, test, link=""):
        self.link = link
        self.header = header
        self.metadata = metadata
        self.shared_with = shared_with
        self.columns_width = columns_width
        self.test = test
    
    def to_json(self):
        return {
            'link': self.link,
            'header': self.header,
            'medata': self.metadata.to_json(),
            'shared_with': self.shared_with,
            'columns_width': self.columns_width,
            'test': self.test.to_json(),
        }

    # def __str__(self):
    #     return f'Sheet(school:{self.school}, inep:{self.inep}, year:{self.year}, shared:{self.shared}, test:{self.test})'

if __name__ == '__main__':
    path = '/home/eduarte/Projects/dulgnostico-desktop/sheet_example.json'
    loader = SheetJsonLoader(path)
    print(loader.sheet.shared_with)