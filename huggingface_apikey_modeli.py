from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import time
import json
from selamlasma import SelamlasmaSistemi

class AIModel:
    def __init__(self):
        self.api_key_loaded= False
        self.model_name="muratsimsek003/bert-kultur-qa-5epoch"
        self.tokenizer=None
        self.model=None
        self.qa_pipeline=None
        self.selamlasma=SelamlasmaSistemi()
        self.model_yukle()
        
    def model_yukle(self):
        print("Transformers tabanlı model yukleniyor...")
        
        start_time=time.time()
        
        try:
            self.load_model()
            self.test_model_connection()
            print("Model çalışma kontrolu başarılı.")
            
            yukleme_suresi=time.time()-start_time
            print(f"Model yüklendi. (Süre: {yukleme_suresi:.2f} saniye)")   
            self.api_key_loaded=True
            
        except Exception as e:
            print(f"Model yüklenemedi: {e}")
            self.api_key_loaded=False
            
            
    def load_model(self):
        
        try:
            self.tokenizer=AutoTokenizer.from_pretrained(self.model_name)
            self.model=AutoModelForQuestionAnswering.from_pretrained(self.model_name)
            
            self.qa_pipeline=pipeline("question-answering",
                                      model=self.model,
                                      tokenizer=self.tokenizer,
                                      max_answer_len=100,
                                      min_answer_len=10)
            
            print("Model ve tokenizer yüklendi.")
            
        except Exception as e:
            raise Exception(f"Model yüklenirken hata oluştu: {e}")
        
        
    def test_model_connection(self):
        try:
            text_context= "Python bir programlama dilidir."
            test_result=self.qa_pipeline(question="Python nedir?", context=text_context)
            return True
        except Exception as e:
            raise Exception(f"Model test edilirken hata oluştu: {e}")
        
        
    def soru_cevapla(self, soru):
          
        if not self.api_key_loaded:
                return "Model yüklenemedi veya API anahtarı geçerli değil.",0
            
        selamlasma_cevabi=self.selamlasma.selamlasmaya_cevap_ver(soru)
        if selamlasma_cevabi:
                return selamlasma_cevabi, 1.0
            
        try:
            start_time=time.time()  
            context="Python progralama dilidir. Türkiye güzel bir ülkedir. Eğitim BTK akademinden alınır."  
            result=self.qa_pipeline(question=soru, context=context)
            
            cevap=result["answer"].strip()
            guven_skoru=result["score"]
            
            islem_suresi=time.time()-start_time
            
            print(f"Soru: {soru} | Cevap: {cevap} | Güven Skoru: {guven_skoru:.2f} | İşlem Süresi: {islem_suresi:.2f} saniye")
            
            return cevap, guven_skoru
            
        except Exception as e:
            print(f"Soru cevaplanırken hata oluştu: {e}")
            return "Cevap alınamadı.", 0
            
            
       
def main():
    ai=AIModel()
    
    if not ai.api_key_loaded:   
        print("\n Model yüklenemedi veya API anahtarı geçerli değil.")
        print("Lütfen internet bağlantınızı kontrol edin ve modeli tekrar yükleyin.")
        print("Programı tekrar çalıştırın")
        return  
    
    print("\n Transformers modeli testi başlıyor... ")
    
    print("Çıkmak için 'çıkış' yazın.")
    
    while True:
        soru=input("\nBir şey sor (veya çıkış yap): ")  
        
        if soru.lower()=="çıkış":
            break
        
        cevap,guven=ai.soru_cevapla(soru)
        
        if guven==1.0:
            print(f"Selamlaşma ile cevaplandırıldı")
            
        else:
            print(f"Transformers modeli ile cevaplandırıldı" )  
        
        print(f"Cevap: {cevap} (Güven: {guven:.2f}) ") 
        
        
        
if __name__=="__main__":    
    main()  
                
             