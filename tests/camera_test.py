from camera import Camera


def test_camera():
    camera = Camera()
    assert camera._is_open