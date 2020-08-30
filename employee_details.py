class Employee:
    def __init__(self, name, id, exp):
        self.name = name
        self.id = id
        self.exp = exp
    organisation = 'Gyanmatrix'

    def emp_details(self):
        print('Emp Name : ', self.name)
        print('E-id :', self.id)
        print('Experience : ', self.exp)
        print(self.organisation)
        print((self))
shannu = Employee('shannu', 'gmx122', 3)
shannu.emp_details()
