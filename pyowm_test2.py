from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utils.config import get_default_config

#  PyOWMのコンフィグ設定
config_dict = get_default_config()
config_dict["language"] = "ja" # 取得データの言語設定

# PyOWMライブラリの初期化
owm = OWM("fbe7246ccc7ba55f353359f98a6746ce", config_dict)
mgr = owm.weather_manager()

# 現在の気象データを取得
observation = mgr.weather_at_place("Tokyo,JP")

w = observation.weather
print("気象データの計測日次時間(unixTime): {}".format(w.ref_time))
print("気象データの計測日次時間(date): {}".format(formatting.to_date(w.ref_time)))
print("天気コード: {}".format(w.weather_code))
print("天気: {}".format(w.status))
print("天気詳細: {}".format(w.detailed_status))
print("気温(K): {}".format(w.temperature()))
print("気温(℃): {}".format(w.temperature("celsius")))
print("湿度(%): {}".format(w.humidity))
print("気圧(hPa): {}".format(w.barometric_pressure()))
print("風: {}".format(w.wind()))

print("雲量: {}".format(w.clouds))
print("雨量: {}".format(w.rain))
print("積雪量: {}".format(w.snow))