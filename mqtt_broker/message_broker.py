import os

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

from logger.logger import logger


class MQTTManager:
    def __init__(self, broker, port, keepalive_interval):
        self.broker = broker
        self.port = port
        self.keepalive_interval = keepalive_interval
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log

    def connect(self):
        self.client.connect(self.broker, self.port, self.keepalive_interval)
        self.client.loop_start()
        logger.info('MQTT-клиент подключен к брокеру')

    def disconnect(self):
        self.client.disconnect()
        logger.info('MQTT-клиент отключен')

    def send_message(self, topic, message):
        self.client.publish(topic, message)
        logger.info(f'Опубликованное сообщение в теме: {topic}')

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Успешное подключение к MQTT брокеру.")
        else:
            logger.error(f"Не удалось подключиться к MQTT брокеру. Код возврата: {rc}")

    @staticmethod
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            logger.warning("Потеряно соединение с MQTT брокером.")

    @staticmethod
    def on_log(client, userdata, level, buf):
        logger.debug(f"MQTT log: {buf}")


load_dotenv()

MQTT_BROKER = os.environ.get("MQTT_BROKER")
MQTT_PORT = int(os.environ.get("MQTT_PORT"))
MQTT_KEEPALIVE_INTERVAL = int(os.environ.get("MQTT_KEEPALIVE_INTERVAL"))

mqtt_manager = MQTTManager(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
