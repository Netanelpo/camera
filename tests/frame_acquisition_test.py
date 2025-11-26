from queue import Empty
from time import sleep

import numpy as np
import pytest

from components.camera import Camera
from components.frame_acquisition import FrameAcquisition


class CameraMock:
    pass


def test_facq_stopped():
    camera = Camera()
    facq = FrameAcquisition(camera)
    with pytest.raises(Empty):
        facq.wait_frame()


def test_facq_start():
    camera = Camera()
    facq = FrameAcquisition(camera)
    facq.start()
    frame = facq.wait_frame()
    assert frame.shape == (1024, 1280, 1)
    assert frame.dtype == np.uint16


def test_facq_start_wait_stop():
    camera = Camera()
    facq = FrameAcquisition(camera)
    facq.start()
    sleep(0.09)
    facq.stop()
    assert facq.wait_frame() is not None
    assert facq.wait_frame() is not None
    assert facq.wait_frame() is not None
    with pytest.raises(Empty):
        facq.wait_frame()
