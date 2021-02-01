# import user 
from user import User
from privileges import Privileges

class Admin(User):
    """ this admin class will iherit user class modules """
    def __init__(self,first_name, last_name, age, location):
        """  """
        super().__init__(first_name, last_name, age, location)
        # self.privileges = ['can add posts','can delete post','can ban user','can approve comments']
        self.privilege = Privileges()