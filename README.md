# Industrial Forging Press Monitoring Dashboard

A prototype exploring AI-assisted predictive maintenance using Gemma 4, AlloyDB Omni, PostgreSQL and a Flask-based monitoring dashboard.

## Project Overview

Industrial forging presses operate under demanding conditions. Changes in hydraulic pressure, oil temperature and vibration can indicate potential equipment problems.

This project explores how machine telemetry can be stored, analysed and presented to support early identification of abnormal operating conditions.

The work has two parts:

1. A Gemma 4 and AlloyDB Omni experiment using SQL-based AI inference.
2. A Flask dashboard that simulates sensor readings and displays rule-based safety alerts.

## Technologies Used

- Python
- Flask
- HTML, CSS and JavaScript
- Chart.js
- Docker
- PostgreSQL
- AlloyDB Omni
- Gemma 4 (via Ollama)
- SQL
- Google Cloud Shell

## Part 1: Gemma 4 + AlloyDB Omni Experiment

The AI and database experiment included:

- Running Gemma 4 (gemma4:e2b) locally using Ollama.
- Running AlloyDB Omni in a Docker container.
- Configuring the Google ML integration extension.
- Registering the Gemma model with AlloyDB Omni.
- Creating a forging press telemetry table.
- Inserting 1,000 simulated sensor records, including abnormal readings.
- Using SQL queries and Gemma inference to analyse abnormal pressure and vibration readings.

The experiment demonstrated how a locally hosted language model can be called through database-integrated ML functions.

## Part 2: Flask Monitoring Dashboard

The dashboard provides a simulated monitoring interface for a 1500T forging press.

### Features

- Simulated hydraulic pressure, oil temperature and vibration readings.
- Normal operation and failure simulation controls.
- Live dashboard updates.
- Sensor trend visualisation.
- Rule-based warning and critical alerts.
- Alert logging when severity changes.
- Recovery confirmation when readings return to normal.

### Alert Thresholds

| Severity | Condition |
|---|---|
| Warning | Pressure below 260 bar or vibration above 4.5 mm/s |
| Critical | Pressure below 240 bar or vibration above 10 mm/s |
| Normal | Neither warning nor critical condition is present |

These thresholds are demonstration values, not validated industrial safety limits.

## Running the Dashboard

### Prerequisites
- Python 3
- Flask

### Install dependencies
```bash
pip install Flask
```

### Start the application
```bash
python app.py
```

Open the dashboard using Cloud Shell Web Preview on port 8080.

## Important Project Notes
- Dashboard sensor readings are simulated; no physical machine is connected.
- Dashboard alerts use Python rule-based logic, not live Gemma inference.
- Gemma 4 and AlloyDB Omni were tested separately.
- The current Flask dashboard does not require AlloyDB Omni to be running.
- This is a learning prototype, not a production-ready safety system.

## Future Improvements
- Connect the dashboard to a persistent telemetry database.
- Integrate AI-generated analysis into the dashboard.
- Test with realistic industrial sensor datasets.
- Add historical trend analysis and predictive maintenance recommendations.
- Explore secure deployment patterns for regulated environments.
