#--import serial.tools.list_ports
#--
#--print("Mencari perangkat yang tercolok...")
#--ports = serial.tools.list_ports.comports()
#--
#--if not ports:
#--    print("❌ Tidak ada perangkat yang terdeteksi! Coba periksa kabel USB.")
#--else:
#--    print("✅ Ditemukan perangkat di:")
#--    for port, desc, hwid in ports:
#--        print(f"-> {port}: {desc}")
#--        
#--    print("\n👉 Ganti 'COM...' di kodingan utamamu dengan port di atas!")

# --- GANTI BAGIAN INI ---
import serial
import time

try:
    print("Mencoba membuka COM3...")
    koneksi_arduino = serial.Serial('COM3', 9600) 
    print("Berhasil terhubung!")
    time.sleep(2) 
except Exception as e:
    # Bagian ini yang penting! Kita print error aslinya
    print(f"❌ GAGAL TOTAL! Penyebabnya: {e}") 
    exit()