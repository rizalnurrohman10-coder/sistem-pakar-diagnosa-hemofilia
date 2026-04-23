import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Hemofilia", page_icon="🩸", layout="wide")

# Custom CSS untuk tampilan profesional
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stButton>button {
        width: 100%; border-radius: 12px; background-color: #d90429;
        color: white; height: 3.5em; font-weight: bold; font-size: 18px;
    }
    .result-card {
        background-color: white; padding: 30px; border-radius: 20px;
        border-top: 10px solid #d90429; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .title-text { color: #d90429; text-align: center; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA GEJALA (G01 - G15) ---
daftar_gejala = {
    "G01": "Pendarahan sulit berhenti",
    "G02": "Memar/lebam tanpa sebab",
    "G03": "Pendarahan spontan pada sendi",
    "G04": "Pendarahan dalam otot (hematoma)",
    "G05": "Pendarahan setelah cabut gigi",
    "G06": "Pendarahan pasca operasi",
    "G07": "Darah pada urin (hematuria)",
    "G08": "Darah pada tinja",
    "G09": "Nyeri pada sendi",
    "G10": "Pembengkakan sendi",
    "G11": "Pendarahan akibat benturan ringan",
    "G12": "Pendarahan tali pusat pada bayi",
    "G13": "Pendarahan hebat saat imunisasi",
    "G14": "Pendarahan hebat saat khitan",
    "G15": "Riwayat keluarga menderita Hemofilia"
}

# --- DATA SOLUSI (S01 - S12) ---
daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)",
    "S02": "Obat pendukung (antifibrinolitik, desmopressin)",
    "S03": "Edukasi pencegahan pendarahan",
    "S04": "Kesadaran terhadap risiko cedera",
    "S05": "Terapi faktor pembekuan saat diperlukan (on-demand)",
    "S06": "Fisioterapi untuk menjaga kesehatan sendi",
    "S07": "Monitoring medis berkala",
    "S08": "Edukasi menghindari olahraga kontak berat",
    "S09": "Terapi profilaksis rutin (faktor VIII/IX)",
    "S10": "Penanganan darurat untuk pendarahan internal",
    "S11": "Rehabilitasi jangka panjang",
    "S12": "Menghindari obat aspirin dan NSAID"
}

# --- BASIS ATURAN (SESUAI PERMINTAAN) ---
rules = [
    {
        "nama": "Hemofilia Ringan",
        "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G09", "G10", "G11", "G15"],
        "solusi": ["S01", "S02", "S03", "S04"]
    },
    {
        "nama": "Hemofilia Sedang",
        "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G15"],
        "solusi": ["S05", "S06", "S07", "S08"]
    },
    {
        "nama": "Hemofilia Berat",
        "gejala": ["G01", "G02", "G04", "G06", "G07", "G08", "G09", "G10", "G12", "G13", "G14", "G15"],
        "solusi": ["S09", "S10", "S11", "S12"]
    }
]

# --- UI WEBSITE ---
st.markdown("<h1 class='title-text'>🩸 SISTEM PAKAR HEMO-DIAGNOSA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Berdasarkan Diagnosa Gejala Klinis Pasien</p>", unsafe_allow_html=True)

# Input Data Pasien
with st.expander("👤 Identitas Pasien", expanded=True):
    c1, c2, c3 = st.columns(3)
    nama = c1.text_input("Nama Pasien")
    umur = c2.number_input("Umur", min_value=0)
    jk = c3.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Input 15 Gejala (Dua Kolom)
st.write("### 🔍 Pilih Gejala yang Dialami:")
col_g1, col_g2 = st.columns(2)
gejala_terpilih = []

for i, (kode, teks) in enumerate(daftar_gejala.items()):
    target_col = col_g1 if i < 8 else col_g2
    if target_col.checkbox(f"{kode}: {teks}"):
        gejala_terpilih.append(kode)

st.divider()

# Logika Diagnosa
if st.button("PROSES DIAGNOSA"):
    if not nama:
        st.warning("⚠️ Masukkan nama pasien.")
    elif not gejala_terpilih:
        st.error("❌ Pilih minimal satu gejala.")
    else:
        hasil_final = None
        # Urutan pengecekan: Berat -> Sedang -> Ringan
        for rule in reversed(rules):
            # Jika gejala yang dipilih user mengandung minimal 60% dari syarat gejala rule
            match_count = len([g for g in rule["gejala"] if g in gejala_terpilih])
            if match_count >= (len(rule["gejala"]) * 0.5): # Threshold 50% kecocokan
                hasil_final = rule
                break
        
        if hasil_final:
            st.markdown(f"""
            <div class="result-card">
                <h4 style='color: gray; margin: 0;'>Hasil Analisis untuk {nama}:</h4>
                <h1 style='color: #d90429; margin: 10px 0;'>{hasil_final['nama']}</h1>
                <hr>
                <p><b>🛡️ Rekomendasi Solusi:</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Menampilkan solusi berdasarkan kode
            cols_s = st.columns(2)
            for idx, kode_s in enumerate(hasil_final['solusi']):
                t_col = cols_s[idx % 2]
                t_col.success(f"**{kode_s}**: {daftar_solusi[kode_s]}")
        else:
            st.info("Gejala tidak cukup spesifik untuk menentukan tingkat keparahan. Silakan konsultasi ke dokter.")

st.caption("Aplikasi ini dibuat berdasarkan data presentasi Sistem Pakar Hemofilia.")
