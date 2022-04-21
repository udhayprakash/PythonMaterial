#!/usr/bin/env python3
import subprocess
import sys
import os

import click

SUBPROCESS_KWARGS = dict(shell=True, check=True)


def containerized():
    return "CONTAINERIZED" in os.environ


@click.group()
def cli():
    pass


@cli.command()
@click.option("--daemon/--no-daemon", "-d/ ", default=False)
def localapi(daemon: bool):
    """Start a local API."""
    daemon_flag = "-d" if daemon else ""
    subprocess.run(
        f"docker compose up --build {daemon_flag} localapi", **SUBPROCESS_KWARGS
    )


@cli.command()
@click.option("--build/--no-build", "-b/ ", default=False)
def pytest(build: bool):
    """Run unit tests"""
    if build:
        subprocess.run(
            "docker compose build --build-arg include_devtools=1 ci",
            **SUBPROCESS_KWARGS,
        )
    subprocess.run("docker compose run --rm ci pytest", **SUBPROCESS_KWARGS)
    # subprocess.run("docker compose run --rm ci pytest src/vtg_auth_api/accounts/controllers_test.py", **SUBPROCESS_KWARGS)


@cli.command()
def lint():
    """Run python linters"""
    subprocess.r
