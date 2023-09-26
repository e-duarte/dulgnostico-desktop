import pandas as pd

class UserCSVLoader:
    def __init__(self, path):
        self.users = []
        df = pd.read_csv(path)

        self.read_user_from_csv(df)
    
    def read_user_from_csv(self, df):
        columns = df.columns.values
        for i, row in df.iterrows():        
            self.users.append(
                User(
                    name=row[columns[0]],
                    email=row[columns[1]],
                    permission=row[columns[3]]
                )
            )

class User:
    def __init__(self, name, email, permission):
        self.name = name
        self.email = email
        self.permission = permission
    
    def to_json(self):
        return {
            'name': self.name,
            'email': self.email,
            'permission': self.permission,
        }
    def __str__(self):
        return f'User(name:{self.name}, email:{self.email}, permission:{self.permission})'
    


if __name__ == '__main__':
    path = '/home/eduarte/Documents/Dulcinéia/Apps e Programas/arquivos de configuração diagnóstico planilhas/data/users.csv'
    loader = UserCSVLoader(path)

    for u in loader.users:
        print(u)