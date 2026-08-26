from pydantic import BaseModel
from typing import List , Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')


patient_info = {'name': 'talha', 'age': '20', 'weight': 67.5, 'married': True, 'allergies': ['throat', 'dust'] , 'contact': {'gmail': 'talha@gamil.com' , 'phone': 123456}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)