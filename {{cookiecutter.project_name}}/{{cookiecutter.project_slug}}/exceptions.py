# -*- coding: utf-8 -*-

"""Exceptions for {{cookiecutter.project_name}}."""
import sys


class {% for x in cookiecutter.project_slug.split("_") %}{{ x.capitalize() }}{% endfor %}Error(Exception):
    body = ''

    def __init__(self, extra_body=''):
        self.extra_body = extra_body

    def __str__(self):
        msg = self.__class__.__name__
        if self.body:
            msg += ': {}'.format(self.body)
        if self.extra_body:
            msg += ('. {}' if self.body else ': {}').format(self.extra_body)
        return msg


def catch(fn):
    def wrap(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except {% for x in cookiecutter.project_slug.split("_") %}{{ x.capitalize() }}{% endfor %}Error as e:
            sys.stderr.write('[Error] {{ cookiecutter.project_name }} Exception:\n{}\n'.format(e))
    return wrap
