# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A small Python 3 learning project with practice functions for analyzing test-run data. It uses only the standard library: there are no dependencies, no build step, and no linter configuration.

## Run

```powershell
python basic_functional_progras.py
```

The script ends by prompting on stdin for the total and passed test counts. To run it without typing input, pipe the answers in: `"5`n3" | python basic_functional_progras.py`

## Structure

- `basic_functional_progras.py` started as a Google Colab export of `Basic_functional_progras.ipynb`. It has since been refactored to be importable, and it is now the source of truth that CI tests. The notebook is the original exercise version.
- The functions in the script:
  - `find_slowest_test` / `find_fastest_test`: a linear scan over `{"name", "status", "duration"}` dicts. Each returns `None` for an empty list.
  - `group_test_results`: normalizes the status with `.strip().upper()` and puts it in a `PASS`/`FAIL`/`SKIP`/`INVALID` bucket.
  - `calculate_pass_percentage`: returns `None` for invalid counts.
  - `main()` prints the results and prompts for input. It runs only under `if __name__ == "__main__":`, so the module can be imported safely. Keep side effects out of module level.

## Testing and CI

- Run all tests: `python -m pytest` (`pyproject.toml` sets `testpaths` and puts the repo root on `pythonpath`)
- Run a single test: `python -m pytest tests/test_basic_functional.py::test_find_slowest_test`
- `.github/workflows/ci.yml` runs pytest on Python 3.10–3.12 for every push to `main` and every pull request, and then runs the script with piped input as a smoke test.

The `pytestArgs` in `.vscode/settings.json` points at a nonexistent `eventhub` directory, and the file is gitignored.
