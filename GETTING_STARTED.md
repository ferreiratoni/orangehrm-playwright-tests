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

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**

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

### ▶️ Running the "View My Info" test

To execute the test that verifies the personal info screen:

```bash
pytest tests/test_view_my_info.py
```

---

### 👁️ Running the Visual AI Test (Applitools)

To run the visual regression test powered by Applitools:

```bash
pytest tests/test_login_visual.py
```

Make sure you have a `.env` file at the root of the project with your Applitools API key:

```
APPLITOOLS_API_KEY=your_applitools_key_here
```

> Create a free account at [applitools.com](https://applitools.com/) to get your API key.

---

## 🧪 Test Reports (Optional)

To generate HTML reports:

```bash
pip install pytest-html
pytest --html=report.html
```

---

## 🤝 Contributing

Feel free to fork this repository and add more test scenarios or enhancements.

---

## 📎 Notes

- This project is for educational and portfolio purposes only.
- OrangeHRM Demo site is used as a public testing sandbox.


---

## 💡 Tip: Using PyCharm?

You can run tests directly in PyCharm:

- Right-click a test file (e.g. `test_login_visual.py`) and select **"Run"**
- To activate your virtual environment, make sure your interpreter is set in:
  `File > Settings > Python Interpreter`
- To view `.env` variables automatically, install the **EnvFile** plugin or set them manually under:
  `Run > Edit Configurations > Environment variables`



---

## 👤 Author

Made by [Antonio Ferreira](https://github.com/ferreiratoni) – QA & Automation Enthusiast.