import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Diagnosis Hemofilia", layout="centered")

# ================== CUSTOM CSS (UI MERAH PUTIH) ==================
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        color: #212121;
    }
    
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

    div.stButton > button:first-child {
        background-color: #D32F2F;
        color: white;
        border-radius: 8px;
        border: none;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #b71c1c;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #D32F2F;
    }
    
    h2, h3 {
        color: #D32F2F !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ================== SESSION ==================
if "login" not in st.session_state:
    st.session_state.login = False

# ================== DATA ==================
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
    "S02": "Pemberian obat antifibrinolitik",
    "S03": "Edukasi pencegahan perdarahan berulang",
    "S04": "Profilaksis cedera fisik",
    "S05": "Terapi penggantian faktor pembekuan darah",
    "S06": "Fisioterapi rutin",
    "S07": "Monitoring medis berkala",
    "S08": "Pembatasan aktivitas fisik intensitas tinggi",
    "S09": "Terapi rutin konsentrat faktor VIII/IX",
    "S10": "Penanganan medis darurat segera",
    "S11": "Rehabilitasi fungsional",
    "S12": "Kontraindikasi penggunaan aspirin dan NSAID"
}

rules = [
    {"nama": "Hemofilia A (Klasifikasi: Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]},
    {"nama": "Hemofilia B (Klasifikasi: Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]},
    {"nama": "Hemofilia C (Klasifikasi: Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]}
]

# ================== HALAMAN LOGIN ==================
if not st.session_state.login:
    st.markdown('<div class="header-box"><h1>🩸 AUTENTIKASI PENGGUNA</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        left_co, cent_co, last_co = st.columns([1,3,1])
        with cent_co:
            st.markdown("### Sistem Pakar Diagnosis Hemofilia")
            st.caption("Silakan masuk ke akun Anda untuk mengakses sistem.")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("MASUK KE SISTEM"):
                if username == "admin" and password == "123":
                    st.session_state.login = True
                    st.rerun()
                else:
                    st.error("Kredensial yang Anda masukkan salah!")

# ================== MENU UTAMA ==================
else:
    st.sidebar.markdown("<h2 style='text-align:center;'>PANEL NAVIGASI</h2>", unsafe_allow_html=True)
    menu = st.sidebar.selectbox("Pilih Layanan", ["Dashboard", "Diagnosis", "Hasil", "Logout"])

    if menu == "Dashboard":
        st.markdown('<div class="header-box"><h1>🩸 PANEL UTAMA</h1></div>', unsafe_allow_html=True)
        st.subheader(f"Selamat Datang di Portal Diagnosis")
        st.info("Sistem ini didukung oleh metode Forward Chaining untuk mengidentifikasi tingkat keparahan Hemofilia berdasarkan manifestasi klinis yang dialami pasien.")
        if st.button("Mulai Analisis Gejala"):
            st.warning("Silakan akses menu 'Diagnosis' melalui bilah navigasi di sebelah kiri.")

    # ================== HALAMAN DIAGNOSIS (TIDAK BERUBAH) ==================
    elif menu == "Diagnosis":
        st.markdown('<div class="header-box"><h1>📋 PROSES DIAGNOSIS</h1></div>', unsafe_allow_html=True)
        
        with st.form("form_diagnosis"):
            col1, col2 = st.columns(2)
            with col1:
                nama = st.text_input("Nama Pasien")
            with col2:
                umur = st.number_input("Umur Pasien", 0, 120)

            st.markdown("---")
            st.subheader("Ceklis Gejala yang Dirasakan:")
            
            gejala_terpilih = []
            cols = st.columns(2)
            items = list(daftar_gejala.items())
            for i, (kode, gejala) in enumerate(items):
                with cols[i % 2]:
                    if st.checkbox(gejala, key=kode):
                        gejala_terpilih.append(kode)

            submitted = st.form_submit_button("ANALISIS SEKARANG")
            if submitted:
                st.session_state.nama = nama
                st.session_state.gejala = gejala_terpilih
                st.success("Analisis selesai! Silakan buka menu 'Hasil'.")

    # ================== HALAMAN HASIL ==================
    elif menu == "Hasil":
        st.markdown('<div class="header-box"><h1>📊 LAPORAN HASIL DIAGNOSIS</h1></div>', unsafe_allow_html=True)

        gejala_terpilih = st.session_state.get("gejala", [])
        nama = st.session_state.get("nama", "Pasien")

        if not gejala_terpilih:
            st.warning("Data diagnosis belum tersedia. Harap melengkapi input gejala pada menu Diagnosis.")
        else:
            hasil = None
            for r in rules:
                cocok = len([g for g in r["gejala"] if g in gejala_terpilih])
                if cocok >= len(r["gejala"]) * 0.5:
                    hasil = r
                    break

            if hasil:
                st.markdown(f"### Kesimpulan Klinis: **{hasil['nama']}**")
                st.write(f"**Identitas Pasien:** {nama}")
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    with st.expander("Manifestasi Klinis yang Terdeteksi", expanded=True):
                        for g in gejala_terpilih:
                            st.write(f"✅ {daftar_gejala[g]}")
                
                with col_res2:
                    with st.expander("Rekomendasi Tindakan & Tata Laksana", expanded=True):
                        for s in hasil["solusi"]:
                            st.write(f"📌 {daftar_solusi[s]}")
                
                st.button("UNDUH LAPORAN (PDF)")
                st.caption("*Hasil ini bersifat sementara berdasarkan analisis sistem pakar. Konsultasikan dengan tenaga medis ahli untuk validasi lebih lanjut.")
            else:
                st.error("Sistem tidak menemukan indikasi spesifik. Gejala yang Anda masukkan belum memenuhi kriteria ambang batas diagnosis Hemofilia dalam database kami.")

    # ================== LOGOUT ==================
    elif menu == "Logout":
        st.session_state.login = False
        st.rerun()
