import streamlit as st

# --- KONFIGURASI TAMPILAN ---
st.set_page_config(page_title="HemoCheck Expert System", page_icon="🩸")

# Custom CSS untuk tampilan profesional
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #d90429;
        color: white;
        font-weight: bold;
    }
    .result-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #d90429;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASIS DATA (RULES) ---
rules = [
    {"gejala": ["Perdarahan", "Mimisan", "Memar", "Nyeri Sendi"], "diagnosa": "Hemofilia C", "keparahan": "Berat", "saran": "Segera konsultasi ke dokter spesialis Hematologi untuk penanganan darurat."},
    {"gejala": ["Perdarahan", "Mimisan", "Nyeri Sendi"], "diagnosa": "Hemofilia B", "keparahan": "Sedang", "saran": "Perlu pengawasan medis rutin dan hindari aktivitas fisik kontak."},
    {"gejala": ["Perdarahan", "Memar"], "diagnosa": "Hemofilia A", "keparahan": "Ringan", "saran": "Hindari aktivitas berat dan pantau perkembangan memar secara berkala."}
]

# --- UI WEBSITE ---
st.title("🩸 HemoCheck")
st.subheader("Sistem Pakar Diagnosa Hemofilia")
st.write("Silakan isi data dan gejala yang dirasakan untuk analisis awal.")

# Kolom Input Pasien
with st.expander("👤 Data Diri Pasien", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Lengkap")
        umur = st.number_input("Umur", min_value=0, max_value=100)
    with col2:
        jk = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Input Gejala
st.write("### 📝 Pilih Gejala yang Dialami")
g1 = st.checkbox("Perdarahan sulit berhenti")
g2 = st.checkbox("Sering Mimisan")
g3 = st.checkbox("Mudah Memar tanpa sebab")
g4 = st.checkbox("Nyeri atau Bengkak pada Sendi")

# Proses Diagnosa
gejala_user = []
if g1: gejala_user.append("Perdarahan")
if g2: gejala_user.append("Mimisan")
if g3: gejala_user.append("Memar")
if g4: gejala_user.append("Nyeri Sendi")

st.divider()

if st.button("Mulai Diagnosa Sekarang"):
    if not nama:
        st.error("Mohon isi nama terlebih dahulu!")
    else:
        # Logika Pencocokan Rule
        hasil = None
        for rule in rules:
            if all(g in gejala_user for g in rule["gejala"]):
                hasil = rule
                break
        
        # Tampilan Hasil yang Profesional
        st.balloons()
        st.markdown("### 📋 Hasil Analisis Medis")
        
        if hasil:
            st.markdown(f"""
            <div class="result-card">
                <p style='color: gray; margin-bottom: 0;'>Nama Pasien: {nama} ({umur} thn)</p>
                <h2 style='color: #d90429; margin-top: 0;'>{hasil['diagnosa']}</h2>
                <hr>
                <p><b>Tingkat Keparahan:</b> {hasil['keparahan']}</p>
                <p><b>Saran Tindakan:</b> {hasil['saran']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info(f"Halo {nama}, berdasarkan gejala yang dipilih, sistem tidak mendeteksi indikasi Hemofilia yang spesifik. Namun, jika keluhan berlanjut, tetaplah periksa ke dokter.")

st.caption("\n\nDisclaimer: Aplikasi ini hanya untuk tujuan edukasi dan skrining awal.")
