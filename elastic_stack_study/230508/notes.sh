
# stopped at:
# https://youtu.be/gS_nHTWZEJ8?t=2294

#
# Elastic Search
#
# Kibana 
# 
# Logstash
# 
# Beats

# https://www.elastic.co/guide/en/elasticsearch/reference/8.7/docker.html
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.5

# https://www.youtube.com/watch?v=U8dNNYeiD9o&ab_channel=VincentStevenson
docker network ls
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.5

docker run -d --name elastic-search-01-test --net elastic \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.5

docker stop elastic-search-01-test
docker rm elastic-search-01-test


docker exec -it elastic-search-01-test bash
# vi /etc/elasticsearch/elasticsearch.yml
cd ~
./bin/elasticsearch-setup-passwords interactive
123456

curl -u elastic:123456 44.211.30.27:9200
curl 44.211.30.27:9200


# install kibana
docker pull docker.elastic.co/kibana/kibana:7.17.5

docker run -d --name kibana-01-test \
    --net elastic \
    -p 5601:5601 \
    -e "ELASTICSEARCH_HOSTS=http://elastic-search-01-test:9200" \
    docker.elastic.co/kibana/kibana:7.17.5

docker kill kibana-01-test
docker rm kibana-01-test

# -----------------------------------------------------------------------------
# copy the certificate from the elastic search container
docker cp elastic-search-01-test:/usr/share/elasticsearch/config/certs/http_ca.crt .

curl --cacert http_ca.crt -u elastic https://localhost:9200

# pass the elastic search certificate to kibana
docker cp http_ca.crt kibana-01-test:/etc/ssl/certs/http_ca.crt



# -----------------------------------------------------------------------------
# I need to rename the cluster 
# https://youtu.be/gS_nHTWZEJ8?t=1919
docker exec -it <elastic-search-container> bash
apt update
apt install vim
vim config/elasticsearch.yml
# need to have those two lines:
cluster.name: "elastic_crash_course"
node.name: "crud_node"

# restart both containers: elasticsearch and kibana
docker restart elastic-search-01-test
docker restart kibana-01-test

# -----------------------------------------------------------------------------
# send api requests to elastic search

# we'll send request through the kibana web ui
# Management > Dev Tools 

# get info about cluster health
GET _cluster/health

curl http://44.211.30.27:9200/_cluster/health
# {
#    "cluster_name":"elastic_crash_course",
#    "status":"green",
#    "timed_out":false,
#    "number_of_nodes":0,
#    "number_of_data_nodes":1,
#    "active_primary_shards":8,
#    "active_shards":9,
#    "relocating_shards":0,
#    "initializing_shards":-1,
#    "unassigned_shards":0,
#    "delayed_unassigned_shards":0,
#    "number_of_pending_tasks":-1,
#    "number_of_in_flight_fetch":0,
#    "task_max_waiting_in_queue_millis":-1,
#    "active_shards_percent_as_number":100.0
# }

GET _nodes/stats

# we need to paste this into the kibana ui
# Management > Dev Tools 
# or we can use curl to make api requests directly to elastic search

# create an index
# this is like a collection in mongodb
PUT <name-of-the-index> 
PUT favorite_candy
# {
#   "acknowledged" : true,
#   "shards_acknowledged" : true,
#   "index" : "favorite_candy"
# }

# post a new documet
POST <name-of-the-index>/_doc
{
    "field": "value"
}







