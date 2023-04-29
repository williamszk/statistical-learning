# how to run flask app?

cd python_flask
flask run --host=127.0.0.1

# run autocannon
autocannon -c 100 -d 5 -p 10 http://localhost:5000/

#!/bin/bash

for i in {1..100}
do
    curl -s -w '\nTime: %{time_total}s\n' -o . http://localhost:5000
done


#==============================================================================
# Trying to put flask into production

# https://www.youtube.com/watch?v=VX-qZ1rJ3b8&ab_channel=YujianTang
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

# gunicorn
pip install gunicorn
pip install fcntl

# -w: number of workers
gunicorn -w 4

gunicorn --bind 0.0.0.0:5000 wsgi:app
# I'll need to try this later connected to a linux machine