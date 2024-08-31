from django.conf import settings


def global_settings(request):
    """
    Add global settings to the context.
    These will be available to all templates.
    """
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_TITLE': f"{settings.SITE_NAME} | " ,
        'DEBUG': settings.DEBUG,
        'LOGIN_REDIRECT_URL': settings.LOGIN_REDIRECT_URL,
    }