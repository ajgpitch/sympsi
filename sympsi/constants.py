"""Constants (like hbar) related to quantum mechanics."""

from __future__ import print_function, division

from sympy.core.compatibility import with_metaclass
from sympy.core.numbers import NumberSymbol
from sympy.core.singleton import Singleton
from sympy.printing.pretty.stringpict import prettyForm

# check sympy version. Version 0.7.7
# mpmath not included in Version 0.7.7. See Sympy install website
import sympy
if sympy.__version__ <= '0.7.6':
    import sympy.mpmath.libmp as mlib
else:
    import mpmath.libmp as mlib

#-----------------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------------

__all__ = [
    'hbar'
]


class HBar(with_metaclass(Singleton, NumberSymbol)):
    """Reduced Plank's constant in numerical and symbolic form [1]_.

    Examples
    ========

        >>> from sympsi.constants import hbar
        >>> hbar.evalf()
        1.05457162000000e-34

    References
    ==========

    .. [1] http://en.wikipedia.org/wiki/Planck_constant
    """

    is_real = True
    is_positive = True
    is_negative = False
    is_irrational = True

    __slots__ = []

    def _as_mpf_val(self, prec):
        return mlib.from_float(1.05457162e-34, prec)

    def _sympyrepr(self, printer, *args):
        return 'HBar()'

    def _sympystr(self, printer, *args):
        return 'hbar'

    def _pretty(self, printer, *args):
        if printer._use_unicode:
            return prettyForm(u'\u210f')
        return prettyForm('hbar')

    def _latex(self, printer, *args):
        return r'\hbar'

# Create an instance for everyone to use.
hbar = HBar()
