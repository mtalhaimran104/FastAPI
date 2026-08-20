def insert_patient_data(name : str, age : int):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('inserted to database')
    else:
        raise TypeError('Incorrect data type')
    
insert_patient_data('talha' , 6)


#Update patient data in database
def update_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('Incorrext data type')

update_patient_data('ahmad' ,17)