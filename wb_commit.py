import requests
import time
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor

task_list = Queue()


class wb_commit(object):
    def __init__(self):
        self.url = '#'

    def add_task(self, t_id):
        task_list.put(self.url.format(int(time.time() * 1000), t_id))

    def handle_task(self, url):
        response = requests.get(url)
        print("HttpCode:%s url:%s" % (response.status_code, url))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=1000)
    start = wb_commit()

    for i in range(1, 100000):
        r = pool.submit(start.add_task, i)

    print(task_list.get())
    while not task_list.empty():
        pool.submit(start.handle_task, task_list.get())

