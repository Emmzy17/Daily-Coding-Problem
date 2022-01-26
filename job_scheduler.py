from time import sleep
def job_scheduler(func, n):
    sleep(n/1000)
    return func()

def func():
    return 'Hello'
print(job_scheduler(func, 2000))

