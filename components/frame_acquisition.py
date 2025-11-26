import threading
from queue import Queue
from time import sleep


class FrameAcquisition:

    def __init__(self, camera):
        self._queue = Queue()
        self._camera = camera
        self._thread = None

    def start(self):
        # TODO: can start be called twice in different threads???
        if self._camera.is_open:
            return

        self._camera.open()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _run(self):
        gen = self._camera.capture_image()
        last_frame = None

        while self._camera.is_open:
            try:
                frame = next(gen)
            except RuntimeError:
                break

            # Only push new frames (avoid duplicates)
            if last_frame is not frame:
                self._queue.put(frame)
                last_frame = frame

            sleep(0.001)

    def wait_frame(self):
        return self._queue.get(timeout=0.05)

    def stop(self):
        if not self._camera.is_open:
            return

        self._camera.close()

        if self._thread is not None:
            self._thread.join(timeout=1)
