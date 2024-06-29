from pynput import mouse, keyboard
import paho.mqtt.client as mqtt

# Создаем клиент MQTT
client = mqtt.Client()

# Подключаемся к брокеру
client.connect("localhost", 1883)


# Отправка сообщения в топик
def topic_keyboard(message):
    client.publish("keyboard", message)


def topic_mouse(message):
    client.publish("mouse", message)


# Тут храним нажатые клавиши
pressed_keys = {}
# Флаг для выполнения скрипта
running = True


# Функция для замены русских букв на английские
def replace_russian_with_english(letter):
    keyboard_letters = {
        "й": "q", "ц": "w", "у": "e", "к": "r", "е": "t", "н": "y", "г": "u", "ш": "i", "щ": "o", "з": "p", "х": "[",
        "ъ": "]", "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "р": "h", "о": "j", "л": "k", "д": "l", "ж": ";",
        "э": "'", "я": "z", "ч": "x", "с": "c", "м": "v", "и": "b", "т": "n", "ь": "m", "б": ",", "ю": "."
    }
    return keyboard_letters.get(letter, letter)


# Функция для обработки событий клавиатуры (при нажатой клавише)
def on_key_pressed(key):
    try:
        button_pressed = replace_russian_with_english(key.char)
    except AttributeError:
        button_pressed = str(key).split(".")[1]
    if button_pressed not in pressed_keys or not pressed_keys[button_pressed]:
        message = f"{button_pressed} = 1"
        topic_keyboard(message)
        pressed_keys[button_pressed] = True


# Функция для обработки событий клавиатуры (при отпущенной клавише)
def on_key_released(key):
    try:
        button_released = replace_russian_with_english(key.char)
    except AttributeError:
        button_released = str(key).split(".")[1]
    message = f"{button_released} = 0"
    topic_keyboard(message)
    pressed_keys[button_released] = False


# Функция для обработки событий мыши
def on_mouse_event(x, y, button, pressed):
    if pressed:
        button_pressed = button.name
        message = f"{button_pressed} = 1"
        topic_mouse(message)
    else:
        button_released = button.name
        message = f"{button_released} = 0"
        topic_mouse(message)


def stop_script():
    global running
    running = False


# Регистрация обработчиков событий клавиатуры и мыши
listener_key = keyboard.Listener(on_press=on_key_pressed, on_release=on_key_released).start()
listener_mouse = mouse.Listener(on_click=on_mouse_event).start()

# Постоянное выполнение скрипта
while running:
    pass
