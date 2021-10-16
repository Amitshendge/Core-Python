class class_address:
    """
    Description:
        This class is blue print of address of addressbook which has following properties/parameters
"""

    def __init__(self,first_name,last_name,address,city,state,zip,mobile_number,email) -> None:
        """
    Description:
        Function is used to initiate the object creation of Address with following parameters
    Parameter:
        self object and some strings and int parameters as following
    Return:
        object of Address created with required parameters
    """

        self.first_name = first_name
        self.last_name =  last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.mobile_number = mobile_number
        self.email = email


    def __str__(self) -> str:
        """
    Description:
        Function is used to print all the properties of the object which is recieved as parameter
    Parameter:
        self object
    Return:
        string of all the properties of the object which is recieved as parameter
    """
    
        return str('first name : '+self.first_name+
        '\nlast name : '+self.last_name+
        '\naddress : '+self.address+
        '\ncity : '+self.city+
        '\nstate : '+self.state+
        '\nzip : '+str(self.zip)+
        '\nmobile number : '+str(self.mobile_number)+
        '\nemail id : '+self.email)