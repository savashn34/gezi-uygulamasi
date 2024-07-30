# Gezi Uygulaması

Bu uygulama turizm firmaları için geliştirilmiş bir turist rehberi uygulamasıdır.

## Kurulum

### Gereksinimler

- Python (3.x sürümü önerilir)
- pip (Python paket yönetim aracı)
- Sanal ortam yönetimi için `venv` modülü

### Adım 1: Depoyu Klonlayın

Öncelikle projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/kullaniciadi/gezi-uygulamasi.git
cd gezi

### Adım 2: Sanal Ortam Oluşturup Etkinleştirme
Bir sanal ortam oluşturup etkinleştirin:

Windows:
python -m venv myenv
myenv\Scripts\activate

MacOS / Linux
python3 -m venv myenv
source myenv/bin/activate

### Adım 3: Gereksinimleri Yükleyin
requirements.txt belgesi içerisindeki uygulama bağımlılıklarını yükleyin:

pip install -r requirements.txt

### Adım 4: Veri Tabanını Bağlayın:
python manage.py makemigrations
python manage.py migrate

### ADIM 5: Uygulamayı Çalıştırın:
python manage.py runserver