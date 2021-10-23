import time


def aa():
    start_time = time.time()
    for n in range(10):
        time.sleep(1)
        print(time.ctime())
        print(start_time)


if __name__ == '__main__':

    s = 4.3
    a = 4
    print(s+a)
