

from duration_formatter import format


def test_format_500():
	assert format(500) == "8:20"


def test_format_4000():
	assert format(4000) == "1:06:40"


def test_format_1():
	assert format(1) == "0:01"


def test_format_5555():
	assert format(5555) == "1:32:35"


def test_format_99999():
	assert format(99999) == "27:46:39"

