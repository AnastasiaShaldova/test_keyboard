from mqtt_broker.message_broker import mqtt_manager


class Mouse:
    def __init__(self):
        self.pressed_mouse_buttons = set()
        self.mqtt_manager = mqtt_manager

    def on_click(self, x, y, button, pressed):
        """Функция для проверки, что кнопка мыши была нажата или отпущена"""

        if pressed:
            if button not in self.pressed_mouse_buttons:
                self.pressed_mouse_buttons.add(button)
                self.mqtt_manager.send_message(topic=f'mouse/{button.name}', message='1')
        else:
            if button in self.pressed_mouse_buttons:
                self.pressed_mouse_buttons.remove(button)
                self.mqtt_manager.send_message(topic=f'mouse/{button.name}', message='0')


on_mouse = Mouse()
