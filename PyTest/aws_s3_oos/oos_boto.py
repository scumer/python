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

# os.environ["AWS_ACCESS_KEY_ID"] = "AKIAJRWHHEK76NKTORWQ"
# os.environ["AWS_SECRET_ACCESS_KEY"] = "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"

os.environ["AWS_ACCESS_KEY_ID"] = "43e9ab6b7d0bc4b5e609"
os.environ["AWS_SECRET_ACCESS_KEY"] = "86ef19440d578b2dfd7a3e66701aad501dcd6e0c"

boto.config.save_user_option('s3', 'host', 'oos-fj.ctyunapi.cn')
# DefaultHost = boto.config.get('s3', 'host', 's3.amazonaws.com')


def create_or_get_bucket(bucket_name, location):
    conn = boto.connect_s3(is_secure=False)
    # print 'get_all_buckets', conn.get_all_buckets()
    # return

    # bucket = conn.lookup(bucket_name);
    # print bucket

    # from boto.s3.key import Key
    # k = Key(bucket)
    # k.key = 'dicom1'
    # # k.set_contents_from_string('This is a test of S3')
    # #fp = file('oos_get.txt','w')
    # #
    # # k.set_contents_from_file(fp)
    # # print bucket.get_key(k.key)
    # # print 'get',k.get_contents_to_file(fp)
    #
    # print 'get', k.get_contents_to_filename('oos_getdicom.dcm')

    # print 'get_key', bucket.get_key('foobar')
    # fp.close()
    # bucket = conn.lookup(bucket_name);
    # # bucket.complete_multipart_upload()
    # # bucket = conn.create_bucket(bucket_name)
    bucket = conn.create_bucket(bucket_name, None,location,None)
    # if bucket is None:
    #     bucket = conn.create_bucket(bucket_name, None,location,None)
    #     print bucket
    # else:
    #     if bucket.get_location() != location:
    #     	pass
    #         # raise Exception('bad bucket location')
    return bucket


if __name__ == "__main__":
    # print '\n'.join(i for i in dir(Location) if i[0].isupper())
    print boto.config.get('s3', 'host')
    bucket = create_or_get_bucket('xuhui-dicomimage2', location='')

    # for key in bucket.get_all_keys():
    #     key.get_contents_to_filename(key.name)