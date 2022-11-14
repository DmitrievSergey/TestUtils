1. В корне создать файл .env прописать
* LOGIN=your login
* PASSWORD=your password
2. В терминале Перейти в папку с проектом и выполнить 3 команды 
- python3 -m venv venv
- source venv/bin/activate
- Если pip не установлен или не последней версии, то обновить его
- pip install -r requirements.txt
3. В хроме посмотреть версию браузера и скачать соответствующий 
chromedriver. Распаковать в директорию Downloads/drivers/
4. Если версия хрома отличается от 106.0 в пункте 5 добавить параметр
--bversion=""
5. Запускать
pytest --fax_number="" --fax_count= 