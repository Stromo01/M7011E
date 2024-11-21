import sqlite3
import mysql.connector

# Simple ORM class
class SimpleORM:
    def __init__(self, db_type='mysql', database='M7011E', db_user='sqldatabas', password='LTU123', host='34.88.71.249'):
        self.db_type = db_type
        if db_type == 'sqlite':
            self.connection = sqlite3.connect(database)
        elif db_type == 'mysql':
            self.connection = mysql.connector.connect(
                host=host,
                user=db_user,
                password=password,
                database=database
            )
        else:
            raise ValueError("Unsupported database type. Use 'sqlite' or 'mysql'.")
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        if self.db_type == 'sqlite':
            query = query.replace("%s", "?")
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            return self.cursor.fetchall()
        else:
            self.connection.commit()
            return self.cursor.lastrowid

    def join(self, table1, table2, on, select="*", conditions=None):
        query = f"SELECT {select} FROM {table1} JOIN {table2} ON {on}"
        if conditions:
            placeholders = ' AND '.join([f"{key} = %s" for key in conditions])
            values = tuple(conditions.values())
            if self.db_type == 'sqlite':
                placeholders = placeholders.replace("%s", "?")
            query += f" WHERE {placeholders}"
            return self.execute(query, values)
        return self.execute(query)

    def close(self):
        self.cursor.close()
        self.connection.close()

# User class
class User:
    _table_name = 'users'

    def __init__(self, db_orm, name=None, db_id=None):
        self.orm = db_orm
        self.id = db_id
        self.name = name

    def save(self):
        if self.id is None:
            self.id = self.orm.execute(
                f"INSERT INTO {self._table_name} (name) VALUES (%s)",
                (self.name,)
            )
        else:
            self.orm.execute(
                f"UPDATE {self._table_name} SET name = %s WHERE id = %s",
                (self.name, self.id)
            )

    @classmethod
    def get(cls, db_orm, db_id):
        users = db_orm.execute(
            f"SELECT * FROM {cls._table_name} WHERE id = %s",
            (db_id,)
        )
        if users:
            user_data = users[0]
            return cls(db_orm, name=user_data[1], db_id=user_data[0])
        return None

    @classmethod
    def all(cls, db_orm):
        users = db_orm.execute(f"SELECT * FROM {cls._table_name}")
        return [cls(db_orm, name=user_data[1], db_id=user_data[0]) for user_data in users]

    def delete(self):
        self.orm.execute(
            f"DELETE FROM {self._table_name} WHERE id = %s",
            (self.id,)
        )
        self.id = None

    def get_posts(self):
        return [Post(self.orm, title=db_post[1], content=db_post[2], user_id=db_post[3], db_id=db_post[0])
                for db_post in
                self.orm.join(Post._table_name, User._table_name, "users.id = posts.user_id", select="posts.*",
                              conditions={"users.id": self.id})]

# Post class
class Post:
    _table_name = 'posts'

    def __init__(self, db_orm, title=None, content=None, user_id=None, db_id=None):
        self.orm = db_orm
        self.id = db_id
        self.title = title
        self.content = content
        self.user_id = user_id

    def save(self):
        if self.id is None:
            self.id = self.orm.execute(
                f"INSERT INTO {self._table_name} (title, content, user_id) VALUES (%s, %s, %s)",
                (self.title, self.content, self.user_id)
            )
        else:
            self.orm.execute(
                f"UPDATE {self._table_name} SET title = %s, content = %s WHERE id = %s",
                (self.title, self.content, self.id)
            )

    @classmethod
    def get(cls, db_orm, db_id):
        posts = db_orm.execute(
            f"SELECT * FROM {cls._table_name} WHERE id = %s",
            (db_id,)
        )
        if posts:
            post_data = posts[0]
            return cls(db_orm, title=post_data[1], content=post_data[2], user_id=post_data[3], db_id=post_data[0])
        return None

    @classmethod
    def all(cls, db_orm):
        posts = db_orm.execute(f"SELECT * FROM {cls._table_name}")
        return [cls(db_orm, title=post_data[1], content=post_data[2], user_id=post_data[3], db_id=post_data[0]) for
                post_data in posts]

    def delete(self):
        self.orm.execute(
            f"DELETE FROM {self._table_name} WHERE id = %s",
            (self.id,)
        )
        self.id = None

    @property
    def table_name(self):
        return self._table_name

# Example usage
if __name__ == "__main__":
    orm = SimpleORM(db_type='mysql', database='M7011E')

    # Create tables
    orm.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))")
    orm.execute(
        "CREATE TABLE IF NOT EXISTS posts (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), content VARCHAR(255), user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))")

    # Create a new user and a post
    user = User(orm, name="John Doe")
    user.save()

    post = Post(orm, title="My First Post", content="Hello, world!", user_id=user.id)
    post.save()

    # Fetch all posts for the user
    user_posts = user.get_posts()
    for post in user_posts:
        print(f"Post: {post.title}, Content: {post.content}")

    orm.close()