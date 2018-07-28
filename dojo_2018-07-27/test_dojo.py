import pytest

from dojo import parse_url


def test_google_example():
    url = "http://www.google.com/mail/user=fulano"
    result = parse_url(url)
    assert "http" == result["protocol"]
    assert "www.google.com/mail/user=fulano" == result["dpath"]
    assert "" == result["query"]

def test_google_example():
    url = "http://www.google.com/mail?user=fulano"
    result = parse_url(url)
    assert "http" == result["protocol"]
    assert "www.google.com/mail" == result["dpath"]
    assert "user=fulano" == result["query"]
    assert "" == result["user"]
    assert "" == result["password"]

def test_sadfasdfasd():
    url = "https://sadfasdfasd"
    result = parse_url(url)
    assert "https" == result["protocol"]
    assert "sadfasdfasd" == result["dpath"]
    assert "" == result["query"]
    assert "" == result["user"]
    assert "" == result["password"]

def test_reinaldo_ssh():
    url = "ssh://reinaldo@127.0.0.1"
    result = parse_url(url)
    assert "ssh" == result["protocol"]
    assert "127.0.0.1" == result["dpath"]
    assert "" == result["query"]
    assert "reinaldo" == result["user"]
    assert "" == result["password"]

@pytest.mark.parametrize("url", ["invalida", "pastel", "dojo"])
def test_invalid_url(url):
    with pytest.raises(ValueError):
        parse_url(url)

def teste_qualquercoisa():
    url = "ftp://qualquercoisa"
    result = parse_url(url)
    assert "ftp" == result["protocol"]
    assert "qualquercoisa" == result["dpath"]
    assert "" == result["query"]
    assert "" == result["user"]
    assert "" == result["password"]

def teste_usuariosenha():
    url = "ssh://usuario:senha@localhost"
    result = parse_url(url)
    assert "ssh" == result["protocol"]
    assert "localhost" == result["dpath"]
    assert "" == result["query"]
    assert "usuario" == result["user"]
    assert "senha" == result["password"]

def test_automate_bash():
    url = (
        "https://egghead.io/courses/automate-daily"
        "-development-tasks-with-bash?utm_source=d"
        "rip&utm_medium=email&utm_term=bash&utm_co"
        "ntent=automate-with-bash"
    )
    result = parse_url(url)
    assert "https" == result["protocol"]
    assert "egghead.io/courses/automate-daily-development-tasks-with-bash" \
        == result["dpath"]
    assert "utm_source=drip&utm_medium=email&utm_term=bash&utm_co" \
           "ntent=automate-with-bash" == result["query"]
    assert "" == result["user"]
    assert "" == result["password"]

def teste_usuariosenha_queried():
    url = "http://senha:usuario@localhost/?umaquery=1"
    result = parse_url(url)
    assert "http" == result["protocol"]
    assert "localhost/" == result["dpath"]
    assert "umaquery=1" == result["query"]
    assert "senha" == result["user"]
    assert "usuario" == result["password"]

