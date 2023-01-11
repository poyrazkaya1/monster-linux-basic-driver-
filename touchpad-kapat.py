# touchpad kapatıp açma
import os 

veri =input("touchpad açılsın mı kapatılsın mı ?")

if veri == "kapat":
    print("Touchpad kapatılıyor...")
    os.system('xinput set-prop 14 "Device Enabled" 0')
if veri == "aç":
    print("touchpad açılıyor....")
    os.system('xinput set-prop 14 "Device Enabled" 1')
