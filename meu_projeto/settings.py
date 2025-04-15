from pathlib import Path
import os
from dotenv import load_dotenv

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as variáveis do .env
load_dotenv(BASE_DIR / '.env')

# Detecta o ambiente (produção ou desenvolvimento)
TARGET_ENV = os.getenv('TARGET_ENV', 'dev')
NOT_PROD = not TARGET_ENV.lower().startswith('prod')

# Chave secreta e modo debug
SECRET_KEY = os.getenv('SECRET_KEY') if not NOT_PROD else '<SUA_SECRET_KEY_LOCAL>'
DEBUG = os.getenv('DEBUG', 'True' if NOT_PROD else 'False').lower() in ['true', '1', 't']

# Hosts permitidos
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split() if not NOT_PROD else []
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split() if not NOT_PROD else []

# Redirecionamento para HTTPS (usado em produção)
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'False').lower() in ['true', '1', 't']
if SECURE_SSL_REDIRECT:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Banco de dados
if NOT_PROD:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DBNAME'),
            'USER': os.getenv('DBUSER'),
            'PASSWORD': os.getenv('DBPASS'),
            'HOST': os.getenv('DBHOST'),
            'OPTIONS': {'sslmode': 'require'},
        }
    }

# Aplicações instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",  # Serve arquivos estáticos com Whitenoise também no runserver
    "forum",
    "widget_tweaks",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Importante para servir arquivos estáticos
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Arquivo de URLs principal
ROOT_URLCONF = 'meu_projeto.urls'

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "base"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI (interface para servidores como gunicorn)
WSGI_APPLICATION = 'meu_projeto.wsgi.application'

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internacionalização
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, JS, imagens, etc.)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'forum' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Onde os arquivos vão no collectstatic
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Otimização com cache e versionamento

# Arquivos de mídia (uploads de usuário, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tipo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
