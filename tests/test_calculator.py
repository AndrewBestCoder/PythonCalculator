import pytest

from Calculator import CalculatorCalculation


@pytest.mark.parametrize(
    "form, res",
    [
        ("2*2", "4"),
        ("10*10", "100"),
        ("2/2", "1.0"),
        ("40/20", "2.0"),
        ("10+2", "12"),
        ("50+40", "90"),
        ("70-30", "40"),
        ("99-9", "90"),
        ("(2+2)*2", "8"),
        ("3+5*2*(50/10)", "53.0"),
    ],
)
def test_calculate(form: str, res: str) -> None:
    result, error = CalculatorCalculation.calculate_string(form)
    assert error == ""
    assert result == res


@pytest.mark.parametrize(
    "form, res", [("2", "4"), ("32", "1024"), ("3", "9"), ("10", "100")]
)
def test_calculate_power(form: str, res: str) -> None:
    result, error = CalculatorCalculation.calculate_power_string(form)
    assert error == ""
    assert result == res


@pytest.mark.parametrize(
    "form, res",
    [
        ("2/0", "Zero division error"),
        ("509999/0", "Zero division error"),
        ("1+", "Syntax error"),
        ("*2", "Syntax error"),
        ("()", "Syntax error"),
        ("50()", "Syntax error"),
        ("35*2+4-", "Syntax error"),
    ],
)
def test_errors_syntax_zero_division(form: str, res: str) -> None:
    result, error = CalculatorCalculation.calculate_string(form)
    assert error == res
    assert result == ""


@pytest.mark.parametrize(
    "form, res",
    [
        ("999999999999", "Too large"),
        ("1000000000000", "Too large"),
    ],
)
def test_errors_too_large(form: str, res: str) -> None:
    result, error = CalculatorCalculation.calculate_string(form)
    assert error == res
    assert result == ""
