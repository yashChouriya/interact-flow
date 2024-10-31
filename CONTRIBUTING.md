# Contributing to InteractFlow

First off, thank you for considering contributing to InteractFlow! It's people like you that make InteractFlow such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include details about your configuration and environment

### Suggesting Enhancements

If you have a suggestion for an enhancement, please create an issue with the tag "enhancement". Include:

* A clear and descriptive title
* A detailed description of the proposed functionality
* Any possible implementation details
* Why this enhancement would be useful to most users

### Pull Requests

Please follow these steps to submit a pull request:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run the tests and add new ones if needed
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

#### Pull Request Guidelines

* Update the README.md with details of changes to the interface, if applicable
* Update the documentation with any new functionality
* The PR should work for Python 3.6+
* Include tests for new functionality
* Follow the existing code style

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a branch for your changes:
   ```bash
   git checkout -b name-of-your-bugfix-or-feature
   ```

## Testing

Before submitting a pull request, please make sure your changes pass all tests:

```bash
python -m unittest discover tests
```

## Style Guide

* Follow PEP 8 guidelines
* Use meaningful variable names
* Add comments for complex logic
* Keep functions focused and small
* Document public functions and classes

## License

By contributing, you agree that your contributions will be licensed under the MIT License.