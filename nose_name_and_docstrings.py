"""
Custom describing docstring
"""

from nose.plugins.base import Plugin

__version__ = '0.1'


class NameWithDocstrings(Plugin):
    """
    Show custom docstring
    """
    name = 'name-and-docstrings'

    def describeTest(self, test):
        """Show test docstring or test name"""
        test_name = str(test)
        default = test.test._testMethodDoc
        if default:
            return '{}: {}'.format(test_name, default.strip())
        return test_name
