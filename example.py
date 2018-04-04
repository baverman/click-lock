import time
import click
from click_lock import lock

@click.command()
@lock
def cmd():
    time.sleep(10)

cmd()
