# coding=utf-8

import os
import boto
import logging
from boto.s3.key import Key
from boto.s3.connection import S3Connection
from boto.s3.connection import Location
from boto.exception import S3CreateError

boto.set_stream_logger('boto', logging.DEBUG, '[%(asctime)s %(filename)s %(funcName)s() line:%(lineno)d %(levelname)s] %(message)s')

# os.environ["AWS_ACCESS_KEY_ID"] = "CD5E0C8514658FD6A8B0"
# os.environ["AWS_SECRET_ACCESS_KEY"] = "Sp/J9+KMxZYgLKwu4/Jeua4b2ScAAAFVFGWP1rH1"

os.environ["AWS_ACCESS_KEY_ID"] = "AKIAI4WPBRA7GAMRWBNA"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"



def create_or_get_bucket(bucket_name, location):
    conn = boto.connect_s3()
    # print 'get_all_buckets',conn.get_all_buckets()

    bucket = conn.lookup(bucket_name);

    from boto.s3.key import Key
    k = Key(bucket)
    k.key = 'foobar'
    # k.set_contents_from_string('This is a test of S3')
    fp = file('oos.txt','r')

    k.set_contents_from_file(fp)
    # bucket = conn.lookup(bucket_name);
    # # bucket.complete_multipart_upload()
    # # bucket = conn.create_bucket(bucket_name)

    # if bucket is None:
    #     bucket = conn.create_bucket(bucket_name, None,location,None)
    # else:
    #     if bucket.get_location() != location:
    #     	pass
    #         # raise Exception('bad bucket location')
    # return bucket


if __name__ == "__main__":
    # print '\n'.join(i for i in dir(Location) if i[0].isupper())
    bucket = create_or_get_bucket('xuhui-dicomimage2', location=None)

    # for key in bucket.get_all_keys():
    #     key.get_contents_to_filename(key.name) 