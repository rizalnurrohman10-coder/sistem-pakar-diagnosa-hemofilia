import streamlit as st

================== KONFIGURASI ==================

st.set_page_config(page_title="Sistem Pakar Hemofilia", layout="wide")

================== STYLE ==================

st.markdown("""

<style>
body {background-color: #f5f5f5;}

.main-box {
    background: linear-gradient(to bottom right, #ffffff, #ffe5e5);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}

.title {
    color: #c1121f;
    font-weight: 900;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #444;
    margin-bottom: 20px;
}

.stButton>button {
    background-color: #c1121f;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
    width: 100%;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 5px 10px rgba(0,0,0,0.05);
}
</style>""", unsafe_allow_html=True)

================== DATA ==================

daftar_gejala = { "G01": "Mimisan mendadak dan sulit berhenti", "G02": "Pendarahan gusi tanpa sebab yang jelas", "G03": "Luka kecil sulit berhenti berdarah", "G04": "Memar (hematoma) lama hilang", "G05": "Pendarahan setelah cabut gigi", "G06": "Pendarahan pasca operasi", "G07": "Pendarahan pada otot", "G08": "Pendarahan pada sendi", "G09": "Nyeri pada sendi", "G10": "Pembengkakan sendi", "G11": "Pendarahan akibat benturan ringan", "G12": "Pendarahan spontan", "G13": "Pendarahan pada saluran pencernaan", "G14": "Pendarahan di kepala", "G15": "Riwayat keluarga hemofilia" }

daftar_solusi = { "S01": "Penanganan lokal (tekan, kompres, perban)", "S02": "Obat antifibrinolitik", "S03": "Edukasi pencegahan", "S04": "Hindari cedera", "S05": "Terapi faktor pembekuan", "S06": "Fisioterapi", "S07": "Monitoring medis", "S08": "Hindari olahraga berat", "S09": "Terapi rutin faktor VIII/IX", "S10": "Penanganan darurat", "S11": "Rehabilitasi", "S12": "Hindari aspirin" }

rules = [ {"nama": "Hemofilia A (Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]}, {"nama": "Hemofilia B (Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]}, {"nama": "Hemofilia C (Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]} ]

================== NAVIGASI ==================

menu = st.sidebar.radio("Menu", ["Login", "Menu Utama", "Diagnosa", "Hasil"])

================== LOGIN ==================

if menu == "Login": st.markdown('<div class="main-box">', unsafe_allow_html=True) st.markdown('<h2 class="title">SISTEM PAKAR HEMOFILIA</h2>', unsafe_allow_html=True) st.markdown('<p class="subtitle">MENU LOGIN</p>', unsafe_allow_html=True)

user = st.text_input("Username")
pw = st.text_input("Password", type="password")

if st.button("LOGIN"):
    st.success("Login berhasil (simulasi)")

st.markdown('</div>', unsafe_allow_html=True)

================== MENU UTAMA ==================

elif menu == "Menu Utama": st.markdown('<div class="main-box">', unsafe_allow_html=True) st.markdown('<h2 class="title">MENU UTAMA</h2>', unsafe_allow_html=True) st.write("Selamat datang di sistem pakar diagnosa hemofilia.") st.markdown('</div>', unsafe_allow_html=True)

================== DIAGNOSA ==================

elif menu == "Diagnosa": st.markdown('<div class="main-box">', unsafe_allow_html=True) st.markdown('<h2 class="title">PROSES DIAGNOSIS</h2>', unsafe_allow_html=True)

nama = st.text_input("Nama")
umur = st.number_input("Umur", 0, 120)

st.write("### Pilih Gejala")
gejala_terpilih = []

col1, col2 = st.columns(2)
items = list(daftar_gejala.items())

for i, (kode, teks) in enumerate(items):
    if (col1 if i < 8 else col2).checkbox(teks):
        gejala_terpilih.append(kode)

if st.button("LIHAT HASIL"):
    st.session_state['nama'] = nama
    st.session_state['gejala'] = gejala_terpilih
    st.switch_page("Hasil")

st.markdown('</div>', unsafe_allow_html=True)

================== HASIL ==================

elif menu == "Hasil": st.markdown('<div class="main-box">', unsafe_allow_html=True) st.markdown('<h2 class="title">HASIL DIAGNOSIS</h2>', unsafe_allow_html=True)

gejala_terpilih = st.session_state.get('gejala', [])
nama = st.session_state.get('nama', '-')

hasil = None
for r in rules:
    cocok = len([g for g in r['gejala'] if g in gejala_terpilih])
    if cocok >= len(r['gejala']) * 0.5:
        hasil = r
        break

if hasil:
    st.success(f"Diagnosis: {hasil['nama']}")
    st.write(f"Pasien: {nama}")

    st.write("### Gejala Terpilih:")
    for g in gejala_terpilih:
        st.write(f"- {daftar_gejala[g]}")

    st.write("### Solusi:")
    for s in hasil['solusi']:
        st.info(daftar_solusi[s])
else:
    st.error("Tidak ditemukan diagnosis")

st.markdown('</div>', unsafe_allow_html=True)
