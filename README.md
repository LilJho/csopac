# CSOPAC

Installation Process
1. Create virtual environment in local machine.
2. Clone the repository inside the virtual machine.
3. Activate the virtual environment.
4. Install dependencies in the requirements.txt <br>
```pip install -r requirements.txt```
5. Create migrations then migrate.<br>
```python manage.py makemigrations```
```python manage.py migrate```
6. Run the server.<br>
```python manage.py  runserver```

