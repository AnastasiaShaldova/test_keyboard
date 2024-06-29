import Xlib
import Xlib.display

from pynput import mouse, keyboard
import paho.mqtt.client as mqtt

# Создаем клиент MQTT
client = mqtt.Client()

# Подключаемся к брокеру
client.connect("localhost", 1883)


# Отправка сообщения в топик
def publish_message(topic, message):
    client.publish(topic, message)


# Тут храним нажатые клавиши
pressed_keys = {}
# Флаг для выполнения скрипта
running = True


# Функция для получения английской раскладки клавиатуры
def get_english_key(key): 
    display = Xlib.display.Display()
    keysym = display.keycode_to_keysym(key, 0)
    if keysym: 
        return Xlib.XK.keysym_to_string(keysym)
    else: 
        return None


# Функция для обработки событий клавиатуры (при нажатой клавише)
def on_key_pressed(key):
    try:
        button_pressed = key.char
    except AttributeError:
        button_pressed = str(key).split(".")[1]
    topic = "keyboard"
    if button_pressed not in pressed_keys or not pressed_keys[button_pressed]:
        message = f"{button_pressed} = 1"
        publish_message(topic, message)
        pressed_keys[button_pressed] = True
        print(message)


# Функция для обработки событий клавиатуры (при отпущенной клавише)
def on_key_released(key):
    try:
        button_released = key.char
    except AttributeError:
        button_released = str(key).split(".")[1]
    topic = "keyboard"
    message = f"{button_released} = 0"
    publish_message(topic, message)
    pressed_keys[button_released] = False
    print(message)


# Функция для обработки событий мыши
def on_mouse_event(x, y, button, pressed):
    if pressed:
        button_pressed = button.name
        topic = "mouse"
        message = f"{button_pressed} = 1"
        publish_message(topic, message)
        print(message)
    else:
        button_released = button.name
        topic = "mouse"
        message = f"{button_released} = 0"
        publish_message(topic, message)
        print(message)


def stop_script():
    global running
    print("Остановка скрипта")
    running = False


# Регистрация обработчиков событий клавиатуры и мыши
listener_key = keyboard.Listener(on_press=on_key_pressed, on_release=on_key_released).start()
listener_mouse = mouse.Listener(on_click=on_mouse_event).start()

# Постоянное выполнение скрипта
while running:
    pass
