#!/Users/devin/.virtualenvs/WestOfRome/bin/python

from fabric.api import local, lcd

def prep():
    local('python manage.py test blog')
    #local('git add -p && git commit -m "FabTestCommit"')

def deploy():
    with lcd('/Library/WebServer/CGI-Executables/WestOfRome/'):
        local('sudo git pull /Users/devin/Desktop/Dropbox/Projects/WebPage/WestOfRome/')
        local('python manage.py migrate blog')
        local('python manage.py test blog')
        local('python manage.py runserver')

