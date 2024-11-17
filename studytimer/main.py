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

            # 시간을 시, 분, 초로 분할
            hours, remainder = divmod(data["sw_seconds"], 3600)
            minutes, seconds = divmod(remainder, 60)

            # UI 업데이트
            self.root.ids[key].text = "{:02d}:{:02d}:{:02d}".format(
                int(hours), int(minutes), int(seconds)
            )
        # 현재 시간 표시
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0.1)

    def start_stop(self, name):
        data = self.stopwatches[name]
        # 시작/중지 상태 전환
        data["sw_started"] = not data["sw_started"]
        # 버튼 텍스트 변경
        self.root.ids[f"{name}_start_stop"].text = "Start" if not data["sw_started"] else "Stop"

    def reset(self, name):
        data = self.stopwatches[name]
        if data["sw_started"]:
            # 동작 중이면 중지
            self.root.ids[f"{name}_start_stop"].text = "Start"
            data["sw_started"] = False
        # 시간 초기화
        data["sw_seconds"] = 0

StopWatchApp().run()