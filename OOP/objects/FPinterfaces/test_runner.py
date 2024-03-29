"""
This is a script to test the ABC class that was created as well as the classes that subclass it.
Scripts that will be tested: creating_abcs.py and extending_abcs.py
"""
import doctest

from creating_abcs import Tombola, Fake

import extending_abcs

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    print('real_subclasses: ', real_subclasses)
    # virtual_subclasses = list(Tombola._abc_registry)
    virtual_subclasses = list()

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))



if __name__=='__main__':
    import sys
    main(sys.argv)
