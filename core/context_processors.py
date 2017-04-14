from django.conf import settings


def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    if settings.GOOGLE_ANALYTICS_PROPERTY_ID is not None:
        return {
            "GOOGLE_ANALYTICS_PROPERTY_ID":settings.GOOGLE_ANALYTICS_PROPERTY_ID
        }
    else:
        return {}

