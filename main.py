import os
import os.path
import subprocess
import time
from argparse import ArgumentParser

from termcolor import colored


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"The file {arg} does not exist!")
    else:
        return arg


def main(**kwargs):
    with open(kwargs["creds"]) as file:
        content = file.read()
        for user_pass in content.split("\n"):
            uname, pswd = user_pass.split(":", 1)
            subprocess.Popen(
                f"openvpn --config {kwargs['config']} "
                "--route-noexec "
                f'--auth-user-pass <(echo -e "{uname}\n{pswd}") '
                "--log ovpn.log --daemon",
                shell=True,
                executable="/bin/bash",
            )
            time.sleep(5)
            if "AUTH_FAILED" in open("ovpn.log").read():
                print(colored(f"{uname}:{pswd} doesnt work", "red"))
            elif "PUSH_REPLY" in open("ovpn.log").read():
                subprocess.Popen(
                    f"openvpn --config {kwargs['config']} "
                    "--route-noexec "
                    f'--auth-user-pass <(echo -e "{uname}\n{pswd}") '
                    "--log ovpn.log --daemon",
                    shell=True,
                    executable="/bin/bash",
                )
                time.sleep(5)
                if "AUTH_FAILED" in open("ovpn.log").read():
                    print(colored(f"{uname}:{pswd} doesnt work", "red"))
                elif "PUSH_REPLY" in open("ovpn.log").read():
                    print(colored(f"{uname}:{pswd} works!", "green"))
                else:
                    print(colored(f"{uname}:{pswd} timeout!", "yellow"))
            else:
                print(colored(f"{uname}:{pswd} timeout!", "yellow"))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--config",
        required=True,
        metavar="FILE",
        type=lambda x: is_valid_file(parser, x),
    )
    parser.add_argument(
        "--creds",
        required=True,
        metavar="FILE",
        type=lambda x: is_valid_file(parser, x),
    )
    args = parser.parse_args()
    main(**vars(args))
