import argparse as ap
import mooncat.pm.mc_data as mcd
import mooncat.pm.lmc_install as mci

def execute_action(mcf_data: dict, args: ap.Namespace):
    match args.action[0]:
        case "info":
            mcd.display_requests(mcf_data, args.args)
        case "install":
            mci.perform_installation(args.args, mcf_data, args.development)
        case _:
            print(f"Unknown action: {args.action}")


