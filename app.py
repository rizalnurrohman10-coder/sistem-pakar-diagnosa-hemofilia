import streamlit as st 
import streamlit.components.v1 as components

#================== KONFIGURASI ==================#

st.set_page_config(page_title="Sistem Pakar Hemofilia", layout="wide")

#================== SESSION ==================#

if 'logged_in' not in st.session_state: st.session_state.logged_in = False

#================== STYLE ==================#

st.markdown("""

<style>
.stApp {
    background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)),
    url('https://images.unsplash.com/photo-1581594693702-fbdc51b2763b');
    background-size: cover;
    background-position: center;
}

.main-box {
    background: rgba(255,255,255,0.96);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    max-width: 520px;
    margin: auto;
}

.title {text-align:center; color:#c1121f; font-weight:900;}
.subtitle {text-align:center; color:#555; margin-bottom:20px;}

.step {display:flex; justify-content:space-between; margin-bottom:20px;}
.step div {
    flex:1; text-align:center; padding:8px;
    border-bottom:3px solid #ddd; font-size:12px; border-radius:5px;
}
.step .active {border-bottom:3px solid #c1121f; font-weight:bold; color:#c1121f;}

.stButton>button {
    background-color:#c1121f; color:white; font-weight:bold;
    border-radius:10px; padding:12px; width:100%; transition:0.3s;
}
.stButton>button:hover {background-color:#9b0d18; transform:scale(1.03);} 
</style>""", unsafe_allow_html=True)

#================== SVG ==================#

def icon_svg(name): icons = { "blood": """<svg width='60' height='60' viewBox='0 0 24 24' fill='#c1121f'><path d='M12 2C12 2 5 10 5 14a7 7 0 0014 0c0-4-7-12-7-12z'/></svg>""", "hospital": """<svg width='60' height='60' viewBox='0 0 24 24' fill='#c1121f'><path d='M3 22V2h18v20h-6v-6H9v6H3z'/></svg>""", "lab": """<svg width='60' height='60' viewBox='0 0 24 24' fill='#c1121f'><path d='M9 2v2l-4 8a5 5 0 0010 0l-4-8V2H9z'/></svg>""", "result": """<svg width='60' height='60' viewBox='0 0 24 24' fill='#c1121f'><path d='M4 2h14v20l-7-3-7 3V2z'/></svg>""" } return icons.get(name, "")

#================== DATA (TETAP) ==================#

daftar_gejala = { "G01": "Mimisan mendadak dan sulit berhenti", "G02": "Pendarahan gusi tanpa sebab yang jelas", "G03": "Luka kecil sulit berhenti berdarah", "G04": "Memar (hematoma) lama hilang", "G05": "Pendarahan setelah cabut gigi", "G06": "Pendarahan pasca operasi", "G07": "Pendarahan pada otot", "G08": "Pendarahan pada sendi", "G09": "Nyeri pada sendi", "G10": "Pembengkakan sendi", "G11": "Pendarahan akibat benturan ringan", "G12": "Pendarahan spontan", "G13": "Pendarahan pada saluran pencernaan", "G14": "Pendarahan di kepala", "G15": "Riwayat keluarga hemofilia" }

daftar_solusi = { "S01": "Penanganan lokal (tekan, kompres, perban)", "S02": "Obat antifibrinolitik", "S03": "Edukasi pencegahan", "S04": "Hindari cedera", "S05": "Terapi faktor pembekuan", "S06": "Fisioterapi", "S07": "Monitoring medis", "S08": "Hindari olahraga berat", "S09": "Terapi rutin faktor VIII/IX", "S10": "Penanganan darurat", "S11": "Rehabilitasi", "S12": "Hindari aspirin" }

rules = [ {"nama": "Hemofilia A (Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]}, {"nama": "Hemofilia B (Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]}, {"nama": "Hemofilia C (Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]} ]

#================== MENU ==================#

if not st.session_state.logged_in: menu = st.sidebar.radio("Menu", ["Login"]) else: menu = st.sidebar.radio("Menu", ["Menu Utama", "Diagnosa", "Hasil", "Logout"])

#================== LOGIN ==================#

if menu == "Login": st.markdown('<div class="main-box">', unsafe_allow_html=True) components.html(icon_svg("blood"), height=70) st.markdown('<h2 class="title">SISTEM PAKAR HEMOFILIA</h2>', unsafe_allow_html=True) st.markdown('<p class="subtitle">Silakan login</p>', unsafe_allow_html=True)

user = st.text_input("Username")
pw = st.text_input("Password", type="password")

if st.button("LOGIN"):
    if user == "admin" and pw == "123":
        st.session_state.logged_in = True
        st.rerun()
    else:
        st.error("Login gagal")

st.markdown('</div>', unsafe_allow_html=True)

#================== MENU UTAMA ==================#

elif menu == "Menu Utama": st.markdown('<div class="main-box">', unsafe_allow_html=True) components.html(icon_svg("hospital"), height=70) st.markdown('<h2 class="title">MENU UTAMA</h2>', unsafe_allow_html=True) st.write("Selamat datang di sistem pakar diagnosa hemofilia.") st.markdown('</div>', unsafe_allow_html=True)

#================== DIAGNOSA ==================#

elif menu == "Diagnosa": st.markdown('<div class="main-box">', unsafe_allow_html=True) components.html(icon_svg("lab"), height=70)

st.markdown("""
<div class='step'>
    <div class='active'>1. Diagnosa</div>
    <div>2. Proses</div>
    <div>3. Hasil</div>
</div>
""", unsafe_allow_html=True)

nama = st.text_input("Nama")
umur = st.number_input("Umur", 0, 120)

gejala_terpilih = []
col1, col2 = st.columns(2)
items = list(daftar_gejala.items())

for i, (kode, teks) in enumerate(items):
    if (col1 if i < 8 else col2).checkbox(teks, key=kode):
        gejala_terpilih.append(kode)

if st.button("LIHAT HASIL"):
    st.session_state['nama'] = nama
    st.session_state['gejala'] = gejala_terpilih
    st.success("Silakan buka menu HASIL")

st.markdown('</div>', unsafe_allow_html=True)

#================== HASIL ==================#

elif menu == "Hasil": st.markdown('<div class="main-box">', unsafe_allow_html=True) components.html(icon_svg("result"), height=70)

st.markdown("""
<div class='step'>
    <div>1. Diagnosa</div>
    <div>2. Proses</div>
    <div class='active'>3. Hasil</div>
</div>
""", unsafe_allow_html=True)

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

#================== LOGOUT ==================#

elif menu == "Logout": st.session_state.logged_in = False st.rerun()
