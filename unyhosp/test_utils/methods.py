class ResourceMethods(object):
    @classmethod
    def _url(cls, *, resource, pk=None):
        pk = f'{pk}/' if pk else ''
        return f'/{resource}/{pk}'
