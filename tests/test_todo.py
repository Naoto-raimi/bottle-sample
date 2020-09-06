import os
import pytest
from webtest import TestApp as AppTest
from bottle import TEMPLATE_PATH

from app import todo

TEMPLATE_PATH.append("../app/template")


class TestTodo(object):

    @classmethod
    def setup_class(cls):
        print('start')

    @classmethod
    def teardown_class(cls):
        print('end')

    def setup_method(self, method):
        print('method={}'.format(method.__name__))

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    # def test_index_webtest(self):
    #     # setup
    #     application = AppTest(todo.app)
    #     # execute
    #     responce = application.get('/')
    #     # assert
    #     assert responce.status_code == 200
    #     assert responce.content_type == 'text/html'

    def test_index(self):
        # execute
        responce = todo.index()
        # assert
        assert responce.status_code == 200
        assert responce.content_type == 'text/html'
