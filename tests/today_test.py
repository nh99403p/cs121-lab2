import importlib
import re
import today

def test_datetime_input():
    assert 'datetime' in importlib.sys.modules

def test_today(capsys):
    if 'datetime' in importlib.sys.modules:
        del importlib.sys.modules["datetime"]
    import datetime
    today.main()
    captured = capsys.readouterr()
    assert str(datetime.date.today()) in captured.out

def test_now(capsys):
    if 'datetime' in importlib.sys.modules:
        del importlib.sys.modules["datetime"]
    import datetime
    today.main()
    captured = capsys.readouterr()
    assert str(datetime.datetime.now()) in captured.out

def test_now_formatted(capsys):
    if 'datetime' in importlib.sys.modules:
        del importlib.sys.modules["datetime"]
    import datetime
    today.main()
    captured = capsys.readouterr()
    assert str(datetime.datetime.now().strftime("%d/%m/%y")) in captured.out

def test_now_formatted_time(capsys):
    if 'datetime' in importlib.sys.modules:
        del importlib.sys.modules["datetime"]
    import datetime
    today.main()
    captured = capsys.readouterr()
    assert str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M")) in captured.out

def test_tz(capsys):
    if 'datetime' in importlib.sys.modules:
        del importlib.sys.modules["datetime"]
    import datetime
    today.main()
    captured = capsys.readouterr()
    assert str(datetime.datetime.now().astimezone().tzinfo) in captured.out