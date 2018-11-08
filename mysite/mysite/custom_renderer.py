from rest_framework import renderers


class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = None
    # charset = 'iso-8859-1'

    def render(self, data, media_type=None, renderer_context=None):
        print('text renderer')
        return data.encode(self.charset)
