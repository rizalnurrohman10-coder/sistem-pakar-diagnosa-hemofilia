import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Diagnosis Hemofilia", page_icon="🩸", layout="centered")

# --- CSS TINGKAT LANJUT (CUSTOM UI) ---
st.markdown("""
    <style>
    /* Import Font Profesional */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&family=Roboto:wght@300;400;700&display=swap');

    /* Global Background: Sel Darah Merah */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(150, 0, 0, 0.6)), 
                    url('https://img.freepik.com/free-photo/red-blood-cells-streaming-vein_1048-6014.jpg');
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Roboto', sans-serif;
    }

    /* Sidebar - Terang agar teks Gelap terlihat */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.9);
        border-right: 4px solid #d90429;
    }
    [data-testid="stSidebar"] * {
        color: #1a1a1a !important; /* Teks Sidebar Gelap */
    }

    /* Header Banner - Merah Solid (Teks Putih) */
    .header-box {
        background: linear-gradient(135deg, #d90429 0%, #8d011f 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #ff4d6d;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
    }
    .header-box h1 {
        font-family: 'Montserrat', sans-serif;
        color: #ffffff !important; /* Teks Terang */
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0;
    }

    /* Card Glassmorphism - Latar Terang (Teks Gelap) */
    .glass-card {
        background: rgba(255, 255, 255, 0.92);
        padding: 30px;
        border-radius: 20px;
        border-left: 8px solid #d90429;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        margin-bottom: 25px;
    }
    .glass-card h3, .glass-card p, .glass-card li {
        color: #1a1a1a !important; /* Teks Dalam Card Gelap agar Jelas */
    }
    .card-label {
        font-family: 'Montserrat', sans-serif;
        color: #d90429 !important;
        font-weight: 700;
        border-bottom: 2px solid #d90429;
        margin-bottom: 15px;
        display: inline-block;
    }

    /* Button Styling - Merah (Teks Putih) */
    .stButton>button {
        background: #d90429;
        color: #ffffff !important; /* Teks Tombol Putih */
        border-radius: 10px;
        border: none;
        padding: 15px 25px;
        font-weight: 700;
        font-family: 'Montserrat', sans-serif;
        width: 100%;
        transition: 0.3s ease;
        box-shadow: 0 5px 15px rgba(217, 4, 41, 0.4);
    }
    .stButton>button:hover {
        background: #ef233c;
        transform: scale(1.02);
    }

    /* Checkbox & Text Input Label - Putih (Karena di luar card) */
    .stMarkdown p, label {
        color: #ffffff !important; 
        font-weight: 500;
    }
    
    /* Hasil Diagnosis Box */
    .result-container {
        background: #ffffff;
        border: 3px solid #d90429;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
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
    "G08": "Pendarahan pada sendi",
    "G09": "Nyeri pada sendi", 
    "G10": "Pembengkakan sendi",
    "G11": "Pendarahan akibat benturan ringan", 
    "G12": "Pendarahan spontan",
    "G13": "Pendarahan pada saluran pencernaan", 
    "G14": "Pendarahan di kepala",
    "G15": "Riwayat keluarga menderita Hemofilia"
}

daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)", 
    "S02": "Obat pendukung (antifibrinolitik)",
    "S03": "Edukasi pencegahan pendarahan", 
    "S04": "Kesadaran terhadap risiko cedera",
    "S05": "Terapi faktor pembekuan on-demand", 
    "S06": "Fisioterapi kesehatan sendi",
    "S07": "Monitoring medis berkala", 
    "S08": "Menghindari olahraga kontak berat",
    "S09": "Terapi profilaksis rutin (Faktor VIII/IX)", 
    "S10": "Penanganan darurat pendarahan internal",
    "S11": "Rehabilitasi jangka panjang", 
    "S12": "Dilarang konsumsi Aspirin/NSAID"
}

# --- SIDEBAR (MENU NAVIGASI) ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>MENU UTAMA</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2764/2764357.png", width=100)
    st.write("---")
    nav = st.radio("Pilih Menu:", ["Beranda", "Diagnosis Baru", "Informasi Penyakit"])
    st.write("---")
    st.caption("Developed by: M. Rizal Nurrohman")

# --- HALAMAN 1: BERANDA ---
if nav == "Beranda":
    st.markdown('<div class="header-box"><h1>Sistem Pakar Hemofilia</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <span class="card-label">SELAMAT DATANG</span>
            <h3>Halo, User!</h3>
            <p>Sistem ini dirancang untuk mendeteksi dini jenis Hemofilia Anda menggunakan metode <b>Forward Chaining</b>.</p>
            <p>Silakan klik menu <b>Diagnosis Baru</b> untuk memulai sesi konsultasi mandiri.</p>
        </div>
    """, unsafe_allow_html=True)

# --- HALAMAN 2: DIAGNOSIS ---
elif nav == "Diagnosis Baru":
    st.markdown('<div class="header-box"><h1>PROSES DIAGNOSIS</h1></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<span class="card-label">DATA PASIEN</span>', unsafe_allow_html=True)
    nama = st.text_input("Masukkan Nama Lengkap Anda:")
    umur = st.number_input("Masukkan Umur:", min_value=0, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### Pilih Gejala yang Anda Rasakan:")
    gejala_terpilih = []
    col1, col2 = st.columns(2)
    items = list(daftar_gejala.items())
    for i in range(len(items)):
        target_col = col1 if i < 8 else col2
        kode, teks = items[i]
        if target_col.checkbox(teks, key=kode):
            gejala_terpilih.append(kode)

    if st.button("LIHAT HASIL DIAGNOSIS"):
        if not nama or not gejala_terpilih:
            st.error("Lengkapi data nama dan pilih gejala terlebih dahulu!")
        else:
            # Aturan sesuai permintaan
            rules = [
                {"nama": "Hemofilia A (Berat)", "gejala": ["G01", "G02", "G04", "G06", "G07", "G08", "G09", "G10", "G12", "G13", "G14", "G15"], "solusi": ["S09", "S10", "S11", "S12"]},
                {"nama": "Hemofilia B (Sedang)", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G15"], "solusi": ["S05", "S06", "S07", "S08"]},
                {"nama": "Hemofilia C (Ringan)", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G09", "G10", "G11", "G15"], "solusi": ["S01", "S02", "S03", "S04"]}
            ]

            hasil = None
            for r in rules:
                matches = len([g for g in r["gejala"] if g in gejala_terpilih])
                if matches >= (len(r["gejala"]) * 0.5):
                    hasil = r
                    break

            if hasil:
                st.markdown(f"""
                    <div class="result-container">
                        <h2 style='color:#d90429;'>HASIL DIAGNOSIS</h2>
                        <h1 style='color:#1a1a1a;'>{hasil['nama']}</h1>
                        <hr style='border: 1px solid #d90429'>
                        <p style='color:#1a1a1a;'>Pasien <b>{nama}</b>, sistem mendeteksi indikasi kuat berdasarkan gejala Anda.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.write("### Solusi yang Disarankan:")
                for s in hasil["solusi"]:
                    st.info(f"**{s}**: {daftar_solusi[s]}")
            else:
                st.warning("Gejala tidak cukup spesifik untuk menentukan jenis Hemofilia.")

# --- HALAMAN 3: INFO ---
elif nav == "Informasi Penyakit":
    st.markdown('<div class="header-box"><h1>EDUKASI HEMOFILIA</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <span class="card-label">PENGERTIAN</span>
            <p>Hemofilia adalah gangguan pembekuan darah akibat kekurangan faktor pembekuan VIII, IX, atau XI.</p>
            <ul>
                <li><b>Hemofilia A:</b> Kekurangan Faktor VIII.</li>
                <li><b>Hemofilia B:</b> Kekurangan Faktor IX.</li>
                <li><b>Hemofilia C:</b> Kekurangan Faktor XI.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
