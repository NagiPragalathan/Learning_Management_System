# build_files.sh

echo " Build start ............." 

yum install sqlite-devel
./configure
make && make altinstall
pip install --upgrade pip
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
 
echo "build end/................."