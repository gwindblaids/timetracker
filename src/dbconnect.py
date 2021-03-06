import sqlite3


class Database:
    def __init__(self, dbname='time_tracker.db'):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()
        if not self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall():
            self.create_tables()
        self.user_id = 1

    def create_user(self, first_name, last_name, image_path):
        sql = "INSERT INTO users VALUES({}, {}, {})".format(first_name, last_name, image_path)
        self.cursor.execute(sql)
        self.connection.commit()
        return True

    def create_tables(self):
        """Create tables in database"""
        self.cursor.execute("""CREATE TABLE users
                          (first_name TEXT NOT NULL, last_name TEXT NOT NULL, profile_photo TEXT)""")
        self.cursor.execute("""CREATE TABLE tracker
        (time_start timestamp NOT NULL, time_end timestamp NOT NULL, text_track TEXT, user_id INTEGER NOT NULL, FOREIGN KEY
         (user_id) REFERENCES users(rowid) )""")
        self.connection.commit()

    @property
    def users_list(self):
        sql = """select rowid, first_name || " " || last_name, profile_photo from users;"""
        result = self.cursor.execute(sql)
        return result.fetchall()

    @property
    def get_track_list(self):
        """getting info about track"""
        sql = """select * from tracker where user_id={};""".format(self.user_id)
        result = self.cursor.execute(sql)
        return result.fetchall()

    def create_track(self, time_start, time_end, text_track):
        sql = """INSERT INTO tracker
        VALUES ('{}', '{}', '{}', {})""".format(time_start, time_end, text_track, self.user_id)
        self.cursor.execute(sql)
        self.connection.commit()


if __name__ == '__main__':
    cn = Database()
