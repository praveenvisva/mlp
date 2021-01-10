import os
import random

import logging
from flask import Flask, jsonify
from healthcheck import HealthCheck

logging.basicConfig(format="%(message)s", level=logging.INFO)
app = Flask(__name__)

logging.info("Ready to take reqeusts")

health = HealthCheck(app, '/hccheck')


def howami():
    return True, "I am alive"


health.add_check(howami)


@app.route('/score', methods=['GET'])
def predict():
    quotes = ["hardwork", "self-discipline", "perserverance"]
    d = {"quote": random.choice(quotes),
         "score": str(random.randint(1, 100))}
    return jsonify(d)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Predictions Application\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5432)))
