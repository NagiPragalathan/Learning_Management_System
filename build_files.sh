# build_files.sh

echo " Build start ............." 

pip install mysqlclient
python3 -m pip install mysql-client
brew reinstall mysql-client
pip install -r requirements.txt
pip install django
pip install django-widget-tweaks
python manage.py migrate
python3.9 manage.py collectstatic --noinput --clear
 
echo "build end/................."