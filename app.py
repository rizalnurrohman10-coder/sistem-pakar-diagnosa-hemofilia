Import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
St.set_page_config(page_title=”Sistem Pakar Diagnosis Hemofilia”, page_icon=”🩸”, layout=”centered”)

# ================== CUSTOM CSS (OPTIMASI KONTRAS & UI MERAH PUTIH) ==================
St.markdown(“””
    <style>
    .stApp {
        Background-color: #F4F6F9 !important;
    }
    
    /* Memastikan teks terbaca jelas */
    P, label, span, li, div, .stMarkdown {
        Color: #1A1D23 !important; 
        Font-weight: 500 !important;
    }

    /* Tombol Merah dengan teks Putih */
    div.stButton > button {
        background-color: #D32F2F !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
    }

    /* Kotak Header */
    .top-header-red {
        Background-color: #B71C1C;
        Color: #FFFFFF !important;
        Padding: 20px;
        Border-radius: 15px;
        Text-align: center;
        Margin-bottom: 20px;
    }
    .top-header-red h1 {
        Color: #FFFFFF !important;
        Margin: 0;
    }

    /* Checkbox agar kontras */
    Div[data-testid=”stCheckbox”] {
        Background-color: #ffffff;
        Padding: 10px;
        Border-radius: 8px;
        Border: 1px solid #ced4da;
        Margin-bottom: 8px;
    }

    /* Card Hasil */
    .result-card {
        Background-color: #FFFFFF;
        Border-radius: 15px;
        Padding: 25px;
        Border: 2px solid #D32F2F;
        Box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    “””, unsafe_allow_html=True)

# ================== DATA (SESUAI DOKUMEN WORD) ==================
# [span_0](start_span)Sumber:[span_0](end_span)
Daftar_gejala = {
    “G01”: “Mimisan mendadak dan sulit berhenti”,
    “G02”: “Pendarahan gusi tanpa sebab yang jelas”,
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
    “G13”: “Pendarahan pada saluran pencernaan”,
    “G14”: “Pendarahan di kepala”,
    “G15”: “Riwayat keluarga hemofilia”
}

# [span_1](start_span)Sumber:[span_1](end_span)
Daftar_solusi = {
    “S01”: “Penanganan lokal (tekan, kompres, perban)”,
    “S02”: “Obat pendukung (antifibrinoltik, desmopressin)”,
    “S03”: “Edukasi pencegahan”,
    “S04”: “Kesadaran terhadap resiko cedera dan pendarahan”,
    “S05”: “Terapi faktor pembekuan saat diperlukan (on-demand)”,
    “S06”: “Fisioterapi untuk mencegah kerusakan sendi”,
    “S07”: “Monitoring medis berkala”,
    “S08”: “Edukasi aktivitas (menghindari olahraga kontak berat) ”,
    “S09”: “Terapi profilaksis rutin (factor VIII/IX)”,
    “S10”: “Penanganan darurat untuk pendarahan internal”,
    “S11”: “Rehabilitasi jangka panjang”,
    “S12”: “Menghindari obat aspirin dan NSAID karena meningkatkan resiko pendarahan”
}

# [span_2](start_span)Sumber:[span_2](end_span)
Rules = [
    {
        “nama”: “Hemofilia A (Klasifikasi: Berat)”, 
        “gejala”: [“G01”,”G02”,”G04”,”G06”,”G07”,”G08”,”G09”,”G10”,”G12”,”G13”,”G14”,”G15”], 
        “solusi”: [“S09”,”S10”,”S11”,”S12”]
    },
    {
        “nama”: “Hemofilia B (Klasifikasi: Sedang)”, 
        “gejala”: [“G01”,”G02”,”G03”,”G04”,”G05”,”G06”,”G07”,”G08”,”G09”,”G10”,”G11”,”G15”], 
        “solusi”: [“S05”,”S06”,”S07”,”S08”]
    },
    {
        “nama”: “Hemofilia C (Klasifikasi: Ringan)”, 
        “gejala”: [“G01”,”G02”,”G03”,”G04”,”G05”,”G06”,”G09”,”G10”,”G11”,”G15”], 
        “solusi”: [“S01”,”S02”,”S03”,”S04”]
    }
]

# ================== STATE MANAGEMENT ==================
If “page” not in st.session_state:
    St.session_state.page = “Login”
If “gejala_terpilih” not in st.session_state:
    St.session_state.gejala_terpilih = []

# ================== HALAMAN LOGIN ==================
If st.session_state.page == “Login”:
    St.markdown(‘<div class=”top-header-red”><h1>🩸 LOGINI</h1></div>’, unsafe_allow_html=True)
    St.write(“<br>”, unsafe_allow_html=True)
    Username = st.text_input(“Username”)
    Password = st.text_input(“Password”, type=”password”)
    
    If st.button(“MASUK KE SISTEM”):
        If username == “admin” and password == “123”:
            St.session_state.page = “Dashboard”
            St.rerun()
        Else:
            [span_3](start_span)st.error(“Kredensial salah[span_3](end_span)!”)

# ================== SISTEM PAKAR HEMOFILIA ==================
Elif st.session_state.page == “Menu Utama”:
    St.markdown(‘<div class=”top-header-red”>🏠 MENU UTAMA</div>’, unsafe_allow_html=True)
    
    St.markdown(f’’’
        <div style=”background:white; padding:20px; border-radius:15px; border-left:8px solid #B71C1C; margin-bottom:20px;”>
            <h3 style=”margin:0; color:#B71C1C !important;”>Halo, Admin! 👋</h3>
            <p style=”margin:0; font-size:14px;”>Selamat datang di sistem deteksi dini Hemofilia.</p>
        </div>
    ‘’’, unsafe_allow_html=True)

    If st.button(“🚀 MULAI DIAGNOSIS  PENYAKIT SEKARANG”):
        St.session_state.page = “Diagnosis Penyakit”
        St.rerun()

    St.markdown(“<br><p style=’text-align:center; font-weight:bold;’>Menu Navigasi Cepat</p>”, unsafe_allow_html=True)
    C1, c2 = st.columns(2)
    With c1:
        St.button(“📖 Edukasi Penyakit”)
    With c2:
        If st.button(“🚪 Keluar Akun”):
            St.session_state.page = “Login”
            St.rerun()


# ================== HALAMAN DIAGNOSIS PENYAKIT==================
Elif st.session_state.page == “Diagnosis  Penyakit”:
    St.markdown(‘<div class=”top-header-red”><h1>📋 PROSES DIAGNOSIS PENYAKIT</h1></div>’, unsafe_allow_html=True)
    
    With st.form(“form_diagnosis_penyakit”):
        Nama = st.text_input(“Nama Pasien”)
        Umur = st.number_input(“Umur Pasien”, 0, 1000)
        St.markdown(“---“)
        St.subheader(“Ceklis Gejala yang Dirasakan:”)
        
        Gejala_user = []
        For kode, teks in daftar_gejala.items():
            If st.checkbox(teks, key=kode):
                Gejala_user.append(kode)
        
St.markdown(“---“)
        St.markdown(“<p style=’font-weight:bold; color:#B71C1C !important;’>Referensi Tingkat Keparahan:</p>”, unsafe_allow_html=True)
        Col1, col2, col3 = st.columns(3)
        With col1:
            St.markdown(‘<div class=”severity-card”><b>RINGAN</b><br><small> Check All</small></div>’, unsafe_allow_html=True)
        With col2:
            St.markdown(‘<div class=”severity-card”><b>SEDANG</b><br><small>Check All</small></div>’, unsafe_allow_html=True)
        With col3:
            St.markdown(‘<div class=”severity-card”><b>BERAT</b><br><small>Check all</small></div>’, unsafe_allow_html=True)
        
        St.write(“<br>”, unsafe_allow_html=True)
        If st.form_submit_button(“PROSES HASIL DIAGNOSIS PENYAKIT”):
            St.session_state.gejala_terpilih = gejala_user
            St.session_state.page = “Hasil”
            St.rerun()

# ================== HASIL DIAGNOSIS PENYAKIT ==================
Elif st.session_state.page == “Hasil”:
    St.markdown(‘<div class=”top-header-red”><h1>📊 LAPORAN HASIL DIAGNOSIS PENYAKIT</h1></div>’, unsafe_allow_html=True)
    
    Gejala_terpilih = st.session_state.gejala_terpilih
    Nama = st.session_state.get(“nama_pasien”, “Pasien”)

    If not gejala_terpilih:
        St.warning(“Data diagnosis belum tersedia.”)
    Else:
        # [span_5](start_span)Logika Forward Chaining (Sesuai[span_5](end_span))
        Hasil_final = None
        For r in rules:
            # Menghitung kecocokan gejala minimal 50% sesuai logika di Word
            Cocok = len([g for g in r[“gejala”] if g in gejala_terpilih])
            If cocok >= len(r[“gejala”]) * 0.5:
                Hasil_final = r
                Break
        
        If hasil_final:
            St.markdown(f’’’
                <div class=”result-card”>
                    <h3 style=”color:#B71C1C !important; text-align:center;”>Kesimpulan: {hasil_final[‘nama’]}</h3>
                    <p><b>Nama Pasien:</b> {nama}</p>
                    <hr>
                    <p><b>Manifestasi Klinis Terdeteksi:</b></p>
                    <ul>
                        {“”.join([f”<li>{daftar_gejala[g]}</li>” for g in gejala_terpilih])}
                    </ul>
                    <p style=”margin-top:15px;”><b>Rekomendasi Tindakan:</b></p>
                    <ul style=”color:#B71C1C !important; font-weight:bold;”>
                        {“”.join([f”<li>{daftar_solusi[s]}</li>” for s in hasil_final[‘solusi’]])}
                    </ul>
                </div>
            ‘’’, unsafe_allow_html=True)
            St.write(“<br>”, unsafe_allow_html=True)
            St.button(“UNDUH LAPORAN (PDF)”)
        Else:
            [span_6](start_span)st.error(“Sistem tidak menemukan indikasi spesifik berdasarkan database kami.[span_6](end_span)”)

    If st.button(“KEMBALI KE MENU UTAMA”):
        St.session_state.page = “Dashboard”
        St.rerun()
