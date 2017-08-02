#!/usr/bin/python
# -*- coding:utf-8 -*-

from threading import Timer

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def api():
    data = {
        'foo': 'hello',
        'method': 'world'
    }
    response = jsonify(data)
    response.status_code = 200
    return response


class Scheduler(object):
    def __init__(self, sleep_time, function):
        self.sleep_time = sleep_time
        self.function = function
        self._t = None

    def start(self):
        if self._t is None:
            self._t = Timer(self.sleep_time, self._run)
            self._t.start()
        else:
            raise Exception("this timer is already running")

    def _run(self):
        self.function()
        self._t = Timer(self.sleep_time, self._run)
        self._t.start()

    def stop(self):
        if self._t is not None:
            self._t.cancel()
            self._t = None


def query_db():
    print("IM QUERYING A DB")


if __name__ == "__main__":
    scheduler = Scheduler(5, query_db)
    scheduler.start()
    app.run(host='127.0.0.1', debug=False, port=1337)
    scheduler.stop()
