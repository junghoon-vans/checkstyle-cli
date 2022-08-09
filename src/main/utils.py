import argparse


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="/google_checks.xml",
        help="checkstyle configuration file",
    )
    parser.add_argument(
        "files", nargs="*",
        help="files to verify",
    )
    return parser
