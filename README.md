## Under Contruction

### Setting up Virtual Environment (first time in repo)

1. `python3 -m pip install --user --upgrade pip` (ensure you have pip installed)

- validate `python3 -m pip --version`

2. `python3 -m pip install --user virtualenv` (ensure you have virtual env installed using pip)
3. `python3 -m venv env` (creating the environment)

- Never use python outside of a virtual environment. I promise you, you will have a terrible time if you do this. Doing so will polute your global system python packages and you risk breaking python/functionalities of your os altogether.
- You should exclude your virtual environment directory from your version control system using .gitignore

4. `source env/bin/activate` (your shell prompt should indicate venv)

- you can confirm you're in the virtual environment by checking the location of your python interpreter, it should point to your `env` directory. `which python` if done correctly will point to .../env/bin/python

5. `deactivate` to leave the virtual environment
6. `pip freeze` can export a list of all installed packages and their versions from the virtual environment creating your `requirements.txt`
7. `pip3 install -r requirements.txt` (installing dependencies for this application)
