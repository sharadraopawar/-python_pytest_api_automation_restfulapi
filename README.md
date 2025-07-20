
# 🔗 Python Pytest API Automation – RESTful API

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Tested_with-Pytest-yellow?logo=pytest)](https://docs.pytest.org/)
[![API](https://img.shields.io/badge/API-Tested-007ec6)](https://restful-api.dev/)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## 📌 Overview

This project is a **modular, scalable API automation framework** built using:

- ✅ **Python 3.10**
- ✅ **Pytest** (with fixtures, parameterization, and modular tests)
- ✅ **Requests** library
- ✅ **Logging**, Assertions, and Clean Reporting
- ✅ Compatible with **CI/CD** like GitHub Actions / Azure DevOps

It tests **CRUD operations** on [`https://restful-api.dev`](https://restful-api.dev) demo API.

---

## 🧱 Folder Structure

```

.
├── tests/                  # Test cases for API endpoints
├── configs/                # Config variables like base URL, endpoints
├── utils/                  # Logger and helper utilities
├── conftest.py             # Pytest fixtures: session, base\_url
├── requirements.txt        # Dependencies
├── README.md

````

---

## 🚀 How to Run Tests

▶️ Run all tests:

```bash
pytest -v --tb=short
````

▶️ Generate HTML report (if using pytest-html):

```bash
pytest -v --html=reports/api_result.html
```

---

## ⚙️ Features

* 📡 **CRUD testing** for RESTful API endpoints
* 🧪 **Pytest fixtures** (session, base URL, object creation)
* 🪵 **Custom logger** for better debugging
* ✅ Simple `assert`-based validation
* 🚀 Ready for CI/CD pipelines (Azure, GitHub)

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Ideal For

* SDET interviews with API knowledge expectation (Google, Amazon, etc.)
* QA engineers learning API testing in a practical, hands-on way
* Beginners to advanced learners building real-world projects

---

## 🙋‍♂️ Author

Made with `pytest.mark.rest_assured` by [Sharadrao Pawar](https://github.com/sharadraopawar)

```


```
