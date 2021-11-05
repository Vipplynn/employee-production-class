class Employee:
#Parent class. Initializes name and number
    def __init__(self,name,number):
        self.__name = name
        self.number = number

    def set_emp_name(self,name):
        self.__name = name

    def set_emp_number(self,number):
        self.__number = number

    def get_emp_name(self):
        return self.__name

    def get_emp_number(self):
        return self.number

class ProductionWorker(Employee):
#Child class. Inherits name and number from Employee Class
    def __init__(self,name,number,shift_num,pay_rate):

        Employee.__init__(self,name,number)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    def set_shift_num(self,shift_num):
        self.__shift_num = shift_num

    def set_pay_rate(self,pay_rate):
        self.__pay_rate = pay_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rates(self):
        return self.__pay_rate
def main():
#Main function of program. Asks for information of employee then returns that information.
    emp_name = input('Employee Name: ')
    number = input('Employee Number: ')
    shift = int(input('Shift Number: '))
    while True:
        if shift == 1 or shift == 2:
            break
        elif shift != 1 or shift != 2:
            shift = int(input('Not between 1 and 2 '))
            continue
    pay = input('Pay Rate: ')
    emp = ProductionWorker(emp_name, number, shift, pay)
    print()
    print('----------Employee Information----------')
    print(f'Name: {emp.get_emp_name()}')
    print(f'Employee Number: {emp.get_emp_number()}')
    print(f'Shift Number: {emp.get_shift_num()}')
    print(f'Pay Rate: ${float(emp.get_pay_rates())}')
main()