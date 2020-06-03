# Django S3

How to setup django static and media file in aws s3.

## Installation

How to install Django s3 set up ?

*** First [Check This Article](https://techincent.com/how-to-setup-django-static-and-media-file-in-aws-s3/) 
```bash
$ mkdir django_s3 && cd $_
$ virtualenv venv  # make sure Virualenv package exist in your computer
$ git clone https://github.com/sajalmia381/django_s3.git
$ pip install -r requirements.txt
```
Please edit django_s3/aws/conf.py files with your aws account configuration

```bash
$ python manage.py collectstatic 
$ python manage.py runserver

```

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)