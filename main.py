import subprocess

import keyboard
from pynput import mouse
import paho.mqtt.client as mqtt

# Создаем клиент MQTT
client = mqtt.Client()

# Подключаемся к брокеру
client.connect("localhost", 1883)


def publish_message(topic, message):
    client.publish(topic, message)


# Функция для обработки событий клавиатуры
def on_key_event(event):
    print(event)
    if event.event_type == keyboard.KEY_DOWN:
        key_pressed = event.name
        if key_pressed in ['backspace', 'ctrl', 'alt', 'j', 'b']:
            topic = "topic1"
            message = "good job"
            print(message)
            publish_message(topic, message)
        if key_pressed in ['1', '2', '3', '4', '5']:
            topic = "topic2"
            message = "WoW"
            publish_message(topic, message)
            print(message)
        if key_pressed in ['p', 'q', 'r', 's', 'n']:
            topic = "topic3"
            message = f"Hello '{key_pressed}'!"
            publish_message(topic, message)
            print(message)


# Функция для обработки событий мыши
def on_mouse_event(x, y, button, pressed):
    if pressed:
        button_pressed = button.name
        if button_pressed in ['left', 'right', 'up', 'down']:
            topic = "mouse"
            message = f"Нажата кнопка: {button_pressed}"
            publish_message(topic, message)
            print(message)


# Регистрация обработчиков событий клавиатуры и мыши
keyboard.on_press(on_key_event)
mouse.Listener(on_click=on_mouse_event).start()

# 'esc' для остановки скрипта
keyboard.wait("esc")

