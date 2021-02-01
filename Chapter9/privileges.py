import admin
class Privileges:
    """  """
    def __init__(self):
        self.privileges = ['can add posts','can delete post','can ban user','can approve comments','can unblock users']

    def show_privileges(self):
        print("Admin's Privileges are: ")
        for p in self.privileges:
            print(p)    