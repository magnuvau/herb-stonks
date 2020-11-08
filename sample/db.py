import psycopg2
import time


def connection():
    return psycopg2.connect('dbname=postgres user=postgres')


def insert(name, date, value, trend):
    conn = connection()
    conn.cursor().execute('''INSERT INTO item VALUES('%s', '%s', %d, %d) ON CONFLICT (date) DO NOTHING;''' % (name, date, value, trend))
    conn.commit()
    conn.close()
