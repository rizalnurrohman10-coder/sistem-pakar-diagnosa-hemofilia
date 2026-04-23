import streamlit as st

# ================== KONFIGURASI ==================
st.set_page_config(page_title="Sistem Pakar Hemofilia", layout="centered")

# ================== SESSION ==================
if "login" not in st.session_state:
    st.session_state.login = False

# ================== DATA ==================
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
    "G15": "Riwayat keluarga hemofilia"
}

daftar_solusi = {
    "S01": "Penanganan lokal (tekan, kompres, perban)",
    "S02": "Obat antifibrinolitik",
    "S03": "Edukasi pencegahan",
    "S04": "Hindari cedera",
    "S05": "Terapi faktor pembekuan",
    "S06": "Fisioterapi",
    "S07": "Monitoring medis",
    "S08": "Hindari olahraga berat",
    "S09": "Terapi rutin faktor VIII/IX",
    "S10": "Penanganan darurat",
    "S11": "Rehabilitasi",
    "S12": "Hindari aspirin"
}

rules = [
    {"nama": "Hemofilia A (Berat)", "gejala": ["G01","G02","G04","G06","G07","G08","G09","G10","G12","G13","G14","G15"], "solusi": ["S09","S10","S11","S12"]},
    {"nama": "Hemofilia B (Sedang)", "gejala": ["G01","G02","G03","G04","G05","G06","G07","G08","G09","G10","G11","G15"], "solusi": ["S05","S06","S07","S08"]},
    {"nama": "Hemofilia C (Ringan)", "gejala": ["G01","G02","G03","G04","G05","G06","G09","G10","G11","G15"], "solusi": ["S01","S02","S03","S04"]}
]

# ================== LOGIN ==================
if not st.session_state.login:
    st.title("LOGIN SISTEM PAKAR HEMOFILIA")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("LOGIN"):
        if username == "admin" and password == "123":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Login gagal")

# ================== MENU ==================
else:
    menu = st.sidebar.selectbox("Menu", ["Diagnosis", "Hasil", "Logout"])

    # ================== DIAGNOSIS ==================
    if menu == "Diagnosis":
        st.title("PROSES DIAGNOSIS")

        nama = st.text_input("Nama")
        umur = st.number_input("Umur", 0, 120)

        st.subheader("Pilih Gejala:")
        gejala_terpilih = []

        for kode, gejala in daftar_gejala.items():
            if st.checkbox(gejala, key=kode):
                gejala_terpilih.append(kode)

        if st.button("PROSES"):
            st.session_state.nama = nama
            st.session_state.gejala = gejala_terpilih
            st.success("Silakan buka menu HASIL")

    # ================== HASIL ==================
    elif menu == "Hasil":
        st.title("HASIL DIAGNOSIS")

        gejala_terpilih = st.session_state.get("gejala", [])
        nama = st.session_state.get("nama", "-")

        hasil = None
        for r in rules:
            cocok = len([g for g in r["gejala"] if g in gejala_terpilih])
            if cocok >= len(r["gejala"]) * 0.5:
                hasil = r
                break

        if hasil:
            st.success(f"Diagnosis: {hasil['nama']}")
            st.write(f"Nama: {nama}")

            st.subheader("Gejala:")
            for g in gejala_terpilih:
                st.write("-", daftar_gejala[g])

            st.subheader("Solusi:")
            for s in hasil["solusi"]:
                st.write("-", daftar_solusi[s])
        else:
            st.error("Diagnosis tidak ditemukan")

    # ================== LOGOUT ==================
    elif menu == "Logout":
        st.session_state.login = False
        st.rerun()
