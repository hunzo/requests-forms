# requests-forms
## start dev
```
source setenv.sh
```
## start conainter
```
docker-compose down -v
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```