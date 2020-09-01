import pytest

from app import dbaccess


class TestDbAccess(object):

    @classmethod
    def setup_class(cls):
        print('start')
        db_name = "mytodo.db"
        cls.db_access = dbaccess.dbAccess(db_name)

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.db_access

    def setup_method(self, method):
        print('method={}'.format(method.__name__))

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_get_todo_list(self, test_data):
        # setup

        # execute
        todo_list = self.db_access.get_todo_list()

        # assert
        assert len(todo_list) == 2
