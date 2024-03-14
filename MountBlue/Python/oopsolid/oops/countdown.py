class Counter:
    def __init__(self):
        self.value = 0

    def incr(self):
        self.value += 1

    def decr(self):
        self.value -= 1

    def incrby(self, n):
        self.value += n

    def decrby(self, n):
        self.value -= n

      
counter_instance = Counter()
print("Initial value:", counter_instance.value)

counter_instance.incr()
print("After incr:", counter_instance.value)

counter_instance.decr()
print("After decr:", counter_instance.value)

counter_instance.incrby(5)
print("After incrby(5):", counter_instance.value)

counter_instance.decrby(3)
print("After decrby(3):", counter_instance.value)
