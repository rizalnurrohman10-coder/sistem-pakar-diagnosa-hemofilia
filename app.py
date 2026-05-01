import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Penyakit Hemofilia", page_icon="🩸", layout="centered")

# ================== CUSTOM CSS ==================
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        color: #212121;
    }
    
    /* Kotak Header Merah */
    .header-box {
        background-color: #D32F2F;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
    }
    .header-box h1 {
        color: white !important;
        margin: 0;
        font-family: 'Helvetica', sans-serif;
    }

    /* Tombol Utama (Merah) */
    div.stButton > button {
        background-color: #D32F2F !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
        height: 3em;
    }

    /* Memperjelas Tombol Hitam (Proses Analisis) */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #1A1D23 !important;
        color: #FFFFFF !important;
        border: 2px solid #D32F2F !important;
        font-size: 16px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 3em;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #D32F2F;
    }
    
    h2, h3 {
        color: #D32F2F !important;
    }

    /* Styling Kotak Referensi Keparahan */
    .severity-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ced4da;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ================== STATE MANAGEMENT ==================
if "akses_diberikan" not in st.session_state:
    st.session_state.akses_diberikan = False
if "gejala_terpilih" not in st.session_state:
    st.session_state.gejala_terpilih = []
if "nama_pasien" not in st.session_state:
    st.session_state.nama_pasien = ""

# ================== DATA SISTEM PAKAR ==================
daftar_gejala = {
    "G01": "Mimisan mendadak dan sulit berhenti",
    "G02": "Pendarahan gusi tanpa sebab yang jelas",
    "G03": "Luka kecil sulit berhenti berdarah",
    "G04": "Memar (hematoma) lama hilang",
    "G05": "Pendarahan setelah cabut gigi",
    "G06": "Pendarahan pasca operasi",
    "G07": "Pendarahan pada otot",
    "G08": "Pendarahan pada sendi",
    "G09": "Nyeri pada sendi",
    "G10": "Pembengkakan sendi",
    "G11": "Pendarahan akibat benturan ringan",
    "G12": "Pendarahan spontan",
    "G13": "Pendarahan pada saluran pencernaan",
    "G14": "Pendarahan di kepala",
    "G15": "Riwayat keluarga hemofilia"
}

daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)",
    "S02": "Obat pendukung (antifibrinolitik, desmopressin)",
    "S03": "Edukasi pencegahan",
    "S04": "Kesadaran terhadap resiko cedera dan pendarahan",
    "S05": "Terapi faktor pembekuan saat diperlukan (on-demand)",
    "S06": "Fisioterapi untuk mencegah kerusakan sendi",
    "S07": "Monitoring medis berkala",
    "S08": "Edukasi aktivitas (menghindari olahraga kontak berat)",
    "S09": "Terapi profilaksis rutin (factor VIII/IX)",
    "S10": "Penanganan darurat untuk pendarahan internal",
    "S11": "Rehabilitasi jangka panjang",
    "S12": "Menghindari obat aspirin dan NSAID karena meningkatkan resiko pendarahan"
}

rules = [
    {
        "nama": "Hemofilia A (Klasifikasi: Berat)", 
        "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], 
        "solusi": ["S09","S10","S11","S12"]
    },
    {
        "nama": "Hemofilia B (Klasifikasi: Sedang)", 
        "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], 
        "solusi": ["S05","S06","S07","S08"]
    },
    {
        "nama": "Hemofilia C (Klasifikasi: Ringan)", 
        "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], 
        "solusi": ["S01","S02","S03","S04"]
    }
]

# ================== HALAMAN AKSES MASUK ==================
if not st.session_state.akses_diberikan:
    st.markdown('<div class="header-box"><h1>🩸 AKSES MASUK</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        left_co, cent_co, last_co = st.columns([1,3,1])
        with cent_co:
            st.markdown("<h3 style='text-align:center;'>Autentikasi Tenaga Medis</h3>", unsafe_allow_html=True)
            username = st.text_input("ID Pengguna (Username)")
            password = st.text_input("Kata Sandi (Password)", type="password")
            
            if st.button("VERIFIKASI AKSES"):
                if username == "admin" and password == "123":
                    st.session_state.akses_diberikan = True
                    st.rerun()
                else:
                    st.error("Kredensial tidak valid. Silakan coba lagi.")

# ================== RUANG KERJA (SISTEM UTAMA) ==================
else:
    st.sidebar.markdown("<h2 style='text-align:center;'>NAVIGASI SISTEM</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Pilih Tindakan:", ["Beranda Utama", "Pemeriksaan Penyakit", "Laporan Penyakit", "Keluar Sistem"])

    # ================== BERANDA UTAMA ==================
    if menu == "Beranda Utama":
        st.markdown('<div class="header-box"><h1>🩸 BERANDA UTAMA</h1></div>', unsafe_allow_html=True)
        st.subheader("Selamat Datang di Portal Analisis Penyakit Hemofilia")
        st.info("Sistem Pakar ini menggunakan metode penalaran Forward Chaining untuk mengklasifikasikan tingkat keparahan Hemofilia berdasarkan manifestasi klinis pasien.")
        
        st.write("Silakan buka menu **Pemeriksaan Penyakit** di panel navigasi (sebelah kiri) untuk memulai pencatatan data dan analisis klinis.")

    # ================== HALAMAN PEMERIKSAAN PENYAKIT ==================
    elif menu == "Pemeriksaan Penyakit":
        st.markdown('<div class="header-box"><h1>📋 PEMERIKSAAN PENYAKIT</h1></div>', unsafe_allow_html=True)
        
        with st.form("form_pemeriksaan"):
            col1, col2 = st.columns(2)
            with col1:
                input_nama = st.text_input("Nama Lengkap Pasien")
            with col2:
                input_umur = st.number_input("Umur Pasien (Tahun)", 0, 120)

            st.markdown("---")
            st.subheader("Pilih Gejala Klinis yang Dialami Pasien:")
            
            gejala_manual = []
            cols_gejala = st.columns(2)
            items = list(daftar_gejala.items())
            for i, (kode, teks) in enumerate(items):
                with cols_gejala[i % 2]:
                    if st.checkbox(teks, key=f"gejala_{kode}"):
                        gejala_manual.append(kode)

            st.markdown("---")
            st.subheader("Pemilihan Cepat Berdasarkan Referensi Keparahan:")
            
            col_ref1, col_ref2, col_ref3 = st.columns(3)
            with col_ref1:
                st.markdown('<div class="severity-box">KLASIFIKASI RINGAN</div>', unsafe_allow_html=True)
                cek_ringan = st.checkbox("Pilih Paket Ringan", key="ref_ringan")
            with col_ref2:
                st.markdown('<div class="severity-box">KLASIFIKASI SEDANG</div>', unsafe_allow_html=True)
                cek_sedang = st.checkbox("Pilih Paket Sedang", key="ref_sedang")
            with col_ref3:
                st.markdown('<div class="severity-box">KLASIFIKASI BERAT</div>', unsafe_allow_html=True)
                cek_berat = st.checkbox("Pilih Paket Berat", key="ref_berat")

            st.write("<br>", unsafe_allow_html=True)
            
            # Tombol Hitam
            submitted = st.form_submit_button("PROSES ANALISIS PENYAKIT")
            
            if submitted:
                # Menggabungkan gejala manual dan gejala dari pilihan paket
                final_gejala = set(gejala_manual)
                if cek_ringan: final_gejala.update(rules[2]["gejala"])
                if cek_sedang: final_gejala.update(rules[1]["gejala"])
                if cek_berat:  final_gejala.update(rules[0]["gejala"])
                
                st.session_state.gejala_terpilih = list(final_gejala)
                st.session_state.nama_pasien = input_nama
                
                if len(final_gejala) > 0:
                    st.success("Analisis berhasil diproses! Silakan buka menu 'Laporan Penyakit' di panel navigasi.")
                else:
                    st.warning("Mohon pilih setidaknya satu gejala klinis untuk diproses.")

    # ================== HALAMAN LAPORAN PENYAKIT ==================
    elif menu == "Laporan Penyakit":
        st.markdown('<div class="header-box"><h1>📊 LAPORAN PENYAKIT</h1></div>', unsafe_allow_html=True)

        gejala = st.session_state.gejala_terpilih
        nama = st.session_state.nama_pasien if st.session_state.nama_pasien else "Pasien Anonim"

        if not gejala:
            st.warning("Belum ada data pemeriksaan yang diproses. Silakan kembali ke menu Pemeriksaan Penyakit.")
        else:
            hasil_pakar = None
            # Logika Inferensi Forward Chaining
            for r in rules:
                cocok = len([g for g in r["gejala"] if g in gejala])
                if cocok >= len(r["gejala"]) * 0.5:
                    hasil_pakar = r
                    break

            if hasil_pakar:
                st.markdown(f"### Kesimpulan Klinis: **{hasil_pakar['nama']}**")
                st.write(f"**Identitas Pasien:** {nama}")
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    with st.expander("Manifestasi Klinis yang Terdeteksi", expanded=True):
                        for g in gejala:
                            st.write(f"✅ {daftar_gejala[g]}")
                
                with col_res2:
                    with st.expander("Rekomendasi Tindakan & Tata Laksana", expanded=True):
                        for s in hasil_pakar["solusi"]:
                            st.write(f"📌 {daftar_solusi[s]}")
                
                st.button("UNDUH LAPORAN (PDF)")
                st.caption("*Catatan: Hasil ini bersifat analitik berdasarkan sistem pakar. Konsultasikan dengan dokter spesialis hematologi untuk validasi medis akhir.")
            else:
                st.error("Sistem tidak menemukan indikasi spesifik. Gejala klinis yang Anda masukkan belum memenuhi kriteria ambang batas database Hemofilia kami.")

    # ================== KELUAR SISTEM ==================
    elif menu == "Keluar Sistem":
        st.session_state.akses_diberikan = False
        st.session_state.gejala_terpilih = []
        st.session_state.nama_pasien = ""
        st.rerun()
