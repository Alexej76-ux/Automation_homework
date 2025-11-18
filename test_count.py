import pytest

@pytest.fixture
def edge_case_inputs():
    """Stellt typische Randfall-Kombinationen aus Text, Target und erwarteter Ausgabe bereit."""
    return [
        ("", "word", 0),                   # 1. Leerer Text
        ("hello world", "", 0),            # 2. Leeres Zielwort
        ("", "", 0),                       # 3. Alles leer
        ("hello   world", "world", 1),     # 4. Mehrere Leerzeichen
        ("  cat  ", "cat", 1),             # 5. Führende/nachgestellte Leerzeichen
        ("cat,dog cat", "cat", 1),         # 6. Satzzeichen -> kein Word-Boundary
        ("x y z", "x", 1),                 # 7. Einzelzeichen
    ]


def count_word_matches(text, target):
    pass


@pytest.mark.parametrize("index", range(7))
def test_count_word_matches_edge_cases(edge_case_inputs, index):
    text, target, expected = edge_case_inputs[index]
    result =count_word_matches(text, target)
    assert result == expected


@pytest.fixture
def edge_case_inputs():
    """Stellt typische Randfall-Kombinationen bereit."""
    return [
        ("", "word", 0),                     # leerer Text
        ("hello world", "", 0),              # leeres Zielwort
        ("", "", 0),                         # beides leer
        ("hello   world", "world", 1),       # mehrere Leerzeichen
        ("  cat  ", "cat", 1),               # führende/nachgestellte Spaces
        ("cat,dog cat", "cat", 1),           # Interpunktion -> nur 1 echtes Wort
        ("x y z", "x", 1),                   # einzelnes Zeichen
    ]
@pytest.mark.parametrize("index", range(7))
def test_count_word_matches_edge_cases(edge_case_inputs, index):
    text, target, expected = edge_case_inputs[index]
    result = count_word_matches(text, target)
    assert result == expected