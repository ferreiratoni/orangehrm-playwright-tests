# Getting Started

This document helps you set up and run the automated UI tests for OrangeHRM using Playwright and Python.

---

## ✅ Prerequisites

- Python 3.10 or higher
- Git
- Recommended: Python virtual environment

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/ferreiratoni/orangehrm-playwright-tests.git
cd orangehrm-playwright-tests
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Install Playwright browsers**

```bash
playwright install
```

---

## ▶️ Running Tests

To run all tests with `pytest`:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_login_success.py
```

---

## 🧪 Test Reports (Optional)

To generate HTML reports:

```bash
pip install pytest-html
pytest --html=report.html
```

### ▶️ Running the "View My Info" test

To execute the newly added test:

```bash
pytest tests/test_view_my_info.py


---

## 🤝 Contributing

Feel free to fork this repository and add more test scenarios or enhancements.

---

## 📎 Notes

- This project is for educational and portfolio purposes only.
- OrangeHRM Demo site is used as a public testing sandbox.

---

## 👤 Author

Made by [Antonio Ferreira](https://github.com/ferreiratoni) – QA & Automation Enthusiast.