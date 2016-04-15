# from __future__ import print_function


import oss2
import Tkinter
import tkFileDialog

from pprint import pprint

endpoint = 'oss-cn-beijing.aliyuncs.com'
auth = oss2.Auth('iICNamwRFHn1qbWF', 'Fhg9wNzNIQeHfV7dPY1kxnPJ3Q0aFZ')
service = oss2.Service(auth, endpoint)

bucket_name = 'modeflip'


# pprint(dir(service))

# print([b.name for b in oss2.BucketIterator(service)])

# bucket = oss2.Bucket(auth, endpoint, bucket_name)
# img = bucket.get_object('img1.JPG')
# pprint(dir(img))

# print img.request_id

# url = 'http://modeflip.oss-cn-beijing.aliyuncs.com/img1.JPG'


# Tkinter.Tk().withdraw() # Close the root window
# selected_file_path = tkFileDialog.askopenfilename()
# selected_file_path = '/Users/mingli/Desktop/image2.JPG'
selected_file_path = '/Users/mingli/Desktop/ModeFlip/small_img1.jpg'
# file_name = selected_file_path.split('/')[-1]
# print file_name






"""
import os, sys
import random
import string
import oss2


access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'iICNamwRFHn1qbWF')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'Fhg9wNzNIQeHfV7dPY1kxnPJ3Q0aFZ')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'modeflip')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-beijing.aliyuncs.com')


bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


def random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))

# filename = random_string(32) + '.txt'
filename = selected_file_path
content = oss2.to_bytes(random_string(1024 * 1024))

with open(filename, 'wb') as fileobj:
    fileobj.write(content)

# oss2.resumable_upload(bucket, 'remote-normal.txt', filename)

# oss2.resumable_upload(bucket, 'remote-multipart.txt', filename, multipart_threshold=100 * 1024)


total_size = os.path.getsize(filename)
print 'total_size:', total_size
part_size = oss2.determine_part_size(total_size, preferred_size=128 * 1024)

key = 'upload.JPG'
upload_id = bucket.init_multipart_upload(key).upload_id

with open(filename, 'rb') as fileobj:
    parts = []
    part_number = 1
    offset = 0
    while offset < total_size:
        num_to_upload = min(part_size, total_size - offset)
        result = bucket.upload_part(key, upload_id, part_number,
                                    oss2.SizedFileAdapter(fileobj, num_to_upload))
        parts.append(oss2.models.PartInfo(part_number, result.etag))

        offset += num_to_upload
        part_number += 1
        print 'part_number:', part_number

    bucket.complete_multipart_upload(key, upload_id, parts)

with open(filename, 'rb') as fileobj:
    assert bucket.get_object(key).read() == fileobj.read()


# os.remove(filename)
"""


"""
import os

from oss2 import SizedFileAdapter, determine_part_size
from oss2.models import PartInfo

key = 'upload.jpg'
filename = selected_file_path

total_size = os.path.getsize(filename)
part_size = determine_part_size(total_size, preferred_size=100 * 1024)

upload_id = bucket.init_multipart_upload(key).upload_id
parts = []

with open(filename, 'rb') as fileobj:
    part_number = 1
    offset = 0
    while offset < total_size:
        num_to_upload = min(part_size, total_size - offset)
        result = bucket.upload_part(key, upload_id, part_number,
                                    SizedFileAdapter(fileobj, num_to_upload))
        parts.append(PartInfo(part_number, result.etag))

        offset += num_to_upload
        part_number += 1
        print part_number

bucket.complete_multipart_upload(key, upload_id, parts)

with open(filename, 'rb') as fileobj:
    assert bucket.get_object(key).read() == fileobj.read()
"""




"""
def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')

        sys.stdout.flush()

# bucket.put_object('upload.jpg', 'a'*1024*1024, progress_callback=percentage)


with open(selected_file_path, 'rb') as fileobj:
	# oss2.resumable_upload(bucket, 'test.jpg', fileobj.read(),
	#     store=oss2.ResumableStore(root='/tmp'),
	#     multipart_threshold=100*1024,
	#     part_size=100*1024,
	#     num_threads=4)

	bucket.put_object('test.jpg', fileobj.read(), progress_callback=percentage)
"""




import upyun

# BUCKETNAME = 'modeflip.b0.aicdn.com'
BUCKETNAME = 'modeflip'
USERNAME = 'lmcgnlzt'
PASSWORD = '2916588anywn'

root = '/modeflip/'

up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30, endpoint=upyun.ED_AUTO)
print up

headers = {}
with open(selected_file_path, 'rb') as f:
	ret = up.put(root + 'test.jpg', f, checksum=False)

print 'Done'