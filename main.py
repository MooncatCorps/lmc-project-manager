#!/usr/bin/env python

from mooncat.mcpm import arguments
from mooncat.mcpm import metafile
from mooncat.mcpm import actions

def main() -> int:
    if not metafile.exists():
        if metafile.prompt_creation():
            metafile.create()
        else:
            metafile.report_non_existent()
            return 1

    parser = arguments.register()
    args = parser.parse_args()

    data = metafile.parse()
    actions.execute_action(args.action[0], data, args)

    return 0

if __name__ == "__main__":
    exit(main())

