import os
import json

class APIManager:
    def __init__(self):
        self.config_file="api_keys.json"
        self.load_api_keys()
        
    def create_config_template(self):
        template={
            "openai_api_key": "your_openai_api_key_here",
            "huggingface_api_key": "your_huggingface_api_key_here",   
        }
        
        with open(self.config_file, 'w', encoding="utf-8") as f:
            json.dump(template, f, indent=4)
            
            print(f"{self.config_file} dosyasi olusturuldu")
            print("Lutfen API anahtarlarinizi bu dosyaya ekleyin.")
            
            
    def  load_api_keys(self): 
        if not os.path.exists(self.config_file):
            print(f"API anahtar dosyası bulunamadı, Oluşturuluyor")
            self.create_config_template()
            return
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                keys=json.load(f)
                
            os.environ["OPENAI_API_KEY"]=keys.get("openai_api_key", "")
            os.environ["HUGGINGFACE_API_KEY"]=keys.get("huggingface_api_key", "")
            
            print("API anahtarları yüklendi.")
        except Exception as e:
            print(f"API anahtarları yüklenirken hata oluştu: {e}")
            
    def check_api_keys(self):
        
        openai_key =  os.getenv("OPENAI_API_KEY")
        hf_token = os.getenv("HUGGINGFACE_API_KEY") 
        
        print("API Anahtarları Kontrol Ediliyor...")
        
        if openai_key and openai_key != "your_openai_api_key_here":
            print("OpenAI API anahtarı mevcut.")
        else:
            print("OpenAI API anahtarı eksik veya hatalı.")
            
        if hf_token and hf_token != "your_huggingface_api_key_here":
            print("Hugging Face API anahtarı mevcut.")
        else:
            print("Hugging Face API anahtarı eksik veya hatalı.")
            
            
def main():
    api_manager= APIManager()
    api_manager.check_api_keys()
    
    print("\nAPI Anahtarları nasıl Alınır:")
    print("1. OpenAI: https://platform.openai.com/api-keys   adresinden API anahtarı alınır")
    print("2. Hugging Face: https://huggingface.co/settings/tokens adresinden API anahtarı alınır")
    
if __name__ == "__main__":
    main()