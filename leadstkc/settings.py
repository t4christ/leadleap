"""
Django settings for leadstkc project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)




#Environment variables
# import dotenv
# from dotenv import load_dotenv
# dotenv.load_dotenv()
# load_dotenv(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=ua60xb55b5y4tfaq_z&x*u*qexx^r@!(k-fx^dn8eb_#+#mi%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.leadleapconsult.com","www.leadleap.herokuapp.com","localhost"]


# Application definition

INSTALLED_APPS = [
    'ldtkc',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'cloudinary_storage',
    'cloudinary',
    'crispy_forms',
    'django_markdown',
    'pagedown',
    'storages',
    # 'chunked_upload',
    # 'tinymce',

]






CRISPY_TEMPLATE_PACK = "bootstrap4"
AUTH_USER_MODEL = 'ldtkc.MyUser'


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'




EMAIL_HOST = "mail.privateemail.com"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True



# STATICFILES_DIRS = (
    # "https://storage.googleapis.com/bezop-uploads/static/",
    #   os.path.join(BASE_DIR, "static"),
# #     #'/Users/jmitch/Desktop/srvup/static/static_dirs/', #on mac
# #     #'\Users\jmitch\Desktop\srvup\static\static_dirs\', somethingl ike this on windows
# #     #  '/var/www/static/',
#   )

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

# # DEFAULT_FILE_STORAGE = 'leadstkc.storage_backend.GoogleCloudMediaStorage'
# DEFAULT_FILE_STORAGE = 'google.storage.googleCloud.GoogleCloudStorage'
# GOOGLE_CLOUD_STORAGE_BUCKET = '/bezop-uploads' # the name of the bucket you have created from the google cloud storage console
# GOOGLE_CLOUD_STORAGE_URL = 'http://storage.googleapis.com/bezop-uploads' #whatever the ulr for accessing your cloud storgage bucket
# GOOGLE_CLOUD_STORAGE_DEFAULT_CACHE_CONTROL = 'public, max-age: 7200' # default cache control headers for your files
# # STATICFILES_STORAGE = 'google.storage.googleCloud.GoogleCloudStorage'
# GS_PROJECT_ID = 'evocative-tube-205107'
# GS_MEDIA_BUCKET_NAME = 'bezop-uploads/media'
# GS_STATIC_BUCKET_NAME = 'bezop-uploads/static'
# STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
# MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)

# CHUNKED_UPLOAD_PATH = 'https://storage.googleapis.com/bezop-uploads/'
# CHUNKED_UPLOAD_TO = CHUNKED_UPLOAD_PATH + 'media/'
# STATIC_ROOT=GS_STATIC_BUCKET_NAME
if  DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        #'/var/www/static/',
    ]

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATIC_URL = '/static/'
  
    MEDIA_URL = '/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR,CHUNKED_UPLOAD_PATH)


# DEFAULT_FILE_STORAGE = "leadstkc.storage.ECGoogleCloudStorage"
# GCS_ROOT = "https://storage.googleapis.com/{bucket_name}/".format(
#     bucket_name=os.getenv("GCS_BUCKET")
# )
else: 
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    STATIC_URL = '/static/'
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
    # DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    # STATIC_URL = '/static/'

    # STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    # GS_ACCESS_KEY_ID =os.getenv("CLIENT_ID")
    # GS_SECRET_ACCESS_KEY = os.getenv("CLIENT_SECRET")
    # GS_BUCKET_NAME = os.getenv("GCS_BUCKET")
    # GS_PROJECT_ID = os.getenv("GCLOUD_PROJECT")
    # MEDIA_URL = 'https://storage.googleapis.com/bezop-uploads/media/'


CLOUDINARY_STORAGE = {
    # other settings, like credentials
    'MEDIA_TAG': 'media',
    'STATIC_TAG': 'static',
    'MAGIC_FILE_PATH': 'magic',
    'PREFIX': '/media/',
    'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, 'manifest')
}





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'leadstkc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'leadstkc.wsgi.application'


# Database
# # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# if DEBUG:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


if  DEBUG:
 


    DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'lead',
            'USER' : 'automart',
            'PASSWORD': 'automart',
            'PORT': '5432',
            'HOST':'localhost',
        }
        }

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }


else:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9o581akhtvc8c',
        'USER' : 'awxrgbhkqxlsaj',
        'PASSWORD': '24ef4b01f18301c313d326b82f514e000fc8a0bb09771264db90ce4bde84485a',
        'PORT': '5432',
        'HOST':'ec2-54-83-12-150.compute-1.amazonaws.com',
    }
    }



 
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#              'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#     },
# }



