#!/usr/bin/env python3
from .shell import KybraShell
import argparse

def main():
    parser = argparse.ArgumentParser(description="Kybra Simple Shell - REPL for Python-based Kybra canisters")
    parser.add_argument(
        "canister_id",
        help="ID of the canister to interact with"
    )
    parser.add_argument(
        "--network",
        type=str,
        default=None,
        help="Network to connect to (e.g. 'ic' for mainnet)"
    )
    parser.add_argument(
        "--ic",
        action="store_true",
        help="Shorthand for --network ic"
    )
    
    args = parser.parse_args()
    
    # Determine the network to use
    network = None
    if args.ic:
        network = "ic"
    elif args.network:
        network = args.network
    
    # Create and run the shell
    shell = KybraShell(canister_name=args.canister_id, network=network)
    shell.run_shell()

if __name__ == "__main__":
    main()
