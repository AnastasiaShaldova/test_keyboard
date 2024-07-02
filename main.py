from pynput import mouse, keyboard

from logger.logger import logger
from mqtt_broker.message_broker import mqtt_manager
from input_devices.on_keyboard import on_keyboard
from input_devices.on_mouse import on_mouse


if __name__ == '__main__':
    try:
        mqtt_manager.connect()

        """Слушаем нажатия клавиш"""
        with keyboard.Listener(on_press=on_keyboard.on_press, on_release=on_keyboard.on_release) as keyboard_listener, \
                mouse.Listener(on_click=on_mouse.on_click) as mouse_listener:

            keyboard_listener.join()
            mouse_listener.join()

    except Exception as e:
        logger.error(f"Ошибка при работе с MQTT брокером: {str(e)}")
