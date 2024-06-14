import arguments
import lmc_parser as lmcp

def main() -> int:
    if not lmcp.file_exists():
        if lmcp.prompt_should_create_file():
            lmcp.create_file()
        else:
            lmcp.report_non_existent_file()

    parser = arguments.register_args()
    parser.parse_args()


    return 0

if __name__ == "__main__":
    exit(main())

