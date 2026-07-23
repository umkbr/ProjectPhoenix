import threading
import time

from phoenix.core.inspection_engine import InspectionEngine


class DeviceMonitor:

    def __init__(self, callback):

        self.callback = callback
        self.running = False

    def start(self):

        self.running = True

        thread = threading.Thread(
            target=self.loop,
            daemon=True,
        )

        thread.start()

    def stop(self):

        self.running = False

    def loop(self):

        while self.running:

            try:

                report = InspectionEngine().inspect()

                self.callback(report)

            except Exception:

                self.callback(None)

            time.sleep(2)