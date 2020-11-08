import psycopg2
import time


def connection():
    return psycopg2.connect('dbname=postgres user=postgres')


def insert(name, price, date):
    conn = connection()
    conn.cursor().execute('INSERT INTO item VALUES(\'%s\', %d, \'%s\')' % (name, price, date))
    conn.commit()
    conn.close()
