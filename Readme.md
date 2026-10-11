# 🔐 Secure File Sharing Through Quantum Computing

A Python desktop application for secure file sharing that combines **AES / RSA encryption**, **LSB image steganography**, and **cloud storage (Amazon S3)**, designed around a **hybrid classical + quantum-safe (QKD)** security model.

> BCA Internship Project – PES Institute of Advanced Management Studies (PESIAMS), Shivamogga
> Affiliated to Kuvempu University | Academic Year 2024–25
> **Author:** Sindhu S B (U06PE22S0022) | **Guide:** Ms. Asma Noorain, Assistant Professor, Dept. of Computer Science

---

## 📌 Overview

Quantum algorithms threaten today's cryptography: **Shor's algorithm** can break RSA, and **Grover's algorithm** effectively halves AES key strength. This project explores a layered defence for file sharing in the cloud:

1. **Encrypt** the file/text with AES (and RSA for key exchange in hybrid schemes).
2. **Hide** the ciphertext inside an image using LSB steganography.
3. **Store / share** the stego-image through cloud storage (Amazon S3) or email.
4. **Design for QKD** – Quantum Key Distribution (via IBM Quantum) is incorporated in the architecture to generate eavesdropping-resistant keys.

---

## ✨ Features

- **AES file encryption & decryption** with a user-supplied key (output `.enc` files)
- **RSA encryption & decryption** (key generation, `M = C^d mod n`)
- **Steganography** – hide encrypted text inside an image (LSB) and extract it back
- **Cloud storage** – upload to / download from an Amazon S3 bucket
- **Email integration** – send encrypted files directly to a receiver
- **User registration & login** with credential storage in a database
- **Operation feedback** – confirmation pop-ups with elapsed time for encryption/decryption
- **Sidebar GUI** – Home, File Encryption, Hide Image in Text, Send Email, Upload to Cloud, Download from Cloud, Contact Us

---

## 🏗️ System Architecture

```
Sender                                              Receiver
  │                                                    ▲
Plain text → Compression → Encryption (Key)            │
                               │              Decompression ← Decryption (Key)
                               ▼                       ▲
        Cover media → Embedding (Stego-Key) → Stego-media → Extracting (Stego-Key)
                                  │
                              (Warden may observe, but cannot easily detect hidden data)
```

### Workflow

1. Select a text file and a cover image
2. Encrypt the text with AES using a secret key
3. Embed the ciphertext in the image (LSB steganography)
4. Upload the stego-image to the cloud (or email it)
5. Receiver downloads the image and extracts the ciphertext
6. Receiver decrypts with the same key to recover the original text

### Actors

| Actor | Responsibilities |
|-------|------------------|
| **User** | Register/login, select files, enter secret key, encrypt/decrypt, upload/download, access quantum server |
| **Admin** | Upload files/images, provide keys, manage cloud upload and quantum server access |

### Components (Sequence Diagram)

`Application` · `EncryptionService` · `QuantumServer` (QKD key generation) · `CloudStorage`

---

## 🧰 Tech Stack

| Area | Tools |
|------|-------|
| Language | Python 3.7+ |
| Encryption | AES, RSA |
| Steganography | LSB (Least Significant Bit) |
| Cloud | Amazon S3 (AWS Free Tier), IBM Quantum Experience / IBM Cloud |
| Libraries (suggested) | NumPy, Pandas, scikit-learn, TensorFlow / PyTorch (analysis) |
| IDE | PyCharm, VS Code |
| Database | User credentials store (Username, Password) |

---

## 💻 Requirements

**Software**
- Windows 10/11, macOS 10.14+, or modern Linux (64-bit)
- Python 3.7 or later
- AWS account (Free Tier) and IBM Quantum account (optional, for QKD experiments)

**Hardware**
- Minimum: Intel Core i5 / Ryzen 5, 8 GB RAM, 500 GB SSD
- Recommended: Core i7 / Ryzen 7, 16 GB RAM, 1 TB SSD, dedicated GPU for quantum simulations
- Stable internet connection for cloud operations

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd <project-folder>

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure AWS credentials (never commit these!)
aws configure

# 5. Run the application
python main.py                  # replace with your entry-point file
```

> ⚠️ **Security note:** Keep AWS keys, IBM Quantum tokens, and email passwords in environment variables or a `.env` file listed in `.gitignore`. Never hard-code them.

---

## 🖥️ Usage

1. **Register / Log in** to the application.
2. **File Encryption:** Browse for a file → enter a key → click **Encrypt** (or **Decrypt**).
3. **Hide Image in Text:** Choose a cover image and ciphertext → embed / extract.
4. **Upload to Cloud:** Enter the S3 bucket name → browse file → **Upload to S3**.
5. **Download from Cloud:** Retrieve the stego-image, extract, and decrypt with the key.
6. **Send Email:** Share the encrypted file directly with the receiver.

---

## 🧪 Testing

| ID | Test | Expected Result |
|----|------|-----------------|
| TC1 | AES encryption & decryption | Decrypted text equals the original plaintext |
| TC2 | LSB embedding & extraction | Extracted data equals the original ciphertext |
| TC3 | Cloud storage integrity | Ciphertext extracted from the downloaded image matches the original |
| TC4 | AES decryption (end-to-end) | Decrypted message equals the original plaintext |
| TC5 | Full system test | Final output matches the original file exactly |

All five test cases passed. Typical encryption/decryption times were in the millisecond range for sample files.

---

## ⚠️ Limitations

- LSB steganography has limited capacity and is vulnerable to advanced steganalysis.
- QKD is part of the architecture and design; real QKD hardware is costly and complex to integrate, so the implemented/tested pipeline focuses on AES, RSA, steganography, and cloud storage.
- Hybrid encryption and steganography add computational overhead for very large files.
- Further real-world validation and scalability testing are needed.

---

## 🔭 Future Scope

- Integrate post-quantum algorithms (e.g., **CRYSTALS-Kyber**)
- Full QKD integration using IBM Quantum backends
- Support audio/video cover media and larger payloads
- Blockchain-based audit trail for traceability and integrity
- Broader multi-cloud support (Google Cloud, Azure)
- Role-based access control and stronger authentication

---

## 📚 References

1. P. K. Mandal, *Hiding Data Using Efficient Combination of RSA Cryptography and Compression Steganography Techniques*, 2018
2. E. D. Sheeba, *Enhancing Security with Cryptographic-Steganographic Combinations*, 2021
3. C. B. Landge, *Efficient Data Hiding Through RSA Cryptography and Compression Steganography Techniques*, 2021
4. Rajkumar et al., *Enhancing AES Security Using Quantum Cryptographic Principles*, 2023
5. Mohd. Anwar et al., *Quantum Cryptography for Secure File Sharing in Cloud Systems*, 2022
6. Jing Liao et al., *Post-Quantum Security: Opportunities and Challenges*, 2023

---

## 🙏 Acknowledgements

SRK Technologies, Shivamogga (internship provider); Ms. Asma Noorain (guide); Ms. Roopa D. S. (HOD); Dr. Sudharshan G. M. (Principal); and the faculty of PESIAMS, Shivamogga.