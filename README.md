# Group-2
CS 472 git and github lab

## Continuous Integration
[![CI Workflow](https://github.com/kenner1-unlv/Group-2/actions/workflows/ci.yml/badge.svg)](https://github.com/kenner1-unlv/Group-2/actions/workflows/ci.yml)

**CI Workflow** starts on every push and pull request
running automatically on configured GitHub Actions.
<ins>Found within:</ins> `.github/workflows/ci.yml`

The workflow performs the following checks:
- **Tests and Coverage**: runs the pytest suite with coverage and fails the build if total coverage drops below 80%.
<ins>Ran with:</ins> `pytest --cov=src --cov-fail-under=80`
- **Linting**: runs Flake8 against `src` for a set of error classes.
<ins>Error classes:</ins> (`E9, F63, F7, F82`)

### How to investigate a failed check

If a PR reports a failed check, or if the badge shows **failing**:
1. Open the **Actions** tab of the repository and select the most recent run for selected branch or PR.
2. Select the failed job to expand and investigate its steps.
3. With a failed step open, logs are available to review the failure in checks (through error messages and the failing commands).
4. Reproduce the run locally, fix the issue, and push again to trigger a fresh run. 

