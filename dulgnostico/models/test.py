class TestVar:
    def __init__(self, name, values):
        self.name = name
        self.values = values
    
    def to_json(self):
        return {
            'name': self.name,
            'values': self.values,
        }

class Test:
    def __init__(self, test_vars):
        self.test_vars = test_vars

    def to_json(self):
        return {
            'test_vars': [var.to_json() for var in self.test_vars]
        }

    # def __str__(self):
    #     return f'Teste(link:{self.link}, subject:{self.subject}, title:{self.title}, grade:{self.grade}, bimester:{self.bimester}, questions:{self.questions})'
    