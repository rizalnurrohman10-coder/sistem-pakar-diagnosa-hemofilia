Import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
St.set_page_config(page_title=”Sistem Pakar Hemofilia”, page_icon=”🩸”, layout=”centered”)

# ================== CUSTOM CSS (OPTIMASI KONTRAS TEKS) ==================
St.markdown(“””
    <style>
    /* 1. Reset Dasar & Background */
    .stApp {
        Background-color: #F4F6F9 !important;
    }
    
    /* 2. MEMASTIKAN SEMUA TEKS TERLIHAT JELAS (TIDAK SAMAR) */
    /* Warna Hitam Pekat untuk teks di background terang */
    P, label, span, li, div, .stMarkdown {
        Color: #1A1D23 !important; 
        Font-weight: 500 !important;
    }

    /* Khusus untuk teks didalam tombol merah agar tetap Putih */
    .stButton > button div p, .stButton > button {
        Color: #FFFFFF !important;
        Font-weight: 700 !important;
    }

    /* 3. LOGIN BOX (GLASSMORPHISM DENGAN TEKS GELAP) */
    .glass-login {
        Background: rgba(255, 255, 255, 0.95);
        Border-radius: 20px;
        Padding: 30px;
        Box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        Border: 2px solid #D32F2F;
        Text-align: center;
    }

    /* 4. HEADER DIAGNOSIS & HASIL (MERAH PEKAT) */
    .top-header-red {
        Background-color: #B71C1C;
        Color: #FFFFFF !important;
        Padding: 20px;
        Border-radius: 15px;
        Text-align: center;
        Font-weight: bold;
        Font-size: 22px;
        Margin-bottom: 20px;
    }
    .top-header-red * {
        Color: #FFFFFF !important;
    }

    /* 5. CHECKBOX STYLING (AGAR TEKS GEJALA JELAS) */
    Div[data-testid=”stCheckbox”] {
        Background-color: #ffffff;
        Padding: 10px;
        Border-radius: 8px;
        Border: 1px solid #ced4da;
        Margin-bottom: 8px;
    }
    Div[data-testid=”stCheckbox”] label p {
        Color: #1A1D23 !important;
        Font-size: 15px !important;
    }

    /* 6. CARD KEPARAHAN & HASIL */
    .severity-card {
        Background-color: #FFFFFF;
        Border-radius: 10px;
        Padding: 15px;
        Text-align: center;
        Border: 1px solid #D32F2F;
    }
    .severity-card b {
        Color: #B71C1C !important;
        Font-size: 16px;
    }

    .result-card {
        Background-color: #FFFFFF;
        Border-radius: 15px;
        Padding: 25px;
        Border: 2px solid #B71C1C;
        Box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    “””, unsafe_allow_html=True)

# ================== STATE MANAGEMENT ==================
If “page” not in st.session_state:
    St.session_state.page = “Login”
If “gejala_terpilih” not in st.session_state:
    St.session_state.gejala_terpilih = []

# ================== DATA SISTEM PAKAR ==================
Daftar_gejala = {
    “G01”: “Mimisan mendadak dan sulit berhenti”,
    “G02”: “Pendarahan gusi tanpa sebab jelas”,
    “G03”: “Luka kecil sulit berhenti berdarah”,
    “G04”: “Memar (hematoma) lama hilang”,
    “G05”: “Pendarahan setelah cabut gigi”,
    “G06”: “Pendarahan pasca operasi”,
    “G07”: “Pendarahan pada otot”,
    “G08”: “Pendarahan pada sendi”,
    “G09”: “Nyeri pada sendi”,
    “G10”: “Pembengkakan sendi”,
    “G11”: “Pendarahan akibat benturan ringan”,
    “G12”: “Pendarahan spontan”,
    “G13”: “Pendarahan pada pencernaan”,
    “G14”: “Pendarahan di kepala”,
    “G15”: “Riwayat keluarga hemofilia”
}

Daftar_solusi = {
    “S09”: “Terapi rutin konsentrat faktor VIII/IX”,
    “S10”: “Penanganan medis darurat segera”,
    “S11”: “Rehabilitasi fungsional”,
    “S12”: “Hindari aspirin dan NSAID”,
    “S05”: “Terapi penggantian faktor pembekuan”,
    “S06”: “Fisioterapi rutin”,
    “S01”: “Penanganan lokal (tekan, kompres)”,
    “S02”: “Obat antifibrinolitik”
}

Rules = [
    {“nama”: “HEMOFILIA A (BERAT)”, “gejala”: [“G01”,”G02”,”G04”,”G07”,”G08”,”G12”,”G14”], “solusi”: [“S09”,”S10”,”S11”,”S12”]},
    {“nama”: “HEMOFILIA B (SEDANG)”, “gejala”: [“G03”,”G05”,”G09”,”G10”,”G11”,”G15”], “solusi”: [“S05”,”S06”]},
    {“nama”: “HEMOFILIA C (RINGAN)”, “gejala”: [“G01”,”G02”,”G03”,”G06”], “solusi”: [“S01”,”S02”]}
]

# ================== HALAMAN LOGIN ==================
If st.session_state.page == “Login”:
    St.write(“<br><br>”, unsafe_allow_html=True)
    St.markdown(‘’’
        <div class=”glass-login”>
            <h1 style=”color:#B71C1C !important; margin-bottom:0;”>🩸 LOGIN</h1>
            <p style=”color:#1A1D23 !important; font-weight:bold;”>SISTEM PAKAR HEMOFILIA</p>
            <p style=”font-size:13px; color:#555 !important;”>Silakan masukkan akun admin untuk memulai</p>
        </div>
    ‘’’, unsafe_allow_html=True)
    
    With st.container():
        St.write(“”)
        Username = st.text_input(“Username”)
        Password = st.text_input(“Kata Sandi”, type=”password”)
        
        If st.button(“MASUK KE SISTEM”):
            If username == “admin” and password == “123”:
                St.session_state.page = “Dashboard”
                St.rerun()
            Else:
                St.error(“Username atau Password salah!”)

# ================== HALAMAN DASHBOARD ==================
Elif st.session_state.page == “Dashboard”:
    St.markdown(‘<div class=”top-header-red”>🏠 DASHBOARD UTAMA</div>’, unsafe_allow_html=True)
    
    St.markdown(f’’’
        <div style=”background:white; padding:20px; border-radius:15px; border-left:8px solid #B71C1C; margin-bottom:20px;”>
            <h3 style=”margin:0; color:#B71C1C !important;”>Halo, Admin! 👋</h3>
            <p style=”margin:0; font-size:14px;”>Selamat datang di sistem deteksi dini Hemofilia.</p>
        </div>
    ‘’’, unsafe_allow_html=True)

    If st.button(“🚀 MULAI DIAGNOSIS SEKARANG”):
        St.session_state.page = “Diagnosis”
        St.rerun()

    St.markdown(“<br><p style=’text-align:center; font-weight:bold;’>Menu Navigasi Cepat</p>”, unsafe_allow_html=True)
    C1, c2 = st.columns(2)
    With c1:
        St.button(“📖 Edukasi Penyakit”)
    With c2:
        If st.button(“🚪 Keluar Akun”):
            St.session_state.page = “Login”
            St.rerun()

# ================== HALAMAN DIAGNOSIS ==================
Elif st.session_state.page == “Diagnosis”:
    St.markdown(‘<div class=”top-header-red”>📋 PROSES DIAGNOSIS</div>’, unsafe_allow_html=True)
    
    With st.form(“diagnosis_form”):
        St.markdown(“<p style=’font-size:16px; font-weight:bold;’>Pilih Gejala yang Terdeteksi:</p>”, unsafe_allow_html=True)
        
        Gejala_user = []
        For kode, teks in daftar_gejala.items():
            If st.checkbox(teks, key=kode):
                Gejala_user.append(kode)
        
        St.markdown(“---“)
        St.markdown(“<p style=’font-weight:bold; color:#B71C1C !important;’>Referensi Tingkat Keparahan:</p>”, unsafe_allow_html=True)
        Col1, col2, col3 = st.columns(3)
        With col1:
            St.markdown(‘<div class=”severity-card”><b>RINGAN</b><br><small>Luka operasi lama sembuh</small></div>’, unsafe_allow_html=True)
        With col2:
            St.markdown(‘<div class=”severity-card”><b>SEDANG</b><br><small>Lebam tanpa sebab jelas</small></div>’, unsafe_allow_html=True)
        With col3:
            St.markdown(‘<div class=”severity-card”><b>BERAT</b><br><small>Pendarahan sendi spontan</small></div>’, unsafe_allow_html=True)
        
        St.write(“<br>”, unsafe_allow_html=True)
        If st.form_submit_button(“PROSES HASIL DIAGNOSIS”):
            St.session_state.gejala_terpilih = gejala_user
            St.session_state.page = “Hasil”
            St.rerun()

# ================== HALAMAN HASIL ==================
Elif st.session_state.page == “Hasil”:
    St.markdown(‘<div class=”top-header-red”>📊 HASIL ANALISIS PAKAR</div>’, unsafe_allow_html=True)
    
    If not st.session_state.gejala_terpilih:
        St.warning(“Tidak ada gejala yang dipilih untuk dianalisis.”)
        If st.button(“Kembali ke Diagnosis”):
            St.session_state.page = “Diagnosis”
            St.rerun()
    Else:
        # Logika Pencocokan
        Gejala_user = st.session_state.gejala_terpilih
        Hasil_final = None
        
        For r in rules:
            Cocok = [g for g in r[“gejala”] if g in gejala_user]
            If len(cocok) >= 2: # Minimal 2 gejala cocok
                Hasil_final = r
                Break
        
        If hasil_final:
            St.markdown(f’’’
                <div class=”result-card”>
                    <h2 style=”color:#B71C1C !important; text-align:center;”>{hasil_final[‘nama’]}</h2>
                    <hr>
                    <p><b>Gejala yang ditemukan:</b></p>
                    <ul style=”color:#1A1D23 !important;”>
                        {“”.join([f”<li>{daftar_gejala[g]}</li>” for g in gejala_user])}
                    </ul>
                    <p style=”margin-top:15px;”><b>Tindakan Medis Disarankan:</b></p>
                    <ul style=”color:#B71C1C !important; font-weight:bold;”>
                        {“”.join([f”<li>{daftar_solusi[s]}</li>” for s in hasil_final[‘solusi’]])}
                    </ul>
                </div>
            ‘’’, unsafe_allow_html=True)
        Else:
            St.error(“Gejala tidak cukup spesifik untuk menentukan jenis Hemofilia.”)

        St.write(“<br>”, unsafe_allow_html=True)
        If st.button(“KEMBALI KE DASHBOARD”):
            St.session_state.page = “Dashboard”
            St.rerun()
