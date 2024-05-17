from flask import Flask, jsonify
import psutil
import time
import os

app = Flask(__name__)


def get_sensor_data():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    # Obtendo a temperatura da CPU
    cpu_temperature = get_cpu_temperature()
    
    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'disk_usage': disk_usage,
        'cpu_temperature': cpu_temperature
    }

def get_cpu_temperature():
    if os.path.exists('/sys/class/thermal/thermal_zone0/temp'):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000.0
        return temp
    else:
        return None

@app.route('/sensor', methods=['GET'])
def sensor_data():
    data = get_sensor_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
