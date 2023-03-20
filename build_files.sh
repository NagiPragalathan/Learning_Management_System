# build_files.sh

echo " Build start ............." 

pip install --upgrade pip
pip install -r requirements.txt
pip install django
python3.9 manage.py collectstatic --noinput --clear
 
echo "build end/................."