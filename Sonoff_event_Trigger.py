from flask import Flask
import requests

app = Flask(__name__)


@app.route('/sonoff_ifttt', methods=['POST'])
def trigger_ifttt():
    requests.post("https://maker.ifttt.com/trigger/sonoff turn on/json/with/key/bpnlqKFsXiiT9g-u-iBU0f")
    return "Done", 201


if __name__ == '__main__':
    app.run()
