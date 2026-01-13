import cv2
import mediapipe as mp
import serial # Import library jembatan
import time   # Buat jeda sedikit

# --- BAGIAN KONEKSI ARDUINO ---
# GANTI 'COM3' dengan port Arduinomu! (Cek di Device Manager)
try:
    koneksi_arduino = serial.Serial('COM3', 9600) 
    print("Berhasil terhubung ke Arduino!")
    time.sleep(2) # Tunggu 2 detik biar Arduino siap (wajib)
except:
    print("Gagal connect ke Arduino. Cek port COM-nya!")
    exit()

# --- PERSIAPAN MEDIA PIPE (Sama kayak tadi) ---
modul_tangan = mp.solutions.hands
modul_gambar = mp.solutions.drawing_utils

detektor = modul_tangan.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
)

kamera = cv2.VideoCapture(0)

print("Mulai deteksi... Angkat telunjukmu!")

while True:
    sukses, gambar = kamera.read()
    if not sukses: break
    
    gambar = cv2.flip(gambar, 1) 
    gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
    hasil_deteksi = detektor.process(gambar_rgb)
    
    # Defaultnya kita kirim 'L' (Mati) kalau tangan gak ada
    pesan_untuk_kirim = 'L' 

    if hasil_deteksi.multi_hand_landmarks:
        for kerangka_tangan in hasil_deteksi.multi_hand_landmarks:
            modul_gambar.draw_landmarks(gambar, kerangka_tangan, modul_tangan.HAND_CONNECTIONS)
            
            tinggi, lebar, c = gambar.shape
            
            # Ambil posisi Ujung Telunjuk (ID 8) dan Ruas Telunjuk (ID 6)
            # Kita pakai cara cepat akses list landmark
            titik_ujung = kerangka_tangan.landmark[8]
            titik_ruas  = kerangka_tangan.landmark[6]
            
            # --- LOGIKA TELUNJUK ---
            # Ingat: Y makin kecil = makin tinggi posisinya
            if titik_ujung.y < titik_ruas.y:
                # Jari TERBUKA (Naik)
                pesan_untuk_kirim = 'H'
                status_teks = "LAMPU NYALA (Telunjuk Naik)"
                warna_teks = (0, 255, 0) # Hijau
            else:
                # Jari TERTUTUP (Turun)
                pesan_untuk_kirim = 'L'
                status_teks = "LAMPU MATI (Telunjuk Turun)"
                warna_teks = (0, 0, 255) # Merah

            # Tulis status di layar laptop
            cv2.putText(gambar, status_teks, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, warna_teks, 2)

    # --- KIRIM KE ARDUINO ---
    # Python butuh data bentuk 'bytes', jadi tambah b di depan huruf
    # b'H' artinya kirim huruf H dalam bahasa mesin
    if pesan_untuk_kirim == 'H':
        koneksi_arduino.write(b'H')
    else:
        koneksi_arduino.write(b'L')

    cv2.imshow("Kontrol LED dengan Jari", gambar)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup koneksi biar sopan
koneksi_arduino.close()
kamera.release()
cv2.destroyAllWindows()