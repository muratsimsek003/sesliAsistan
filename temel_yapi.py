import time

class Timer:
    def __init__(self, name):
        self.name=name
        self.start_time= None
        
        
    def __enter__(self):
        self.start_time=time.time()
        return self
    
    
    def __exit__(self, *args):
        end=time.time()
        minutes=int((end-self.start_time)//60)
        seconds=(end-self.start_time)%60
        print(f"\n{self.name} işlemi süreleri:")
        print(f"Dakika:{minutes:02d}:{seconds:05.2f}")
        
        

class TemelAsistan:
    def __init__(self):
        print("Temel Asistan Başlatıldı")
        self.wake_word="hey asistan"
        
    def test_timer(self):
        with Timer("Test"):
            time.sleep(2)
            print("Test işlemi tamamlandı.")
    
def main():
    asistan= TemelAsistan()
    asistan.test_timer()
    print(f"Uyandirma kelimesi:{asistan.wake_word}")
    
    
if __name__ == "__main__":
    main()
        
            