import random


class Employee:
    def __init__(self) -> None:
        self.present = False

    def emp_present(self):
        randomNum = random.random()
        if randomNum<0.5:
            self.present = True
        else:
            self.present = False


if __name__ == '__main__':
    emp1 = Employee()
    emp1.emp_present()
    print(emp1.present)
