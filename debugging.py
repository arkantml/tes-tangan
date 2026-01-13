import sys
try:
    import serial
    print("\n--- INFO PENTING ---")
    print(f"1. Lokasi Serial: {serial.__file__}") 
    print(f"2. Isi Serial: {dir(serial)}")
    print("--------------------\n")
    
    # Cek apakah 'Serial' ada di dalam
    if 'Serial' in dir(serial):
        print("✅ KABAR BAIK: Modul Serial ditemukan! Harusnya programmu jalan.")
    else:
        print("❌ BAHAYA: Modul 'serial' yang terload PALSU/KOSONG. Tidak ada class 'Serial'.")
        
except ImportError:
    print("❌ ERROR: Python bilang library 'serial' BELUM terinstall sama sekali.")
except Exception as e:
    print(f"Error aneh: {e}")