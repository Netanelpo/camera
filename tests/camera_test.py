import numpy as np
import pytest

from camera.camera import Camera


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
    frame = next(camera.capture_image())
    assert frame.shape == (1024, 1280, 1)
    assert frame.dtype == np.uint16
