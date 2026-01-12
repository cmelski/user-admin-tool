from repository import Repository
from roles import Roles
from users import User

repo = Repository()
roles = Roles()
admin1 = User(1, "Chris", roles.admin.__dict__['_permissions']).__dict__
guest1 = User(2, "Karen", roles.guest.__dict__['_permissions']).__dict__
admin2 = User(3, "Dave", roles.admin.get_permissions()).__dict__
guest2 = User(4, "Sam", roles.guest.get_permissions()).__dict__
super1 = User(5, "Keith", roles.super.get_permissions()).__dict__
repo.append_to_user_list(admin1)
repo.append_to_user_list(guest1)
repo.append_to_user_list(admin2)
repo.append_to_user_list(guest2)
repo.append_to_user_list(super1)
