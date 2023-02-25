1. Clone Project
2. Create venv (Settings> Add Interpreter) and activate: venv/Scripts/activate
3. Use <pip list> to see the local libraries
4. Install Pytest: pip install pytest
5. Upgrade pip: python.exe -m pip install --upgrade pip
6. Install requirements: pip install -r requirements.txt
7. To create requirements.txt use: pip freeze > requirements.txt
8. Run tests, e.g. by marker: pytest -m login
9. or by test name: pytest -k <test_name>
10. Install request library: pip install requests

Allure:
Add allure package to the venv:
>>  pip install allure-pytest    

Add allure results to allure_results folder
>> pytest -v -s tests/users/test_users.py --alluredir=allure_results 

Run Allure report:
>> allure serve allure_results 

