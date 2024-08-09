try:
    from picamera2 import Picamera2, Preview
except ModuleNotFoundError:
    class Picamera2:
        def __init__(self, *args, **kwargs):
            pass
        # Add any other methods you need to mock here

    class Preview:
        def __init__(self, *args, **kwargs):
            pass
        # Add any other methods you need to mock here