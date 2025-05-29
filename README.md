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

## ⚙Wiring Guide

| DHT11 Pin | Connects to Raspberry Pi |
|-----------|--------------------------|
| VCC       | 5V (Physical pin 2 or 4) |
| DATA      | GPIO4 (Physical pin 7)   |
| GND       | GND (e.g., pin 6)        |

Use a **10kΩ resistor** between VCC and Data for stability.

---

## 💻 Software Setup

1. **Clone this repo:**
   ```bash
   git clone https://github.com/gamer5333/summer2025-smart-sensor.git
   cd summer2025-smart-sensor
