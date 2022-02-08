'''
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/FerterH/django.git
git push -u origin main


 django-admin startproject taskmanager
PS C:\Users\IT-12\PycharmProjects\Django> cd .\taskmanager\
PS C:\Users\IT-12\PycharmProjects\Django\taskmanager> python manage.py runserver

при создании нового приложения (в осовном) командой: python manage.py startapp Название
За тем в папке этого проекта нужно создать файл urls.py

python manage.py makemigrations создать миграции для создания таблицек
python manage.py migrate

python manage.py createsuperuser для создания админского пользователя

зарегистрировать табличку в админе f
rom  .models import Task
admin.site.register(Task)

'''
