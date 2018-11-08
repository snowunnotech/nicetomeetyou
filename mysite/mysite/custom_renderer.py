from rest_framework import renderers


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = None

    def render(self, data, media_type=None, renderer_context=None):
        return data.encode(self.charset)
