import bs4

from soccer_sdk_utils.anchor import get_href, get_text


class TestGetHref:
    def test_with_none(self):
        # Arrange
        tag = None

        # Act
        actual = get_href(tag)

        # Assert
        assert actual is None

    def test_with_non_anchor(self):
        # Arrange
        tag = bs4.element.Tag(name="div")

        # Act
        actual = get_href(tag)

        # Assert
        assert actual is None

    def test_with_anchor_without_href(self):
        # Arrange
        tag = bs4.element.Tag(name="a")

        # Act
        actual = get_href(tag)

        # Assert
        assert actual is None

    def test_with_anchor_with_empty_href(self):
        # Arrange
        tag = bs4.element.Tag(name="a")
        tag["href"] = ""

        # Act
        actual = get_href(tag)

        # Assert
        assert actual is None

    def test_with_anchor_with_href(self):
        # Arrange
        tag = bs4.element.Tag(name="a")
        tag["href"] = "https://example.com"

        # Act
        actual = get_href(tag)

        # Assert
        assert actual == "https://example.com"


class TestGetText:
    def test_with_none(self):
        # Arrange
        tag = None

        # Act
        actual = get_text(tag)

        # Assert
        assert actual is None

    def test_with_non_anchor(self):
        # Arrange
        tag = bs4.element.Tag(name="div")

        # Act
        actual = get_text(tag)

        # Assert
        assert actual is None

    def test_with_anchor_without_text(self):
        # Arrange
        tag = bs4.element.Tag(name="a")

        # Act
        actual = get_text(tag)

        # Assert
        assert actual is None

    def test_with_anchor_with_empty_text(self):
        # Arrange
        tag = bs4.element.Tag(name="a")
        tag.string = ""

        # Act
        actual = get_text(tag)

        # Assert
        assert actual is None

    def test_with_anchor_with_text(self):
        # Arrange
        tag = bs4.element.Tag(name="a")
        tag.string = "Example"

        # Act
        actual = get_text(tag)

        # Assert
        assert actual == "Example"

