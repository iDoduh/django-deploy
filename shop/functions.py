def generate_settings(site):

    local_settings = []

    # timezone
    local_settings.append("TIME_ZONE = '%s'" % 'Europe/Kiev')

    # language
    local_settings.append("LANGUAGE_CODE = '%s'" % 'ru')
    local_settings.append("LANGUAGES = (('%s', '%s'),)" % ('ru', 'Russian'))

    # currency
    local_settings.append("CURRENCY = '%s'" % site.currency)

    # database
    local_settings.append(
        "DATABASES = {'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'shop_%s', 'USER': 'isells',"
        "'PASSWORD': 'vdlk39dG46isells', 'HOST': '137.117.163.172' }}" % site.id)

    # debug
    local_settings.append("DEBUG = False")

    return '\n'.join(local_settings)
