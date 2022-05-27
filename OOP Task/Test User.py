import Admin

admin = Admin.Admin("Андрій", "Парайко", "18", "andriyparayko2017@gmail.com", 5)
print(admin.priv.show_privileges())

from Admin import Admin, Privileges
