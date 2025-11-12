

import pytest
def count_word_matches(text, target):

    """
    Zählt, wie oft ein Zielwort als eigenständiges Wort im Text vorkommt.
    Die Übereinstimmung erfolgt ohne Berücksichtigung der Groß-/Kleinschreibung,
    und Wörter sind durch Leerzeichen getrennt.

    Args:
        text (str): Eingabetext, in dem gesucht wird.
        target (str): Das gesuchte Wort.

    Returns:
        int: Anzahl der Vorkommen des Zielwortes als eigenständiges Wort.
    """
    if not text or not target:
        return 0

    # Text in Wörter aufteilen und für case-insensitive Vergleich in
    # Kleinbuchstaben umwandeln
    words = text.lower().split()
    target = target.lower()

    # Eigenständige Vorkommen des Zielwortes zählen
    return words.count(target)


def test_count_word_matches():
    ergebnis = count_word_matches("text text text","text" )
    assert ergebnis == 3

def test_umpf(text = "text text text",target = "text", ergebnis = 3):
    testergebnis = count_word_matches(text,target)
    assert ergebnis == testergebnis

@pytest.mark.parametrize("text,target,ergebnis", [
    ("text text text","text" ,3),
    ("text1 text1 text1","text1" ,3)
])
def test_count_word_matches_simpleParameter(text,target, ergebnis):
    testergebnis = count_word_matches(text,target)
    assert (ergebnis == testergebnis)

import pytest
from your_module_name import count_word_matches   # <-- replace with your real module name


@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1),           # basic match
        ("Dog dog DOG dOg", "dog", 1),                  # mixed-case
        ("Hello world", "world", 1),                    # simple match
        ("hello hello HELLO", "hello", 3),              # repeated mixed-case
        ("No matches here", "yes", 0),                  # no match
        ("catcat cat catdog", "cat", 1),                # only standalone match
        ("a a a", "a", 3),                              # single-character words
    ]
)
def test_count_word_matches_basic(text, target, expected):
    assert count_word_matches(text, target) == expected

import re

def count_word_matches(text: str, target: str) -> int:
    pattern = rfr"\b{re.escape(target)}\b"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))
