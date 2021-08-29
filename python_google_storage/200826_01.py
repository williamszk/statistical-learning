# https://www.youtube.com/watch?v=pEbL_TT9cHg&ab_channel=JieJenn

import os
from google.cloud import storage


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "../secret/project-tabas-994f1da38d93.json"

storage_client = storage.Client()

dir(storage_client)


# how to create a new bucket?
bucket_name = "my-new-test-bucket-tabas"
bucket = storage_client.bucket(bucket_name)
bucket.location = "US"

storage_client.create_bucket(bucket)
# this will create a new bucket in your account


# ---------------------------
# print bucket detail
vars(bucket)


# select a bucket
bucket_name = "my-new-test-bucket-tabas"
my_bucket = storage_client.get_bucket(bucket_name) 
vars(bucket)

# how to upload files to the bucket?
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True

    except Exception as e:
        print(e)
        return False


file_path = "../data/appl_stock.csv"
blob_name = "appl_stock.csv"
bucket_name = "my-new-test-bucket-tabas"
upload_to_bucket(blob_name, file_path, bucket_name)

# send the file to another directory in cloud storage
file_path = "../data/appl_stock.csv"
blob_name = "keras_course/appl_stock.csv"
bucket_name = "my-new-test-bucket-tabas"
upload_to_bucket(blob_name, file_path, bucket_name)
# here we create a new directory called keras_course

# -------------------------------------------
# How to download files?
def download_from_bucket(blob_name,file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, 'wb') as file:
            storage_client.download_blob_to_file(blob, file)        
        return True

    except Exception as e:
        print(e)
        return False

file_path = "../data/appl_stock_from_cloud.csv"
blob_name = "keras_course/appl_stock.csv"
bucket_name = "my-new-test-bucket-tabas"
download_from_bucket(blob_name,file_path, bucket_name)





