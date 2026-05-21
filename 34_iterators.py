# Exercise 34: Custom Iterators
# Task: Create a custom iterator class Counter that counts up to max_limit.

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count

if __name__ == "__main__":
    for num in Counter(3):
        print(num)
