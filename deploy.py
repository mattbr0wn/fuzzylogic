#!/usr/bin/env python3

import os
import subprocess


def run_command(command):
    subprocess.run(command, shell=True, check=True)


def create_network():
    run_command("sudo docker network create fuzzylogic")


def copy_env():
    print("copy caddy.env to caddy/caddy.env")
    print("copy plausible.env to plausible/plausible.env")
    input("Press Enter when you're ready to continue...")


def deploy():
    run_command("sudo docker compose -f docker-compose.yaml up -d --build")


if __name__ == "__main__":
    create_network()
    copy_env()
    deploy()
