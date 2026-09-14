from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    married: bool
    height: float #meters
    weight: float #kg
    allergies: list[str]
    contact_detail: dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print('BMI', patient.calculate_bmi)
    print(patient.email)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_detail)


patient_info = {'name': 'Talha', 'email': 'mtalhaimran104@gmail.com', 'age': 20, 'married': False, 'height': 56.5, 'weight': 56.5, 'allergies': ['none', 'none'], 'contact_detail': {'Phone': '0000000', 'email': 'mtalha@gmail.com'}}

patient1 = Patient(**patient_info)
patient_data(patient1)
