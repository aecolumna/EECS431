from heapq import heappop, heappush
from collections import deque

class Job:
    def __init__(self, mTimeArrival, mTimeDuration):
        self.mTimeArrival = mTimeArrival
        self.mTimeDuration = mTimeDuration

    def __lt__(self, other):
        return self.mTimeDuration < other.mTimeDuration

    def ___le__(self, other):
        return self.mTimeDuration <= other.mTimeDuration

    def __eq__(self, other):
        return self.mTimeDuration == other.mTimeDuration

    def __ne__(self, other):
        return self.mTimeDuration != other.mTimeDuration

    def __gt__(self, other):
        return self.mTimeDuration > other.mTimeDuration

    def __ge__(self, other):
        return self.mTimeDuration >= other.mTimeDuration

    def __repr__(self):
        return "Duration: {} Arrival: {}".format(self.mTimeDuration, self.mTimeArrival)


onDeck = deque()  # use insert left, then pop! [-1] to check largest value to go.
heap = []
time = 0
cumulativeTimes = 0

numOfJobs = 5  # given by input. Use it to calculate average in the end

j1 = Job(961148050, 385599125)
j2 = Job(951133776, 376367013)
j3 = Job(283280121, 782916802)
j4 = Job(317664929, 898415172)
j5 = Job(980913391, 847912645)



onDeck.appendleft(j1)
onDeck.appendleft(j2)
onDeck.appendleft(j3)
onDeck.appendleft(j4)
onDeck.appendleft(j5)

job = onDeck.pop()
heap.append(job)
time = job.mTimeArrival

while heap:

    job = heappop(heap)
    time += job.mTimeDuration  # maybe we have to wait sometimes!
    cumulativeTimes += time - job.mTimeArrival

    while (onDeck and onDeck[-1].mTimeArrival <= time):
        heappush(heap, onDeck.pop())

    if onDeck and not heap:
        job = onDeck.pop()
        heappush(heap, job)
        time = job.mTimeArrival  # catch up on time

print(int(cumulativeTimes / numOfJobs))