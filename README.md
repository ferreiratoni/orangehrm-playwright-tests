![CI](https://github.com/ferreiratoni/orangehrm-playwright-tests/actions/workflows/python-tests.yml/badge.svg)

# OrangeHRM – E2E UI Tests with Playwright and Visual AI (Applitools)

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


### 👁️ Visual AI Testing with Applitools

This project includes a visual regression test using [Applitools Eyes](https://applitools.com/), which applies AI to validate that the UI remains visually consistent across changes.

#### ✅ What it does:

- Takes a snapshot of the login page
- Logs into the application
- Takes a snapshot of the dashboard page
- Sends both snapshots to the Applitools dashboard
- Detects visual differences using AI (like moved buttons, missing labels, or layout shifts)

---

### 🔐 CI Setup for Applitools

To run visual tests using Applitools on GitHub Actions, you need to securely provide your API key.

#### 📌 Steps:

1. Go to your GitHub repository:  
   [https://github.com/ferreiratoni/orangehrm-playwright-tests](https://github.com/ferreiratoni/orangehrm-playwright-tests)

2. Navigate to:  
   `Settings > Secrets and variables > Actions`

3. Click on **“New repository secret”** and add:

| Name                 | Value                       |
|----------------------|-----------------------------|
| `APPLITOOLS_API_KEY` | Your API key from Applitools |

4. Save it.  
   Your GitHub Actions workflow will automatically use this key when running tests.

> 🔒 This keeps your credentials safe and hidden from the codebase.


#### 🧪 How to run the test:

```bash
pytest tests/test_login_visual.py
```

#### 📌 Requirements:

- A free [Applitools account](https://applitools.com/)
- A `.env` file at the project root with your API key:

```
APPLITOOLS_API_KEY=your_key_here
```

> This test demonstrates how visual validation can be added to end-to-end tests without relying on pixel-perfect assertions or manual checks.





This new test validates the visibility of the logged-in user's personal details:

- Logs in using valid admin credentials
- Navigates to the “My Info” section
- Checks if the first name input is visible and filled

> Test File: `tests/test_view_my_info.py`


### 🔗 Visual Test Example

This test was executed using [Applitools Eyes](https://applitools.com/) and passed successfully.

👉 [View test result (Applitools Dashboard)](https://eyes.applitools.com/app/test-results/00000251650774888792?accountId=x3tirYl5wEu7WPVVe4kErA__&display=details&top=00000251650774888792%283%29)



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
│ ├── test_login_success.py
│ ├── test_login_failure.py
│ ├── test_view_my_info.py
│ └── test_login_visual.py
├── requirements.txt
├── pytest.ini
├── .env # <- not committed to Git
└── README.md
```

---

## 🚀 Getting Started

For local setup and execution steps, please refer to the [GETTING_STARTED.md](GETTING_STARTED.md) guide.