import RPi.GPIO as GPIO
import datetime
import time
import board
from devices import dht11
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image , ImageDraw ,ImageFont

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
FONT_SANS_12 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc" ,12)

display = SSD1306_I2C(128, 64, board.I2C(), addr=0x3C)

if __name__== '__main__':
    th_sensor = dht11.DHT11(pin=14) 
    pre_datetime = ''
    display.fill(0)
    display.show()
    while True:
        data = th_sensor.read()
        timestamp = datetime.datetime.now()
        if data.is_valid():
            img = Image.new("1",(display.width, display.height))
            draw = ImageDraw.Draw(img)
            draw.text((0,0),'時刻  ' + timestamp.strftime('%H:%M:%S'),font=FONT_SANS_12,fill=1)
            draw.text((0,20),'温度  ' + str(data.temperature) + '℃',font=FONT_SANS_12,fill=1)
            draw.text((0,40),'湿度  ' + str(data.humidity) + '%' ,font=FONT_SANS_12,fill=1)
            display.image(img)
            display.show()
        

