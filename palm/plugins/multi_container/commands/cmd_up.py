import click
import subprocess
from typing import List, Optional


@click.command("up")
@click.argument("flags", nargs=-1)
def cli(flags: Optional[List] = []):
    """Bring up all containers, flags can be passed like -d or --build"""
    cmd = ["docker-compose", "up"] + flags
    subprocess.run(cmd, check=True)
