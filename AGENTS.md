# Repository Guidelines

## Project Structure & Module Organization

Project Phoenix is a Python 3.12+ Android recovery and device-management application. Application code lives in `src/phoenix/`, organized by responsibility: `core/` and `adb/` handle device access, feature packages such as `debloat/`, `doctor/`, `backup/`, and `report/` contain domain logic, and `gui/` contains the PySide6 interface. Keep reusable business logic outside the GUI layer. Tests mirror features in `tests/` (for example, `tests/test_debloat_engine.py`). Runtime knowledge and sample device data are under `database/`; visual assets are under `resources/`.

## Build, Test, and Development Commands

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run the full test suite with `pytest`. Run one focused test with `pytest tests/test_adb_client.py`. Use `python run.py` for the inspection/report workflow, `python -m phoenix` for the CLI, or `phoenix` after editable installation. Hardware-facing commands may require Android Platform Tools and an authorized ADB device; keep tests independent of a connected device where possible.

## Coding Style & Naming Conventions

Use four-space indentation, `snake_case` for functions, variables, modules, and test names, and `PascalCase` for classes (for example, `DebloatEngine`). Prefer small, single-purpose modules and explicit imports. Follow the surrounding code's whitespace and type-annotation conventions. No formatter or linter is currently configured; avoid drive-by reformatting and keep diffs focused.

## Testing Guidelines

Add or update pytest tests for every behavior change. Name files `test_<feature>.py` and tests `test_<expected_behavior>()`. Test public behavior and safety decisions, especially ADB command construction, debloat recommendations, backups, and restores. Run `pytest` before opening a pull request; the project has no stated coverage threshold.

## Commit & Pull Request Guidelines

Recent history uses imperative summaries and conventional prefixes when useful, such as `feat: add sidebar widget`, `refactor(debloat): add preview and execute workflow`, and `chore: update .gitignore`. Keep commits narrowly scoped. Pull requests should explain the user-visible change, list validation performed, link the related issue when available, and include screenshots for GUI changes. Call out any ADB/device prerequisites or data-format changes.

## Security & Configuration

Never commit device identifiers, logs, backups, or local ADB output. Treat destructive ADB operations as safety-critical: retain preview/confirmation behavior and add regression tests before changing execution paths.
