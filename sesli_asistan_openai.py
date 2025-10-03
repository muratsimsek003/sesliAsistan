import time 
from openai_apikey_modeli import AIModel
from wake_word import WakeWordDetector
from text_to_speech import MetinToSes
from ses_tanima import SesToMetin
from temel_yapi import Timer


class SesliAIModel(AIModel):
    def __init__(self):

        super().__init__()
        
        print("Sesli özellikler ekleniyor...")
        
        # Sesli modülleri başlat
        with Timer("Ses modülleri yükleme"):
            self.wake_word_detector = WakeWordDetector()
            self.tts = MetinToSes()
            self.stt = SesToMetin()
        
        if self.api_key_loaded:
            print("Mikrofon ayarlamaları yapılıyor...")
            self.stt.mikrofon_ayarla()
            self.wake_word_detector.mikrofon_ayarla()
            print(" Sesli AI Asistan hazır! 'Hey Asistan' komutunu bekliyor...")
        else:
            print(" Sistem tam olarak yüklenemedi!")


def main():
    try:
        print("="*60)
        print(" SESLİ AI ASİSTAN")
        print("="*60)
        
        ai = SesliAIModel()
        
        if not ai.api_key_loaded:   
            print("\n API anahtarı yüklenemedi")
            print("Programı tekrar çalıştırın")
            return

        print("\n" + "="*60)
        print("Sistem hazır! 'Hey Asistan' diyerek başlayın.")
        print(" Çıkmak için 'çıkış' veya 'kapat' deyin.")
        print("="*60 + "\n")

        session_start = time.time()
        question_count = 0

        while True:
            try:

                if not ai.wake_word_detector.wake_word_bekle():
                    continue
                
                print("🎯 Hey Asistan algılandı! Dinlemeye başlıyorum...")

                ai.tts.konus("Evet, sizi dinliyorum.")

                soru = ai.stt.tek_dinleme()
                if not soru:
                    ai.tts.konus("Sorunuzu anlayamadım, lütfen tekrar 'Hey Asistan' diyerek başlayın.")
                    continue

                print(f"\n📝 Soru {question_count + 1}: {soru}")
                

                if any(word in soru.lower() for word in ["çıkış",  "kapat"]):
                    ai.tts.konus("Hoşça kalın! İyi günler dilerim.")
                    break


                with Timer("Toplam soru-cevap işlemi"):
                    cevap, guven = ai.soru_cevapla(soru)
                    
                    ai.tts.konus(cevap)

                question_count += 1
                
                if guven == 1.0:
                    print(f"Selamlaşma ile cevaplandırıldı")
                else:
                    print(f"Openai ile cevaplandırıldı")
                    
                print(f"Cevap: {cevap} (Güven: {guven:.2f})")
                print("\n" + "-"*40)
                print("Yeni bir soru için 'Hey Asistan' deyin.")
                print("-"*40)
                
            except KeyboardInterrupt:
                ai.tts.konus("Program sonlandırılıyor. Hoşça kalın!")
                break
                
            except Exception as e:
                print(f"İşlem hatası: {e}")
                print("Sistem devam ediyor, tekrar 'Hey Asistan' diyebilirsiniz.")

        # Oturum istatistikleri
        total_time = time.time() - session_start
        print("\n" + "="*60)

        print(f"Toplam soru sayısı: {question_count}")
        print(f" Oturum süresi: {int(total_time//60)} dakika {total_time%60:.2f} saniye")
        if question_count > 0:
            print(f" Ortalama soru başına süre: {total_time/question_count:.2f} saniye")
        print("="*60)
        
    
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")


if __name__ == "__main__":
    main()