click-lock
==========

Adds locks and timeouts to `Click <http://click.pocoo.org/>`_ entrypoints.

Where is only one function ``click_lock.lock_group`` with the
same interface as ``click.group``. You define root group and can
use it to declare commands or subgroups:

.. code:: python

    # example.py
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

Now you have some additional options::

    Usage: example.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --lock fname          Path to lock file
      --timeout seconds     Limit script execution time
      --trace / --no-trace  Log traceback in case of timeout  [default: True]
      --help                Show this message and exit.

    Commands:
      wait  Wait for particular amount of seconds

For example, lock script execution::

    python example.py --lock /tmp/example.lck wait 10

Limit script execution::

    python example.py --timeout 5 wait 10
