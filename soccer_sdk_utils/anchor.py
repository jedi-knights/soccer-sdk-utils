def get_href(anchor):
    if anchor is None:
        return None

    if anchor.name != "a":
        anchor = anchor.find("a")

    href = anchor.get("href")
    if href is None:
        return None

    href = href.strip()
    if len(href) == 0:
        return None

    return href


def get_text(anchor):
    if anchor is None:
        return None

    if anchor.name != "a":
        anchor = anchor.find("a")

    if anchor is None:
        return None

    text = anchor.text.strip()
    if len(text) == 0:
        return None

    return text
