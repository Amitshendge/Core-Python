'''
@Author: Amit Shendge
@Date: 17-10-2021 11:43PM
@Last Modified by: Amit Shendge
@Last Modified time: 17-10-2021 11:43PM
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
    def function_from_json_to_obj(cls, json_string):
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


    def function_total_value(list_inventory):
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


    def function_each_value(list_inventory):
        """
    Description:
        Function is used to calculate total of single item in inventory in Ruppes
    Parameter:
        list of inventory objects
    Return:
        sum of cost of all the present items in inventory
    """
        for item in list_inventory:
            print('total value of ', item.name ,' is : ', (item.weight * item.rate))


    def function_catagory_value(list_inventory):
        """
    Description:
        Function is used to calculate total value of same category item in inventory in Ruppes
    Parameter:
        list of inventory objects
    Return:
        sum of cost of all the present items in inventory category wise
    """
        rice_value = 0
        pulses_value = 0
        wheat_value = 0
        for item in list_inventory:
            if item.type == 'Rice':
                rice_value = rice_value + (item.weight * item.rate)
            elif item.type == 'Pulses':
                pulses_value = pulses_value + (item.weight * item.rate)
            elif item.type == 'Wheat':
                wheat_value = wheat_value + (item.weight * item.rate)
        print('total value of Rice is : ', rice_value)
        print('total value of Pulses is : ', pulses_value)
        print('total value of Wheat is : ', wheat_value)


    def function_toJSON(list_inventory):
        """
    Description:
        Function is used to convert object to JSON string
    Parameter:
        list of inventory objects
    Return:
        Does not return anything but prints JSON string of all the objects present in list
    """
        for item in list_inventory:
            print(json.dumps(item.__dict__))

    


if __name__ == "__main__":

    list_inventory = []

    with open('my_JSON.json','r') as json_file:
        json_data = json.loads(json_file.read())
        for u in json_data:
            list_inventory.append(class_Inventory(**u))

    class_Inventory.function_each_value(list_inventory)
    print()
    print('Total value of whole Inventory is : ',(class_Inventory.function_total_value(list_inventory)), 'Rupees')
    print()
    class_Inventory.function_catagory_value(list_inventory)
    # class_Inventory.function_toJSON(list_inventory)