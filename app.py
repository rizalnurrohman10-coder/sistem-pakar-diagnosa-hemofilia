import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Penyakit Hemofilia", page_icon="🩸", layout="centered")

# ================== CUSTOM CSS (FIX NAVIGASI & KONTRAS) ==================
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    
    /* FIX NAVIGASI: Memaksa teks sidebar menjadi hitam pekat agar jelas */
    section[data-testid="stSidebar"] .st-emotion-cache-17l6i46, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }

    /* Header Merah */
    .header-box {
        background-color: #D32F2F;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
    }
    .header-box h1 { color: white !important; margin: 0; }

    /* Tombol Utama */
    div.stButton > button {
        background-color: #D32F2F !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 3em;
        width: 100%;
    }

    /* Tombol Hitam (Proses) */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #1A1D23 !important;
        color: #FFFFFF !important;
        border: 2px solid #D32F2F !important;
        font-weight: bold !important;
        width: 100% !important;
    }

    /* Severity Box */
    .severity-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ced4da;
        text-align: center;
        font-weight: bold;
        color: #1A1D23;
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
    {"id": "ringan", "nama": "Hemofilia C (Klasifikasi: Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]},
    {"id": "sedang", "nama": "Hemofilia B (Klasifikasi: Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]},
    {"id": "berat", "nama": "Hemofilia A (Klasifikasi: Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]}
]

# ============= STATE & LOGIN =============
if "akses" not in st.session_state: st.session_state.akses = False
if "gejala_terpilih" not in st.session_state: st.session_state.gejala_terpilih = []

if not st.session_state.akses:
    st.markdown('<div class="header-box"><h1>🩸 AKSES MASUK</h1></div>', unsafe_allow_html=True)
    user = st.text_input("ID Pengguna")
    pw = st.text_input("Kata Sandi", type="password")
    if st.button("VERIFIKASI"):
        if user == "admin" and pw == "123":
            st.session_state.akses = True
            st.rerun()
        else: st.error("Kredensial salah!")
else:
    # Sidebar Navigasi (Teks diperbaiki lewat CSS di atas)
    st.sidebar.markdown("### 🧭 MENU NAVIGASI")
    menu = st.sidebar.radio("Pilih Halaman:", ["Beranda Utama", "Pemeriksaan Penyakit", "Laporan Penyakit", "Keluar Sistem"])

    # ============= BERANDA =============
    if menu == "Beranda Utama":
        st.markdown('<div class="header-box"><h1>🏠 BERANDA UTAMA</h1></div>', unsafe_allow_html=True)
        st.info("Selamat datang. Sistem ini siap membantu analisis klasifikasi penyakit Hemofilia.")

    # ============= PEMERIKSAAN =============
    elif menu == "Pemeriksaan Penyakit":
        st.markdown('<div class="header-box"><h1>📋 PEMERIKSAAN PENYAKIT</h1></div>', unsafe_allow_html=True)
        with st.form("f_pemeriksaan"):
            st.session_state.nama_pasien = st.text_input("Nama Pasien", value=st.session_state.get("nama_pasien", ""))
            
            st.subheader("Pilih Gejala Manual:")
            gejala_m = []
            c_g = st.columns(2)
            for i, (k, v) in enumerate(daftar_gejala.items()):
                with c_g[i%2]:
                    if st.checkbox(v, key=f"chk_{k}"): gejala_m.append(k)
            
            st.markdown("---")
            st.subheader("Atau Pilih Cepat (Referensial):")
            cr1, cr2, cr3 = st.columns(3)
            with cr1:
                st.markdown('<div class="severity-box">RINGAN</div>', unsafe_allow_html=True)
                p_ringan = st.checkbox("Pilih Ringan", key="p_r")
            with cr2:
                st.markdown('<div class="severity-box">SEDANG</div>', unsafe_allow_html=True)
                p_sedang = st.checkbox("Pilih Sedang", key="p_s")
            with cr3:
                st.markdown('<div class="severity-box">BERAT</div>', unsafe_allow_html=True)
                p_berat = st.checkbox("Pilih Berat", key="p_b")

            if st.form_submit_button("PROSES ANALISIS PENYAKIT"):
                final = set(gejala_m)
                # Pemilihan cepat (Otomatis mengambil data gejala di rules)
                if p_ringan: final.update(rules[0]["gejala"])
                if p_sedang: final.update(rules[1]["gejala"])
                if p_berat:  final.update(rules[2]["gejala"])
                
                st.session_state.gejala_terpilih = list(final)
                st.success("Data diproses. Buka Laporan Penyakit.")

    # ============= LAPORAN (LOGIKA AKURASI DI SINI) =============
    elif menu == "Laporan Penyakit":
        st.markdown('<div class="header-box"><h1>📊 LAPORAN PENYAKIT</h1></div>', unsafe_allow_html=True)
        gejala = st.session_state.gejala_terpilih
        
        if not gejala:
            st.warning("Data belum diinput.")
        else:
            # PERBAIKAN LOGIKA: Mencari yang paling cocok (Scoring)
            skor_rules = []
            for r in rules:
                cocok = len([g for g in r["gejala"] if g in gejala])
                persentase = cocok / len(r["gejala"])
                skor_rules.append({"rule": r, "skor": persentase})
            
            # Urutkan dari skor tertinggi
            skor_rules = sorted(skor_rules, key=lambda x: x["skor"], reverse=True)
            terbaik = skor_rules[0]

            if terbaik["skor"] >= 0.5:
                hasil = terbaik["rule"]
                st.success(f"### Hasil Analisis: {hasil['nama']}")
                st.write(f"**Nama Pasien:** {st.session_state.get('nama_pasien', 'Anonim')}")
                
                c1, c2 = st.columns(2)
                with c1:
                    with st.expander("Gejala Terdeteksi", expanded=True):
                        for g in gejala: st.write(f"✅ {daftar_gejala[g]}")
                with c2:
                    with st.expander("Rekomendasi", expanded=True):
                        for s in hasil["solusi"]: st.write(f"📌 {daftar_solusi[s]}")
            else:
                st.error("Gejala tidak memenuhi ambang batas (50%) untuk klasifikasi tertentu.")

    elif menu == "Keluar Sistem":
        st.session_state.akses = False
        st.rerun()
