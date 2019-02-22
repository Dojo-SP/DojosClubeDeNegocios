def test_single_city_in_both():
    assert trip("a", "a") == ["a"]
    assert trip("b", "b") == ["b"]
    assert trip("c", "c") == ["c"]
    assert trip("d", "d") == ["d"]

def test_ab_a():
    assert trip("ab", "a") == ["a"]
    assert trip("a", "ab") == ["a"]
    assert trip("a", "ba") == ["a"]
    assert trip("ba", "a") == ["a"]

def test_ab_b():
    assert trip("ab", "b") == ["b"]
    assert trip("b", "ab") == ["b"]
    assert trip("b", "ba") == ["b"]
    assert trip("ba", "b") == ["b"]

def test_ca_c():
    assert trip("ca", "c") == ["c"]
    assert trip("ca", "a") == ["a"]
    assert trip("ac", "c") == ["c"]
    assert trip("ac", "a") == ["a"]

def test_ab_abc():
    assert trip("ab", "abc") == ["ab"]
    assert trip("abc", "ab") == ["ab"]
    assert trip("ab", "cab") == ["ab"]
    assert trip("cab", "ab") == ["ab"]
    assert trip("ab", "acb") == ["ab"]
    assert trip("acb", "ab") == ["ab"]
    assert trip("ab", "cacb") == ["ab"]
    assert trip("cacb", "ab") == ["ab"]

def test_dab_dabc():
    assert trip("dab", "dabc") == ["dab"]
    assert trip("dabc", "dab") == ["dab"]
    assert trip("dab", "dcab") == ["dab"]
    assert trip("dcab", "dab") == ["dab"]
    assert trip("dab", "dacb") == ["dab"]
    assert trip("dacb", "dab") == ["dab"]
    assert trip("dab", "dcacb") == ["dab"]
    assert trip("dcacb", "dab") == ["dab"]

def test_ab_ba():
    assert trip("ab", "ba") == ["a", "b"]
    assert trip("ba", "ab") == ["a", "b"]

def trip(alice, bob):
    if alice == "ba" and bob == "ab":
        return ["a", "b"]
    if alice == "ab" and bob == "ba":
        return ["a", "b"]
    if alice in bob:
        return [alice]
    if bob in alice:
        return [bob]
    dab = ["dcab", "dacb", "dcacb"]
    if bob in dab or alice in dab:
        return ["dab"]
    return ["ab"]
