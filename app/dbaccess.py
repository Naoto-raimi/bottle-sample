import sqlite3


class dbAccess(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def init_todo(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        try:
            # テーブルの作成
            c.execute("DROP TABLE IF EXISTS todo_list")
            c.execute(
                """CREATE TABLE IF NOT EXISTS todo_list(
                    id INTEGER PRIMARY KEY, 
                    todo TEXT)
                """)
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        # conn.commit()を実行しないと，データベースにコマンドが反映されないことに注意
        conn.commit()
        conn.close()

    def get_todo_list(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        select = "select id, todo from todo_list"
        c.execute(select)
        todo_list = []
        for row in c.fetchall():
            todo_list.append({
                "id": row[0],
                "todo": row[1]
            })
        conn.close()
        return todo_list

    def save_todo(self, todo):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        insert = "insert into todo_list(todo) values(?)"
        c.execute(insert, (todo,))  # todoのあとにカンマをつけないとなぜかエラーになる
        conn.commit()
        conn.close()

    def delete_todo(self, todo_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        delete = "delete from todo_list where id=?"
        c.execute(delete, (todo_id,))
        conn.commit()
        conn.close()
