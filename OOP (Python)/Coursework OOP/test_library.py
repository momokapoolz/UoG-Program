import video_library as lib

def test_get_name01():
    assert lib.get_name("1") == "Tom and Jerry"

def test_get_name02():
    assert lib.get_name("asdfgh") is None

def test_get_director01():
    assert lib.get_director("1") == "Fred Quimby"

def test_get_director02():
    assert lib.get_director(69.00) == None

def test_get_rating01():
    assert lib.get_rating("1") == 4

def test_get_rating02():
    assert lib.get_rating(-5738) == -1

def test_playcount():
    assert lib.get_play_count("1") == 0





