import bs4
import pytest

from soccer_sdk_utils.tools import urljoin
from soccer_sdk_utils.tools import slugify
from soccer_sdk_utils.tools import get_text_from_anchor
from soccer_sdk_utils.tools import get_href_from_anchor


class TestSlugify:
    def test_undefined(self):
        assert slugify(None) is None

    def test_empty(self):
        assert slugify("") == ""

    def test_spaces(self):
        assert slugify("    ") == ""

    def test_all_lower_case(self):
        assert slugify("all") == "all"

    def test_all_upper_case(self):
        assert slugify("ALL") == "all"

    def test_all_mixed_case(self):
        assert slugify("All") == "all"

    def test_replaces_spaces(self):
        assert slugify("All lower case") == "all-lower-case"

    def test_removes_dot(self):
        assert slugify("All.lower.case") == "alllowercase"

    def test_removes_single_quote(self):
        assert slugify("All'lower'case") == "alllowercase"


class TestUrlJoin:
    def test_undefined_base(self):
        with pytest.raises(ValueError, match="Undefined base URL!"):
            urljoin(None, "path")

    def test_undefined_path(self):
        with pytest.raises(ValueError, match="Undefined path!"):
            urljoin("base", None)

    # def test_empty_base(self):
    #     with pytest.raises(ValueError, match="Empty base URL!"):
    #         urljoin("", "path")

    # def test_empty_path(self):
    #     with pytest.raises(ValueError, match="Empty path!"):
    #         urljoin("base", "")

    def test_base_ends_with_slash(self):
        assert urljoin("base/", "path") == "base/path"

    def test_path_starts_with_slash(self):
        assert urljoin("base", "/path") == "base/path"

    def test_base_ends_with_slash_and_path_starts_with_slash(self):
        assert urljoin("base/", "/path") == "base/path"

    def test_base_does_not_end_with_slash_and_path_does_not_start_with_slash(self):
        assert urljoin("base", "path") == "base/path"

    def test_base_ends_with_slash_and_path_does_not_start_with_slash(self):
        assert urljoin("base/", "path") == "base/path"

    def test_base_does_not_end_with_slash_and_path_starts_with_slash(self):
        assert urljoin("base", "/path") == "base/path"

    def test_base_ends_with_slash_and_path_is_empty(self):
        assert urljoin("base/", "") == "base/"

    def test_base_is_empty_and_path_starts_with_slash(self):
        assert urljoin("", "/path") == "/path"

    def test_base_is_empty_and_path_is_empty(self):
        assert urljoin("", "") == ""

    def test_base_is_empty_and_path_does_not_start_with_slash(self):
        assert urljoin("", "path") == "path"

    def test_base_is_empty_and_path_ends_with_slash(self):
        assert urljoin("", "path/") == "path/"


class TestGetHrefFromAnchor:
    def test_undefined(self):
        assert get_href_from_anchor(None) is None

    def test_anchor(self):
        html = "<a href='https://www.acme.com'>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert get_href_from_anchor(anchor) == "https://www.acme.com"

    def test_container(self):
        html = "<div><a href='https://www.acme.com'>Acme</a></div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert get_href_from_anchor(container) == "https://www.acme.com"

    def test_no_anchor(self):
        html = "<div>Acme</div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert get_href_from_anchor(container) is None

    def test_no_href(self):
        html = "<a>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert get_href_from_anchor(anchor) is None

    def test_empty_href(self):
        html = "<a href=''>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert get_href_from_anchor(anchor) is None


class TestGetTextFromAnchor:
    def test_undefined(self):
        assert get_text_from_anchor(None) is None

    def test_anchor(self):
        html = "<a href='https://www.acme.com'>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert get_text_from_anchor(anchor) == "Acme"

    def test_container(self):
        html = "<div><a href='https://www.acme.com'>Acme</a></div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert get_text_from_anchor(container) == "Acme"

    def test_no_anchor(self):
        html = "<div>Acme</div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert get_text_from_anchor(container) is None

    def test_no_text(self):
        html = "<a href='https://www.acme.com'></a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert get_text_from_anchor(anchor) is None

    def test_text_with_only_spaces(self):
        html = "<a href='https://www.acme.com'>  </a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert get_text_from_anchor(anchor) is None
