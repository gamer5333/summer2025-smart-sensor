# Azure-Connected Smart Sensor with Raspberry Pi + DHT11

This project demonstrates how to collect real-world sensor data from a DHT11 temperature/humidity sensor using a Raspberry Pi and send it securely to **Azure IoT Hub** for cloud processing and visualization.

---

## Project Overview

- **Hardware:** Raspberry Pi 4B + DHT11 sensor
- **Language:** Python
- **Cloud Platform:** Microsoft Azure IoT Hub
- **Protocols:** MQTT (via Azure SDK)
- **Use Case:** Real-time environmental telemetry for dashboards, alerts, or automation

---

## Hardware Components

| Component      | Description                           |
|----------------|---------------------------------------|
| Raspberry Pi   | Model 3B+, 4, or Zero 2 W              |
| DHT11 Sensor   | Temp & Humidity Digital Sensor         |
| Jumper Wires   | Female-to-female recommended           |
| Resistor       | 10kΩ between VCC and data (pull-up)    |
| Breadboard     | For prototyping                        |

---

## Wiring Guide

| DHT11 Pin | Connects to Raspberry Pi |
|-----------|--------------------------|
| VCC       | 5V (Physical pin 2 or 4) |
| DATA      | GPIO4 (Physical pin 7)   |
| GND       | GND (e.g., pin 6)        |

Use a **10kΩ resistor** between VCC and Data for stability.

---
## Real-Time Telemetry Chart Integration
This project includes a real-time dashboard that visualizes temperature and humidity data from IoT devices.

## Features
- Live data updates via WebSocket
- Support for multiple devices
- Interactive chart using Chart.js
- Automatic parsing of telemetry payloads, including buffer decoding

## Implementation Details
- The chart-device-data.js script handles WebSocket messages, decodes buffer payloads, and updates the chart accordingly.
- Telemetry payloads are decoded from buffers to JSON strings, accommodating single-quoted keys.
- The chart updates in real-time as new data arrives.

## File Overview
- chart-device-data.js: Handles WebSocket communication and chart updates.
- index.html: Contains the HTML structure for the dashboard.
- styles.css: Styles the dashboard components.

## Live Demo
To see the dashboard in action, run the application and navigate to http://localhost:3000.
![sensor-chart](https://github.com/user-attachments/assets/50ea7bb9-dfa8-42c2-b72a-576b6094d486)

---
## Software Setup

1. **Clone this repo:**
   ```bash
   git clone https://github.com/gamer5333/summer2025-smart-sensor.git
   cd summer2025-smart-sensor
