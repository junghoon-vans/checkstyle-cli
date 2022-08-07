import argparse
import subprocess

parser = argparse.ArgumentParser(description="checkstyle launcher")
parser.add_argument(
    "-c",
    "--config",
    type=str,
    default="/google_checks.xml",
    help="checkstyle configuration file",
)
parser.add_argument(
    "path",
    type=str,
)


def main():
    args = parser.parse_args()
    run_checkstyle(
        config=args.config,
        path=args.path,
    )


def run_checkstyle(config: str, path: str):
    cmd = ['java', '-jar']
    args = ['../checkstyle-10.3.2-all.jar', '-c', config, path]
    subprocess.run(cmd+args)


if __name__ == "__main__":
    main()
