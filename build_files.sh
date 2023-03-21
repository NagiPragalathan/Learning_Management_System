# build_files.sh

echo " Build start ............." 

pip install --upgrade pip
sudo apt-get install libpq-dev
pip install psycopg2-binary
pip install -r requirements.txt
pip install psycopg2
pip install django
pip install django-widget-tweaks==1.4.8
pip install django-widget-tweaks
python3.9 manage.py collectstatic --noinput --clear
 
echo "build end/................."