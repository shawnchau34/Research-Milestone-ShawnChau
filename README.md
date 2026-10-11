# Rent Payment Tracker — Project Setup

This is a small Python and Streamlit project for the research milestone.
The current app is only a setup check; rent payment features will be added in later stages.

## Files

- `app.py` starts the Streamlit app and shows a simple interactive greeting.
- `requirements.txt` lists the Python package needed to run the app.
- `.gitignore` keeps local environments, caches, and editor files out of Git.

## Run locally

From the repository folder, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install Streamlit and start the app:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`).
Enter your name to check that the page responds. Press `Ctrl+C` in the terminal
to stop the app.

On macOS or Linux, use `python3 -m venv .venv` and
`source .venv/bin/activate` instead of the first two PowerShell commands.
