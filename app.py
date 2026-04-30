import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Penyakit Hemofilia", page_icon="🩸", layout="centered")

# ================== CUSTOM CSS (UI & KONTRAS) ==================
st.markdown("""
    <style>
    .stApp {
        background-color: #F4F6F9 !important;
    }
    
    /* Teks utama hitam pekat agar jelas */
    p, label, span, li, div, h3, .stMarkdown {
        color: #1A1D23 !important; 
        font-weight: 500 !important;
    }

    /* Tombol Merah Utama */
    div.stButton > button {
        background-color: #D32F2F !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
    }

    /* Memperjelas Tombol Hitam (Submit Button) */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #1A1D23 !important;
        color: #FFFFFF !important;
        border: 2px solid #D32F2F !important;
        font-size: 16px !important;
        font-weight: bold !important;
        width: 100% !important;
    }

    /* Kotak Header Merah */
    .top-header-red {
        background-color: #B71C1C;
        color: #FFFFFF !important;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .top-header-red h1 {
        color: #FFFFFF !important;
        margin: 0;
    }

    /* Styling Kotak Referensi Keparahan */
    .severity-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ced4da;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

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

rules = [
    {"id": "berat", "nama": "Hemofilia A (Klasifikasi: Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"]},
    {"id": "sedang", "nama": "Hemofilia B (Klasifikasi: Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"]},
    {"id": "ringan", "nama": "Hemofilia C (Klasifikasi: Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"]}
]

# ================== STATE MANAGEMENT ==================
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "gejala_terpilih" not in st.session_state:
    st.session_state.gejala_terpilih = []

# ================== HALAMAN LOGIN ==================
if st.session_state.page == "Login":
    st.markdown('<div class="top-header-red"><h1>🩸 LOGIN SISTEM</h1></div>', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("MASUK KE SISTEM"):
        if username == "admin" and password == "123":
            st.session_state.page = "Menu Utama"
            st.rerun()
        else:
            st.error("Kredensial salah!")

# ================== MENU UTAMA ==================
elif st.session_state.page == "Menu Utama":
    st.markdown('<div class="top-header-red"><h1>🏠 MENU UTAMA</h1></div>', unsafe_allow_html=True)
    if st.button("🚀 MULAI PROSES PENYAKIT"):
        st.session_state.page = "Penyakit"
        st.rerun()

# ================== HALAMAN PROSES PENYAKIT ==================
elif st.session_state.page == "Penyakit":
    st.markdown('<div class="top-header-red"><h1>📋 PROSES PENYAKIT</h1></div>', unsafe_allow_html=True)
    
    with st.form("main_form"):
        nama_pasien = st.text_input("Nama Pasien")
        
        st.subheader("Pilih Gejala yang Dialami:")
        gejala_manual = []
        cols_gejala = st.columns(2)
        items = list(daftar_gejala.items())
        for i, (kode, teks) in enumerate(items):
            with cols_gejala[i % 2]:
                if st.checkbox(teks, key=f"m_{kode}"):
                    gejala_manual.append(kode)

        st.markdown("---")
        st.subheader("Ceklis Berdasarkan Referensi Keparahan:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="severity-box">RINGAN</div>', unsafe_allow_html=True)
            cek_ringan = st.checkbox("Pilih Ringan", key="ref_ringan")
        with col2:
            st.markdown('<div class="severity-box">SEDANG</div>', unsafe_allow_html=True)
            cek_sedang = st.checkbox("Pilih Sedang", key="ref_sedang")
        with col3:
            st.markdown('<div class="severity-box">BERAT</div>', unsafe_allow_html=True)
            cek_berat = st.checkbox("Pilih Berat", key="ref_berat")

        st.write("<br>", unsafe_allow_html=True)
        
        # TOMBOL HITAM YANG DIPERJELAS
        submitted = st.form_submit_button("PROSES HASIL PENYAKIT")
        
        if submitted:
            final_gejala = set(gejala_manual)
            if cek_ringan: final_gejala.update(rules[2]["gejala"])
            if cek_sedang: final_gejala.update(rules[1]["gejala"])
            if cek_berat: final_gejala.update(rules[0]["gejala"])
                
            st.session_state.gejala_terpilih = list(final_gejala)
            st.session_state.nama_pasien = nama_pasien
            st.session_state.page = "Hasil"
            st.rerun()

    if st.button("Kembali"):
        st.session_state.page = "Menu Utama"
        st.rerun()

# ================== HALAMAN HASIL PENYAKIT ==================
elif st.session_state.page == "Hasil":
    st.markdown('<div class="top-header-red"><h1>📊 HASIL PENYAKIT</h1></div>', unsafe_allow_html=True)
    
    gejala = st.session_state.gejala_terpilih
    nama = st.session_state.get("nama_pasien", "Pasien")
    
    if not gejala:
        st.warning("Silakan pilih gejala terlebih dahulu.")
    else:
        hasil_pakar = None
        for r in rules:
            cocok = len([g for g in r["gejala"] if g in gejala])
            if cocok >= len(r["gejala"]) * 0.5:
                hasil_pakar = r
                break
        
        if hasil_pakar:
            st.success(f"### Kesimpulan: {hasil_pakar['nama']}")
            st.write(f"**Nama Pasien:** {nama}")
        else:
            st.error("Indikasi tidak spesifik ditemukan.")

    if st.button("KEMBALI KE MENU UTAMA"):
        st.session_state.page = "Menu Utama"
        st.rerun()
