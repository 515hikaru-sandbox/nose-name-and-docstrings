"""
Custom describing docstring
"""

from nose.plugins.base import Plugin

__version__ = '0.1'


class CustomDocstrings(Plugin):
    """
    Show custom docstring
    """
    name = 'custom-docstrings'

    def describeTest(self, test, default_desc='foo'):
        return '{}: {}'.format(str(test), default_desc)
