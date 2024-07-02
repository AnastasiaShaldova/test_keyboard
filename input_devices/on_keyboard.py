from mqtt_broker.message_broker import mqtt_manager


class Keyboard:
    def __init__(self):
        self.pressed_keys = set()
        self.mqtt_manager = mqtt_manager

    def on_press(self, key):
        """Функция для проверки нажатия клавиши и добавления ее во множество"""
        if hasattr(key, 'vk'):
            if key.vk not in self.pressed_keys:
                self.pressed_keys.add(key.vk)
                self.mqtt_manager.send_message(topic=f'keyboard/{key.vk}', message='1')
        else:
            if key not in self.pressed_keys:
                self.pressed_keys.add(key)
                self.mqtt_manager.send_message(topic=f'keyboard/{str(key).split(".")[1]}', message='1')

    def on_release(self, key):
        """Функция для проверки, что клавиша была ранее нажата и удаления из множества"""
        if hasattr(key, 'vk'):
            if key.vk in self.pressed_keys:
                self.pressed_keys.remove(key.vk)
                self.mqtt_manager.send_message(topic=f'keyboard/{key.vk}', message='0')
        else:
            if key in self.pressed_keys:
                self.pressed_keys.remove(key)
                self.mqtt_manager.send_message(topic=f'keyboard/{str(key).split(".")[1]}', message='0')


on_keyboard = Keyboard()
