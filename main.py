from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget

class SoundWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 加载声音文件（与 main.py 同目录）
        self.sound = SoundLoader.load('gugu.mp3')
        if self.sound:
            self.sound.volume = 1.0  # 最大音量
            # 启动后立即播放一次，实现点击图标即发声
            self.sound.play()

    def on_touch_down(self, touch):
        # 每次触摸屏幕都播放声音（可重叠）
        if self.sound:
            self.sound.play()
        return super().on_touch_down(touch)

class GuGuApp(App):
    def build(self):
        return SoundWidget()

if __name__ == '__main__':
    GuGuApp().run()