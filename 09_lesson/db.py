from sqlalchemy import create_engine, text


class StudentGroupTable:
    __scripts = {
        "select_all": text("SELECT * FROM group_student"),
        "insert_new": text("INSERT INTO group_student(user_id, group_id) VALUES (:user_id, :group_id) RETURNING user_id"),
        "update_group": text("UPDATE group_student SET group_id = :group_id WHERE user_id = :user_id"),
        "delete_by_id": text("DELETE FROM group_student WHERE user_id = :user_id"),
        "select_by_id": text("SELECT * FROM group_student WHERE user_id = :user_id"),
        "get_max_id": text("SELECT MAX(user_id) FROM group_student")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_all(self):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["select_all"])
        rows = result.fetchall()
        conn.close()
        return rows

    def create(self, user_id, group_id):
        conn = self.db.connect()
        result = conn.execute(
            self.__scripts["insert_new"], 
            {"user_id": user_id, "group_id": group_id}
        )
        conn.commit()
        new_id = result.fetchone()[0]
        conn.close()
        return new_id

    def update(self, user_id, new_group_id):
        conn = self.db.connect()
        conn.execute(
            self.__scripts["update_group"],
            {"user_id": user_id, "group_id": new_group_id}
        )
        conn.commit()
        conn.close()

    def delete(self, user_id):
        conn = self.db.connect()
        conn.execute(
            self.__scripts["delete_by_id"],
            {"user_id": user_id}
        )
        conn.commit()
        conn.close()

    def get_by_id(self, user_id):
        conn = self.db.connect()
        result = conn.execute(
            self.__scripts["select_by_id"],
            {"user_id": user_id}
        )
        row = result.fetchone()
        conn.close()
        return row

    def get_max_id(self):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.fetchone()[0]
        conn.close()
        return max_id if max_id is not None else 0
