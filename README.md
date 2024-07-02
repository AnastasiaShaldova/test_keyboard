# test_keyboard

### Запуск проекта 
1. Склонировать репозиторий
```bash
git clone git@github.com:AnastasiaShaldova/test_keyboard.git
```
2. В системе Linux перейти в режим суперпользователя
```bash
sudo su
```
3. Создать виртуальное окружение 
```bash
python3 -m venv venv
```
4. Установить пакеты из requirements.txt
```bash
pip install -r requirements.txt
```
5. Скопировать переменные из файла .env.example в .env файл который должен находится в корне проекта. Прописать необходимые данные для подключения к MQTT. 
6. Создаем файл в systemd и копируем туда из файла репозитория test-keyboard.service (заменить пути до виртуального окружения и исполняемго файла)
```bash
sudo vim /etc/systemd/system/test_keyboard.service
```
7. Перезагрузите systemd, чтобы он обнаружил новый юнит-файл
```bash 
sudo systemctl daemon-reload
```
8. Запустите сервис
```bash
sudo systemctl start test_keyboard
```
9. Настройте автозапуск сервиса при загрузке
```bash
sudo systemctl enable test_keyboard
```
