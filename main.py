class Clock:
    def __init__(self, name):
        self.name = name
        self.time = 0

    def tick(self):
        self.time += 1

    def send_message(self, clock):
        self.tick()
        clock.receive_message(self)

    def receive_message(self, clock):
        self.time = max(self.time, clock.time)
        print(str(self.time) + ": " + clock.name + " -> " + self.name)


clock1 = Clock("Часы 1")
clock2 = Clock("Часы 2")
clock3 = Clock("Часы 3")

clock1.send_message(clock3)
clock2.send_message(clock2)
clock3.send_message(clock1)
clock1.send_message(clock3)
