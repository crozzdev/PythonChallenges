import pytest
from image_search import image_search


@pytest.mark.parametrize(
    "images, term, expected",
    [
        # Provided examples from image_search.md
        (["dog.png", "cat.jpg", "parrot.jpeg"], "dog", ["dog.png"]),
        (
            ["Sunset.jpg", "Beach.png", "sunflower.jpeg"],
            "sun",
            ["Sunset.jpg", "sunflower.jpeg"],
        ),
        (["Moon.png", "sun.jpeg", "stars.png"], "PNG", ["Moon.png", "stars.png"]),
        (
            [
                "cat.jpg",
                "dogToy.jpeg",
                "kitty-cat.png",
                "catNip.jpeg",
                "franken_cat.gif",
            ],
            "Cat",
            ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"],
        ),
        # Additional edge and useful cases
        ([], "cat", []),  # empty image list
        (
            ["a.png", "b.jpg"],
            "",
            ["a.png", "b.jpg"],
        ),  # empty search term should match all (empty substring)
        (
            ["dog.png", "Dog.png", "doG.JPG"],
            "dog",
            ["dog.png", "Dog.png", "doG.JPG"],
        ),  # case-insensitive, keep order
        (
            ["weird.name.png", "another.weird.PNG", "plain.jpeg"],
            "weird.",
            ["weird.name.png", "another.weird.PNG"],
        ),  # special characters in name
        (
            ["file1.txt", "image.png", "photo.jpg"],
            "img",
            [],
        ),  # match inside name (not just extension)
    ],
)
def test_image_search_various(images, term, expected):
    assert image_search(images, term) == expected
