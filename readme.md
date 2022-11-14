1. В корне создать файл .env прописать
LOGIN=
PASSWORD=
2. Перейти в папку с проектом
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Запускать
pytest --fax_number="" --fax_count= 