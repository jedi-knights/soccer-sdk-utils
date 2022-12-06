import pytest

from soccer_sdk_utils.gender import Gender, string_to_gender


class TestStringToGender:
    def test_undefined(self):
        with pytest.raises(ValueError, match="Undefined gender string!"):
            string_to_gender(None)

    def test_empty(self):
        with pytest.raises(ValueError, match="Empty gender string!"):
            string_to_gender("")

    def test_spaces(self):
        with pytest.raises(ValueError, match="Empty gender string!"):
            string_to_gender("    ")

    def test_all_lower_case(self):
        assert string_to_gender("all") == Gender.All

    def test_all_upper_case(self):
        assert string_to_gender("ALL") == Gender.All

    def test_all_mixed_case(self):
        assert string_to_gender("All") == Gender.All

    def test_m_lower_case(self):
        assert string_to_gender("m") == Gender.Male

    def test_f_lower_case(self):
        assert string_to_gender("f") == Gender.Female

    def test_m_upper_case(self):
        assert string_to_gender("M") == Gender.Male

    def test_f_upper_case(self):
        assert string_to_gender("F") == Gender.Female

    def test_male_lower_case(self):
        assert string_to_gender("male") == Gender.Male

    def test_female_lower_case(self):
        assert string_to_gender("female") == Gender.Female

    def test_male_upper_case(self):
        assert string_to_gender("MALE") == Gender.Male

    def test_female_upper_case(self):
        assert string_to_gender("FEMALE") == Gender.Female

    def test_male_mixed_case(self):
        assert string_to_gender("Male") == Gender.Male

    def test_female_mixed_case(self):
        assert string_to_gender("Female") == Gender.Female

    def test_invalid(self):
        with pytest.raises(ValueError, match="Invalid gender string 'invalid'!"):
            string_to_gender("invalid")
