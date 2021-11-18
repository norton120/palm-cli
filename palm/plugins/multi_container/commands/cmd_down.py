import click
import subprocess
from typing import List, Optional


@click.command("down")
@click.argument("flags", nargs=-1)
def cli(flags: Optional[List] = []):
    """Spin down all running containers for the application"""
    cmd = ["docker-compose", "down"] + flags
    subprocess.run(cmd, check=True)
