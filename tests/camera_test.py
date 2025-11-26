from camera.camera import Camera


def test_camera():
    camera = Camera()
    assert not camera._is_open
    camera.open()
    assert  camera.is_open
    camera.close()
    assert not camera.is_open