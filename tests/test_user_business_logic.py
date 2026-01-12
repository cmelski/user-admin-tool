from users import User
import logging
from roles import Roles

roles = Roles()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def test_user_is_active_by_default():
    user = User(1, "guest_user", roles.guest.get_permissions())
    logger.info(f'User Default Details: {user.__dict__}')

    assert user.is_active is True


def test_user_can_be_deactivated():
    user = User(2, "inactive_user", roles.guest.get_permissions())

    user.deactivate_user()
    logger.info(f'User Details After Deactivation: {user.__dict__}')

    assert user.is_active is False


def test_user_permissions_are_returned_correctly():
    user = User(3, "admin_user", roles.admin.get_permissions())
    logger.info(f'User permissions: {user.get_permissions()}')

    assert user.get_permissions() == ["read", "write", "delete"]


def test_users_can_have_different_permissions():
    admin = User(4, "admin", roles.admin.get_permissions())
    guest = User(5, "guest", roles.guest.get_permissions())

    assert admin.get_permissions() != guest.get_permissions()


def test_user_permissions_can_change_without_new_user():
    user = User(6, "promoted_user", roles.guest.get_permissions())
    logger.info(f'User original permissions: {user.get_permissions()}')

    user.permissions = roles.admin.get_permissions()
    logger.info(f'User updated permissions: {user.get_permissions()}')

    assert "delete" in user.get_permissions()
