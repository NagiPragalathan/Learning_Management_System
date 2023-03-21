# build_files.sh

echo " Build start ............." 

pip install mysqlclient
pip install -r requirements.txt
pip install django
pip install django-widget-tweaks
python manage.py migrate
python3.9 manage.py collectstatic --noinput --clear
 
echo "build end/................."