import pytest
from booking_refund import is_refundable


class TestIsRefundableValid:
    def test_flexible_exactly_48_hours(self):
        # boundary: exactly 48 hours qualifies
        assert is_refundable(48, True) is True

    def test_flexible_49_hours(self):
        assert is_refundable(49, True) is True

    def test_flexible_large_hours(self):
        assert is_refundable(1000, True) is True

    def test_flexible_47_hours_not_refundable(self):
        # less than 48 hours = not refundable even with flexible rate
        assert is_refundable(47, True) is False

    def test_flexible_zero_hours(self):
        assert is_refundable(0, True) is False

    def test_non_flexible_48_hours(self):
        # non-flexible rate is never refundable
        assert is_refundable(48, False) is False

    def test_non_flexible_zero_hours(self):
        assert is_refundable(0, False) is False

    def test_non_flexible_large_hours(self):
        assert is_refundable(1000, False) is False

    def test_returns_bool_true(self):
        result = is_refundable(48, True)
        assert type(result) is bool

    def test_returns_bool_false(self):
        result = is_refundable(47, True)
        assert type(result) is bool


class TestIsRefundableTypeError:
    def test_hours_as_float(self):
        with pytest.raises(TypeError):
            is_refundable(48.0, True)

    def test_hours_as_string(self):
        with pytest.raises(TypeError):
            is_refundable("48", True)

    def test_hours_as_bool(self):
        # bool is subclass of int but must not be accepted as hours
        with pytest.raises(TypeError):
            is_refundable(True, True)

    def test_flexible_rate_as_int(self):
        # int is not a valid bool
        with pytest.raises(TypeError):
            is_refundable(48, 1)

    def test_flexible_rate_as_zero(self):
        with pytest.raises(TypeError):
            is_refundable(48, 0)

    def test_flexible_rate_as_string(self):
        with pytest.raises(TypeError):
            is_refundable(48, "True")

    def test_both_wrong_type(self):
        with pytest.raises(TypeError):
            is_refundable(48.0, 1)


class TestIsRefundableValueError:
    def test_hours_negative_one(self):
        with pytest.raises(ValueError):
            is_refundable(-1, True)

    def test_hours_large_negative(self):
        with pytest.raises(ValueError):
            is_refundable(-100, True)

    def test_hours_negative_non_flexible(self):
        with pytest.raises(ValueError):
            is_refundable(-1, False)
