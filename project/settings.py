# Configuração de arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "app/static"]

# Configuração importante para usar MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',  # Ou o IP do seu servidor MySQL
        'PORT': '3306',       # Porta padrão do MySQL
    }
}

