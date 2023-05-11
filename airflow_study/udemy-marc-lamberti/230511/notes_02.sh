
docker compose -f docker-compose-es.yaml up -d 

docker compose -f docker-compose-es.yaml ps 

docker exec -it 230511-airflow-scheduler-1 bash
# [inside the container]
curl -X GET 'http://elastic:9200'
# {
#   "name" : "1ec63cc3dc7c",
#   "cluster_name" : "docker-cluster",
#   "cluster_uuid" : "GhB0TffGTIKCaD2HpPBSHg",
#   "version" : {
#     "number" : "8.3.3",
#     "build_flavor" : "default",
#     "build_type" : "docker",
#     "build_hash" : "801fed82df74dbe537f89b71b098ccaff88d2c56",
#     "build_date" : "2022-07-23T19:30:09.227964828Z",
#     "build_snapshot" : false,
#     "lucene_version" : "9.2.0",
#     "minimum_wire_compatibility_version" : "7.17.0",
#     "minimum_index_compatibility_version" : "7.0.0"
#   },
#   "tagline" : "You Know, for Search"
# } 

pip install elasticsearch

# to make the new plugin to show we need to restart airflow
# let's check if with just restart it will work
# then I'll check inside the scheduler using
# airflow plugins
# then we should find our plugin in there

docker compose restart

# if we restart we need to change the owner of some directories
ll
sudo chown -R ubuntu:ubuntu plugins
sudo chown -R ubuntu:ubuntu dags 

# check the name of the container of the scheduler
docker compose ps 

# enter into the container
docker exec -it 230511-airflow-scheduler-1 bash

# check the plugins that are installed
airflow plugins
# /home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:367: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
#   FutureWarning,
# name    | hooks                    | source                                       
# ========+==========================+==============================================
# elastic | elastic_hook.ElasticHook | $PLUGINS_FOLDER/hooks/elastic/elastic_hook.py



