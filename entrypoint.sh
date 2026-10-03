echo "migration start"
# python -m flask --app wsgi db init 
# python -m flask --app wsgi db migrate -m "Initial migration"
# python -m flask --app wsgi db upgrade
set e 
alembic db upgrade
echo "migration end"
exec gunicorn --host 0.0.0.0 --port 5000 wsgi:app