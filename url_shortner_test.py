import url_shortner

def test_check_length():
    assert len(url_shortner.shorten("www.google.com", {})) == 6


def test_check_duplicate():
    shortened_url_dict = {
        "www.google.com": "123abc"
    }
    assert url_shortner.shorten("www.google.com", shortened_url_dict) == "123abc"


def test_check_restore():
    shortened_url_dict = {
        "www.google.com": "123abc"
    }
    assert url_shortner.restore("123abc", shortened_url_dict) == "www.google.com"


def test_check_restore_none():
    shortened_url_dict = {
        "www.google.com": "123abc"
    }
    assert url_shortner.restore("123abcd", shortened_url_dict) == None


def test_check_hexadecimal():
    short_url = url_shortner.shorten("www.google.com", {})
    assert short_url.isalnum() == True
