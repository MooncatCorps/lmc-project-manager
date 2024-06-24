# mooncat-project-manager
A project manager library for Mooncat projects.

## Usage
This is meant to be used as python library which means that there is no
executable for it. In order to manage projects one must spawn an interactive
python session or write a custom script for it.

All of the main actions that are meant to be executed exist within
`mooncat.mcpm.actions`. For example, to install the project located in the
current working directory:

```py
from mooncat.mcpm import actions
actions.install()
```

## Supported actions
- Install \
Installs the project. Automatically determines locations based on project type.

- Uninstall \
Uninstalls the project. Automatically determines locations based on project type.


