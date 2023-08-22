import importlib
import re
import sys_info

def test_os_input():
    assert 'os' in importlib.sys.modules

def test_sys_input():
    assert 'sys' in importlib.sys.modules

def test_version(capsys):
    if 'sys' in importlib.sys.modules:
        del importlib.sys.modules["sys"]
    import sys
    sys_info.main()
    captured = capsys.readouterr()
    assert str(sys.version) in captured.out

def test_platform(capsys):
    if 'sys' in importlib.sys.modules:
        del importlib.sys.modules["sys"]
    import sys
    sys_info.main()
    captured = capsys.readouterr()
    assert str(sys.platform) in captured.out

def test_login(capsys):
    if 'os' in importlib.sys.modules:
        del importlib.sys.modules["os"]
    import os
    sys_info.main()
    captured = capsys.readouterr()
    assert str(os.getlogin()) in captured.out

def test_cwd(capsys):
    if 'os' in importlib.sys.modules:
        del importlib.sys.modules["os"]
    import os
    sys_info.main()
    captured = capsys.readouterr()
    assert str(os.getcwd()) in captured.out

def test_listdir(capsys):
    if 'os' in importlib.sys.modules:
        del importlib.sys.modules["os"]
    import os
    sys_info.main()
    captured = capsys.readouterr()
    assert str(os.listdir()) in captured.out

def test_listdir_parent(capsys):
    if 'os' in importlib.sys.modules:
        del importlib.sys.modules["os"]
    import os
    sys_info.main()
    captured = capsys.readouterr()
    assert str(os.listdir("..")) in captured.out

def test_listdir_root(capsys):
    if 'os' in importlib.sys.modules:
        del importlib.sys.modules["os"]
    import os
    sys_info.main()
    captured = capsys.readouterr()
    assert str(os.listdir("/")) in captured.out