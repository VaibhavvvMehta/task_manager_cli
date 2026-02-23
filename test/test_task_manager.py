import pytest
from task_manager import TaskManager
from exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
    InvalidPasswordError,
    TaskNotFoundError,
    InvalidInputError
)

@pytest.fixture
def manager(tmp_path):
    return TaskManager(
        users_file=str(tmp_path / "users.json"),
        session_file=str(tmp_path / "session.json"),
        tasks_folder=str(tmp_path / "tasks")
    )

def test_register_user(manager):
    manager.register_user("user", "1234")
    assert "user" in manager.load_users()

def test_duplicate_register(manager):
    manager.register_user("user", "1234")
    with pytest.raises(UserAlreadyExistsError):
        manager.register_user("user", "1234")

def test_login_success(manager):
    manager.register_user("user", "1234")
    assert manager.get_current_user() == "user"

def test_login_wrong_password(manager):
    manager.register_user("user", "1234")
    with pytest.raises(InvalidPasswordError):
        manager.login_user("user", "wrong")

def test_login_non_user(manager):
    with pytest.raises(UserNotFoundError):
        manager.login_user("abc", "123")

def test_logout(manager):
    manager.register_user("user", "1234")
    manager.logout_user()
    with pytest.raises(InvalidInputError):
        manager.get_current_user()

def test_add_task(manager):
    manager.register_user("user", "1234")
    manager.add_task("Gym", "6AM", 1, "2026-02-20")
    assert len(manager.load_tasks()) == 1


def test_update_task(manager):
    manager.register_user("user", "1234")
    manager.add_task("Gym", "6AM", 1, "2026-02-20")
    manager.update_task(1, status="completed")
    assert manager.load_tasks()[0]["status"] == "completed"

def test_update_invalid_task(manager):
    manager.register_user("user", "1234")
    with pytest.raises(TaskNotFoundError):
        manager.update_task(5, status="completed")

def test_delete_task(manager):
    manager.register_user("user", "1234")
    manager.add_task("Gym", "6AM", 1, "2026-02-20")
    manager.delete_task(1)
    assert manager.load_tasks() == []


def test_delete_invalid_task(manager):
    manager.register_user("user", "1234")
    with pytest.raises(TaskNotFoundError):
        manager.delete_task(10)

def test_show_tasks(manager):
    manager.register_user("user", "1234")
    manager.add_task("Gym", "6AM", 1, "2026-02-20")
    tasks = manager.show_tasks()
    assert len(tasks) == 1

def test_filter_status(manager):
    manager.register_user("user", "1234")
    manager.add_task("Gym", "6AM", 1, "2026-02-20")
    manager.update_task(1, status="completed")
    tasks = manager.show_tasks(status="completed")
    assert len(tasks) == 1

def test_filter_no_match(manager):
    manager.register_user("user", "1234")
    manager.add_task("Gym", "6AM", 1, "2026-02-20")
    with pytest.raises(TaskNotFoundError):
        manager.show_tasks(status="completed")

def test_add_without_login(manager):
    with pytest.raises(InvalidInputError):
        manager.add_task("Gym", "6AM", 1, "2026-02-20")


