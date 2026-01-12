class PermissionSet:
    def __init__(self, permissions: list[str]):
        self._permissions = permissions

    def get_permissions(self) -> list[str]:
        return self._permissions
