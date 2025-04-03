import argparse
from pipeline.hello import HelloWorld

def main():
    parser = argparse.ArgumentParser(description="Python CLI for Jenkins Pipeline")
    subparsers = parser.add_subparsers(dest="command")

    # Hello World Command
    hello_parser = subparsers.add_parser("hello", help="Print Hello, World!")

    args = parser.parse_args()

    if args.command == "hello":
        HelloWorld.run()

if __name__ == "__main__":
    main()