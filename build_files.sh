 echo "BUILD START"
 python3.9 -m venv env
 source env/bin/activate
 echo "Virtual ENV ACTIVATED"
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic
 echo "BUILD END"