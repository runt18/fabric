"""
Custom Fabric exception classes.

Most are simply distinct Exception subclasses for purposes of message-passing
(though typically still in actual error situations.)
"""


class NetworkError(Exception):
    # Must allow for calling with zero args/kwargs, since pickle is apparently
    # stupid with exceptions and tries to call it as such when passed around in
    # a multiprocessing.Queue.
    def __init__(self, message=None, wrapped=None):
        self.message = message
        self.wrapped = wrapped

    def __str__(self):
        return self.message or ""

    def __repr__(self):
        return "{0!s}({1!s}) => {2!r}".format(
            self.__class__.__name__, self.message, self.wrapped
        )


class CommandTimeout(Exception):
    def __init__(self, timeout):
        self.timeout = timeout

        message = 'Command failed to finish in {0!s} seconds'.format((timeout))
        self.message = message
        super(CommandTimeout, self).__init__(message)
