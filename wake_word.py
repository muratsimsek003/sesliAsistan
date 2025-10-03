import speech_recognition as sr
import time

class WakeWordDetector: 
    def __init__(self):
        self.recognizer=sr.Recognizer()
        self.recognizer.energy_threshold=300 
        self.recognizer.pause_threshold=0.5
        self.wake_word="hey asistan"
        
    def mikrofon_ayarla(self):
        
        print("Mikrofon ayarlanıyor...  ")
        with sr.Microphone() as kaynak:
            self.recognizer.adjust_for_ambient_noise(kaynak, duration=0.5)
            print("Mikrofon ayarlandı.")
            
    def wake_word_bekle(self):
        
        print(f"{self.wake_word} bekleniyor...")
        
        with sr.Microphone() as kaynak:
            
            while True:
                try:
                    audio=self.recognizer.listen(kaynak, timeout=5, phrase_time_limit=5)
                    text=self.recognizer.recognize_google(audio, language="tr-TR").lower()
                    print(f"Algınan Metin:{text}")
                    
                    if self.wake_word in text:
                        print("Hey Asistan algılandı!")
                        return True
                    
                except (sr.UnknownValueError, sr.WaitTimeoutError):
                    continue
                
                except sr.RequestError:
                    print("ses tanıma servisine ulaşılamıyor.   ")
                    continue
                    
                    
                    
def main():
    detector= WakeWordDetector()
    detector.mikrofon_ayarla()
    
    print("Ctrl+C ile çıkış yapabilirsiniz. ")
    
    try:
        while True:
            if detector.wake_word_bekle():
                print("Wake word  algılandı şimdi komut verebilirsiniz.")
                time.sleep(2)
                
    except KeyboardInterrupt:
        print("\n Program sonlandırıldı")
        
if __name__=="__main__":
    main()
    
                
           
    

