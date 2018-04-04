click-lock
==========

Adds locks and timeouts to `Click <http://click.pocoo.org/>`_ entrypoints.

There is only one decorator ``click_lock.lock`` which can be applied
to click commands and groups:

.. code:: python

    # example.py
    import time
    import click
    import click_lock

    @click.command()
    @click_lock.lock
    def cmd():
        time.sleep(10)

    cmd()

Now you have some additional options::

    Usage: example.py [OPTIONS]

    Options:
      --lock fname          Path to lock file
      --timeout seconds     Limit script execution time
      --trace / --no-trace  Log traceback in case of timeout  [default: True]
      --help                Show this message and exit.

For example, lock script execution::

    python example.py --lock /tmp/example.lck

Limit script execution time::

    python example.py --timeout 1
