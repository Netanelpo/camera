from time import sleep

import numpy as np
import pytest

from components.camera import Camera


def test_close():
    camera = Camera()
    assert not camera._is_open
    camera.open()
    assert camera.is_open
    camera.close()
    assert not camera.is_open


def test_image_closed():
    camera = Camera()
    with pytest.raises(RuntimeError):
        next(camera.capture_image())

def test_image_opened():
    camera = Camera()
    camera.open()
    frame1 = next(camera.capture_image())
    assert frame1.shape == (1024, 1280, 1)
    assert frame1.dtype == np.uint16

    frame2 = next(camera.capture_image())
    assert np.array_equal(frame1, frame2)

    sleep(0.03)
    frame3 = next(camera.capture_image())
    assert not np.array_equal(frame1, frame3)