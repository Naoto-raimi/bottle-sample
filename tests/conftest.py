import pytest
import sqlite3

from app.dbaccess import dbAccess


@pytest.fixture(scope='session', autouse=False)
def test_data():
    test_todo_list = ['ご飯を食べる', '美術館にいく']
    db_access = dbAccess("mytodo.db")
    db_access.init_todo()
    for test_todo in test_todo_list:
        db_access.save_todo(test_todo)

    yield
    conn = sqlite3.connect("mytodo.db")
    c = conn.cursor()
    delete = "delete from todo_list"
    c.execute(delete)
    conn.commit()
    conn.close()
