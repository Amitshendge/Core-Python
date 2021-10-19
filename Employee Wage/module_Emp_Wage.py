'''
@Author: Amit Shendge
@Date: 19-10-2021 11:17PM
@Last Modified by: Amit Shendge
@Last Modified time: 19-10-2021 11:17PM
@Title : Employee wage with daily wages
'''

import random

class Employee:
    def __init__(self,present=False,part_time=False) -> None:
        self.present = present
        self.part_time = part_time

    def emp_present(self):
        """
        Description:
            Function is used generate random to assign present or absent to employee object
        Parameter:
            self object is passed
        Return:
            doesn't returns anything but sets present status of employee
        """
        randomNum = random.random()
        if randomNum<0.5:
            self.present = True
            print('Employee is Present')
        else:
            self.present = False
            print('Employee is Absent')

    def daily_emp_wage(self):
        """
        Description:
            Function is used generate daily wages made by employee as part or full time
        Parameter:
            self object is passed
        Return:
            doesn't returns anything but prints daily wages as part or full time
        """
        static_var_WagePerHr = 20
        static_var_FullDayHr = 8
        static_var_PartWagePerHr = 8
        static_var_PartDayHr = 4
        if self.present == False:
            print('Employee wage of the day will be Zero because he/she is Absent')
        elif self.present == True and self.part_time == False:
            print('Employee wage of the day will be : ',(static_var_WagePerHr * static_var_FullDayHr),'$')
        else:
            print('Employee wage of the day will be : ',(static_var_PartWagePerHr * static_var_PartDayHr),'$')
    

if __name__ == '__main__':
    emp1 = Employee(part_time=True)
    emp1.emp_present()
    emp1.daily_emp_wage()
