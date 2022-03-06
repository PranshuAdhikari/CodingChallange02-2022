import sqlite3
from sqlite3 import Error

database = "pythonsqlite.db"

sql_create_webpage_table = """ CREATE TABLE IF NOT EXISTS webpage (
                                    url text,
                                    html text
                                ); """

sql_create_tags_table = """CREATE TABLE IF NOT EXISTS tags (
                                url text,
                                nodes text,
                                parent_tags text,
                                left_sibling_tags text,
                                right_sibling_tags text
                            );"""


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, timeout=10)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def get_connection():
    """ get connection to db and create table
        :return: Connection object or None
        """

    # create a database connection

    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create tags table
        create_table(conn, sql_create_webpage_table)

        # create webpage table
        create_table(conn, sql_create_tags_table)
    else:
        print("Error! cannot create the database connection.")

    return conn


def insert_data(url, html, nodes, parent_tags, left_sibling_tags, right_sibling_tags):
    """  data insertion to sqllite db in webpage and tags table.
    :param url: source url string
    :param html: html string
    :param nodes: parent tags list as string
    :param parent_tags: node tags list as string
    :param left_sibling_tags: left_sibling_tags list as string
    :param right_sibling_tags: right_sibling_tags list as string
    :return:
            """

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO webpage(url, html ) VALUES (?,? )'
            'Except SELECT url, html from webpage where url = ? and html = ?',
            (url, html, url, html))

        cursor.execute(
            "INSERT INTO tags(url, nodes, parent_tags, left_sibling_tags, right_sibling_tags ) VALUES (?, ?, ?, ?, ?)"
            "Except SELECT url, nodes, parent_tags, left_sibling_tags, right_sibling_tags from tags "
            "where url = ? and nodes = ? and parent_tags= ? and left_sibling_tags = ? and right_sibling_tags= ?",
            (url, nodes, parent_tags, left_sibling_tags, right_sibling_tags,
             url, nodes, parent_tags, left_sibling_tags, right_sibling_tags))

        conn.commit()
        print("Records inserted !")

    except Error as e:
        print(e)

    # Closing the connection
    conn.close()

