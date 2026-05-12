<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-27ae60?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Security-Defensive%20Only-red?style=for-the-badge&logo=shield&logoColor=white"/>

# 🛡️ VPS Security Toolkit

**Advanced modular security toolkit for VPS auditing, SSL/TLS analysis, log monitoring, port scanning, and AI-generated media detection.**

*Built for defenders. Designed for clarity. Powered by Python.*

[Features](#-features) · [Installation](#-installation) · [Usage](#-quick-start) · [Modules](#-modules-overview) · [Reports](#-reports--database) · [License](#-license)

</div>

---

## 📌 About

VPS Security Toolkit (`momoru.py`) adalah toolkit keamanan berbasis Python yang dirancang untuk membantu **sysadmin**, **security researcher**, dan **developer** dalam melakukan audit keamanan server, analisis jaringan, dan investigasi insiden secara modular dan efisien.

> ⚠️ Toolkit ini **hanya** diperuntukkan untuk keperluan **defensive security**, **audit internal**, dan **riset pendidikan**. Penggunaan di luar tujuan tersebut adalah tanggung jawab pengguna sepenuhnya.

---

## ✨ Features

| # | Fitur | Deskripsi |
|---|-------|-----------|
| 🔐 | **VPS Security Audit** | Audit konfigurasi keamanan server via SSH |
| 🌐 | **SSL/TLS Analyzer** | Analisis sertifikat HTTPS dan konfigurasi TLS |
| 🚪 | **Port & Service Scanner** | Deteksi port terbuka dan identifikasi layanan |
| 📄 | **Log Anomaly Detector** | Deteksi aktivitas mencurigakan dari log server |
| 🖼️ | **AI Media Detector** | Heuristik deteksi media yang dibuat oleh AI |
| 📊 | **JSON Report Export** | Ekspor hasil scan ke laporan terstruktur |
| 🎨 | **Rich Terminal UI** | Tampilan terminal modern dan interaktif |
| ⚡ | **Modular Architecture** | Arsitektur bersih dan mudah dikembangkan |
| 🗂️ | **Local DB & Report Storage** | Penyimpanan hasil scan dengan SQLite |

---

## 📁 Project Structure

```
VPS-SECURITY-TOOLKIT/
│
├── core/
│   └── session.py              # Session & shared utilities
│
├── data/
│   ├── cache/                  # Cache hasil scan
│   ├── reports/                # Output laporan JSON
│   └── momoru.db               # SQLite database
│
├── logs/
│   └── test.log
│
├── modules/
│   ├── ai/                     # AI media detection
│   ├── logs/                   # Log anomaly detection
│   ├── ports/                  # Port & service scanner
│   ├── ssl/                    # SSL/TLS analyzer
│   └── vps/                    # VPS security audit
│
├── venv/                       # Virtual environment
├── momoru.py                   # Entry point utama
├── requirements.txt
├── sample.log
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/USERNAME/VPS-SECURITY-TOOLKIT.git
cd VPS-SECURITY-TOOLKIT
```

### 2️⃣ Buat Virtual Environment

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

```bash
python momoru.py
```

atau di Windows:

```bash
py momoru.py
```

Setelah dijalankan, pilih modul yang diinginkan dari menu interaktif.

---

## 🧩 Modules Overview

### 🔐 VPS Security Audit

Melakukan audit mendalam terhadap konfigurasi keamanan server melalui koneksi SSH.

**Deteksi meliputi:**
- SSH Hardening & Root Login Check
- Password Authentication Policy
- Firewall Status (UFW / iptables)
- Fail2Ban Detection
- Dangerous Services
- Hidden UID 0 Users
- Security Updates
- Kernel Security Configuration

---

### 🌐 SSL/TLS Analyzer

Analisis konfigurasi HTTPS dan validasi sertifikat SSL/TLS.

**Deteksi meliputi:**
- Expired / Self-Signed Certificate
- TLS Version Support
- Weak Cipher Detection
- HSTS Validation
- SAN & CN Mismatch

**Fitur tambahan:**
- TLS Risk Rating
- Cipher Enumeration
- Certificate Parsing & HTTPS Validation

---

### 🚪 Port & Service Scanner

Scanner TCP port untuk identifikasi layanan aktif dan potensi exposure.

**Deteksi meliputi:**
- Open Ports & Service Identification
- Banner Grabbing
- Public Database Exposure
- Dangerous Default Ports
- Docker API Exposure

**Layanan yang didukung:**

`MySQL` · `Redis` · `MongoDB` · `FTP` · `SSH` · `RDP` · `VNC` · `HTTP/HTTPS`

---

### 📄 Log Anomaly Detector

Mendeteksi aktivitas mencurigakan dari log server secara otomatis.

**Deteksi meliputi:**
- SSH Brute Force
- SQL Injection & XSS Attempt
- Directory Traversal
- Port Scanning Activity
- Reverse Shell Indicators
- DDoS Indicators
- Root & Sudo Abuse
- Persistence Behavior

**Contoh file log yang didukung:**
```
/var/log/auth.log
/var/log/syslog
/var/log/nginx/access.log
```

---

### 🖼️ AI Media Detector

Mendeteksi indikasi media yang dibuat oleh AI menggunakan analisis heuristik.

**Analisis meliputi:**
- Noise Pattern Analysis
- FFT Frequency Analysis
- Edge Smoothness Detection
- Metadata EXIF Inspection
- AI Resolution Pattern
- Color Distribution

**Format yang didukung:**

| Kategori | Format |
|----------|--------|
| 🖼️ Image | JPG, JPEG, PNG, WEBP |
| 🎥 Video | MP4, AVI, MOV |

> ⚠️ Analisis heuristik **tidak menjamin akurasi 100%**. Gunakan sebagai indikasi awal saja.

---

## 📊 Reports & Database

### Output Laporan

Semua hasil scan dapat disimpan ke direktori:
```
data/reports/
```

Format output: **JSON** — mudah diintegrasikan dengan tools lain.

### Database

Toolkit menggunakan **SQLite** untuk menyimpan:
- Cache hasil scan
- Findings & anomali
- Riwayat scan
- Hasil analisis

```
data/momoru.db
```

---

## 📦 Dependencies

| Package | Kegunaan |
|---------|----------|
| `requests` | HTTP requests |
| `httpx` | Async HTTP client |
| `rich` | Modern terminal UI |
| `typer` | CLI framework |
| `colorama` | Terminal color support |
| `paramiko` | SSH connection |
| `cryptography` | SSL/TLS parsing |
| `Pillow` | Image processing |
| `numpy` | Numerical computation |
| `scipy` | Statistical analysis |
| `pyyaml` | YAML parser |

---

## 🧠 Architecture

```
core/       →  Session management & shared utilities
modules/    →  Semua scanner & analyzer (modular)
data/       →  Cache, reports, dan database
logs/       →  Logging system
```

**Keunggulan arsitektur ini:**
- ✅ Scalable — mudah ditambah modul baru
- ✅ Reusable — komponen dapat digunakan ulang
- ✅ Clean Separation — setiap modul berdiri sendiri
- ✅ Maintainable — mudah di-debug dan dikembangkan

---

## 🖥️ Platform Support

| Platform | Status |
|----------|--------|
| 🐧 Linux | ✅ Full Support |
| 🪟 Windows | ✅ Full Support |
| 🍎 macOS | ✅ Full Support |

---

## ⚡ Recommended Usage

**Audit VPS Linux:**
```bash
python momoru.py
# Pilih: [VPS SECURITY]
```

**Analisis Log Lokal:**
```bash
python momoru.py
# Pilih: [LOG ANALYZER]
```

**Audit SSL/TLS Domain:**
```bash
python momoru.py
# Masukkan: example.com
```

---

## 🔒 Ethical Use & Disclaimer

Toolkit ini dikembangkan **semata-mata** untuk tujuan:

- ✅ Defensive security
- ✅ Audit internal server
- ✅ VPS hardening
- ✅ Educational & research
- ✅ Incident investigation

**Dilarang keras** menggunakan toolkit ini untuk:

- ❌ Aktivitas ilegal dalam bentuk apapun
- ❌ Scanning tanpa izin eksplisit
- ❌ Unauthorized access ke sistem pihak ketiga
- ❌ Attacking atau disrupting third-party systems

> Pengembang **tidak bertanggung jawab** atas penyalahgunaan toolkit ini.

---

## 📝 Notes

- Gunakan **Python 3.10+**
- **Virtual environment** sangat direkomendasikan
- Jalankan dengan **izin yang sesuai** (beberapa modul butuh root/admin)
- Beberapa fitur memerlukan **koneksi internet aktif**
- Beberapa modul memberikan hasil lebih optimal dengan akses **root/admin**

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">

## 👨‍💻 Author

**Momoru**

*Focused on Defensive Security · VPS Hardening · Security Research · Threat Analysis*

⭐ **Star this repo** jika toolkit ini bermanfaat bagi Anda!

</div>
