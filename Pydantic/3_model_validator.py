from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    married: bool
    allergies: list[str]
    contact_detail: dict[str, str]

    @model_validator(mode= 'after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError('Patient greater than 60 must be have emergency contact')
        else:
            return model


def patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_detail)

patient_info = {'name': 'Talha', 'email': 'mtalhaimran104@gmail.com', 'age': 70, 'married': False, 'allergies': ['none', 'none'], 'contact_detail': {'Phone': '0000000', 'email': 'mtalha@gmail.com', 'emergency': '0000'}}

patient1 = Patient(**patient_info)
patient_data(patient1)
