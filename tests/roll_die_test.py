import importlib
import re
import roll_die

def test_random_input():
    assert 'random' in importlib.sys.modules

def test_roll_die_1(capsys, monkeypatch):
    inputs, output = ("1", "1")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    roll_die.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_roll_die_6(capsys, monkeypatch):
    inputs, output = ("6", range(1, 7))
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    roll_die.main()
    captured = capsys.readouterr()
    inrange = False
    for i in output:
        if str(i) in captured.out:
            inrange = True
    assert inrange