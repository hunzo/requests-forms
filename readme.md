# requests-forms
## start dev
- create venv
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- start app
```
source setenv.sh
python manage.py runserver
```
## start containter
```
docker-compose down -v
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```