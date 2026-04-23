import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem Pakar Diagnosis Hemofilia", page_icon="🩸", layout="centered")

# --- CSS CUSTOM: FOKUS KONTRAS (MERAH-PUTIH) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Latar Belakang Putih agar Teks Jelas */
    .stApp {
        background-color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Abu Terang */
    [data-testid="stSidebar"] {
        background-color: #fcfcfc;
        border-right: 2px solid #d90429;
    }

    /* Banner Judul Merah Solid (Teks Putih) */
    .header-banner {
        background-color: #d90429;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 30px;
    }
    .header-banner h1 {
        color: #ffffff !important;
        font-weight: 900;
        margin: 0;
        text-transform: uppercase;
        font-size: 22px;
    }

    /* Card Putih Bersih (Teks Hitam) */
    .info-card {
        background-color: #ffffff;
        padding: 20px;
        border: 1px solid #eeeeee;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Warna Teks */
    h3 { color: #d90429 !important; font-weight: 700; }
    p, li, label { color: #000000 !important; font-weight: 500; }

    /* Tombol Merah */
    .stButton>button {
        background-color: #d90429;
        color: white !important;
        border-radius: 6px;
        border: none;
        padding: 10px;
        font-weight: 700;
        width: 100%;
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
    "S12": "Hindari konsumsi Aspirin/NSAID"
}

# --- MENU UTAMA ---
with st.sidebar:
    st.markdown("### **NAVIGASI**")
    nav = st.radio("Pilih Halaman:", ["Beranda", "Proses Diagnosis", "Informasi"])
    st.write("---")
    st.caption("Pakar: M. Rizal Nurrohman")

# --- KONTEN ---
if nav == "Beranda":
    st.markdown('<div class="header-banner"><h1>SISTEM PAKAR DIAGNOSA HEMOFILIA</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            <h3>Informasi Sistem</h3>
            <p>Sistem pakar ini dirancang untuk mendiagnosa tingkat keparahan hemofilia berdasarkan gejala yang dialami pengguna.</p>
            <p><b>Klasifikasi Penyakit:</b></p>
            <ul>
                <li><b>Hemofilia A:</b> Tingkat Berat</li>
                <li><b>Hemofilia B:</b> Tingkat Sedang</li>
                <li><b>Hemofilia C:</b> Tingkat Ringan</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

elif nav == "Proses Diagnosis":
    st.markdown('<div class="header-banner"><h1>PROSES DIAGNOSIS</h1></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    nama = st.text_input("Nama Lengkap:")
    umur = st.number_input("Umur:", min_value=0, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### Pilih Gejala yang Dirasakan:")
    gejala_terpilih = []
    c1, c2 = st.columns(2)
    items = list(daftar_gejala.items())
    for i in range(len(items)):
        target_col = c1 if i < 8 else c2
        kode, teks = items[i]
        if target_col.checkbox(teks, key=kode):
            gejala_terpilih.append(kode)

    if st.button("ANALISIS HASIL"):
        if not nama or not gejala_terpilih:
            st.warning("Mohon lengkapi nama dan centang gejala.")
        else:
            rules = [
                {"nama": "Hemofilia A (Berat)", "gejala": ["G01", "G02", "G04", "G06", "G07", "G08", "G09", "G10", "G12", "G13", "G14", "G15"], "solusi": ["S09", "S10", "S11", "S12"]},
                {"nama": "Hemofilia B (Sedang)", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10", "G11", "G15"], "solusi": ["S05", "S06", "S07", "S08"]},
                {"nama": "Hemofilia C (Ringan)", "gejala": ["G01", "G02", "G03", "G04", "G05", "G06", "G09", "G10", "G11", "G15"], "solusi": ["S01", "S02", "S03", "S04"]}
            ]
            
            hasil = None
            for r in rules:
                cocok = len([g for g in r["gejala"] if g in gejala_terpilih])
                if cocok >= (len(r["gejala"]) * 0.5):
                    hasil = r
                    break
            
            if hasil:
                st.success(f"### Hasil: {hasil['nama']}")
                st.write(f"Pasien: **{nama}**")
                st.write("---")
                st.write("**Solusi:**")
                for s in hasil["solusi"]:
                    st.info(f"{s}: {daftar_solusi[s]}")
            else:
                st.error("Diagnosis tidak ditemukan secara spesifik.")

elif nav == "Informasi":
    st.markdown('<div class="header-banner"><h1>INFORMASI PENYAKIT</h1></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="info-card">
            <h3>Tentang Hemofilia</h3>
            <p>Hemofilia adalah gangguan perdarahan yang disebabkan oleh kekurangan faktor pembekuan darah tertentu. Kondisi ini memerlukan penanganan medis yang tepat sesuai tingkat keparahannya.</p>
        </div>
    """, unsafe_allow_html=True)
