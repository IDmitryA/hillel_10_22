# <span style='color:blue' >Hillel course "Python Pro"</span>


## About
```mermaid
graph TD
hillel_10_22 --> lesson_02
hillel_10_22 --> README.md
hillel_10_22 --> Pipfile
hillel_10_22 --> Pipfile.lock
lesson_02 --> homework_02.py
```
## Quick start

### Install deps

```bash
# Install pipenv
pip install pipenv

# Activate virtual env
pipenv shell

# Install deps
pipenv sync
```

#### Additional
```bash
# Regenerate Pipfile.lock file
pipenv lock

# pipenv lock & pipenv sync
pipenv update
```

## Use formatters and linters
```bash
flake8 5.0.4
black 22.10.0
isort 5.10.1
```