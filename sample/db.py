import psycopg2
import time


def connection():
    connection = None
    while connection is None:
        try:
            connection = psycopg2.connect('dbname=postgres user=postgres')
        except psycopg2.OperationalError:
            print("Failed to connect to postgres...")
            time.sleep(2)
    return connection


def insert(name, date, value):
    conn = connection()
    conn.cursor().execute('''INSERT INTO item VALUES('%s', '%s', %d) ON CONFLICT (name, date) DO NOTHING;''' % (name, date, value))
    conn.commit()
    conn.close()
