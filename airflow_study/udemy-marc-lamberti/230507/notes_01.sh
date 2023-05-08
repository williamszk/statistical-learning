docker ps -a
docker exec -it 230424-airflow-worker-1 bash

# check for this file
# /tmp/processed_user.csv
cat /tmp/processed_user.csv

docker exec -it 230424-airflow-worker-1 cat /tmp/processed_user.csv
# Malone,Roussel,France,tinysnake675,suzanne,malone.roussel@example.com

docker exec -it 230424-postgres-1 bash
psql -U airflow -W -h localhost

\dt
select * from users;
#  firstname | lastname  |   country   |     username      | password |             email             
# -----------+-----------+-------------+-------------------+----------+-------------------------------
#  Josette   | Chevalier | Switzerland | crazywolf334      | redsox   | josette.chevalier@example.com
#  بنیامین   | احمدی     | Iran        | sadgorilla814     | bonbon   | bnymyn.hmdy@example.com
#  Rose      | Steward   | Ireland     | yellowelephant703 | squeeze  | rose.steward@example.com
#  Byron     | Austin    | Ireland     | lazyfish709       | madonna  | byron.austin@example.com
#  William   | Anderson  | Canada      | tinytiger104      | skiing   | william.anderson@example.com
#  Malone    | Roussel   | France      | tinysnake675      | suzanne  | malone.roussel@example.com
# (6 rows)

docker cp 230424-airflow-scheduler-1:/opt/airflow/airflow.cfg .

docker compose down && docker compose --profile flower up -d

docker compose down && docker compose -d

# localhost:5555
