import url_shortner

def test_check_length():
    assert len(url_shortner.shorten("www.google.com", {})) == 6
