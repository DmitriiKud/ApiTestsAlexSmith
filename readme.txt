Как установить Allure

1. установить allure в систему
scoop install allure

2. установить allure в виртуалку
pip install allure-pytest
pip show allure-pytest

3. запускать тесты с указанием диерктории для отчетов
pytest -s -v --alluredir=test_results\ tests\test_google_maps_api.py

4. составить и открыть html отчет
allure serve test_results/
