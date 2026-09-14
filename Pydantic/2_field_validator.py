from pydantic import BaseModel, AnyUrl, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact: dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hbl.com', 'ubl.com', 'iub.edu.pk']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.contact)
    print('updated')

patient_info = {'name': 'Talha', 'email': 'mtalhaimran104@iub.edu.pk', 'age': '20', 'weight': 55.5, 'married': True, 'allergies': ['none', 'none', 'none'], 'contact': {'phone': '0000000', 'email': "absc@gmail.com"}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
