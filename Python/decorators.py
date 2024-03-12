import time

def time_taken(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'Took {t2} seconds')
    return wrapper

@time_taken
def doThis():
    time.sleep(1.5)

@time_taken
def doThat():
    time.sleep(3)
    
doThis()
doThat()