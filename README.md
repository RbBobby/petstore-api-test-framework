# Autotests (Petstore API)

Pytest-based API autotests for Swagger Petstore.

## Requirements

- macOS (Apple Silicon/Intel)
- Python 3.10+ (recommended: Homebrew Python)
- `pip`

Check versions:

```bash
python3 --version
python3 -m pip --version
```

---

## 1) Clone and open project

```bash
git clone <your-repository-url>
cd Autotests
```

---

## 2) Create and activate virtual environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation you should see `(venv)` in terminal prompt.

### Windows (if needed)

```powershell
python -m venv venv
venv\Scripts\activate
```

---

## 3) Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Current required packages:
- `pytest`
- `requests`

---

## 4) Run tests

Run all tests:

```bash
python -m pytest -v
```

Run a specific file:

```bash
python -m pytest tests/test_auth.py -v
```

Run a specific test:

```bash
python -m pytest tests/test_auth.py::test_user_login -v
```

---

## 5) VS Code setup (recommended)

1. Open project in VS Code.
2. Select interpreter from `./venv`:
   - **Cmd+Shift+P** → `Python: Select Interpreter` → choose `venv/bin/python`.
3. Ensure pytest is enabled (already configured in `.vscode/settings.json`).
4. Use **Testing** tab to run/debug tests.

---

## 6) Debug tests in VS Code

Use launch config: **"pytest debug - specific file"**  
It runs:

```bash
python -m pytest <current_file> -v
```

---

## 7) Deactivate virtual environment

When finished:

```bash
deactivate
```

---

## Troubleshooting

### `No module named pytest`
Usually means wrong interpreter is selected.

Fix:

```bash
source venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

Also verify VS Code uses `venv/bin/python`.

### Import/module issues
Run commands from project root:

```bash
cd /Users/alexandr/dev/Autotests
```

---

## Project structure

```text
Autotests/
├── api/
│   ├── client.py
│   ├── pet_api.py
│   └── user_api.py
├── tests/
│   ├── test_auth.py
│   ├── test_pet.py
│   └── test_dummy.py
├── conftest.py
├── config.py
├── requirements.txt
└── .vscode/
    ├── settings.json
    └── launch.json
```