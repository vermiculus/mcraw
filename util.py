# used in recipe concatenation.
def add_dict(a, b):
    """Join the dictionaries a and b and return a new dictionary with
    all the keys of a and b, where duplicate keys' values are added"""
    return {i: a.get(i, 0) + b.get(i, 0) for i in set(a) | set(b)}

class McRawError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(message)

# My best idea ever!
output_streams = {
    "status": True,
    "debug": True,
    "trace": True,
    "warning": True,
    "error": True}

def message(stream, msg, *args):
    """
    If stream is defined and enabled in output_streams, then print to
    stdout the stream and the message formatted with its arguments.
    """
    if stream not in output_streams:
        raise McRawError("I can't find the '{}' stream.  Did you declare it in `output_streams`?".format(stream))
    if output_streams[stream]:
        print("{}: {}".format(stream, msg.format(*args)))
