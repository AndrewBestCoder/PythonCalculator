import pytest

from Calculator import Calculator


@pytest.mark.parametrize("form, res", [("2*2", "4"), ("10*10", "100")])
def test_multiply(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("2/2", "1.0"), ("50/10", "5.0")])
def test_divide(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("2+2", "4"), ("10+10", "20")])
def test_add(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("2-2", "0"), ("50-40", "10")])
def test_minus(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("1049124", "0"), ("10928", "0")])
def test_clear(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("C")
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("1049124", "104912"), ("10928", "1092")])
def test_delete(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("DEL")
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("2", "4"), ("16", "256")])
def test_power(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("X^2")
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize("form, res", [("(2+2)*2", "8"), ("3+5*2*(50/10)", "53.0")])
def test_hooks(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.formula == res


@pytest.mark.parametrize(
    "form, res", [("2/0", "Zero Division Error"), ("509999/0", "Zero Division Error")]
)
def test_zeroDivision(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.errormessage == res


@pytest.mark.parametrize(
    "form, res",
    [
        ("1+", "Syntax Error"),
        ("*2", "Syntax Error"),
        ("()", "Syntax Error"),
        ("50()", "Syntax Error"),
        ("35*2+4-", "Syntax Error"),
    ],
)
def test_syntaxError(form, res):
    calc = Calculator()
    calc.Calculate(form)
    calc.Calculate("=")
    assert calc.errormessage == res


@pytest.mark.parametrize(
    "form, res", [("999999", "Too large"), ("1000000", "Too large")]
)
def test_largeError(form, res):
    calc = Calculator()
    calc.Calculate(form)
    for i in range(10):
        calc.Calculate("X^2")
    calc.Calculate("=")
    assert calc.errormessage == res
