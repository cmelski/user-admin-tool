from permission import PermissionSet

ADMIN_PERMISSIONS = PermissionSet(["read", "write", "delete"])
GUEST_PERMISSIONS = PermissionSet(["read"])
SUPER_PERMISSIONS = PermissionSet(["read", "write", "delete", "audit"])


class Roles:

    def __init__(self):
        self.admin = ADMIN_PERMISSIONS
        self.guest = GUEST_PERMISSIONS
        self.super = SUPER_PERMISSIONS



