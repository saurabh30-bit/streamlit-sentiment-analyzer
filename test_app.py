from utils import clean_text

def test_clean_text():
    assert clean_text('hello http://example.com') == 'hello'
    print('Tests pass!')
