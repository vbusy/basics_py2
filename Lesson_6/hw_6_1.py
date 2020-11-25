from time import sleep

class TrafficLight:
    __trafficlight_color = ["red", "yellow", "green"]

    def running(self):
        s = 0
        while s != 3:
            print(TrafficLight.__trafficlight_color[s])
            if s == 0:
                sleep(7)
            elif s == 1:
                sleep(2)
            elif s == 2:
                sleep(10)
            s = s + 1

traf = TrafficLight()
traf.running()