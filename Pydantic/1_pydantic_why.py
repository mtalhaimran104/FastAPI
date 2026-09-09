from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List , Dict , Optional

class Patient(BaseModel):
    name: str = Field(max_length= 50)
    email: EmailStr
    linkedin: AnyUrl
    age: int = Field(gt = 10, lt = 50)
    weight: float
    married: bool
    allergies: Optional[list[str]] = None
    contact: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print('updated')


patient_info = {'name': 'talha', 'email': 'mtalhaimran104@gmail.com', 'linkedin': 'https://www.linkedin.com/in/talha-imran-ai/', 'age': '20', 'weight': 67.5, 'married': True, 'contact': { 'phone': '1233', 'landline': '124321'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

