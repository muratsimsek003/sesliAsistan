import json
import os

class SelamlasmaSistemi:
    def __init__(self):
        self.selamlasmalar_dosyasi = "greetings.json"
        self.selamlasmalar = self.selamlasmalar_yukle()
        
    def selamlasmalar_yukle(self):
        """Selamlaşmaları yükle"""
        if os.path.exists(self.selamlasmalar_dosyasi):
            try:
                with open(self.selamlasmalar_dosyasi, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
                
        # Varsayılan selamlaşmalar
        varsayilan = {
            "merhaba": "Merhaba, size nasıl yardımcı olabilirim?",
            "selam": "Selam, nasıl yardımcı olabilirim?",
            "nasılsın": "İyiyim, teşekkür ederim. Siz nasılsınız?",
            "güle güle": "Güle güle! İyi günler dilerim.",
            "hoşça kal": "Hoşça kalın! Tekrar görüşmek üzere."
        }
        
        # Dosyaya kaydet
        with open(self.selamlasmalar_dosyasi, "w", encoding="utf-8") as f:
            json.dump(varsayilan, f, ensure_ascii=False, indent=4)
            
        return varsayilan
        
    def selamlasmaya_cevap_ver(self, text):
        """Selamlaşma varsa cevap ver"""
        text_lower = text.lower()
        
        for anahtar, cevap in self.selamlasmalar.items():
            if anahtar in text_lower:
                print(f"Selamlaşma algılandı: {anahtar}")
                print(f"Cevap: {cevap}")
                return cevap
                
        return None

def main():
    selamlasma = SelamlasmaSistemi()
    
    print("Selamlaşma Sistemi Testi")
    print("Çıkmak için 'çıkış' yazın")
    
    while True:
        text = input("\nBir şey söyleyin: ")
        
        if text.lower() == "çıkış":
            break
            
        cevap = selamlasma.selamlasmaya_cevap_ver(text)
        
        if cevap:
            print(f"Asistan: {cevap}")
        else:
            print("Asistan: Selamlaşma algılanmadı.")

if __name__ == "__main__":
    main()
