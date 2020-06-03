import datetime
import os

AWS_USERNAME = 'django_s3' # not matter
AWS_GROUP_NAME = 'django_s3_group' # not matter
# Aws config
AWS_SECRET_ACCESS_KEY = '2IF3Z/k4gni+YIl4RVIA4Xp0ncBqFsrncqdHqf'
AWS_ACCESS_KEY_ID = 'AKIA6IVWV2ZU5T2VV'
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'django_s3.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'django_s3.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'djang-s3-bucket'
S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = S3_URL + 'media/'
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWS_S3_FILE_OVERWRITE = False
two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()),),
}