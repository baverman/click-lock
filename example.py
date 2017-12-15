import click
from click_lock import lock_group

cli = lock_group()

@cli.command()
@click.argument('seconds', type=int)
def wait(seconds):
    """Wait for particular amount of seconds"""
    import time
    time.sleep(seconds)


cli()
