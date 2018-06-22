'''
    Cell.py

    The Cell class is used to store info about each matrix cell.  This includes
    both current edit distance value and backtrace information.  Utilized by
    the Matrix class.
'''

from .Util import BTFLAG_UP, BTFLAG_LEFT, BTFLAG_DIAG

class Cell(object):
    '''
    The Cell class is used to store info about each matrix cell.  This includes
    both current edit distance value and backtrace information.  Utilized by
    the Matrix class.
    '''

    def __init__(self):
        self.distance = 0           # Distance value of the cell

        self.backtrace_flags = 0    # Bitflag value used to store backtrace info

        self.equivalent = False     # Boolean for when diagonal flag is set:
                                    # If the two letters being compared are
                                    # equivalent, this flag is set.  If two
                                    # letters are not equivalent, a
                                    # substitution, this flag is false.

    def _getflag(self, flag):
        '''
        Generalized function to get backtrace_flags info - internal use only.
        '''
        return bool(self.backtrace_flags & flag)

    def _setflag(self, flag, value):
        '''
        Generalized function to set backtrace_flags info - internal use only.
        '''
        if value == True:
            self.backtrace_flags |= flag
        elif value == False:
            self.backtrace_flags &= ~flag
        else:
            raise ValueError("Flag can only be true or false")

    @property
    def up(self):
        '''
        Returns the backtrace up flag
        '''
        return self._getflag(BTFLAG_UP)

    @property
    def left(self):
        '''
        Returns the backtrace left flag
        '''
        return self._getflag(BTFLAG_LEFT)

    @property
    def diag(self):
        '''
        Returns the backtrace diagonal flag
        '''
        return self._getflag(BTFLAG_DIAG)

    @up.setter
    def up(self, value):
        '''
        Set the backtrace up flag
        '''
        self._setflag(BTFLAG_UP, value)

    @left.setter
    def left(self, value):
        '''
        Set the backtrace left flag
        '''
        self._setflag(BTFLAG_LEFT, value)

    @diag.setter
    def diag(self, value):
        '''
        Set the backtrace diagonal flag
        '''
        self._setflag(BTFLAG_DIAG, value)
