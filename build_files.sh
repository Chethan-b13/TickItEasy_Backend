 echo "BUILD START"
 python3.9 -m pip install pipwin
 pipwin install psycopg2
 python3.9 -m pip install -r requirements.txt
 python3.9 -m pip uninstall pipwin
 echo "BUILD END"SS