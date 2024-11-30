# nopCommercePOM

This project implements a Page Object Model (POM) structure for automated testing of the [nopCommerce demo site](https://demo.nopcommerce.com/).

Website Link: https://demo.nopcommerce.com/

## Test Objective

The objective of this project is to implement an automated testing framework for the nopCommerce demo site using the Page Object Model (POM) design pattern. The primary goals are to:
- **Validate Functionalities:** Ensure the core functionalities of the nopCommerce site (such as user registration, login, product selection, cart management, and checkout process) work as expected.
- **Improve Test Maintenance:** Using the POM structure, separate the web page interaction logic from test scripts, making it easier to maintain and extend as the application evolves.
- **Enhance Test Reusability:** The Page Object Model promotes reusability of code for interactions with page elements, reducing duplication across test scripts.
- **Support Data-Driven Testing:** Leverage test data (stored in TestData/data.py) to run multiple test scenarios with different input sets to verify robustness and edge case handling.
- **Increase Test Coverage:** Automate critical paths such as user registration, login, product selection, cart functionality, and order processing to ensure high test coverage across essential user flows.
- **Ensure Browser Compatibility:** Run tests across multiple browsers (e.g., Chrome, Firefox) to validate cross-browser compatibility and identify potential issues.
- **Enable Continuous Testing:** Integrate with continuous integration (CI) tools to run tests automatically, ensuring that new changes do not introduce regressions or break existing functionality.

By achieving these objectives, this project aims to create a robust, maintainable, and scalable test automation framework for the nopCommerce platform.

Here's a professional `README.md` template for the GitHub repository of a project titled **"nopCommerce Site using pytest and Selenium"**. 

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Page Object Model (POM):** Separation of test logic and UI interactions. Each web page has its own corresponding class that defines methods for interacting with the elements on that page.
- **Pytest Framework:** Used to manage test cases, execute tests, and generate detailed reports.
- **Reusable Components:** Common actions like login, navigating to sections, and performing shutdown operations are encapsulated in reusable methods, improving maintainability.
- **Cross-Platform Compatibility:** The framework can be run across different environments, supporting different operating systems and web browsers.
- **Automation and Reporting:** Automation of repetitive tests with detailed reports on test results, making it easier to monitor and debug test executions.


## Tech Stack

- **Programming Language**: Python
- **Test Framework**: pytest
- **Automation Tool**: Selenium WebDriver
- **Reporting**: pytest-html
- **Browser Compatibility**: Chrome, Firefox, and optionally, Edge
- **CI/CD Integration**: GitHub Actions


## Setup and Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/nopCommercePOM.git
   cd nopCommercePOM
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory to store sensitive information such as login credentials and URLs. Example:
     ```
     BASE_URL=https://example.com
     USER_EMAIL=test@example.com
     USER_PASSWORD=yourpassword
     ```

## Running Tests

To execute tests, use the following commands:

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Generate HTML Report**:
   ```bash
   pytest --html=Reports/test_report.html
   ```

3. **Run Tests by Marker** (e.g., only "login" tests):
   ```bash
   pytest TestScripts/test_LoginPage.py::test_user_login
   ```

4. **Headless Browser Execution**:
   - You can set up tests to run in Headless mode directly in your test script.

## Project Structure
```
nopCommercePOM/
├── Jenkins/                                                                # Contains script running video and console output.
│   ├── Jenkins Console Output - Freestyle Project - nopCommercePOM #4.txt  # Console Output in Freestyle Project
│   ├── Jenkins Console Output - Pipeline Project - nopCommercePOM #2.txt   # Console Output in Pipeline Project
│   └── Script running [Jenkins].mp4                                        # Jenkins script running video for Freestyle and Pipeline Project
│   
├── PageObjects/                                                            # Contains Page Object Models for each page
│   ├── RegistrationPage.py                                                 # Handles methods and elements of the Registration page
│   ├── LoginPage.py                                                        # Handles methods and elements of the Login page
│   ├── ProductPage.py                                                      # Handles methods and elements of the Product page
│   ├── CartPage.py                                                         # Handles methods and elements of the Cart page
│   ├── CheckoutPage.py                                                     # Handles methods and elements of the Checkout page
│   └── LogoutPage.py                                                       # Handles methods and elements of the Logout page
│
├── TestData/                                                               # Stores test data for the test cases
│   └── data.py                                                             # Contains reusable test data
│
├── TestLocators/                                                           # Stores locators for web elements
│   └── locators.py                                                         # Contains locators for all web elements used in the tests
│
├── TestScripts/                                                            # Contains all test cases
│   ├── test_RegistrationPage.py                                            # Test cases for Registration page functionality
│   ├── test_LoginPage.py                                                   # Test cases for Login page functionality
│   ├── test_ProductPage.py                                                 # Test cases for Product page functionality
│   ├── test_CartPage.py                                                    # Test cases for Cart page functionality
│   ├── test_CheckoutPage.py                                                # Test cases for Checkout page functionality
│   └── test_LogoutPage.py                                                  # Test cases for Logout page functionality
│
├── requirements.txt                                                        # Lists project dependencies
│
└── README.md                                                               # Project documentation
```

## License
This project is open-source and available under the **"MIT License"**.

   ```bash
   Feel free to adjust the content based on your specific project setup!
   ```
