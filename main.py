import mooncat.pm.arguments as cmdargs
import mooncat.pm.mc_file as mcf
import mooncat.pm.action_handler as acthandler

def main() -> int:
    if not mcf.file_exists():
        if mcf.prompt_should_create_file():
            mcf.create_file()
        else:
            mcf.report_non_existent_file()
            return 1

    parser = cmdargs.register_args()
    proc_args = parser.parse_args()

    data = mcf.get_file_data()

    acthandler.execute_action(data, proc_args)

    return 0

if __name__ == "__main__":
    exit(main())

