import time
import board
import adafruit_dht
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "PASTE_YOUR_AZURE_DEVICE_CONNECTION_STRING_HERE"

dht_sensor = adafruit_dht.DHT11(board.D4)
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("Connecting to Azure IoT Hub...")
client.connect()
print("Connected. Starting telemetry loop...")

try:
    while True:
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity

            if temperature is not None and humidity is not None:
                payload = {
                    "temperature": temperature,
                    "humidity": humidity
                }
                msg = Message(str(payload))
                print("Sending:", payload)
                client.send_message(msg)
            else:
                print("Sensor returned None. Skipping.")

        except RuntimeError as error:
            print("Sensor error:", error.args[0])
        except Exception as fatal:
            print("Fatal error:", fatal)
            break

        time.sleep(10)

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    client.disconnect()
    print("Disconnected from Azure.")
