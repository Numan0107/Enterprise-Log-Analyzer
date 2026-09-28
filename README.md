# 🚀 Enterprise Log Analyzer & Incident Reporter

Bu proje; büyük ölçekli kurumsal sunucuların ürettiği milyonlarca satırlık hata loglarını (Log Files) saniyeler içinde tarayıp, kritik sistem çökmelerini tespit eden ve bunları otomatik olarak kurumsal bir rapora dönüştüren yüksek performanslı bir **Python Otomasyon Servisidir**.

## 🎯 Proje Ne Yapıyor?
* **Sahte Log Simülasyonu (`generate_logs.py`):** Gerçek bir .NET backend sisteminin üretebileceği veritabanı zamanaşımları, thread kilitlenmeleri (deadlock) ve sunucu tabanlı ağ hataları gibi binlerce kurumsal log satırını otomatik simüle eder.
* **Regex ile Milisaniyede Tarama (`analyzer.py`):** Düzenli ifadeler (Regular Expressions) kullanarak devasa metin dosyalarını işlemciyi yormadan tarar ve sadece `CRITICAL` ve `ERROR` seviyesindeki tehditleri ayıklar.
* **Incident Raporlama:** Tespit edilen tüm sistem açıklarını ve kritik hataları `incident_report.txt` adında kurumsal İngilizce bir özet rapora dönüştürür.

## 🛠️ Teknik Altyapı
* **Dil:** Python 3.13
* **Ana Modüller:** `re` (Regex Engine), `os` (File System Operations), `datetime` (UTC Time Tracking)
