import pytest
from cutp import extract_chars, extract_fields, parse_index, parse_pos


# --------------------------------------------------
def test_extract_chars() -> None:
    """ Test extract_chars """

    assert extract_chars('', [0]) == ''
    assert extract_chars('abc', [0]) == 'a'
    assert extract_chars('abc', [2, 1, 3]) == 'cb'


# --------------------------------------------------
def test_extract_fields() -> None:
    """ Test extract_fields """

    assert extract_fields([], [0]) == []
    assert extract_fields(['abc', 'def'], [0]) == ['abc']
    assert extract_fields(['abc', 'def'], [1, 0, 2]) == ['def', 'abc']


# --------------------------------------------------
def test_parse_index() -> None:
    """ Test parse_index """

    assert parse_index('1') == 0
    assert parse_index('2') == 1

    with pytest.raises(ValueError):
        parse_index('+1')

    with pytest.raises(ValueError):
        parse_index('0')

    with pytest.raises(ValueError):
        parse_index('foo')


# --------------------------------------------------
def test_parse_pos() -> None:
    """ Test parse_pos """

    assert parse_pos('1') == [0]
    assert parse_pos('01') == [0]
    assert parse_pos('001,0003') == [0, 2]
    assert parse_pos('1-2') == [0, 1]
    assert parse_pos('1-2,9,4-6') == [0, 1, 8, 3, 4, 5]

    with pytest.raises(ValueError):
        parse_pos('')

    with pytest.raises(ValueError):
        parse_pos('0')

    with pytest.raises(ValueError):
        parse_pos('0-1')

    with pytest.raises(ValueError):
        parse_pos('+1-2')

    with pytest.raises(ValueError):
        parse_pos('1-+2')

    with pytest.raises(ValueError):
        parse_pos('a')

    with pytest.raises(ValueError):
        parse_pos('1,a')

    with pytest.raises(ValueError):
        parse_pos('1-a')

    with pytest.raises(ValueError):
        parse_pos('a-1')

    with pytest.raises(ValueError):
        parse_pos('-')

    with pytest.raises(ValueError):
        parse_pos(',')

    with pytest.raises(ValueError):
        parse_pos('1-')

    with pytest.raises(ValueError):
        parse_pos('1-1-1')

    with pytest.raises(ValueError):
        parse_pos('1-1-a')

    with pytest.raises(ValueError):
        parse_pos('1-1')

    with pytest.raises(ValueError):
        parse_pos('2-1')
