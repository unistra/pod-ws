from django.utils.encoding import smart_unicode
from rest_framework import renderers


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, media_type=None, renderer_context=None):
        try:
            return data.encode(self.charset)
        except:
            return data['error'] if 'error' in data else 'unknown error'