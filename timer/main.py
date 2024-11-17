from time import strftime
from kivy.clock import Clock
from kivy.app import App
from kivy.core.window import Window

Window.size = (720, 400)

class StopWatchApp(App):
   sw_seconds = 0
   sw_started = False

   def update_time(self, t):
      if self.sw_started:
         self.sw_seconds += t
      minutes, seconds = divmod(self.sw_seconds, 60)
      part_seconds = seconds * 100 % 100

      self.root.ids.stopwatch.text = "{:2d} : {:2d}.{:2d}".format(int(minutes), int(seconds), int(part_seconds))
      self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

   def on_start(self):
      Clock.schedule_interval(self.update_time, 0)
      
   def start_stop(self):
      self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
      self.sw_started = not self.sw_started

   def reset(self):
      if self.sw_started:
         self.root.ids.start_stop.text = 'Start'
         self.sw_started = False
      self.sw_seconds = 0
      
StopWatchApp().run()