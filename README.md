# OrangeHRM – E2E Automated Tests with Playwright and Python

This repository contains end-to-end UI automation tests for [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/), written in Python using [Playwright](https://playwright.dev/python/).

The project structure is organized with best practices in mind, enabling easy maintenance, scalability, and integration into a CI/CD pipeline. All test cases are written using natural language to simulate real-world user behavior.

---

## 🔍 Features

- ✅ Automated login tests (successful & failed attempts)
- 🧠 Natural language test scenarios
- 📁 Modular test structure with separation of concerns
- 🧪 Easy-to-run with `pytest`
- 🌐 Ready to scale for future test coverage

### ✅ New Test Added: View Personal Info

This new test validates the visibility of the logged-in user's personal details:

- Logs in using valid admin credentials
- Navigates to the “My Info” section
- Checks if the first name input is visible and filled

> Test File: `tests/test_view_my_info.py`



---

## 🛠 Tech Stack

- **Playwright** (Python)
- **Pytest**
- **Python 3.10+**

---

## 📂 Project Structure

```
orangehrm-tests/
├── tests/
│   ├── test_login_success.py
│   └── test_login_failure.py
|   └── test_login_failure.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🚀 Getting Started

For local setup and execution steps, please refer to the [GETTING_STARTED.md](GETTING_STARTED.md) guide.