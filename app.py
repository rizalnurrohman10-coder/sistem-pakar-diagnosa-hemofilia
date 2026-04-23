import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Hemofilia", page_icon="🩸", layout="wide")

# --- CSS CUSTOM UNTUK TAMPILAN MODERN (MERAH-PUTIH) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }
    .stApp {
        background-color: #f8f9fa;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #d90429;
    }
    .header-banner {
        background-color: #d90429;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .custom-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .card-title {
        color: #d90429;
        font-weight: bold;
        border-bottom: 2px solid #d90429;
        padding-bottom: 10px;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button {
        background-color: #d90429;
        color: white;
        border-radius: 8px;
        width: 100%;
        border: none;
        padding: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ef233c;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA MASTER (15 GEJALA & 12 SOLUSI) ---
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
    st.markdown("<h2 style='color:#d90429; text-align:center;'>SISTEM PAKAR HEMOFILIA</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2764/2764357.png", width=100)
    st.write("---")
    nav = st.radio("MENU UTAMA", ["🏠 Beranda", "🩺 Proses Diagnosa", "📚 Edukasi"])
    st.write("---")
    st.caption("Pengembang: M. Rizal Nurrohman")

# --- HALAMAN 1: BERANDA ---
if nav == "🏠 Beranda":
    st.markdown('<div class="header-banner"><h1>SELAMAT DATANG DI HEMOSMART AI</h1></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image("https://img.freepik.com/free-vector/blood-donation-concept-illustration_114360-5554.jpg")
    with col2:
        st.markdown(f"""
            <div class="custom-card">
                <h3 class="card-title">Tentang Aplikasi</h3>
                <p>Aplikasi ini adalah sistem pakar berbasis web yang dirancang untuk membantu masyarakat melakukan deteksi dini terhadap tingkat keparahan penyakit <b>Hemofilia</b>.</p>
                <p>Dengan menjawab beberapa pertanyaan mengenai gejala yang dialami, sistem akan memberikan hasil analisis berdasarkan pengetahuan medis yang terintegrasi.</p>
                <hr>
                <p style="color: #666; font-size: 0.9em;"><i>*Hasil diagnosa ini hanyalah indikasi awal. Harap konsultasikan kembali dengan dokter ahli hematologi untuk hasil yang akurat.</i></p>
            </div>
        """, unsafe_allow_html=True)

# --- HALAMAN 2: DIAGNOSA ---
elif nav == "🩺 Proses Diagnosa":
    st.markdown('<div class="header-banner"><h1>PROSES DIAGNOSA: CHECKLIST GEJALA</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">Biodata Pasien</h3>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        nama = c1.text_input("Nama Lengkap")
        umur = c2.number_input("Umur", min_value=0, step=1)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">Daftar Gejala Klinis</h3>', unsafe_allow_html=True)
        st.write("Centang gejala yang Anda rasakan selama ini:")
        
        gejala_terpilih = []
        col_g1, col_g2 = st.columns(2)
        items = list(daftar_gejala.items())
        for i in range(len(items)):
            target_col = col_g1 if i < 8 else col_g2
            kode, teks = items[i]
            if target_col.checkbox(f"{teks}", key=kode):
                gejala_terpilih.append(kode)
        
        st.write("---")
        if st.button("ANALISIS HASIL SEKARANG"):
            if not nama or not gejala_terpilih:
                st.warning("Pastikan Anda sudah mengisi Nama dan memilih minimal satu gejala.")
            else:
                # Logika Forward Chaining
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
                        <div class="custom-card" style="border-left: 10px solid #d90429; background-color: #fffafa;">
                            <h2 style='color:#d90429; margin-top:0;'>HASIL ANALISIS SISTEM</h2>
                            <p>Nama: <b>{nama}</b> | Umur: <b>{umur} Tahun</b></p>
                            <hr>
                            <h4 style='margin-bottom:5px;'>KEMUNGKINAN BESAR:</h4>
                            <h2 style='color:#d90429; margin-top:0;'>{hasil_final['nama'].upper()}</h2>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
                    st.markdown('<h3 class="card-title">Solusi & Rekomendasi:</h3>', unsafe_allow_html=True)
                    for kode_s in hasil_final['solusi']:
                        st.success(f"**{kode_s}**: {daftar_solusi[kode_s]}")
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("Sistem tidak menemukan hasil yang cukup kuat. Segera hubungi dokter spesialis darah.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- HALAMAN 3: EDUKASI ---
elif nav == "📚 Edukasi":
    st.markdown('<div class="header-banner"><h1>EDUKASI HEMOFILIA</h1></div>', unsafe_allow_html=True)
    col_a, col_b = st.columns([1,1])
    with col_a:
        st.markdown("""
            <div class="custom-card">
                <h3 class="card-title">Mengenal Hemofilia</h3>
                <p>Hemofilia adalah gangguan pembekuan darah akibat kekurangan Faktor VIII (Hemofilia A) atau Faktor IX (Hemofilia B).</p>
                <ul>
                    <li><b>Ringan:</b> Pendarahan hanya terjadi setelah cedera berat atau operasi.</li>
                    <li><b>Sedang:</b> Pendarahan terjadi setelah benturan ringan.</li>
                    <li><b>Berat:</b> Pendarahan sering terjadi secara spontan (tanpa sebab).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.video("https://www.youtube.com/watch?v=1oW_fFm-v24")
