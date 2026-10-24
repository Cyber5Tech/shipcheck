# ShipCheck

ShipCheck is a small, dependency-free command-line tool for checking whether a repository has the basics people expect from an open-source project.

It checks for:

- A `README.md`
- An OSI-approved license file (`LICENSE` or `LICENSE.md`)
- A contribution guide
- A code of conduct
- A security policy
- Issue templates or a pull-request template
- A CI workflow

## Quick start

Run it directly from a checkout:

```console
python -m shipcheck .
```

Or install the package in editable mode:

```console
python -m pip install -e .
shipcheck .
```

Use `--json` in automation:

```console
shipcheck . --json
```

The command exits with status `0` when all checks pass and `1` when one or more checks fail.

## Development

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
