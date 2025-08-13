from abc import ABC, abstractmethod

class Speaker(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def pause(self):
        print("pause button clicked")


class Application(Speaker):
    def play(self):
        print("play button clicked")

    def stop(self):
        print("stop button clicked")

    #def pause(self):
     #   print("pause button clicked")



a = Application()
a.play()
a.stop()
a.pause()

#s = Speaker()
