 echo "BUILD START"
 python3.9 -m venv env
 source env/bin/activate
 python3.9 -m pip install pipwin
 pipwin install psycopg2
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"