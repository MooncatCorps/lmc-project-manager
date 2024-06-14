import argparse as ap

def register_args() -> ap.ArgumentParser:
    parser = ap.ArgumentParser(description="The official MooncatCorps project manager")

    parser.add_argument("--version",
                        action = "store_true",
                        help = "Retrieve version data about the project manager")

    parser.add_argument("--about",
                        action = "store_true",
                        help = "Retrieve the current project's information")
    
    return parser


