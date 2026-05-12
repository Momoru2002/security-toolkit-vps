# 🛡️ VPS Security Toolkit

Toolkit lengkap untuk audit keamanan VPS & server — 5 modul defensif.

> ⚠️ **ETHICAL USE ONLY**
> Semua tools hanya untuk server/domain **yang kamu miliki sendiri** atau sudah mendapat izin eksplisit.

---

## 📦 Struktur Project

```
vps-security-toolkit/
├── config.yaml                       ← Isi dulu sebelum pakai!
├── requirements.txt
├── findings.json                     ← Output temuan (dibuat otomatis)
│
├── 1_vps_security_checker/
│   └── vps_security_checker.py       ← Audit konfigurasi VPS via SSH
│
├── 2_ai_media_detector/
│   └── ai_media_detector.py          ← Deteksi gambar/video AI generated
│
├── 3_ssl_tls_analyzer/
│   └── ssl_tls_analyzer.py           ← Audit sertifikat & enkripsi SSL/TLS
│
├── 4_port_service_scanner/
│   └── port_service_scanner.py       ← Scan port terbuka & identifikasi risiko
│
└── 5_log_anomaly_detector/
    └── log_anomaly_detector.py       ← Analisis log server untuk deteksi serangan
```

---

## 🚀 Setup

```bash
pip install -r requirements.txt
nano config.yaml    # Isi host VPS dan target_url kamu
```

---

## ▶️ Cara Jalankan Per Modul

### Modul 1 — VPS Security Checker
```bash
cd 1_vps_security_checker
python vps_security_checker.py                         # pakai config.yaml
python vps_security_checker.py --host 1.2.3.4 --user root --key ~/.ssh/id_rsa
python vps_security_checker.py --output hasil.json
```
Apa yang dicek:
- SSH hardening (root login, password auth, port default)
- Firewall UFW & iptables aktif atau tidak
- OS & security updates tertinggal
- User dengan UID 0 tersembunyi
- Fail2ban terinstall
- Service berbahaya (Telnet, FTP)
- Konfigurasi kernel (SYN cookies, IP forwarding)

---

### Modul 2 — AI Media Detector
```bash
cd 2_ai_media_detector
python ai_media_detector.py --file foto.jpg            # satu file
python ai_media_detector.py --folder ./images/         # satu folder
python ai_media_detector.py --file video.mp4           # video
python ai_media_detector.py --file foto.jpg --threshold 70  # ubah sensitivitas
python ai_media_detector.py --folder ./media/ --output hasil.json
```
Apa yang dianalisis:
- Noise pattern (terlalu bersih = indikasi AI)
- Distribusi warna (terlalu sempurna = AI)
- Edge smoothness (khas diffusion model)
- Metadata EXIF (ada/tidaknya info kamera asli)
- Analisis frekuensi domain (FFT)
- Resolusi standar AI generator

---

### Modul 3 — SSL/TLS Analyzer
```bash
cd 3_ssl_tls_analyzer
python ssl_tls_analyzer.py                             # pakai config.yaml
python ssl_tls_analyzer.py --host example.com
python ssl_tls_analyzer.py --host example.com --port 8443
python ssl_tls_analyzer.py --host example.com --output ssl_result.json
```
Apa yang dicek:
- Sertifikat expired atau hampir expired
- CN mismatch & self-signed cert
- Protokol TLS lama masih aktif (TLS 1.0, 1.1)
- Cipher lemah (RC4, DES, 3DES, dll)
- HSTS header aktif atau tidak
- Subject Alternative Name (SAN)

---

### Modul 4 — Open Port & Service Scanner
```bash
cd 4_port_service_scanner
python port_service_scanner.py                         # pakai config.yaml
python port_service_scanner.py --host 1.2.3.4
python port_service_scanner.py --host 1.2.3.4 --ports 1-10000
python port_service_scanner.py --host 1.2.3.4 --ports 22,80,443,3306,6379
python port_service_scanner.py --host 1.2.3.4 --threads 200 --timeout 0.5
python port_service_scanner.py --host 1.2.3.4 --output ports.json
```
Apa yang dicek:
- Port terbuka dengan identifikasi service
- Risk rating per port (CRITICAL/HIGH/MEDIUM/LOW)
- Banner grabbing untuk deteksi versi
- Database yang expose ke publik (MySQL, Redis, MongoDB, dll)
- Docker API tanpa auth
- Port default berbahaya (Telnet, RDP, VNC, dll)

---

### Modul 5 — Log Anomaly Detector
```bash
cd 5_log_anomaly_detector
python log_anomaly_detector.py                         # tampilkan panduan log
python log_anomaly_detector.py --log /var/log/auth.log
python log_anomaly_detector.py --log /var/log/nginx/access.log
python log_anomaly_detector.py --log /var/log/syslog --lines 50000
python log_anomaly_detector.py --log auth.log --output anomali.json
python log_anomaly_detector.py --log access.log --top-ips 20
```
Apa yang dideteksi:
- SSH brute force (login gagal berulang)
- SQL injection attempt
- XSS attempt
- Directory traversal
- Web scanner & automated tools
- Login root dari IP eksternal
- Sudo abuse
- Port scan pattern
- DDoS indicator
- Reverse shell attempt
- Crontab modification (persistence backdoor)

---

## 🔄 Workflow Lengkap

```bash
# 1. Jalankan semua modul
cd 1_vps_security_checker && python vps_security_checker.py && cd ..
cd 3_ssl_tls_analyzer     && python ssl_tls_analyzer.py     && cd ..
cd 4_port_service_scanner && python port_service_scanner.py && cd ..
cd 5_log_anomaly_detector && python log_anomaly_detector.py \
    --log /var/log/auth.log && cd ..

# 2. Analisis media jika perlu
cd 2_ai_media_detector && python ai_media_detector.py --folder ./suspect/ && cd ..

# 3. Lihat semua temuan
cat findings.json
```

---

## 🧩 Tabel Modul

| Modul | Tools | Target Input | Koneksi |
|-------|-------|-------------|---------|
| 1 | VPS Security Checker | VPS kamu | SSH |
| 2 | AI Media Detector | File gambar/video | Lokal |
| 3 | SSL/TLS Analyzer | Domain/IP | HTTPS |
| 4 | Port Scanner | IP/domain | TCP |
| 5 | Log Anomaly Detector | File log | Lokal |

---

## 📦 Dependencies

```
httpx        → HTTP requests (modul 3)
rich         → Terminal UI yang bagus
pyyaml       → Baca config.yaml
typer        → CLI framework
colorama     → Warna terminal Windows
paramiko     → SSH connection (modul 1)
cryptography → SSL/TLS parsing
Pillow       → Analisis gambar (modul 2)
numpy        → Komputasi numerik (modul 2)
scipy        → Analisis statistik (modul 2)
```

---

*Dibuat untuk keperluan defensive security — audit VPS & media verification.*