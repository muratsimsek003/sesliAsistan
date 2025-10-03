import sys

def kurulum_testi():
    print("Kurulum testi baslatiliyor...")
    
    print(f"Python surumu: {sys.version}")
    
    kutuphaneler=[
        "speech_recognition",
        "transformers",
        "torch",
        "pygame",
        "edge_tts",
        "sklearn",
        "numpy",
        "pyaudio"
    ]
    
    for kutuphane in kutuphaneler:
        try:
            __import__(kutuphane)
            print(f"{kutuphane} kutuphanesi basariyla yuklendi.")
        except ImportError:
            print(f"{kutuphane} kutuphanesi yuklenemedi. Lutfen kurulumlari kontrol edin.")
            
    print("Kurulum testi tamamlandi")
    
if __name__ == "__main__":
    kurulum_testi()