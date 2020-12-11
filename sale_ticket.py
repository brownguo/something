import threading
import time
import logging
import sys


class sale_ticket(object):

    def __init__(self):
        self.total = 10
        self.lock = threading.RLock()
        self.logger = logging.getLogger(__name__)

    def sale(self):
        self.lock.acquire()
        logging.debug(('当前出售:%s张票\n' % self.total))
        time.sleep(0.2)
        self.total -= 1
        self.lock.release()


if __name__ == '__main__':

    if not sys.platform.startswith('win'):
        import coloredlogs
        coloredlogs.install(level='DEBUG')

        start = sale_ticket()
        threads = []

        # 搞10个窗口去买票
        for i in range(10):
            t = threading.Thread(target=start.sale(), args=())
            threads.append(t)

        for t in threads:
            t.start()
