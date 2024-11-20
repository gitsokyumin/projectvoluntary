from time import strftime
from kivy.clock import Clock
from kivy.app import App
from kivy.core.window import Window

Window.size = (720, 600)

class StopWatchApp(App):
    # 스톱워치별 상태 초기화
    stopwatches = {
        "korean": {"sw_seconds": 0, "sw_started": False},
        "mathmatics": {"sw_seconds": 0, "sw_started": False},
        "english": {"sw_seconds": 0, "sw_started": False},
    }

    def update_time(self, t):
        for key, data in self.stopwatches.items():
            if data["sw_started"]:
                data["sw_seconds"] += t  # 시간 업데이트

            
            hours, remainder = divmod(data["sw_seconds"], 3600)
            minutes, seconds = divmod(remainder, 60)

            
            self.root.ids[key].text = "{:02d}:{:02d}:{:02d}".format(
                int(hours), int(minutes), int(seconds)
            )
        
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0.1)

    def start_stop(self, name):
        data = self.stopwatches[name]
       
        data["sw_started"] = not data["sw_started"]
      
        self.root.ids[f"{name}_start_stop"].text = "Start" if not data["sw_started"] else "Stop"

    def reset(self, name):
        data = self.stopwatches[name]
        if data["sw_started"]:
            
            self.root.ids[f"{name}_start_stop"].text = "Start"
            data["sw_started"] = False
        
        data["sw_seconds"] = 0

StopWatchApp().run()