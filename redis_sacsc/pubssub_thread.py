import threading
import redis


class LocalPubSubWorkerThread(threading.Thread):
    def __init__(self, manager, pubsub, sleep_time, daemon=False):
        super(LocalPubSubWorkerThread, self).__init__()
        self._manager = manager
        self.daemon = daemon
        self.pubsub = pubsub
        self.sleep_time = sleep_time
        self._running = threading.Event()

    def run(self):
        if self._running.is_set():
            return
        self._running.set()
        pubsub = self.pubsub
        sleep_time = self.sleep_time
        while self._running.is_set():
            try:
                pubsub.get_message(ignore_subscribe_messages=True, timeout=sleep_time)
            except redis.exceptions.ConnectionError:
                print("reset called" * 20)
                self._manager.reset()
                raise
        pubsub.close()
