from prometheus_client import start_http_server, Counter
import time

if __name__ == '__main__':

    c = Counter('my_failures', 'Description of counter')

    start_http_server(8000)

    while True:
        time.sleep(1)
        c.inc()
