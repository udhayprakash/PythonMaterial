#!/usr/bin/python3
"""
Purpose: pytest fixtures
    - For testing some scenaries, we may need arbitrary resources, 
      like temporary directory, paths, ... 
    - pytest provides them as 'fixtures'.
    - Used for Dependency Injections
    - To see the list of all (built-in and custom) pytest fixtures
        ~pytest --fixtures
"""
import pytest
import os


def test_work_with_tmp_dirs(tmpdir):
    """
    tmpdir
      Return a temporary directory path object, unique for entire test session
    """
    print('tmpdir:', tmpdir)
    assert 0


def test_work_with_tmp_files(tmp_path):
    """
    tmp_path
      Return a temporary directory path object, unique for entire test session
    """
    print('tmp_path:', tmp_path)
    assert 0


def test_output(capsys):
    """
    Enable text capturing of writes to sys.stdout and sys.stderr.
    """
    print("hello")
    out, err = capsys.readouterr()
    assert out == "hello\n"


def test_output(capsysbinary):
    """
    Enable bytes capturing of writes to sys.stdout and sys.stderr.
    """
    print("hello")
    captured = capsysbinary.readouterr()
    assert captured.out == b"hello\n"


def test_system_echo(capfd):
    """
    Enable text capturing of writes to file descriptors 1 and 2.
    """
    os.system('echo "hello"')
    captured = capfd.readouterr()
    assert captured.out == "hello\n"


def test_system_echo(capfdbinary):
    """
    Enable bytes capturing of writes to file descriptors 1 and 2.
    returns a namedtuple
    """
    os.system('echo "hello"')
    captured = capfdbinary.readouterr()
    assert captured.out == b"hello\n"
