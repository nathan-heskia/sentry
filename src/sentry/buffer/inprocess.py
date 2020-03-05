from __future__ import absolute_import

from sentry.buffer import Buffer


class InProcessBuffer(Buffer):
    """
    In-process buffer which computes changes in real-time.

    **Note**: This does not actually buffer anything, and should only be used
              in development and testing environments.
    """

    def incr(self, model, columns, filters, extra=None, exclude_filters=None):
        self.process(model, columns, filters, extra)
