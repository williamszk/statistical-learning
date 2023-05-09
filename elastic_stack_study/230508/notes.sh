
# stopped at:
# https://youtu.be/gS_nHTWZEJ8?t=2294

# Next video:
# https://www.youtube.com/watch?v=CCTgroOcyfM&ab_channel=OfficialElasticCommunity

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


#-------------------------------------------------------------------------------
# start the elastic search and kibana containers
docker ps 

docker start elastic-search-01-test
docker start kibana-01-test

# go to the dev tools in kibana
# Management > Dev Tools 
GET _cluster/health

POST favorite_candy/_doc
{
    "first_name": "Lisa",
    "candy": "Sour Skittles"
}
# 201 response - created
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "lKUHAYgBfKuxGVD5dwF8",
#   "_version" : 1,
#   "result" : "created",
#   "_shards" : {
#     "total" : 2,
#     "successful" : 1,
#     "failed" : 0
#   },
#   "_seq_no" : 0,
#   "_primary_term" : 2
# }

# we can assign the id that we want in the document, using PUT instead of POST
PUT <name-of-the-index>/_doc/<id-you-want-to-assign>
{
    "field": "value"
}

PUT favorite_candy/_doc/1
{
    "first_name": "John",
    "candy": "Starburst"
}
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "1",
#   "_version" : 1,
#   "result" : "created",
#   "_shards" : {
#     "total" : 2,
#     "successful" : 1,
#     "failed" : 0
#   },
#   "_seq_no" : 1,
#   "_primary_term" : 2
# }


PUT favorite_candy/_doc/2
{
    "first_name": "Rachel",
    "candy": "Rolos"
}

PUT favorite_candy/_doc/3
{
    "first_name": "Tom",
    "candy": "Sweet Tarts"
}

# read the documents that are in the index
GET <name-of-the-index>/_doc/<id-you-want-to-assign>

GET favorite_candy/_doc/1
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "1",
#   "_version" : 1,
#   "_seq_no" : 1,
#   "_primary_term" : 2,
#   "found" : true,
#   "_source" : {
#     "first_name" : "John",
#     "candy" : "Starburst"
#   }
# }

GET favorite_candy/_doc/2



PUT favorite_candy/_doc/1
{
    "first_name": "Sally",
    "candy": "Snickers"
}
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "1",
#   "_version" : 2,       # <-- notice the version here
#   "result" : "updated", # <-- it says updated instead of created
#   "_shards" : {
#     "total" : 2,
#     "successful" : 1,
#     "failed" : 0
#   },
#   "_seq_no" : 8,
#   "_primary_term" : 2
# }

# _doc endpoint will overwrite the document underlying
# if we want to create we use the _create this will throw an error
# if the document already exists
PUT favorite_candy/_create/1
{
    "first_name": "Sally",
    "candy": "Snickers"
}
# The response is a 409 - conflict message
# {
#   "error" : {
#     "root_cause" : [
#       {
#         "type" : "version_conflict_engine_exception",
#         "reason" : "[1]: version conflict, document already exists (current version [2])",
#         "index_uuid" : "M9htLW8OTVWlZ0pQwG-v5w",
#         "shard" : "0",
#         "index" : "favorite_candy"
#       }
#     ],
#     "type" : "version_conflict_engine_exception",
#     "reason" : "[1]: version conflict, document already exists (current version [2])",
#     "index_uuid" : "M9htLW8OTVWlZ0pQwG-v5w",
#     "shard" : "0",
#     "index" : "favorite_candy"
#   },
#   "status" : 409
# }

# we can update document by
POST <name-of-the-index>/_update/<id-you-want-to-assign>
{
    "doc": { # <-- use this to specify some fields to change, and not the whole document
        "field1": "value",
        "field2": "value"
    }
}

POST favorite_candy/_update/1
{
    "doc": {
        "candy": "M&M's"
    }
}
# the response was 200 - Ok
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "1",
#   "_version" : 3,
#   "result" : "updated",
#   "_shards" : {
#     "total" : 2,
#     "successful" : 1,
#     "failed" : 0
#   },
#   "_seq_no" : 9,
#   "_primary_term" : 2
# }

# Check the value of the document
GET favorite_candy/_doc/1
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "1",
#   "_version" : 3,
#   "_seq_no" : 9,
#   "_primary_term" : 2,
#   "found" : true,
#   "_source" : {
#     "first_name" : "Sally",
#     "candy" : "M&M's"
#   }
# }

# to delete a document
DELETE <name-of-the-index>/_doc/<id-you-want-to-assign>

DELETE favorite_candy/_doc/1
# response was 200 - Ok
# {
#   "_index" : "favorite_candy",
#   "_type" : "_doc",
#   "_id" : "1",
#   "_version" : 4,
#   "result" : "deleted",
#   "_shards" : {
#     "total" : 2,
#     "successful" : 1,
#     "failed" : 0
#   },
#   "_seq_no" : 10,
#   "_primary_term" : 2
# }

