import sys
import errno
import fcntl
import signal
import logging
import traceback

import click


def lock_group(name=None, **attrs):
    @click.group(name, **attrs)
    @click.option('--lock', help='Path to lock file', metavar='fname')
    @click.option('--timeout', type=int, metavar='seconds',
                  help='Limit script execution time')
    @click.option('--trace/--no-trace', default=True,
                  show_default=True, help='Log traceback in case of timeout')
    def cli(lock, timeout, trace):
        lock and _set_lock(lock)
        timeout and _set_timeout(timeout, trace)

    return cli


def _set_lock(path):
    global _flock
    _flock = open(path, 'w+')
    try:
        fcntl.flock(_flock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError as e:
        if e.errno != errno.EAGAIN:
            raise
        else:
            sys.exit(2)


def _set_timeout(timeout, log_trace):
    handler = _alarm_with_trace if log_trace else _alarm_silent
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)


def _alarm_with_trace(signum, frame):
    trace = ''.join(traceback.format_stack(frame))
    logging.getLogger('click_lock.timeout').error(
        'Script timeout (%r):\n %s', sys.argv, trace)
    sys.exit(3)


def _alarm_silent(signum, frame):
    sys.exit(3)
