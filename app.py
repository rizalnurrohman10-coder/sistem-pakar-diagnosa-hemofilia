import streamlit as st

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(page_title="Sistem Pakar Penyakit Hemofilia", page_icon="🩸", layout="centered")

# ================== CUSTOM CSS (UI & NAVIGASI PUTIH) ==================
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    
    /* FIX NAVIGASI: Latar belakang sidebar merah tua, teks putih agar kontras */
    section[data-testid="stSidebar"] {
        background-color: #B71C1C !important;
    }
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    section[data-testid="stSidebar"] label {
        font-size: 16px !important;
        font-weight: bold !important;
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
        border: 2px solid #D32F2F !important;
    }
    div.stButton > button:hover {
        background-color: #1A1D23 !important;
        border: 2px solid #1A1D23 !important;
    }

    /* Tombol Hitam (Proses Analisis) */
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #1A1D23 !important;
        color: #FFFFFF !important;
        border: 2px solid #D32F2F !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 3.5em !important;
        font-size: 16px !important;
    }

    /* Kotak Keparahan */
    .severity-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ced4da;
        text-align: center;
        font-weight: bold;
        color: #1A1D23 !important;
        margin-bottom: 5px;
    }
    
    /* Box Edukasi */
    .info-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #D32F2F;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
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

# ============= STATE MANAGEMENT =============
if "akses" not in st.session_state: st.session_state.akses = False
if "gejala_terpilih" not in st.session_state: st.session_state.gejala_terpilih = []
if "menu" not in st.session_state: st.session_state.menu = "Beranda Utama"

# ============= HALAMAN AKSES MASUK (LOGIN) =============
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
    # Sidebar Navigasi
    st.sidebar.markdown("<h3 style='text-align:center;'>🧭 NAVIGASI SISTEM</h3>", unsafe_allow_html=True)
    
    # Sync radio button dengan session_state menu
    menu_options = ["Beranda Utama", "Pemeriksaan Penyakit", "Laporan Penyakit", "Keluar Sistem"]
    menu = st.sidebar.radio("Pilih Halaman:", menu_options, index=menu_options.index(st.session_state.menu))
    
    # Deteksi perubahan menu dari sidebar
    if menu != st.session_state.menu:
        st.session_state.menu = menu
        st.rerun()

    # ============= HALAMAN 1: BERANDA UTAMA =============
    if st.session_state.menu == "Beranda Utama":
        st.markdown('<div class="header-box"><h1>🏠 BERANDA UTAMA</h1></div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-box">
            <h3 style="color:#D32F2F; margin-top:0;">Apa itu Hemofilia?</h3>
            <p style="text-align:justify; font-size:15px; margin-bottom:0;">
                <b>Hemofilia</b> adalah gangguan pembekuan darah bawaan yang langka. Kondisi ini menyebabkan penderitanya kekurangan protein yang dibutuhkan untuk proses pembekuan darah (Faktor Pembekuan). Akibatnya, penderita hemofilia akan mengalami pendarahan lebih lama dibandingkan orang normal saat mengalami luka. Hemofilia dapat memicu pendarahan internal pada sendi dan otot yang bisa merusak organ secara permanen jika tidak didiagnosis dan ditangani dengan tepat.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 MULAI PEMERIKSAAN PENYAKIT SEKARANG"):
            st.session_state.menu = "Pemeriksaan Penyakit"
            st.rerun()

    # ============= HALAMAN 2: PEMERIKSAAN PENYAKIT =============
    elif st.session_state.menu == "Pemeriksaan Penyakit":
        st.markdown('<div class="header-box"><h1>📋 PEMERIKSAAN PENYAKIT</h1></div>', unsafe_allow_html=True)
        
        with st.form("f_pemeriksaan"):
            st.session_state.nama_pasien = st.text_input("Nama Lengkap Pasien", value=st.session_state.get("nama_pasien", ""))
            
            st.subheader("Ceklis Gejala Manual:")
            gejala_m = []
            c_g = st.columns(2)
            for i, (k, v) in enumerate(daftar_gejala.items()):
                with c_g[i%2]:
                    if st.checkbox(v, key=f"chk_{k}"): gejala_m.append(k)
            
            st.markdown("---")
            st.subheader("Pilih Cepat Berdasarkan Referensi Keparahan:")
            cr1, cr2, cr3 = st.columns(3)
            with cr1:
                st.markdown('<div class="severity-box">RINGAN</div>', unsafe_allow_html=True)
                p_ringan = st.checkbox("Pilih Paket Ringan", key="p_r")
            with cr2:
                st.markdown('<div class="severity-box">SEDANG</div>', unsafe_allow_html=True)
                p_sedang = st.checkbox("Pilih Paket Sedang", key="p_s")
            with cr3:
                st.markdown('<div class="severity-box">BERAT</div>', unsafe_allow_html=True)
                p_berat = st.checkbox("Pilih Paket Berat", key="p_b")

            if st.form_submit_button("PROSES ANALISIS PENYAKIT"):
                final = set(gejala_m)
                # Paksa masuk gejala jika pilih cepat
                if p_ringan: final.update(rules[0]["gejala"])
                if p_sedang: final.update(rules[1]["gejala"])
                if p_berat:  final.update(rules[2]["gejala"])
                
                st.session_state.gejala_terpilih = list(final)
                
                # OTOMATIS REDIRECT KE LAPORAN
                st.session_state.menu = "Laporan Penyakit"
                st.rerun()

    # ============= HALAMAN 3: LAPORAN PENYAKIT =============
    elif st.session_state.menu == "Laporan Penyakit":
        st.markdown('<div class="header-box"><h1>📊 LAPORAN PENYAKIT</h1></div>', unsafe_allow_html=True)
        gejala = st.session_state.gejala_terpilih
        nama = st.session_state.get('nama_pasien', '')
        if nama == "": nama = "Pasien Anonim"
        
        if not gejala:
            st.warning("Data pasien belum diinput. Silakan kembali ke menu Pemeriksaan Penyakit.")
        else:
            # PERBAIKAN LOGIKA AKURASI (Jaccard Index)
            # Menjamin 100% akurat sesuai paket yang dipilih
            skor_rules = []
            for r in rules:
                cocok = len([g for g in r["gejala"] if g in gejala])
                total_unik = len(set(r["gejala"] + gejala))
                skor = cocok / total_unik if total_unik > 0 else 0
                skor_rules.append({"rule": r, "skor": skor})
            
            # Urutkan berdasarkan kemiripan paling tinggi
            skor_rules = sorted(skor_rules, key=lambda x: x["skor"], reverse=True)
            terbaik = skor_rules[0]

            if terbaik["skor"] > 0.3: # Ambang batas diturunkan agar lebih toleran pada manual
                hasil = terbaik["rule"]
                st.success(f"### Kesimpulan Analisis: **{hasil['nama']}**")
                st.write(f"**Identitas Pasien:** {nama}")
                
                c1, c2 = st.columns(2)
                with c1:
                    with st.expander("Manifestasi Klinis Terdeteksi", expanded=True):
                        for g in gejala: st.write(f"✅ {daftar_gejala[g]}")
                with c2:
                    with st.expander("Rekomendasi Tindakan Medis", expanded=True):
                        for s in hasil["solusi"]: st.write(f"📌 {daftar_solusi[s]}")
                
                # --- FITUR UNDUH LAPORAN ---
                teks_laporan = f"LAPORAN HASIL ANALISIS HEMOFILIA\n{'='*40}\n"
                teks_laporan += f"Nama Pasien : {nama}\n"
                teks_laporan += f"Diagnosis   : {hasil['nama']}\n\n"
                teks_laporan += "GEJALA TERDETEKSI:\n"
                for g in gejala: teks_laporan += f"- {daftar_gejala[g]}\n"
                teks_laporan += "\nREKOMENDASI PENANGANAN:\n"
                for s in hasil["solusi"]: teks_laporan += f"- {daftar_solusi[s]}\n"
                
                st.write("<br>", unsafe_allow_html=True)
                st.download_button(
                    label="📥 UNDUH LAPORAN (Dokumen Text)",
                    data=teks_laporan,
                    file_name=f"Laporan_Hemofilia_{nama.replace(' ','_')}.txt",
                    mime="text/plain"
                )
            else:
                st.error("Gejala tidak memenuhi ambang batas untuk mendiagnosis klasifikasi tertentu.")
        
        # --- TOMBOL BAWAH ---
        st.markdown("---")
        b1, b2 = st.columns(2)
        with b1:
            if st.button("Kembali ke Beranda Utama"):
                st.session_state.menu = "Beranda Utama"
                st.rerun()
        with b2:
            if st.button("🚪 Keluar Sistem (Login)"):
                st.session_state.akses = False
                st.session_state.menu = "Beranda Utama"
                st.rerun()

    # ============= KELUAR SISTEM =============
    elif st.session_state.menu == "Keluar Sistem":
        st.session_state.akses = False
        st.session_state.menu = "Beranda Utama"
        st.session_state.gejala_terpilih = []
        st.rerun()
