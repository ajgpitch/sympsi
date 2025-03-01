from sympy.physics.quantum.operatorset import (
    operators_to_state, state_to_operators
)

from sympy.physics.quantum.cartesian import (
    XOp, XKet, PxOp, PxKet, XBra, PxBra
)

from sympy.physics.quantum.state import Ket, Bra
from sympy.physics.quantum.operator import Operator
from sympy.physics.quantum.spin import (
    JxKet, JyKet, JzKet, JxBra, JyBra, JzBra,
    JxOp, JyOp, JzOp, J2Op
)

from sympy.utilities.pytest import raises

from sympy.utilities.pytest import XFAIL


def test_spin():
    assert operators_to_state(set([J2Op, JxOp])) == JxKet
    assert operators_to_state(set([J2Op, JyOp])) == JyKet
    assert operators_to_state(set([J2Op, JzOp])) == JzKet
    #FIXME ajgpitch 22 Sept 2019:
    # JxKet() etc seems to require positional arguments: 'j' and 'm'
    # So these tests cannot work
    # Probably easy to work out what 'j' and 'm' should be from the physics
    assert operators_to_state(set([J2Op(), JxOp()])) == JxKet()
    assert operators_to_state(set([J2Op(), JyOp()])) == JyKet()
    assert operators_to_state(set([J2Op(), JzOp()])) == JzKet()

    assert state_to_operators(JxKet) == set([J2Op, JxOp])
    assert state_to_operators(JyKet) == set([J2Op, JyOp])
    assert state_to_operators(JzKet) == set([J2Op, JzOp])
    assert state_to_operators(JxBra) == set([J2Op, JxOp])
    assert state_to_operators(JyBra) == set([J2Op, JyOp])
    assert state_to_operators(JzBra) == set([J2Op, JzOp])

    #FIXME ajgpitch 22 Sept 2019:
    # JxKet() etc seems to require positional arguments: 'j' and 'm'
    # So these tests cannot work
    # Probably easy to work out what 'j' and 'm' should be from the physics
    assert state_to_operators(JxKet()) == set([J2Op(), JxOp()])
    assert state_to_operators(JyKet()) == set([J2Op(), JyOp()])
    assert state_to_operators(JzKet()) == set([J2Op(), JzOp()])
    assert state_to_operators(JxBra()) == set([J2Op(), JxOp()])
    assert state_to_operators(JyBra()) == set([J2Op(), JyOp()])
    assert state_to_operators(JzBra()) == set([J2Op(), JzOp()])


def test_op_to_state():
    assert operators_to_state(XOp) == XKet()
    assert operators_to_state(PxOp) == PxKet()
    assert operators_to_state(Operator) == Ket()

    assert state_to_operators(operators_to_state(XOp("Q"))) == XOp("Q")
    assert state_to_operators(operators_to_state(XOp())) == XOp()

    raises(NotImplementedError, lambda: operators_to_state(XKet))


def test_state_to_op():
    assert state_to_operators(XKet) == XOp()
    assert state_to_operators(PxKet) == PxOp()
    assert state_to_operators(XBra) == XOp()
    assert state_to_operators(PxBra) == PxOp()
    assert state_to_operators(Ket) == Operator()
    assert state_to_operators(Bra) == Operator()

    assert operators_to_state(state_to_operators(XKet("test"))) == XKet("test")
    assert operators_to_state(state_to_operators(XBra("test"))) == XKet("test")
    assert operators_to_state(state_to_operators(XKet())) == XKet()
    assert operators_to_state(state_to_operators(XBra())) == XKet()

    raises(NotImplementedError, lambda: state_to_operators(XOp))
