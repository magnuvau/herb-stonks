from prometheus_client import start_http_server, Gauge, Counter
from multiprocessing import Process
import random
import time

# Create a metric to track time spent and requests made.
#REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
#@REQUEST_TIME.time()
#def process_request():
#    """A dummy function that takes some time."""
#    while True:
#        time.sleep(random.random())

if __name__ == '__main__':

    c = Counter('my_failures', 'Description of counter')

    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.

#    p = Process(target=process_request)
#    p.start()

    while True:
        time.sleep(1)
        c.inc()

