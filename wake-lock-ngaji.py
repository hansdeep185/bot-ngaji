import schedule
import time
import os

def open_link(link):
    os.system(f"termux-open-url '{link}'")

def demo_meeting():
    open_link('https://telkomsel.zoom.us/j/99366710744?pwd=Sk5UYVpPZ0hVTnJpV2FJOUwwa3d6UT09')

# Mencegah HP masuk ke sleep mode
os.system('termux-wake-lock')

schedule.every().friday.at("12:25").do(demo_meeting)

# Jalankan scheduler
print("[INFO] Scheduler aktif. Menunggu waktu yang dijadwalkan...")
while True:
    schedule.run_pending()
    time.sleep(1)

# Lepaskan lock setelah selesai
os.system('termux-wake-unlock')