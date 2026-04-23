import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Diagnosis Hemofilia", page_icon="🩸", layout="wide")

# --- CSS CUSTOM UNTUK VISUAL KOMPLEKS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    /* Background Utama dengan Gambar Sel Darah */
    .stApp {
        background: linear-gradient(rgba(141, 1, 31, 0.8), rgba(141, 1, 31, 0.95)), 
                    url('https://www.transparenttextures.com/patterns/carbon-fibre.png'),
                    url('https://img.freepik.com/free-photo/red-blood-cells-streaming-vein_1048-6014.jpg');
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.95);
        border-right: 5px solid #d90429;
    }
    
    /* Banner Header Atas */
    .header-banner {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    .header-banner h1 {
        font-weight: 800;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        color: #ffffff;
    }

    /* Card Styling (Glassmorphism) */
    .custom-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 35px;
        border-radius: 25px;
        border: none;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        color: #333;
    }

    /* Label Header pada Card */
    .card-title {
        color: #d90429;
        font-weight: 800;
        border-bottom: 3px solid #d90429;
        padding-bottom: 15px;
        margin-bottom: 25px;
        text-transform: uppercase;
        font-size: 1.5rem;
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #d90429, #ef233c);
        color: white;
        border-radius: 12px;
        width: 100%;
        border: none;
        padding: 15px;
        font-weight: 700;
        font-size: 1.1rem;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(217, 4, 41, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(217, 4, 41, 0.6);
        color: white;
    }

    /* Warna Teks Input */
    label, p, li {
        color: #444;
        font-weight: 500;
    }

    /* Hasil Diagnosis Card */
    .result-box {
        background: #fff3f3;
        border-left: 10px solid #d90429;
        padding: 20px;
        border-radius: 10px;
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
    "S12": "Menghindari obat aspirin dan NSAID"
}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color:#d90429; text-align:center;'>HEMOSMART AI</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2764/2764357.png", width=120)
    st.write("---")
    nav = st.radio("MENU NAVIGASI", ["🏠 Beranda", "🩺 Diagnosis Baru", "📚 Edukasi Pasien"])
    st.write("---")
    st.caption("Pakar: M. Rizal Nurrohman")

# --- HALAMAN 1: BERANDA ---
if nav == "🏠 Beranda":
    st.markdown('<div class="header-banner"><h1>SISTEM PAKAR DIAGNOSIS HEMOFILIA</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image("https://img.freepik.com/free-vector/blood-donation-concept-illustration_114360-5554.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""
            <div class="custom-card">
                <h3 class="card-title">Selamat Datang</h3>
                <p>Gunakan sistem ini untuk melakukan deteksi dini terhadap kondisi kesehatan Anda. 
                Sistem kami menggunakan algoritma <b>Forward Chaining</b> untuk mencocokkan gejala klinis dengan database medis.</p>
                <p><b>Cara Penggunaan:</b></p>
                <ol>
                    <li>Pilih menu <b>Diagnosis Baru</b>.</li>
                    <li>Isi biodata Anda.</li>
                    <li>Centang gejala yang Anda rasakan.</li>
                    <li>Klik tombol Analisis untuk melihat hasil dan solusi.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

# --- HALAMAN 2: DIAGNOSA ---
elif nav == "🩺 Diagnosis Baru":
    st.markdown('<div class="header-banner"><h1>PROSES DIAGNOSIS: CHECKLIST GEJALA</h1></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">Biodata Pasien</h3>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        nama = c1.text_input("Nama Lengkap")
        umur = c2.number_input("Umur (Tahun)", min_value=0, step=1)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">Daftar Gejala Yang Dialami</h3>', unsafe_allow_html=True)
        
        gejala_terpilih = []
        col_g1, col_g2 = st.columns(2)
        items = list(daftar_gejala.items())
        for i in range(len(items)):
            target_col = col_g1 if i < 8 else col_g2
            kode, teks = items[i]
            if target_col.checkbox(f"{teks}", key=kode):
                gejala_terpilih.append(kode)
        
        st.write("---")
        if st.button("LIHAT HASIL ANALISIS"):
            if not nama or not gejala_terpilih:
                st.error("Silakan lengkapi Nama dan minimal pilih 1 gejala!")
            else:
                # Logika Diagnosis Sesuai Permintaan Baru
                rules = [
                    {"nama": "Hemofilia A (Berat)", "gejala": ["G01", "G02", "G04", "G06", "G07", "G08", "G09", "G10", "G12", "G13", "G14", "G15"], "solusi": ["S09", "S10", "S11", "S12"]},
                    {"nama": "Hemofilia B (Sedang)", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G15"], "solusi": ["S05", "S06", "S07", "S08"]},
                    {"nama": "Hemofilia C (Ringan)", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G09", "G10", "G11", "G15"], "solusi": ["S01", "S02", "S03", "S04"]}
                ]

                hasil_final = None
                for rule in rules: # Cek urutan prioritas
                    match_count = len([g for g in rule["gejala"] if g in gejala_terpilih])
                    if match_count >= (len(rule["gejala"]) * 0.5):
                        hasil_final = rule
                        break

                if hasil_final:
                    st.markdown(f"""
                        <div class="result-box">
                            <h2 style='color:#d90429;'>HASIL DIAGNOSIS:</h2>
                            <h1 style='color:#d90429;'>KEMUNGKINAN BESAR {hasil_final['nama'].upper()}</h1>
                            <p>Pasien: <b>{nama}</b> | Umur: <b>{umur} Tahun</b></p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown('<h3 style="color:white;">Solusi & Saran Lanjutan:</h3>', unsafe_allow_html=True)
                    for kode_s in hasil_final['solusi']:
                        st.success(f"**{kode_s}**: {daftar_solusi[kode_s]}")
                else:
                    st.warning("Gejala tidak cukup kuat untuk didiagnosis secara spesifik.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- HALAMAN 3: EDUKASI ---
elif nav == "📚 Edukasi Pasien":
    st.markdown('<div class="header-banner"><h1>INFORMASI EDUKASI HEMOFILIA</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="custom-card">
            <h3 class="card-title">Mengenal Jenis Hemofilia</h3>
            <p>Berdasarkan tingkat keparahan dan jenis faktor pembekuan yang hilang:</p>
            <ul>
                <li><b>Hemofilia A:</b> Kekurangan Faktor VIII. Jenis yang paling umum.</li>
                <li><b>Hemofilia B:</b> Kekurangan Faktor IX (Christmas Disease).</li>
                <li><b>Hemofilia C:</b> Kekurangan Faktor XI. Biasanya gejalanya paling ringan.</li>
            </ul>
            <hr>
            <h3 class="card-title">Saran Pencegahan</h3>
            <ul>
                <li>Hindari olahraga kontak fisik (Sepak bola, Karate, dll).</li>
                <li>Gunakan sikat gigi yang lembut.</li>
                <li>Selalu sedia pertolongan pertama pendarahan di rumah.</li>
                <li>Lakukan kontrol rutin ke dokter ahli hematologi.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
