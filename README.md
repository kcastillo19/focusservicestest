# focusservicestest
automated scripts for Focus web Page

Requirements:
1. Google Chrome Versión 89 (Build oficial) (64 bits)
2. Git Clone or unzip Downloaded files under the correct path
3. Pycharm Edition 2020.1.1 or any othe Python IDE
4. Python v3.8 installed and selected as interpreter
5. Have a Github account


Setup Instructions for local environment:
1. Install Python from https://www.python.org/downloads/
2. Configure environment variables (path) pointing to current python folder in use for example: C:\Users\username\AppData\Local\Programs\Python\Python38-32
3. Open a cmd console as administrator and run pip install selenium from C:\Users\username\
4. Run pip install pytest from C:\Users\username
5. Install gitbash or Github Desktop(https://docs.github.com/es/desktop/installing-and-configuring-github-desktop/installing-github-desktop)
6. git clone https://github.com/kcastillo19/focusservicestest.git in the correct path: C:\Users\username\PycharmProjects\
7. Open the project in Pycharm IDE from File - Open - C:\Users\username\PycharmProjects\ - Select "focusservicestest" - Click OK
8. Go to Interpreter settings and select the correct interpreter for python version 
9. Go to Edit Configurations - click on + - select Python tests and search the location for C:\Users\username\PycharmProjects\focusservicestest\tests\test_search.py

Run scrip
10. Set Chrome driver in the correct path and must match with the path set in the conftest.py "/usr/local/bin/chromedriver"
11. Open a cmd console as administrator and run cd C:\Users\username\PycharmProjects\focusservicestest\tests
12. run py.test test_search.py -v -s

