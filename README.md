# ShipCheck

ShipCheck is a small, dependency-free command-line tool for checking whether a repository has the basics people expect from an open-source project.

## Installation

ShipCheck supports Python 3.9 and newer. From a local clone, install it in editable mode:

```console
python -m pip install -e .
```

## Usage

Check the current repository:

```console
shipcheck .
```

Check another repository by providing its path:

```console
shipcheck C:\path\to\repository
```

Use JSON output in scripts and CI jobs:

```console
shipcheck . --json
```

If you do not want to install the package, run it directly from a checkout by setting the source path:

```powershell
$env:PYTHONPATH = "src"
python -m shipcheck .
```

## Checks

ShipCheck looks for:

- A `README`, `README.md`, or `README.rst`
- An OSI-approved license file (`LICENSE`, `LICENSE.md`, or `LICENSE.txt`)
- A contribution guide
- A code of conduct
- A security policy
- An issue template or pull-request template
- A continuous-integration workflow

Each check reports `PASS` or `FAIL` with a next step for missing files.

## Exit codes

- `0` — all checks pass
- `1` — one or more checks fail
- `2` — the supplied path is not a directory

## Development

Run the test suite from the project root:

```console
python -m unittest discover -s tests -v
```

## Roadmap

- Configurable checks and project standards
- GitHub/GitLab provider-aware checks
- Optional autofixes for safe files
- Markdown and repository metadata linting

## Contributing

Bug reports and pull requests are welcome. See `CONTRIBUTING.md` for the development workflow.
