import openai
import time 
import json
from selamlasma import SelamlasmaSistemi


class AIModel:
    def __init__(self):
        self.api_key_loaded=False
        self.model_name="gpt-3.5-turbo"
        self.selamlasma=SelamlasmaSistemi()
        self.model_yukle()
        
        
    def model_yukle(self):
        print("OpenAI API modeli yükleniyor...  ")
        
        start_time=time.time()
        
        try:
            
            self.load_api_key()
            
            self.test_api_connection()
            print("API anahtarı çalışma kontrolu başarılı.")
            
            yukleme_suresi=time.time()-start_time
            print(f"OpenAI API modeli yüklendi. (Süre: {yukleme_suresi:.2f} saniye)")
            self.api_key_loaded=True
            
        except Exception as e:
            print(f"OpenAI API modeli yüklenemedi: {e}")
            self.api_key_loaded=False  
            
            
    def load_api_key(self):
         
         try:
              with open("api_keys.json", "r", encoding="utf-8") as f:
                  keys=json.load(f)
                  
              api_key=keys.get("openai_api_key", "")
            
              if not api_key or api_key.startswith("your-openai-api-key-here"):
                  raise ValueError("Lütfen geçerli bir OpenAI API anahtarı sağlayın.")
              
              openai.api_key=api_key
              print("OpenAI API anahtarı yüklendi.")
              
         except FileNotFoundError:
                raise FileNotFoundError("api_keys.json dosyası bulunamadı.")
            
            
              
    def test_api_connection(self):
       try:
           response=openai.chat.completions.create(
               model=self.model_name,
               messages=[
                   {"role": "user", "content": "Test"},],
               max_tokens=5
           )
           return True
       except Exception as e:        
              raise Exception(f"API bağlantı testi başarısız: {e}   ")
          
    
    def soru_cevapla(self, soru):
        
        if not self.api_key_loaded:
            return "API anahtarı yüklenemediği için cevap verilemiyor.", 0
        
        selamlasma_cevabi=self.selamlasma.selamlasmaya_cevap_ver(soru)
        if  selamlasma_cevabi:
            return selamlasma_cevabi, 1.0
        
        try:
            start_time=time.time()
            
            system_message="Sen yardımcı bir asistanısın."  
            
            response=openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": soru}
                ],
                max_tokens=150,
                temperature=0.7
                
            )
            
            cevap= response.choices[0].message.content.strip()
            
            token_used=response.usage.total_tokens
            islem_suresi=time.time()-start_time
            
            print(f" Openai Cevabı: {cevap}")
            print(f"Token kullanımı: {token_used}")
            print(f"İşlem süresi: {islem_suresi:.2f} saniye")
            
            
            guven= 0.85
            
            return cevap, guven    
        
        except openai.RateLimitError:
            return "API istek limiti aşıldı. Lütfen daha sonra tekrar deneyin.", 0
        
        except openai.AuthenticationError:
            return "API kimlik doğrulama hatası. Lütfen API anahtarınızı kontrol edin.", 0  
        except Exception as e:
            return f"Bir hata oluştu: {e}", 0
        
def main():
    ai=AIModel()
    
    if not ai.api_key_loaded:   
        print("\n API anahtarı yüklenemedi")
        print("Lütfen api_keys.json dosyasını kontrol edin ve geçerli bir OpenAI API anahtarı ekleyin.")
        print("Programı tekrar çalıştırın")
        return      
    
    print("\n AI Model Testi Başlıyor")
    
    print("Çıkmak için 'çıkış' yazın")
    
    while True:
        soru=input("\nBir şey sor (veya çıkış yap): ")  
        
        if soru.lower()=="çıkış":   
            break
        
        cevap,guven=ai.soru_cevapla(soru)
        
        if guven==1.0:
            print(f"Selamlaşma ile cevaplandırıldı")
            
        else:
            print(f"Openai ile cevaplandırıldı" )
            
            
        print(f"Cevap: {cevap} (Güven: {guven:.2f}) ")   
        
        
if __name__=="__main__":
    main()
                

        
        
        
