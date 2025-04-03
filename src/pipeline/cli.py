import argparse
from pipeline.build import BuildPipeline
from pipeline.deploy import DeployPipeline

def main():
    parser = argparse.ArgumentParser(description="Jenkins Python Shared Library CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Hello World Command
    hello_parser = subparsers.add_parser("hello", help="Print Hello, World!")

    # Build command
    build_parser = subparsers.add_parser("build", help="Run build pipeline")

    # Deploy command
    deploy_parser = subparsers.add_parser("deploy", help="Run deployment")
    deploy_parser.add_argument("--env", default="staging", help="Deployment environment")

    args = parser.parse_args()

    if args.command == "build":
        BuildPipeline.run()
    elif args.command == "deploy":
        DeployPipeline.run(args.env)
    elif args.command == "hello":
        HelloWorld.run()

if __name__ == "__main__":
    main()