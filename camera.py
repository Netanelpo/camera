import numpy as np
import time


class Camera:
    def __init__(self):
        self._is_open = False
        self._last_captured_image = 0, None

    def open(self):
        self._is_open = True

    def close(self):
        self._is_open = False

    def capture_image(self):
        while self._is_open:
            now = time.time()
            if self._last_captured_image[0] + 0.033 <= now:  # simulate 30 FPS
                self._last_captured_image = time.time(), np.random.randint(0, 65_535, (1024, 1280, 1), dtype=np.uint16)
            yield self._last_captured_image[1]
        raise RuntimeError("camera is closed")

    @property
    def is_open(self):
        return self._is_open
