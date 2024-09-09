# Selenium Web Automation for Phy-X Shielding Simulation

This project automates the interaction with the [Phy-X shielding simulator](https://phy-x.net/module/physics/shielding/) using Selenium. The script logs into the website, fills in required data fields from a CSV file, runs simulations, and exports the results to an Excel file.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Script](#running-the-script)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Google Chrome browser
- Chrome WebDriver (must match your Chrome browser version)

## Installation

1. **Clone the repository**:

    ```bash
    [git clone https://github.com/wahidcs50/Py.X-Automation-.git]
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows, use .venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Chrome WebDriver**:

   Download the Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads) and ensure it matches your Chrome version. Place the driver path in your environment file or local configuration.

## Environment Variables

Set the following variables in a `.env` file located in the project root:

```env
DRIVER_PATH=/path/to/chromedriver
DATA_PATH=/path/to/input_data.csv
PHY_USERNAME=your_email@example.com
PASSWORD=your_password

