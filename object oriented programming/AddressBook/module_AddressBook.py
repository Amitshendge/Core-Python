from module_Address import class_address

class class_operation:
    """
    Description:
        This class has all the operations to be perform on Object of Addressbook class which we have imported
"""
    
    def add():
        """
    Description:
        Function is used to add entries in addressbook
    Parameter:
        no parameters required
    Return:
        object of Address created with required parameters
    """

        f_name = input('first name : ')
        l_name = input('last name : ')
        add = input('address : ')
        city = input('city : ')
        state = input('state : ')
        zip = input('zip : ')
        m_num = input('mobile number : ')
        email = input('email id : ')
        return class_address(f_name,l_name,add,city,state,zip,m_num,email)

    def remove(self):
        """
    Description:
        Function is used to remove entries from addressbook
    Parameter:
        self parameter or an object as parameter required
    Return:
        does not return anything
    """

        result.remove(self)


    def add_dummy():
        """
    Description:
        Function is used to add 3 dummy entries in addressbook
    Parameter:
        no parameters required
    Return:
        does not return anything
    """

        result.append(class_address('Amit','Shendge','Panvel','New Panvel','Maharashtra','410206','9892126741','Amitshendge1990@gmail.com'))
        result.append(class_address('mahesh','sargar','kamothe','New Panvel','Maharashtra','410206','1234567890','maheshsargar@gmail.com'))
        result.append(class_address('rajat','nikam','khandacolony','New Panvel','Maharashtra','410206','9876543210','rajatnikam@gmail.com'))


    def function_show():
        """
    Description:
        Function is used to show all the entries in addressbook
    Parameter:
        no parameters required
    Return:
        does not return anything
    """

        for i in result:
            print(i,'\n')


    def function_find(fname):
        """
    Description:
        Function is used to find entry in addressbook with similar name as parameter
    Parameter:
        string parameter as first name of person to be searched in addressbook
    Return:
        returns an object which has first_name property as parameter passed
    """

        for i in result:
            if i.first_name == fname:
                return i


    def function_removeAddress():
        """
    Description:
        Function is used to remove entries from addressbook with using remove and find method
    Parameter:
        no parameters required
    Return:
        does not return anything
    """

        user_data = input('Enter first name to remove that address : ')
        class_operation.remove(class_operation.function_find(user_data))

    def function_update_data(self):
        """
    Description:
        Function is used to update previous entries
    Parameter:
        self or object which to be updated
    Return:
        does not return anything
    """

        self.first_name = input('first name : ')
        self.last_name = input('last name : ')
        self.address = input('address : ')
        self.city = input('city : ')
        self.state = input('state : ')
        self.zip = input('zip : ')
        self.mobile_number = input('mobile number : ')
        self.email = input('email id : ')
    
    def function_update_call():
        class_operation.function_update_data(class_operation.function_find('mahesh'))


if __name__ == '__main__':
    result = []

    # result.append(class_operation.add())
    class_operation.add_dummy()
    # class_operation.remove(result[2])
    # class_operation.function_show()
    # class_operation.function_removeAddress()
    # class_operation.function_update_call()
    class_operation.function_show()