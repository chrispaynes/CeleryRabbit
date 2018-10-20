from celerie_queue.tasks import addTime
import time
if __name__ == '__main__':
    for i in range(5):
        result = addTime.delay(i)
        print('Taking result: ', result)
