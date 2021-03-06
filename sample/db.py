import psycopg2
import time

def connection():
    connection = None
    while connection is None:
        try:
            connection = psycopg2.connect(
                host='172.20.128.2',
                database='postgres',
                user='postgres',
                password='postgres'
            )
        except psycopg2.OperationalError:
            print("Failed to connect to postgres...")
            time.sleep(2)
    return connection


def insert_average(name, date, value):
    conn = connection()
    conn.cursor().execute('''INSERT INTO average VALUES('%s', '%s', %d) ON CONFLICT (name, date) DO NOTHING;''' % (name, date, value))
    conn.commit()
    conn.close()
    
def count_average(name):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(1) FROM average WHERE name = \'%s\';''' % name)
    count = cursor.fetchone()[0]
    conn.close()
    return count
