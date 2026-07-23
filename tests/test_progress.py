from phoenix.ui.progress import Progress


def test_progress():

    progress = Progress()

    progress.show(1, 3, "Weather")

    assert True