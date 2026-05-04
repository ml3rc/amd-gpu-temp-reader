from flask import Flask, jsonify
import glob

app = Flask(__name__)

def get_gpu_temp():
    paths = glob.glob("/sys/class/drm/card*/device/hwmon/hwmon*/temp1_input")
    temps = {}

    for path in paths:
        try:
            card = path.split("/")[4]
            with open(path) as f:
                temps[card] = int(f.read().strip()) / 1000.0
        except:
            pass

    return temps

@app.route("/gpu-temp")
def gpu_temp():
    return jsonify(get_gpu_temp())

app.run(host="0.0.0.0", port=5000)