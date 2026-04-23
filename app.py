import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="HemoSmart AI", page_icon="🩸", layout="wide")

# --- CSS CUSTOM UNTUK BACKGROUND & STYLE ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
    }
    [data-testid="stSidebar"] {
        background-color: #d90429;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    .result-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border-left: 10px solid #d90429;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .header-text {
        color: #d90429;
        font-size: 45px;
        font-weight: 800;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA MASTER ---
daftar_gejala = {
    "G01": "Mimisan mendadak dan sulit berhenti", 
    "G02": "Pendarahan gusi tanpa sebab yang jelas",
    "G03": "Luka kecil sulit berhenti berdarah", 
    "G04": "Memar (hematoma) lama hilang",
    "G05": "Pendarahan setelah cabut gigi", 
    "G06": "Pendarahan pasca operasi",
    "G07": "Pendarahan pada otot", 
    "G08": "Pendarahan pada sendi (lutut, siku, pergelangan)",
    "G09": "Nyeri pada sendi", 
    "G10": "Pembengkakan sendi",
    "G11": "Pendarahan akibat benturan ringan", 
    "G12": "Pendarahan spontan (tanpa sebab yang jelas)",
    "G13": "Pendarahan pada saluran pencernaan", 
    "G14": "Pendarahan di kepala (gejala neurologis)",
    "G15": "Riwayat keluarga menderita Hemofilia"
}

daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)", 
    "S02": "Obat pendukung (antifibrinolitik, desmopressin)",
    "S03": "Edukasi pencegahan pendarahan", 
    "S04": "Kesadaran terhadap risiko cedera dan pendarahan",
    "S05": "Terapi faktor pembekuan saat diperlukan (on-demand)", 
    "S06": "Fisioterapi untuk menjaga kesehatan sendi",
    "S07": "Monitoring medis berkala", 
    "S08": "Edukasi aktivitas (menghindari olahraga kontak berat)",
    "S09": "Terapi profilaksis rutin (faktor VIII/IX)", 
    "S10": "Penanganan darurat untuk pendarahan internal",
    "S11": "Rehabilitasi jangka panjang", 
    "S12": "Menghindari obat aspirin dan NSAID karena meningkatkan resiko pendarahan"
}

# --- MENU SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2764/2764357.png", width=100)
    st.title("Menu Utama")
    nav = st.radio("Pilih Halaman:", ["🏠 Beranda", "🩺 Mulai Diagnosa", "📚 Info Hemofilia"])
    st.divider()
    st.write("Dibuat oleh: Muhammad Rizal Nurrohman")

# --- HALAMAN 1: BERANDA ---
if nav == "🏠 Beranda":
    st.markdown("<h1 class='header-text'>Selamat Datang di HemoSmart AI</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://img.freepik.com/free-vector/blood-donation-concept-illustration_114360-5554.jpg", use_container_width=True)
    with col2:
        st.write("### Apa itu Sistem Pakar ini?")
        st.write("""
        Sistem ini dirancang untuk membantu mendeteksi tingkat keparahan penyakit Hemofilia secara dini 
        menggunakan metode **Forward Chaining**.
        """)
        if st.button("Mulai Diagnosa Sekarang →"):
            st.info("Silakan klik menu 'Mulai Diagnosa' di samping kiri!")

# --- HALAMAN 2: DIAGNOSA ---
elif nav == "🩺 Mulai Diagnosa":
    st.markdown("<h2 style='text-align: center; color: #d90429;'>Formulir Konsultasi Pasien</h2>", unsafe_allow_html=True)
    
    with st.container():
        c1, c2, c3 = st.columns(3)
        nama = c1.text_input("Nama Lengkap")
        umur = c2.number_input("Umur", min_value=0)
        jk = c3.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])

    st.write("---")
    st.write("### Pilih Gejala yang Anda Rasakan:")
    col_g1, col_g2 = st.columns(2)
    gejala_terpilih = []
    
    for i, (kode, teks) in enumerate(daftar_gejala.items()):
        target_col = col_g1 if i < 8 else col_g2
        if target_col.checkbox(f"[{kode}] {teks}"):
            gejala_terpilih.append(kode)

    if st.button("ANALISIS HASIL"):
        if not nama or not gejala_terpilih:
            st.error("Mohon isi Nama dan pilih minimal 1 gejala!")
        else:
            rules = [
                {"nama": "Hemofilia Ringan", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G09", "G10", "G11", "G15"], "solusi": ["S01", "S02", "S03", "S04"]},
                {"nama": "Hemofilia Sedang", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G15"], "solusi": ["S05", "S06", "S07", "S08"]},
                {"nama": "Hemofilia Berat", "gejala": ["G01", "G02", "G04", "G06", "G07", "G08", "G09", "G10", "G12", "G13", "G14", "G15"], "solusi": ["S09", "S10", "S11", "S12"]}
            ]
            
            hasil_final = None
            for rule in reversed(rules):
                match_count = len([g for g in rule["gejala"] if g in gejala_terpilih])
                if match_count >= (len(rule["gejala"]) * 0.5):
                    hasil_final = rule
                    break

            if hasil_final:
                st.markdown(f"""
                <div class="result-card">
                    <h3 style='margin:0;'>Laporan Diagnosa: {nama}</h3>
                    <h1 style='color: #d90429;'>{hasil_final['nama']}</h1>
                    <p>Berdasarkan gejala yang dipilih, sistem mengidentifikasi kondisi Anda masuk dalam kategori ini.</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("#### 🛡️ Langkah Penanganan:")
                cols_s = st.columns(2)
                for idx, kode_s in enumerate(hasil_final['solusi']):
                    t_col = cols_s[idx % 2]
                    t_col.success(f"**{kode_s}**: {daftar_solusi[kode_s]}")
            else:
                st.warning("Gejala belum cukup spesifik. Silakan hubungi dokter Hematologi.")

# --- HALAMAN 3: INFO ---
elif nav == "📚 Info Hemofilia":
    st.title("Informasi Edukasi")
    st.write("Hemofilia adalah gangguan pembekuan darah akibat kekurangan faktor VIII atau faktor IX.")
    st.video("https://www.youtube.com/watch?v=1oW_fFm-v24")
