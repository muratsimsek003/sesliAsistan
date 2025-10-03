import speech_recognition as sr
import time

class SesToMetin:
    def __init__(self):
        self.recognizer=sr.Recognizer()
        self.recognizer.energy_thresold=300
        self.recognizer.pause_threshold=0.5
        
    def mikrofon_ayarla(self):
        print("Mikrofon ayarlanıyor...")
        
        with sr.Microphone() as kaynak:
            self.recognizer.adjust_for_ambient_noise(kaynak, duration=1)
            print("Mikrofon ayarlandı.")
            
    def tek_dinleme(self):
        print("Konuşun...")
        
        with sr.Microphone() as kaynak:
            try:
                audio=self.recognizer.listen(kaynak, timeout=5, phrase_time_limit=10)
                print("Ses işleniyor...")
                
                text= self.recognizer.recognize_google(audio, language="tr-TR")
                print(f"Algılanan Metin: {text}")
                return text
            except sr.WaitTimeoutError:
                print("Zaman aşımı: Belirtilen süre içinde konuşma algılanamadı.")
                return None
            except sr.UnknownValueError:
                print("Anlaşılamayan ses.")
                return None 
            
def main():
    ses_tanima=SesToMetin()
    ses_tanima.mikrofon_ayarla()
    
    while True:
        print("\n 1. Tek dinleme")
        print(" 2. Çıkış")
        
        secim=input("Seçiminiz (1/2): ")
        
        if secim=="1":
            ses_tanima.tek_dinleme()
            
        elif secim=="2":
            print("Çıkış yapılıyor...")
            break
            
if __name__=="__main__":
    main()
        
