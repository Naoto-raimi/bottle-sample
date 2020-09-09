from bottle import Bottle, route, run, template, redirect, request, TEMPLATE_PATH
import sqlite3

try:
    from app.dbaccess import dbAccess
except ImportError:
    from dbaccess import dbAccess


TEMPLATE_PATH.append("./app/template")

# データベースに接続
# db_nameと同名のファイルがなければ，ファイルが作成される
db_name = "mytodo.db"
db_access = dbAccess(db_name)
db_access.init_todo()

app = Bottle()


@app.route("/")
def index():
    todo_list = db_access.get_todo_list()
    return template('index.html', todo_list=todo_list)


@app.route("/add", method="POST")
def add():
    todo = request.forms.getunicode("todo_list")
    db_access.save_todo(todo)
    return redirect("/")


# @routeデコレータの引数で<xxxx>と書いた部分は引数として関数に引き渡すことができます。
# intは数字のみ受け付けるフィルタ
@app.route("/delete/<todo_id:int>")
def delete(todo_id):
    db_access.delete_todo(todo_id)
    return redirect("/")


# テスト用のサーバをlocalhost:8080で起動する
# run(app=app, host="localhost", port=8080, debug=True, reloader=True)
run(app=app, host='0.0.0.0', port=3031, debug=True, reloader=True)
