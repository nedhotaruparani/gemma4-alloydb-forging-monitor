import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Machine simulation state
machine_state = 'normal'
current_pressure = 280.0
current_temp = 42.0
current_vib = 1.8


@app.route('/')
def index():
    return render_template('dashboard.html')


@app.route('/api/control', methods=['POST'])
def control():
    global machine_state

    data = request.json or {}
    mode = data.get('mode', 'normal')

    if mode not in ('normal', 'anomaly'):
        return jsonify({"status": "error", "message": "Invalid mode"}), 400

    machine_state = mode
    return jsonify({"status": "success", "mode": machine_state})


@app.route('/api/stream')
def stream():
    global current_pressure, current_temp, current_vib, machine_state

    # Generate normal or abnormal sensor readings
    if machine_state == 'normal':
        current_pressure = (
            current_pressure * 0.9
            + 280.0 * 0.1
            + random.uniform(-2, 2)
        )
        current_temp = (
            current_temp * 0.9
            + 42.0 * 0.1
            + random.uniform(-0.5, 0.5)
        )
        current_vib = (
            current_vib * 0.9
            + 1.8 * 0.1
            + random.uniform(-0.1, 0.1)
        )

    else:
        current_pressure -= random.uniform(2, 6)
        current_temp += random.uniform(1, 3)
        current_vib += random.uniform(0.5, 1.8)

    # Prevent negative sensor readings
    current_pressure = max(0, current_pressure)
    current_temp = max(0, current_temp)
    current_vib = max(0, current_vib)

    # Rule-based safety alert
    insight = None

    if current_pressure < 255 or current_vib > 4.5:
        issues = []

        if current_pressure < 255:
            issues.append(
                f"Low hydraulic pressure: {current_pressure:.1f} bar"
            )

        if current_vib > 4.5:
            issues.append(
                f"High vibration: {current_vib:.2f} mm/s"
            )

        insight = (
            "CRITICAL SAFETY ALERT: "
            + "; ".join(issues)
            + ". Inspect the machine immediately."
        )

    return jsonify({
        "pressure": current_pressure,
        "temperature": current_temp,
        "vibration": current_vib,
        "state": machine_state,
        "insight": insight
    })


if __name__ == '__main__':
    print("Starting Forging Press Safety Dashboard on http://0.0.0.0:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)
PY
