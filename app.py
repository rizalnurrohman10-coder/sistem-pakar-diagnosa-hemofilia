Import streamlit as st
 
# --- KONFIGURASI HALAMAN ---
St.set_page_config(page_title=”HemoSmart AI”, page_icon=”🩸”, layout=”wide”)
 
# --- CSS CUSTOM UNTUK BACKGROUND & STYLE ---
St.markdown(“””
    <style>
    /* Background utama dengan gradasi lembut */
    .stApp {
        Background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
    }
    
    /* Style untuk Sidebar/Menu */
    [data-testid=”stSidebar”] {
        Background-color: #d90429;
    }
    [data-testid=”stSidebar”] * {
        Color: white !important;
    }
 
    /* Kartu Hasil Diagnosa */
    .result-card {
        Background: white;
        Padding: 30px;
        Border-radius: 20px;
        Border-left: 10px solid #d90429;
        Box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        Margin-top: 20px;
    }
    
    /* Animasi Judul */
    .header-text {
        Color: #d90429;
        Font-size: 45px;
        Font-weight: 800;
        Text-align: center;
        Text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    “””, unsafe_allow_html=True)
 
# --- DATA MASTER ---
Daftar_gejala = {
    “G01”: “Mimisan mendadak dan sulit berhenti”, “G02”: “Pendarahan gusi tanpa sebab yang jelas”,
    “G03”: “Luka kecil sulit berhenti berdarah”, “G04”: “Memar (hemoatoma) lama hilang”,
    “G05”: “Pendarahan setelah cabut gigi”, “G06”: “Pendarahan pasca operasi”,
    “G07”: “Pendarahan pada otot”, “G08”: “Pendarahan pada sendi (lutut, siku, pergelangan)”,
    “G09”: “Nyeri pada sendi”, “G10”: “Pembengkakan sendi”,
    “G11”: “Pendarahan akibat benturan ringan”, “G12”: “Pendarahan spontan (tanpa sebab yang jelas)”,
    “G13”: “Pendarahan pada saluran pencernaan”, “G14”: “Pendarahan di kepala (gejala neurologis)”,
    “G15”: “Riwayat keluarga menderita Hemofilia”
}
 
Daftar_solusi = {
    “S01”: “Penanganan lokal (tekan, kompres, perban)”, “S02”: “Obat pendukung (antifibrinolitik, desmopressin)”,
    “S03”: “Edukasi pencegahan pendarahan”, “S04”: “Kesadaran terhadap risiko cedera dan pendarahan”,
    “S05”: “Terapi faktor pembekuan saat diperlukan (on-demand)”, “S06”: “Fisioterapi untuk menjaga kesehatan sendi”,
    “S07”: “Monitoring medis berkala”, “S08”: “Edukasi aktivitas (menghindari olahraga kontak berat)”,
    “S09”: “Terapi profilaksis rutin (faktor VIII/IX)”, “S10”: “Penanganan darurat untuk pendarahan internal”,
    “S11”: “Rehabilitasi jangka panjang”, “S12”: “Menghindari obat aspirin dan NSAID karena meningkatkan resiko pendarahan”
}
 
# --- MENU SIDEBAR ---
With st.sidebar:
    St.image(https://cdn-icons-png.flaticon.com/512/2764/2764357.png, width=100)
    St.title(“Menu Utama”)
    Nav = st.radio(“Pilih Halaman:”, [“🏠 Beranda”, “🩺 Mulai Diagnosa”, “📚 Info Hemofilia”])
    St.divider()
    St.write(“Dibuat oleh: Muhammad Rizal Nurrohman”)
 
# --- HALAMAN 1: BERANDA ---
If nav == “🏠 Beranda”:
    St.markdown(“<h1 class=’header-text’>Selamat Datang di HemoSmart AI</h1>”, unsafe_allow_html=True)
    Col1, col2 = st.columns([1, 1])
    With col1:
        St.image(https://img.freepik.com/free-vector/blood-donation-concept-illustration_114360-5554.jpg, use_container_width=True)
    With col2:
        St.write(“### Apa itu Sistem Pakar ini?”)
        St.write(“””
        Sistem ini dirancang untuk membantu mendeteksi tingkat keparahan penyakit Hemofilia secara dini 
        Menggunakan metode **Forward Chaining**.
        
        **Keunggulan:**
        - Cepat dan Akurat (Berdasarkan basis pengetahuan pakar).
        - Mudah digunakan oleh pasien maupun tenaga medis.
        - Menyediakan solusi penanganan pertama (S01 – S12).
        “””)
        If st.button(“Mulai Diagnosa Sekarang →”):
            St.info(“Silakan klik menu ‘Mulai Diagnosa’ di samping kiri!”)
 
# --- HALAMAN 2: DIAGNOSA ---
Elif nav == “🩺 Mulai Diagnosa”:
    St.markdown(“<h2 style=’text-align: center; color: #d90429;’>Formulir Konsultasi Pasien</h2>”, unsafe_allow_html=True)
    
    With st.container():
        C1, c2, c3 = st.columns(3)
        Nama = c1.text_input(“Nama Lengkap”)
        Umur = c2.number_input(“Umur”, min_value=0)
        Jk = c3.selectbox(“Jenis Kelamin”, [“Laki-laki”, “Perempuan”])
 
    St.write(“---“)
    St.write(“### Pilih Gejala yang Anda Rasakan:”)
    Col_g1, col_g2 = st.columns(2)
    Gejala_terpilih = []
    
    For i, (kode, teks) in enumerate(daftar_gejala.items()):
        Target_col = col_g1 if i < 8 else col_g2
        If target_col.checkbox(f”[{kode}] {teks}”):
            Gejala_terpilih.append(kode)
 
    If st.button(“ANALISIS HASIL”):
        If not nama or not gejala_terpilih:
            St.error(“Mohon isi Nama dan pilih minimal 1 gejala!”)
        Else:
            # Logika Diagnosa
            Rules = [
                {“nama”: “Hemofilia Ringan”, “gejala”: [“G01”, “G02”, “G03”, “G04”, “G05”, “G06”, “G09”, “G10”, “G11”, “G15”], “solusi”: [“S01”, “S02”, “S03”, “S04”]},
                {“nama”: “Hemofilia Sedang”, “gejala”: [“G01”, “G02”, “G03”, “G04”, “G05”, “G06”, “G07”, “G08”, “G09”, “G10”, “G11”, “G15”], “solusi”: [“S05”, “S06”, “S07”, “S08”]},
                {“nama”: “Hemofilia Berat”, “gejala”: [“G01”, “G02”, “G04”, “G06”, “G07”, “G08”, “G09”, “G10”, “G12”, “G13”, “G14”, “G15”], “solusi”: [“S09”, “S10”, “S11”, “S12”]}
            ]
            
            Hasil_final = None
            For rule in reversed(rules):
                Match_count = len([g for g in rule[“gejala”] if g in gejala_terpilih])
                If match_count >= (len(rule[“gejala”]) * 0.5):
                    Hasil_final = rule
                    Break
 
            If hasil_final:
                St.markdown(f”””
                <div class=”result-card”>
                    <h3 style=’margin:0;’>Laporan Diagnosa: {nama}</h3>
                    <h1 style=’color: #d90429;’>{hasil_final[‘nama’]}</h1>
                    <p>Berdasarkan gejala yang dipilih, sistem mengidentifikasi kondisi Anda masuk dalam kategori ini.</p>
                </div>
                “””, unsafe_allow_html=True)
                
                St.write(“#### 🛡️ Langkah Penanganan:”)
                Cols_s = st.columns(2)
                For idx, kode_s in enumerate(hasil_final[‘solusi’]):
                    T_col = cols_s[idx % 2]
                    T_col.success(f”**{kode_s}**: {daftar_solusi[kode_s]}”)
            Else:
                St.warning(“Gejala belum cukup spesifik. Silakan hubungi dokter Hematologi.”)
 
# --- HALAMAN 3: INFO ---
Elif nav == “📚 Info Hemofilia”:
    St.title(“Informasi Edukasi”)
    St.write(“””
    Hemofilia adalah gangguan pembekuan darah akibat kekurangan faktor VIII (Hemofilia A) atau faktor IX (Hemofilia B).
    “””)
    St.video(https://www.youtube.com/watch?v=1oW_fFm-v24) # Contoh video edukasi
 

