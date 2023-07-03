# osetrit exception pro flask

import prometheus_client, time, os
from logging_module import setup_logging
from prometheus_client.core import CollectorRegistry
from prometheus_client import Counter, Histogram

#setup logging
logger_name = os.path.basename(__file__).split('.')[0]
logger = setup_logging(logger_name)


# create graphs variables for metrics
_INF = float("inf")
graphs = {}
graphs['counter'] = Counter('my_counter', 'The total number of requests processed')
graphs['histogram'] = Histogram('my_histogram', 'Histogram for the duration in seconds', buckets=(1, 2, 5, 6, 10, _INF))


# app = Flask(__name__)

# # create route for ticker metrics
# @app.route('/')
# def index():
#     return 'app is running'

# @app.route('/hello')
# def hello():
#     start = time.time()
#     graphs['counter'].inc()

#     time.sleep(0.2)
#     end = time.time()
#     graphs['histogram'].observe(end - start)
#     logger.info("aaa")
#     return 'Hello, World!'

# @app.route('/metrics')
# def metrics():
#     res = []
#     for key, value in graphs.items():
#         res.append(prometheus_client.generate_latest(value))
#     return Response(res, mimetype='text/plain')




# run the application
if __name__ == '__main__':
# following is for dev server only!!!
    app.run(debug=True)

#  run the application in production mode
    #  app.run()


