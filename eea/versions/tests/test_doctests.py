""" Doc tests
"""
import doctest
import unittest
from eea.versions.tests.base import VersionsFunctionalTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)


def test_suite():
    """ Suite
    """
    return unittest.TestSuite((
            Suite('docs/versions.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.versions',
                  test_class=VersionsFunctionalTestCase) ,
              ))
