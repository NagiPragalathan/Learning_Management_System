# build_files.sh
echo " Build start ............." 

pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py collectstatic

echo "build end/................."