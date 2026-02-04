import kivy
kivy.require('2.1.0')  # 固定Kivy版本，避免兼容问题
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# ---------------------- 已嵌入所有直播地址（无需修改） ----------------------
LIVE_CHANNELS = [
    {"name": "CCTV-1综合频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9201?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-2财经频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9202?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-3综艺频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9203?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-4国际频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9239?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-5体育频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9204?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-6电影频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9206?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-7国防军事频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9271?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-8电视剧频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9208?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-9纪录频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9209?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-10科教频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9210?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-11戏曲频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9011?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-12社会与法频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9211?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-13新闻频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9013?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-14少儿频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9212?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-15音乐频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9015?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-16奥林匹克频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9305?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-17农业农村频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9207?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV 5+ 体育赛事道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9205?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9200?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁都市频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9330?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁影视剧频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9332?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁体育频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9331?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁生活频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9991?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁教育青少频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9327?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁北方频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9992?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁公共频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9122?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "辽宁经济频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9121?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "移动电视频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9329?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CHC动作电影频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9301?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CHC高清电影频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9303?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CHC家庭影院频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9304?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "北京卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9220?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "天津卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9221?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "上海东方卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9223?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "浙江卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9250?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "江苏卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9251?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "安徽卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9215?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "湖南卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9214?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "贵州卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9269?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "山东卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9217?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "山西卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9046?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "广东卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9218?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "广西卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9309?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "湖北卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9216?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "江西卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9310?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "河北卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9311?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "河南卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9312?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "四川卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9241?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "重庆卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9240?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "福建东南卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9253?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "海南卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9272?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "青海卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9062?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "云南卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9313?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "陕西卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9059?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "内蒙古卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9060?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "宁夏卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9061?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "吉林卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9270?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "新疆卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9063?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "甘肃卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9064?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "西藏卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9065?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "黑龙江卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9213?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "深圳卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9219?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "厦门卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9056?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CETV1", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9244?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CETV4", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9314?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "山东教育卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9276?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "兵团卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9068?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "农林卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9069?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "延边卫视", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9277?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "金鹰卡通频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9328?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "炫动卡通频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9071?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "优漫卡通频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9072?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "嘉佳卡通频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9073?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "卡酷少儿频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9334?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "金鹰纪实频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9225?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "北京纪实频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9224?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-4 欧洲", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9317?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "CCTV-4 美洲", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9318?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "电视指南频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9088?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "证券服务频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9316?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "家庭理财频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9024?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "新动漫频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9034?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "快乐垂钓频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9267?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "高尔夫网球频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9285?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "4K欢笑剧场频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9294?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "百姓健康频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9324?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "先锋乒羽频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9302?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "第一剧场频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9090?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "怀旧剧场频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9093?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "风云剧场频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9092?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "风云足球频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9089?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "风云音乐频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9094?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "央视台球频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9126?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "央视文化精品频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9095?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "世界地理频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9091?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "兵器科技频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9125?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "女性时尚频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9097?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "茶频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9268?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "都市剧场频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9292?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "法治天地频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9286?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "金色学堂频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9287?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "动漫秀场频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9290?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "游戏风云频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9289?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "乐游频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9293?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "生活时尚频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9288?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "梨园频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9306?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "武术世界频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9307?virtualDomain=ZTE_EPG16.live_hls.zte.com"},
    {"name": "文物宝库频道", "url": "http://10.255.129.26:6060/ZTE_EPG16/2/9308?virtualDomain=ZTE_EPG16.live_hls.zte.com"}
]

# 主APP界面逻辑
class TVTestApp(App):
    def build(self):
        # 整体布局：视频区（上70%）+ 频道按钮区（下30%）
        main_layout = BoxLayout(orientation='vertical')
        
        # 1. 视频播放窗口
        self.video = Video(
            size_hint=(1, 0.7),  # 宽占满，高70%
            state='stop',
            allow_stretch=True  # 视频自适应窗口大小
        )
        main_layout.add_widget(self.video)
        
        # 2. 频道按钮滚动区（按钮太多，支持上下滚动）
        scroll_view = ScrollView(size_hint=(1, 0.3))
        channel_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        channel_layout.height = len(LIVE_CHANNELS) * 80  # 每个按钮高80px，计算总高度
        
        # 批量添加所有频道按钮
        for channel in LIVE_CHANNELS:
            btn = Button(
                text=channel["name"],
                font_size=25,
                size_hint_y=None,
                height=80,
                on_press=lambda x, url=channel["url"]: self.play_channel(url)  # 点击播放
            )
            channel_layout.add_widget(btn)
        
        scroll_view.add_widget(channel_layout)
        main_layout.add_widget(scroll_view)
        
        return main_layout
    
    # 播放频道的函数
    def play_channel(self, url):
        self.video.source = url  # 传入直播地址
        self.video.state = 'play'  # 开始播放
        # 播放失败时在命令行提示（新手可忽略）
        self.video.bind(on_error=lambda x, err: print(f"该频道播放失败：{err}"))

# 运行APP
if __name__ == '__main__':
    TVTestApp().run()