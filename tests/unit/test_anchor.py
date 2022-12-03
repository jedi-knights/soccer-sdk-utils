from soccer_sdk_utils.anchor import get_href, get_text


class TestGetHref:
    def test_with_none(self):
        assert get_href(None) is None


class TestGetText:
    def test_with_none(self):
        assert get_text(None) is None
