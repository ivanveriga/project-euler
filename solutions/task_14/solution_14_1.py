# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


import threading


NUM = (0, 0)


class NewThread(threading.Thread):
   def __init__(self, fromNum, toNum):
      threading.Thread.__init__(self)
      self.fromNum = fromNum
      self.toNum = toNum

   def run(self):
        global NUM

        for i in range(self.fromNum, self.toNum):
            count = 0

            n = i
            while n > 1:
                if n % 2 == 0:
                    n /= 2
                else:
                    n = (3 * n) + 1

                count += 1

            if count > NUM[1]:
                NUM = (i, count)

        print(NUM)


for i in range(0, 10):
    thread = NewThread(i * 100_000, ((i + 1) * 100_000) + 1)
    thread.start()