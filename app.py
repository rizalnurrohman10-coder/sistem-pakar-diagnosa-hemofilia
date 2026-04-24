import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Hemofilia", layout="centered")

# ================== CUSTOM CSS (UI MERAH PUTIH) ==================
st.markdown("""
    <style>
    /* Mengubah font dan warna background utama */
    .main {
        background-color: #f8f9fa;
        color: #212121;
    }
    
    /* Header Merah */
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
    }

    /* Tombol Custom */
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

    /* Kartu (Card) untuk Login & Hasil */
    .st-emotion-cache-1r6slb0 {
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        background-color: white;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #D32F2F;
    }
    
    /* Judul Subheader */
    h2, h3 {
        color: #D32F2F !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ================== SESSION ==================
if "login" not in st.session_state:
    st.session_state.login = False

# ================== DATA (TETAP SAMA) ==================
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
    "S02": "Obat antifibrinolitik",
    "S03": "Edukasi pencegahan",
    "S04": "Hindari cedera",
    "S05": "Terapi faktor pembekuan",
    "S06": "Fisioterapi",
    "S07": "Monitoring medis",
    "S08": "Hindari olahraga berat",
    "S09": "Terapi rutin faktor VIII/IX",
    "S10": "Penanganan darurat",
    "S11": "Rehabilitasi",
    "S12": "Hindari aspirin"
}

rules = [
    {"nama": "Hemofilia A (Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]},
    {"nama": "Hemofilia B (Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]},
    {"nama": "Hemofilia C (Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]}
]

# ================== HALAMAN LOGIN ==================
if not st.session_state.login:
    st.markdown('<div class="header-box"><h1>🩸 LOGIN SISTEM</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        left_co, cent_co, last_co = st.columns([1,3,1])
        with cent_co:
            st.markdown("### Selamat Datang Kembali")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("MASUK KE SISTEM"):
                if username == "admin" and password == "123":
                    st.session_state.login = True
                    st.rerun()
                else:
                    st.error("Username atau Password salah!")

# ================== MENU UTAMA ==================
else:
    st.sidebar.markdown("<h2 style='text-align:center;'>MENU</h2>", unsafe_allow_html=True)
    menu = st.sidebar.selectbox("Navigasi", ["Dashboard", "Diagnosis", "Hasil", "Logout"])

    if menu == "Dashboard":
        st.markdown('<div class="header-box"><h1>🩸 DASHBOARD</h1></div>', unsafe_allow_html=True)
        st.subheader(f"Halo, Selamat Datang!")
        st.info("Sistem ini menggunakan metode Forward Chaining untuk mendeteksi tingkat keparahan Hemofilia berdasarkan gejala yang Anda berikan.")
        if st.button("Mulai Diagnosis"):
            # Programmatically change menu is tricky in simple selectbox, 
            # for now we guide user to sidebar.
            st.warning("Silakan pilih menu 'Diagnosis' di sidebar sebelah kiri.")

    # ================== HALAMAN DIAGNOSIS ==================
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
            # Menampilkan checklist dalam 2 kolom agar rapi
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
        st.markdown('<div class="header-box"><h1>📊 HASIL DIAGNOSIS</h1></div>', unsafe_allow_html=True)

        gejala_terpilih = st.session_state.get("gejala", [])
        nama = st.session_state.get("nama", "Pasien Umum")

        if not gejala_terpilih:
            st.warning("Belum ada data diagnosis. Silakan lakukan diagnosis terlebih dahulu.")
        else:
            hasil = None
            # Logika pencocokan aturan
            for r in rules:
                cocok = len([g for g in r["gejala"] if g in gejala_terpilih])
                if cocok >= len(r["gejala"]) * 0.5:
                    hasil = r
                    break

            if hasil:
                st.markdown(f"### Diagnosis: **{hasil['nama']}**")
                st.write(f"**Nama Pasien:** {nama}")
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    with st.expander("Gejala yang Terdeteksi", expanded=True):
                        for g in gejala_terpilih:
                            st.write(f"✅ {daftar_gejala[g]}")
                
                with col_res2:
                    with st.expander("Solusi & Saran Medis", expanded=True):
                        for s in hasil["solusi"]:
                            st.write(f"📌 {daftar_solusi[s]}")
                
                st.button("CETAK HASIL (PDF)")
            else:
                st.error("Maaf, gejala yang Anda masukkan tidak mencukupi untuk mendiagnosa jenis Hemofilia tertentu secara spesifik.")

    # ================== LOGOUT ==================
    elif menu == "Logout":
        st.session_state.login = False
        st.rerun()
