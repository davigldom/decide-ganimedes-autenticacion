% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && python manage.py makemigrations && python manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('"'"'admin@decide.com'"'"', '"'"'practica'"'"')" | python3 ./manage.py shell'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'