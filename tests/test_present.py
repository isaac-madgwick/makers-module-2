from lib.present import *
import pytest

def test_present():
    present1 = Present()
    present1.wrap("test")
    with pytest.raises(Exception) as e: # <-- New code
        present1.wrap("test")
    assert str(e.value) == "A contents has already been wrapped."

    present2 = Present()
    with pytest.raises(Exception) as e:
        present2.unwrap()
    assert str(e.value) == "No contents have been wrapped."