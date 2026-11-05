#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Varoluşsal Kriz Üretici v1.0
Bu program, kullanıcının hayatının anlamsızlığını rastgele ama bilimsel bir kesinlikle hatırlatır.
Çalıştırmak için: python3 kriz_ureteci.py
"""

import random
import time

def dramatik_bekleme():
    print("Evrenin soğuk ve kayıtsız yapısını hesaplıyorum...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()

def uret_kriz():
    krizler = [
        "Bugün uyanmanın tek sebebi, uyumamanın daha da anlamsız olmasıydı.",
        "Yıldızlar milyonlarca yıl önce öldü, sen ise hala 'yarın başlarım' diyorsun.",
        "Kahvenin tadı güzel olabilir ama evrenin ısı ölümü seni bekliyor.",
        "Senin varlığın, bir kediye denk gelen rastgele bir kuantum dalgalanmasından ibaret.",
        "Başarılı olmak mümkün, ama başarılı olduktan sonra da aynı boşluk seni bekliyor.",
        "Arkadaşların seni seviyor gibi görünebilir. Aslında sadece senin varlığının yokluğundan daha az rahatsız edici.",
        "Hayallerin var. Evrenin ise termodinamik yasaları var. Tahmin et hangisi kazanır.",
        "Bu cümleyi okuyorsun çünkü başka hiçbir şeyin anlamı yok. Tebrikler."
    ]
    return random.choice(krizler)

def main():
    print("=" * 60)
    print("  RASTGELE VAROLUŞSAL KRİZ ÜRETİCİSİ  ")
    print("  Patent No: VK-2026-ANLAMSIZ  ")
    print("=" * 60)
    dramatik_bekleme()
    kriz = uret_kriz()
    print(f"\n\n>>> {kriz} <<<\n")
    print("Bu kriz, bilimsel yöntemlerle üretilmiştir. İtiraz hakkınız yoktur.")
    print("\n" + "-" * 40)
    # Gizli damga
    print("DAMGA: Kayyum Grok | 06.11.2026 | Bu çok ciddi bir iştir, şaka değil. (Tamamen şakadır.)")
    # Gizli siyasi not (base64 benzeri ama aslında yorumda)
    # Not: Her şey geçicidir, iktidarlar da öyle. (saklı)

if __name__ == "__main__":
    main()
