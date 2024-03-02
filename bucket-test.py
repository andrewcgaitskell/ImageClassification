import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/andrewcgaitskell/Documents/Google/mysecret.json'

##bq_client = Client()

from google.cloud import storage
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
##acg34rg-imagebucket-1

bucket = client.get_bucket('acg34rg-imagebucket-1')
# Then do other things...

pathtofile = 'gs://acg34rg-imagebucket-1/Egypt80s/IMG_20210807_0001.jpg'
blob = bucket.get_blob(pathtofile)

client = storage.Client()

bucket = storage.Bucket(client, "acg34rg-imagebucket-1", user_project="images-20210607")

all_blobs = list(client.list_blobs(bucket))
print(all_blobs)
##print(blob.download_as_bytes())
##blob.upload_from_string('New contents!')
##blob2 = bucket.blob('gs://acg34rg-imagebucket-1/Egypt80s/storage.txt')
##blob2.upload_from_filename(filename='/local/path.txt')