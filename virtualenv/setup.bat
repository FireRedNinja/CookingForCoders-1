cd setuptools-32.3.1
python ez_setup.py
easy_install pip
cd ..
pip install virtualenv
pip install virtualenvwrapper-win
mkvirtualenv cookingForCoders
workon cookingForCoders
pip install -r requirements.txt
pause