def image_search(images: list[str], term: str) -> list[str]:
    term_lower = term.lower()
    return [image for image in images if term_lower in image.lower()]
