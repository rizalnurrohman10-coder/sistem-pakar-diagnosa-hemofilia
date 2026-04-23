import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Hemofilia", page_icon="🩸", layout="wide")

# --- CSS CUSTOM UNTUK TAMPILAN SEPERTI GAMBAR ---
st.markdown("""
    <style>
    /* Mengubah font global */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }

    /* Background Aplikasi */
    .stApp {
        background-color: #f8f9fa;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #d90429;
    }
    
    /* Header Merah */
    .header-banner {
        background-color: #d90429;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Card Style untuk Diagnosa & Hasil */
    .custom-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Label Header pada Card */
    .card-title {
        color: #d90429;
        font-weight: bold;
        border-bottom: 2px solid #d90429;
        padding-bottom: 10px;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Button Styling */
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

    /* Styling Checkbox */
    .stCheckbox {
        padding: 5px;
        border-bottom: 1px solid #f0f0f0;
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

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#d90429; text-align:center;'>SISTEM PAKAR HEMOFILIA</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2764/2764357.png", width=100)
    st.write("---")
    nav = st.radio("MENU UTAMA", ["🏠 Beranda", "🩺 Proses Diagnosa", "📚 Edukasi"])
    st.write("---")
    st.caption("Pakar: M. Rizal Nurrohman")

# --- HALAMAN 1: BERANDA ---
if nav == "🏠 Beranda":
    st.markdown('<div class="header-banner"><h1>SISTEM PAKAR HEMOFILIA</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image("https://img.freepik.com/free-vector/blood-donation-concept-illustration_114360-5554.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""
            <div class="custom-card">
                <h3 class="card-title">Informasi Sistem</h3>
                <p>Hemofilia adalah gangguan perdarahan yang memerlukan perhatian khusus. 
                Sistem pakar ini menggunakan metode <b>Forward Chaining</b> untuk memberikan 
                indikasi awal tingkat keparahan berdasarkan gejala klinis yang Anda alami.</p>
                <hr>
                <p><i>Silakan pilih menu <b>Proses Diagnosa</b> untuk memulai konsultasi mandiri.</i></p>
            </div>
        """, unsafe_allow_html=True)

# --- HALAMAN 2: DIAGNOSA ---
elif nav == "🩺 Proses Diagnosa":
    st.markdown('<div class="header-banner"><h1>PROSES DIAGNOSA: CHECKLIST GEJALA</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">Data Pasien & Gejala</h3>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        nama = c1.text_input("Nama Lengkap")
        umur = c2.number_input("Umur", min_value=0, step=1)
        
        st.write("---")
        st.write("Silakan centang gejala yang dirasakan:")
        
        gejala_terpilih = []
        col_g1, col_g2 = st.columns(2)
        
        items = list(daftar_gejala.items())
        for i in range(len(items)):
            target_col = col_g1 if i < 8 else col_g2
            kode, teks = items[i]
            if target_col.checkbox(f"{teks}", key=kode):
                gejala_terpilih.append(kode)
        
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("LIHAT HASIL DIAGNOSA"):
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
                        <div class="custom-card" style="border-left: 10px solid #d90429;">
                            <h2 style='color:#d90429;'>HASIL DIAGNOSA</h2>
                            <p>Nama Pasien: <b>{nama}</b> ({umur} Tahun)</p>
                            <hr>
                            <h3 style='background-color:#fff3f3; padding:10px; border-radius:5px;'>
                                KEMUNGKINAN BESAR: <br><span style='color:#d90429;'>{hasil_final['nama'].upper()}</span>
                            </h3>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
                    st.markdown('<h3 class="card-title">Solusi & Saran Lanjutan:</h3>', unsafe_allow_html=True)
                    for kode_s in hasil_final['solusi']:
                        st.info(f"**{kode_s}**: {daftar_solusi[kode_s]}")
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("Gejala belum cukup spesifik. Silakan hubungi dokter Hematologi.")

# --- HALAMAN 3: INFO ---
elif nav == "📚 Edukasi":
    st.markdown('<div class="header-banner"><h1>EDUKASI HEMOFILIA</h1></div>', unsafe_allow_html=True)
    col_a, col_b = st.columns([1,1])
    with col_a:
        st.markdown("""
            <div class="custom-card">
                <h3 class="card-title">Apa itu Hemofilia?</h3>
                <p>Hemofilia adalah kondisi langka di mana darah tidak membeku secara normal karena kekurangan protein pembekuan darah (faktor VIII atau IX).</p>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.video("https://www.youtube.com/watch?v=1oW_fFm-v24")
