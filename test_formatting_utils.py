import pytest

from formatting_utils import *


class TestFormattingUtils:
    def test_contains_invalid_unicode_true(self):
        assert contains_invalid_unicode("abc�def")

    def test_contains_invalid_unicode_false(self):
        assert not contains_invalid_unicode("abcdef")

    def test_format_timestamp_valid(self):
        TIMESTAMP = "12/31/16 11:59:59 PM"
        EXPECTED = "2016-12-31T20:59:59Z"

        assert format_timestamp(TIMESTAMP) == EXPECTED

    def test_format_timestamp_invalid(self):
        TIMESTAMP = "12/31/16�11:59:59 PM"
        with pytest.raises(ValueError):
            format_timestamp(TIMESTAMP)


    def test_format_address_valid(self):
        ADDRESS = "124 Conch Street, Bikini Bottom, Pacific Ocean"

        assert format_address(ADDRESS) == ADDRESS

    def test_format_address_invalid(self):
        ADDRESS = "124 Conc� Street, Bikini Bottom, Pacific Ocean"

        with pytest.raises(ValueError):
            format_address(ADDRESS)

    def test_format_zipcode_five_digits(self):
        ZIPCODE = "12345"

        assert format_zip(ZIPCODE) == ZIPCODE

    def test_format_zipcode_less_than_five_digits(self):
        ZIPCODE = "123"
        EXPECTED = "00123"

        assert format_zip(ZIPCODE) == EXPECTED

    def test_format_zipcode_invalid(self):
        ZIPCODE = "124�"

        with pytest.raises(ValueError):
            format_zip(ZIPCODE)

    def test_format_name_english(self):
        NAME = "Patrick Star"
        EXPECTED = "PATRICK STAR"

        assert format_name(NAME) == EXPECTED

    def test_format_address_nonenglish(self):
        NAME = "エレン・イェーガー"

        assert format_name(NAME) == NAME

    def test_format_duration_valid(self):
        TIMESTAMP = "5:4:3.21"
        EXPECTED = "18243.21"

        assert format_duration(TIMESTAMP) == EXPECTED




