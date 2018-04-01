from inspect import isclass

from django.conf.urls import url


class Patterns(list):
    '''
    Helper for generating urlpatterns lists.
    '''
    def __call__(self, pattern, kwargs=None, name=None):
        '''
        Act as a class or function decorator for appending a new url.
        '''
        def _inner(func):
            '''Actual decorator function'''
            if isclass(func):
                view = func.as_view()
            else:
                view = func
            self.append(url(pattern, view, kwargs=kwargs, name=name))
            return func
        return _inner
