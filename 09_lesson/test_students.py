from db import StudentGroupTable


CONNECTION_STRING = "postgresql://postgres:123@localhost:5432/QA"
db = StudentGroupTable(CONNECTION_STRING)


def test_add_student():
    max_id = db.get_max_id()
    test_user_id = max_id + 1
    test_group_id = 100

    rows_before = db.get_all()
    len_before = len(rows_before)

    new_id = db.create(test_user_id, test_group_id)

    rows_after = db.get_all()
    len_after = len(rows_after)

    db.delete(test_user_id)

    assert len_after - len_before == 1
    assert new_id == test_user_id


def test_update_student():
    max_id = db.get_max_id()
    test_user_id = max_id + 1
    old_group_id = 100
    new_group_id = 200

    db.create(test_user_id, old_group_id)
    db.update(test_user_id, new_group_id)
    updated = db.get_by_id(test_user_id)
    db.delete(test_user_id)

    # Обращаемся по индексу: 0 - user_id, 1 - group_id
    assert updated[1] == new_group_id
    assert updated[0] == test_user_id


def test_delete_student():
    max_id = db.get_max_id()
    test_user_id = max_id + 1
    test_group_id = 100

    db.create(test_user_id, test_group_id)
    assert db.get_by_id(test_user_id) is not None

    rows_before = db.get_all()
    len_before = len(rows_before)

    db.delete(test_user_id)

    rows_after = db.get_all()
    len_after = len(rows_after)

    assert len_before - len_after == 1
    assert db.get_by_id(test_user_id) is None
