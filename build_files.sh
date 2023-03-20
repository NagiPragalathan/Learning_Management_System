# build_files.sh

echo " Build start ............." 

virtualenv newenv
source newenv/bin/activate
pip install django
pip install --upgrade pip
pip install -r requirements.txt
deactivate
python3.9 manage.py collectstatic --noinput --clear
 
echo "build end/................."