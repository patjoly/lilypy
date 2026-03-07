# lilypy

`lilypy` is a Python module that provides utilities and scripts for working with LilyPond. It can create templates for various instruments, convert music files, thereby streamlining music notation workflows.

## Installation

Install `lilypy` in your current Python environment:

```
python -m pip install .
```

## Usage

Once installed, you can run the CLI:

```
lilypy new --instrument guitar  --key g --mode minor --title "This one" --composer "Sor" --opus "Op.30, no.6" --output "Sor 30 no 6.ly"
lilypy new --instrument trumpet --key f --mode major --title "My Piece" --composer "Mendelssohn, Felix" --output "My Piece.ly"
lilypy new --instrument trumpet --key f --mode major --title "My Piece" --composer "Mendelssohn, Felix" --output "My Piece.ly" --concert --lyrics

lilypy convert --relative ...   # convert: not implemented yet
```

Check the help for available options:

```
lilypy --help
```

You can also use the module programmatically in Python:

```
from lilypy import cli

# Example: call the main function
cli.main()
```

## Dependencies

- [Jinja2](https://pypi.org/project/Jinja2/) – for templating
- [python-ly](https://pypi.org/project/python-ly/) – for parsing and processing LilyPond files

## License

Copyright (c) 2026 P. Joly

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

