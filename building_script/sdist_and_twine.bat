@echo off

set pyprojects_root="C:\Users\amcsparron\Desktop\Python_Projects\"
set project_full_path="%pyprojects_root%\PythonDocxAJM"

cd %project_full_path%
echo pwd changed to %cd%

REM need LICENSE.txt README.md setup.cfg setup.py - see https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
REM DONT FORGET TO UPDATE setup.py, push commit to remote, and create a new release!! THEN run this!!!
echo running sdist setup
python setup.py sdist

REM You can upload your distributions to TestPyPI using twine by specifying the --repository flag:
REM twine upload --repository testpypi dist/*
echo running twine to update pypi - token username is __token__
twine upload dist/*

REM You can tell pip to download packages from TestPyPI instead of PyPI by specifying the --index-url flag:
REM py -m pip install --index-url https://test.pypi.org/simple/ your-package
