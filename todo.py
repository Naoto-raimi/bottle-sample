from bottle import route, run, template, redirect, request
import sqlite3
from dbaccess import dbAccess

# データベースに接続
# db_nameと同名のファイルがなければ，ファイルが作成される
db_name = "mytodo.db"
db_access = dbAccess(db_name)
db_access.init_todo()


@route("/")
def index():
    todo_list = db_access.get_todo_list()
    return template("index", todo_list=todo_list)


@route("/add", method="POST")
def add():
    todo = request.forms.getunicode("todo_list")
    db_access.save_todo(todo)
    return redirect("/")


# @routeデコレータの引数で<xxxx>と書いた部分は引数として関数に引き渡すことができます。
# intは数字のみ受け付けるフィルタ
@route("/delete/<todo_id:int>")
def delete(todo_id):
    db_access.delete_todo(todo_id)
    return redirect("/")


# テスト用のサーバをlocalhost:8080で起動する
run(host="localhost", port=8080, debug=True, reloader=True)
