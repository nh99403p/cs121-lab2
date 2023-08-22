import re
import circle_area

def test_circle_area_three(capsys, monkeypatch):
    inputs, output = ("3", "28.27")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    circle_area.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_circle_area_zero(capsys, monkeypatch):
    inputs, output = ("0", "0")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    circle_area.main()
    captured = capsys.readouterr()
    assert output in captured.out