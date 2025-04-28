# Tax App

A simple financial calculator web application built with **FastAPI** and **Jinja2**. This app provides three calculators:

1. **Compound Interest Calculator**
2. **Mortgage Calculator**
3. **Tax Calculator**

## Features

- **Compound Interest Calculator**: Calculates the future value of an investment based on principal, rate, time, and compounding frequency.
- **Mortgage Calculator**: Computes monthly payments, total payments, and total interest for a loan.
- **Tax Calculator**: Determines taxable income and tax owed based on income, deductions, and tax rate.
- Responsive UI built with **Bootstrap 5**.
- API endpoints for each calculator.

## Installation

### Prerequisites

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/) for dependency management

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Tax-App.git
   cd Tax-App
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Run the development server:

   ```bash
   poetry run dev
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000`.

## Deployment

### Docker Deployment

1. Build the Docker image:

   ```bash
   docker build -t tax-app .
   ```

2. Run the container:

   ```bash
   docker run -p 8000:8000 tax-app
   ```

3. Access the app at `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

- **Adam Larson** - [alarson7767@sdsu.edu](mailto:alarson7767@sdsu.edu)