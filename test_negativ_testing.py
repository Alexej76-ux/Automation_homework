"""Teste die Funktion auf ungültige Eingaben wie `None`,
Ganzzahlen oder Listen, um sicherzustellen,
dass sie die entsprechenden Ausnahmen (Exceptions) auslöst.

Verwende ein Fixture, um Testfälle für ungültige Eingaben bereitzustellen."""

import pytest

# Beispiel-Implementierung (falls nicht importiert)
# Achtung: Für diese Tests MUSS die Funktion TypeError werfen.
def count_word_matches(text: str, target: str) -> int:
    if not isinstance(text, str) or not isinstance(target, str):
        raise TypeError("text and target must be strings")
    import re
    pattern = rfr"\b{re.escape(target)}\b"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


# -------------------------------------------------------------------
# FIXTURE: Ungültige Eingaben
# -------------------------------------------------------------------

@pytest.fixture
def invalid_input_cases():
    """Stellt ungültige Eingaben für Negative Tests bereit."""
    return [
        (None, "word", TypeError),              # 1. Text = None
        ("hello world", None, TypeError),       # 2. Target = None
        (123, "word", TypeError),               # 3. Text = int
        ("hello world", 456, TypeError),        # 4. Target = int
        (["hello", "world"], "world", TypeError),  # 5. Text = Liste
        ("hello world", ["world"], TypeError),     # 6. Target = Liste
    ]


# -------------------------------------------------------------------
# TEST: Negative Test Cases
# -------------------------------------------------------------------

@pytest.mark.parametrize("index", range(6))
def test_count_word_matches_invalid_inputs(invalid_input_cases, index):
    text, target, expected_exception = invalid_input_cases[index]

    with pytest.raises(expected_exception):
        count_word_matches(text, target)
