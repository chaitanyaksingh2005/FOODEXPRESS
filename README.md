# FoodExpress

A small FoodExpress project used to demonstrate Git, GitHub, Continuous Integration, and Jenkins.

## Current Project

The project currently contains:

- `cart.py` - FoodExpress cart calculation functions
- `test_cart.py` - Automated tests for the cart functions

## Testing

Tests are executed using pytest.

```bash
python -m pytest
Jenkins automatic CI trigger enabled.

# FoodExpress

FoodExpress is a small Python-based project created to understand and demonstrate Git, GitHub, Continuous Integration (CI), and Jenkins.

## Project Structure

```text
FoodExpress/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── README.md
├── Jenkinsfile
├── cart.py
└── test_cart.py

Git and GitHub

The project is maintained using Git and hosted on GitHub.

The main branch used for the project is:
Continuous Integration with GitHub Actions

A GitHub Actions workflow is configured in:

.github/workflows/ci.yml
Jenkins CI

Jenkins is configured to use the FoodExpress GitHub repository.

Jenkins obtains the pipeline instructions from:Jenkinsfile

The Jenkins pipeline performs the following stages:

Checkout the FoodExpress repository.
Install pytest.
Run the project's tests.

The tests are executed using:

The current test suite contains 3 tests, and the Jenkins build successfully produces:
3 passed
Finished: SUCCESS

Automatic Jenkins Trigger

Jenkins is configured with Poll SCM to check the GitHub repository for changes.

When a new commit is pushed to the repository, Jenkins detects the change and automatically starts a new build.

The automatic trigger was successfully tested and produced a green Jenkins build.

Technologies Used
Git
GitHub
Python
pytest
GitHub Actions
Jenkins