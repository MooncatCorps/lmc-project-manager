import argparse as ap

def register_args() -> ap.ArgumentParser:
    parser = ap.ArgumentParser(prog = "mcpm",
                               description = "The official MooncatCorps project manager")

    parser.add_argument("action",
                        nargs = 1,
                        choices = [
                            "info",
                            "install",
                        ])

    parser.add_argument("args",
                        nargs = "*")

    parser.add_argument("--version",
                        action = "store_true",
                        help = "Retrieve version data about the project manager")

    parser.add_argument("-D", "--development",
                        action = "store_true",
                        help = "Enables development mode (Facilitates development)")
    
    return parser


