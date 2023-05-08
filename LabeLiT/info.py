



SITE_PROTOCOL = "http://"

CURRENT_SITE = "127.0.0.1:8000"
      
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000", SITE_PROTOCOL+CURRENT_SITE]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nnanyereugofrancis.o@gmail.com'
EMAIL_HOST_PASSWORD = 'cthbrdgstkkwrfuy'
ACCOUNT_EMAIL_VERIFICATION = 'none'


