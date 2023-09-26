from dulgnostico.init import FireBaseInit
from dulgnostico.models.student import Student

if __name__ == '__main__':
    firestore = FireBaseInit()
    joao = Student('João', classroom='F1M901')

    doc_ref = firestore.get_db().collection('student').document()
    doc_ref.set(joao.to_json())

    

    