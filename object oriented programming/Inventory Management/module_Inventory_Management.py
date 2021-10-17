'''
@Author: Amit Shendge
@Date: 17-10-2021 11:23PM
@Last Modified by: Amit Shendge
@Last Modified time: 17-10-2021 11:23PM
@Title : Inventory Management
'''

import json

class class_Inventory:

    def __init__(self, type, name, weight, rate):
        """
    Description:
        Function is used to initiate the object creation of Inventory with following parameters
    Parameter:
        self object and some strings and int parameters as following
    Return:
        object of Address created with required parameters
    """
        self.type = type
        self.name = name
        self.weight = weight
        self.rate = rate


    @classmethod
    def from_json_to_obj(cls, json_string):
        """
    Description:
        Function is used to create an object of Inventory from json input
    Parameter:
        this is a class method so the class gets added as parameter and json as string format
    Return:
        object of Inventory created with given parameters
    """
        json_dict = json.loads(json_string)
        return cls(**json_dict)


    def __repr__(self) -> str:
        """
    Description:
        Function is used to represent the actions to perform when this object is called inside print method
    Parameter:
        self object parameters as following
    Return:
        name property of that object passed in as parameter
    """
        return self.name


    def total_value(list_inventory):
        """
    Description:
        Function is used to calculate total inventory value in Ruppes
    Parameter:
        list of inventory objects
    Return:
        sum of cost of all the present items in inventory
    """
        sum = 0
        for item in list_inventory:
            sum = sum + (item.weight*item.rate)
        return sum


if __name__ == "__main__":

    list_inventory = []

    with open('my_JSON.json','r') as json_file:
        json_data = json.loads(json_file.read())
        for u in json_data:
            list_inventory.append(class_Inventory(**u))

    print((class_Inventory.total_value(list_inventory)), 'Rupees')