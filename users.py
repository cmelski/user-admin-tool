from permission import PermissionSet


class User:

    def __init__(self, id: int, username: str, permissions: list):
        self.id = id
        self.username = username
        self.permissions = permissions
        self.is_active = True

    def deactivate_user(self):
        self.is_active = False

    def get_permissions(self) -> list[str]:
        return self.permissions
