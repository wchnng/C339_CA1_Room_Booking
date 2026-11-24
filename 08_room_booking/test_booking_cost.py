import pytest
from booking_cost import calculate_booking_cost


class TestCalculateBookingCostValid:
    def test_one_night(self):
        assert calculate_booking_cost(1, 10000) == 10000

    def test_multiple_nights(self):
        assert calculate_booking_cost(3, 5000) == 15000

    def test_seven_nights_no_discount(self):
        # spec: no free night or long stay discount applies
        assert calculate_booking_cost(7, 10000) == 70000

    def test_thirty_nights(self):
        assert calculate_booking_cost(30, 5000) == 150000

    def test_zero_nightly_rate(self):
        assert calculate_booking_cost(1, 0) == 0

    def test_zero_rate_multiple_nights(self):
        assert calculate_booking_cost(5, 0) == 0

    def test_minimum_nights_minimum_rate(self):
        assert calculate_booking_cost(1, 1) == 1

    def test_returns_integer(self):
        result = calculate_booking_cost(2, 3000)
        assert type(result) is int


class TestCalculateBookingCostTypeError:
    def test_nights_as_float(self):
        with pytest.raises(TypeError):
            calculate_booking_cost(1.0, 10000)

    def test_nights_as_string(self):
        with pytest.raises(TypeError):
            calculate_booking_cost("1", 10000)

    def test_nights_as_bool_true(self):
        # bool is a subclass of int but must not be accepted
        with pytest.raises(TypeError):
            calculate_booking_cost(True, 10000)

    def test_nights_as_bool_false(self):
        with pytest.raises(TypeError):
            calculate_booking_cost(False, 10000)

    def test_rate_as_float(self):
        with pytest.raises(TypeError):
            calculate_booking_cost(1, 100.0)

    def test_rate_as_string(self):
        with pytest.raises(TypeError):
            calculate_booking_cost(1, "100")

    def test_rate_as_bool(self):
        with pytest.raises(TypeError):
            calculate_booking_cost(1, True)

    def test_both_wrong_type(self):
        with pytest.raises(TypeError):
            calculate_booking_cost(1.0, 100.0)


class TestCalculateBookingCostValueError:
    def test_nights_zero(self):
        with pytest.raises(ValueError):
            calculate_booking_cost(0, 10000)

    def test_nights_negative(self):
        with pytest.raises(ValueError):
            calculate_booking_cost(-1, 10000)

    def test_nights_thirty_one(self):
        with pytest.raises(ValueError):
            calculate_booking_cost(31, 10000)

    def test_nights_large(self):
        with pytest.raises(ValueError):
            calculate_booking_cost(100, 10000)

    def test_rate_negative(self):
        with pytest.raises(ValueError):
            calculate_booking_cost(1, -1)

    def test_rate_large_negative(self):
        with pytest.raises(ValueError):
            calculate_booking_cost(1, -500)
