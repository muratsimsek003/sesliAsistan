import edge_tts
import pygame
import asyncio
import tempfile
import os
import time


class MetinToSes:
    def __init__(self):
        self.voice="tr-TR-EmelNeural"
        pygame.mixer.init()
        
    async def metin_to_ses_dosyasi(self, text):
        
        print(f"Ses üretiliyor: {text[:30]}...")
        
        comm=edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate="+5%",
            volume="+75%" ,
            pitch="-20Hz"
        )
        
        temp_file=tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        
        await comm.save(temp_file.name)
        return temp_file.name   
    
    def ses_dosyasi_cal(self, dosya_yolu):
        
        print("Ses dosyasi caliniyor...")
        
        try:
            pygame.mixer.music.unload()
        except:
            pass
        
        pygame.mixer.music.load(dosya_yolu)
        pygame.mixer.music.set_volume(0.95)
        pygame.mixer.music.play()
        
        clock=pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(10)
            
        pygame.mixer.music.unload()
        os.remove(dosya_yolu)
        print("Ses dosyasi calindi ve silindi.  ")
        
    def konus(self, text):
        dosya= asyncio.run(self.metin_to_ses_dosyasi(text))
        self.ses_dosyasi_cal(dosya)
        
        
def main():
    tts=MetinToSes()
    
    while True:
        print("\n 1. Metin to Ses")
        print("\n 2. Çıkış")
        secim=input("Seçiminiz (1/2): ")
        
        if secim=="1":
            metin=input("Metin girin: ")
            tts.konus(metin)
        elif secim=="2":
            print("Çıkış yapılıyor...")
            break
        
if __name__=="__main__":
    main()
        
    
        
        
        

