# Rent Payment Tracker

## Project Overview

Rent Payment Tracker is an individual CSCE research milestone related to our team's student-housing property-management capstone. It is a small local application for entering a tenant's monthly rent and payment, calculating the remaining balance, and keeping a basic payment history. It explores Python application logic, a simple web interface, and file-based storage. It is a prototype, not a complete property-management system.

## Features

- Enter a tenant name, monthly rent, and amount paid in a Streamlit form.
- Calculate the remaining balance and label the payment **Paid** (full amount), **Partial** (some paid), or **Unpaid** (nothing paid).
- Reject a blank tenant name, rent of zero or less, a negative payment, or a payment above the monthly rent.
- Save a valid calculation with **Save Payment** and display saved records in a history table.
- Keep records in a local `payments.csv` file after the application closes.

## Technologies Used

- **Python** implements the validation, calculation, and file handling in [`app.py`](app.py).
- **[Streamlit](https://docs.streamlit.io/get-started)** provides the form, buttons, result display, and history table without a separate frontend.
- **[Python's `csv` module](https://docs.python.org/3/library/csv.html)** reads and writes payment rows; no database is used.
- **`requirements.txt`** lists the direct third-party dependency, Streamlit, for installation with [pip](https://pip.pypa.io/en/stable/user_guide/#requirements-files). A Python virtual environment keeps installed packages local to this project. See the [Python `venv` documentation](https://docs.python.org/3/library/venv.html).

## Installation and Setup

Install Python and Git first. [Clone the repository](https://git-scm.com/docs/git-clone) in a terminal. If you already cloned it, skip these commands and open your existing folder.

```bash
git clone https://github.com/shawnchau34/Research-Milestone-ShawnChau.git
cd Research-Milestone-ShawnChau
```

On **Windows PowerShell**, create a virtual environment and install the dependency:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On **macOS or Linux**, use:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`. Press `Ctrl+C` to stop the server. Streamlit documents the [`python -m streamlit run` command](https://docs.streamlit.io/develop/concepts/architecture/run-your-app).

## How the Application Works

1. The Streamlit form collects the tenant name and two dollar amounts. Clicking **Calculate** runs input validation, then subtracts the amount paid from monthly rent and rounds the balance to cents.
2. A zero balance is **Paid**; a zero payment with a balance is **Unpaid**; any other valid payment is **Partial**. The result stays available in the current Streamlit session until it is saved or another calculation replaces it. [Streamlit Session State](https://docs.streamlit.io/get-started/fundamentals/advanced-concepts) supports this behavior across page reruns.
3. Clicking **Save Payment** appends one row to `payments.csv` beside `app.py`. The first save creates the file and writes the column headers: tenant name, monthly rent, amount paid, remaining balance, and payment status. The pending result is then cleared so a page rerun does not save it again.
4. The app reads `payments.csv` when it runs and displays all saved rows below the calculator. The CSV file is local and is excluded from Git by `.gitignore`. Use fictional tenant information when demonstrating the project.

## Technology Research and Tradeoffs

**Streamlit** fits this milestone because its Python widgets and display components make a small interactive interface possible with little setup. [Flask](https://flask.palletsprojects.com/en/stable/quickstart/) offers more direct control over web routes and templates, but this one-page calculator would require more web application setup. [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) is well suited to building APIs and provides automatic API documentation; an API alone would not provide this project's simple browser interface. Flask and FastAPI were researched, not implemented.

**CSV** is easy to inspect and works with Python's standard library, which is enough for a small local history. Its limits include no built-in relationships, transactions, or reliable handling of simultaneous writes. [SQLite](https://docs.python.org/3/library/sqlite3.html) would provide a local SQL database without a separate server and would be a reasonable next step for structured records. [PostgreSQL](https://www.postgresql.org/about/) would better suit a larger multi-user system, but adds database setup and administration beyond this milestone. SQLite and PostgreSQL were researched, not implemented.

## Testing

The developer has confirmed that the Streamlit application runs locally, calculates balances and payment statuses, and saves and displays payment history. During development, temporary Streamlit app checks also covered valid statuses, invalid inputs, CSV creation and append behavior, a page rerun after saving, and loading history in a fresh app session. These checks are not included as a committed test suite.

Before submitting, personally verify these cases with **fictional** tenant names:

| Input or action | Expected result |
| --- | --- |
| Rent `$1,000`, paid `$1,000` | Balance `$0.00`; **Paid** |
| Rent `$1,000`, paid `$400` | Balance `$600.00`; **Partial** |
| Rent `$1,000`, paid `$0` | Balance `$1,000.00`; **Unpaid** |
| Blank name, rent `0` or below, negative payment, or payment above rent | Error message; no save option for that calculation |
| Save a valid payment, then stop and restart Streamlit | Record still appears in payment history |
| Click **Save Payment** once, then let the page rerun | Only one new CSV row is added |
| Clone into a new folder and follow the setup steps | App starts without needing an existing `payments.csv` |

`payments.csv` is created on the first save, so a new clone starts with an empty history. The saved file is intentionally not committed.

## Limitations and Future Improvements

This prototype stores only a tenant name and one payment calculation per saved row. It has no payment dates, property or unit identifiers, edit or delete controls, authentication, or automatic detection of repeated records across separate saves. The local CSV file is not suitable for simultaneous multi-user updates. Future work could add editing, authentication, property records, and a database such as SQLite or PostgreSQL if the capstone grows into a larger system. For financial use, money calculations would also need more careful decimal handling.
