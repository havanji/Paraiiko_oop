import User


class Admin(User):
    def __init__(self):
        self.priv = list([["«Allowed to add message»"],
                          ["«Allowed to delete users»"],
                          ["«Allowed to ban users»"]])

    def show_privileges(self):
        return self.priv

    pass


# Admin = Admin()
# print(Admin.show_privileges())


class Privileges(Admin):
    def __init__(self):
        self.privilegies = list([["«Allowed to add message»"],
                                 ["«Allowed to delete users»"],
                                 ["«Allowed to ban users»"]])

    def show_privileges(self):
        return self.privilegies

    pass

# admin = Privileges()
# print(admin.show_privileges())
