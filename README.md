# witherlabs-project-manager-lib
A project manager library for Wither Labs projects.

## Plans
Currently doubles as a library and installer; however, it is destined to only
function as a library (hence the -lib sufix). Polishing must be done.
Eventually, the library will be put to use in a separate cli tool.

## Usage
This is meant to be used as python library which means that there is no
executable for it (See the above section).

Currently, in order to manage projects one must spawn an interactive
python session or write a custom script for it.

All of the main actions that are meant to be executed by users whilst the
project is immature exist within `witherlabs.projman.actions`. \

For example, to install the project located in the current working directory:

```py
from witherlabs.projman import actions
actions.install()
```

## Supported actions
- Install \
Installs the project. Automatically determines locations based on project type.

- Uninstall \
Uninstalls the project. Automatically determines locations based on project type.

