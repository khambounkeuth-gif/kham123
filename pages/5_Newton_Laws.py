import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from utils import quiz

st.title("🍏 ບົດທີ 5: ກົດຂອງນິວຕັນ")

st.header("🎯 ຈຸດປະສົງການຮຽນ")
st.markdown("""
- ບອກ ແລະ ອະທິບາຍກົດຂໍ້ທີ 1, 2 ແລະ 3 ຂອງນິວຕັນ
- ໃຊ້ ΣF = ma ແກ້ໂຈດ ລວມທັງແຮງສຽດທານ
""")

tab1, tab2, tab3 = st.tabs(["ກົດຂໍ້ 1 (ແຮງເຉື່ອຍ)", "ກົດຂໍ້ 2 (ΣF = ma)", "ກົດຂໍ້ 3 (ແຮງກິລິຍາ-ປະຕິກິລິຍາ)"])

# ---------------- ກົດຂໍ້ 1 ----------------
with tab1:
    st.subheader("ກົດແຫ່ງແຮງເຉື່ອຍ")
    st.write("ວັດຖຸຈະຮັກສາສະພາບ **ຢຸດນິ້ງ** ຫຼື **ເຄື່ອນທີ່ດ້ວຍຄວາມໄວຄົງທີ່** ຖ້າແຮງລັບທີ່ມາກະທຳ = 0")
    st.latex(r"\sum F = 0 \;\Rightarrow\; a = 0")
    st.markdown("ຕົວຢ່າງ: ຜູ້ໂດຍສານຕົວໂຍກໄປໜ້າເມື່ອລົດເບຣກກະທັນຫັນ ເພາະຮ່າງກາຍຍັງຢາກເຄື່ອນທີ່ຕໍ່")
    v1 = st.slider("ຄວາມໄວຂອງວັດຖຸເທິງນ້ຳແຂງລື່ນ (m/s)", 0.0, 10.0, 3.0, key="n1_v")
    st.write(f"ເມື່ອບໍ່ມີແຮງຕ້ານ ວັດຖຸຈະໄປດ້ວຍ {v1:.1f} m/s ຕະຫຼອດໄປ: ໃນ 5 s ຈະໄປໄດ້ **{v1*5:.1f} m**")

# ---------------- ກົດຂໍ້ 2 ----------------
with tab2:
    st.subheader("ກົດແຫ່ງຄວາມເລັ່ງ")
    st.latex(r"\sum F = m a \quad\Rightarrow\quad a = \frac{F - f}{m},\quad f = \mu m g")
    st.markdown("""
- ແຮງລັບໃຫຍ່ຂຶ້ນ → ຄວາມເລັ່ງຫຼາຍຂຶ້ນ
- ມວນຫຼາຍຂຶ້ນ → ຄວາມເລັ່ງນ້ອຍລົງ
""")
    c_a, c_b, c_c = st.columns(3)
    m = c_a.slider("ມວນ m (kg)", 1.0, 50.0, 10.0, key="n2_m")
    F = c_b.slider("ແຮງດຶງ F (N)", 0.0, 200.0, 50.0, key="n2_F")
    mu = c_c.slider("ສຳປະສິດສຽດທານ μ", 0.0, 1.0, 0.2, 0.05, key="n2_mu")
    g = 9.8
    t_max = 10.0

    f_max = mu * m * g
    if F <= f_max:
        a = 0.0
        st.warning(f"ແຮງດຶງ ({F:.1f} N) ບໍ່ເກີນແຮງສຽດທານສູງສຸດ ({f_max:.1f} N): ວັດຖຸ **ບໍ່ເຄື່ອນທີ່**")
    else:
        a = (F - f_max) / m
    net = max(F - f_max, 0.0)

    c1, c2, c3 = st.columns(3)
    c1.metric("ແຮງສຽດທານ f", f"{f_max:.1f} N")
    c2.metric("ແຮງລັບ ΣF", f"{net:.1f} N")
    c3.metric("ຄວາມເລັ່ງ a", f"{a:.2f} m/s²")

    t = np.linspace(0, t_max, 200)
    v = a * t
    x = 0.5 * a * t**2
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
    ax[0].plot(t, v, color="tab:red")
    ax[0].set(title="Velocity - Time", xlabel="t (s)", ylabel="v (m/s)")
    ax[1].plot(t, x, color="tab:blue")
    ax[1].set(title="Position - Time", xlabel="t (s)", ylabel="x (m)")
    for p in ax:
        p.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

    with st.expander("✏️ ຕົວຢ່າງໂຈດ"):
        st.write("ກ່ອງ 5 kg ຖືກດຶງດ້ວຍແຮງ 30 N ເທິງພື້ນລື່ນ (f = 0) ຄວາມເລັ່ງເທົ່າໃດ?")
        st.latex(r"a = \frac{30}{5} = 6 \text{ m/s}^2")

# ---------------- ກົດຂໍ້ 3 ----------------
with tab3:
    st.subheader("ກົດແຮງກິລິຍາ - ປະຕິກິລິຍາ")
    st.write("ທຸກແຮງກິລິຍາມີແຮງປະຕິກິລິຍາ **ເທົ່າກັນ ແຕ່ທິດກົງກັນຂ້າມ** ແລະ ກະທຳຕໍ່ **ວັດຖຸຄົນລະກ້ອນ**")
    st.latex(r"F_{A \to B} = -F_{B \to A}")
    st.markdown("**ການທົດລອງ:** ນັກສະເກັດສອງຄົນຢືນເທິງນ້ຳແຂງ ຄົນໜຶ່ງຍູ້ອີກຄົນ")
    d1, d2, d3 = st.columns(3)
    m1 = d1.slider("ມວນຄົນ A (kg)", 30.0, 100.0, 50.0, key="n3_m1")
    m2 = d2.slider("ມວນຄົນ B (kg)", 30.0, 100.0, 80.0, key="n3_m2")
    Fp = d3.slider("ແຮງຍູ້ (N)", 10.0, 200.0, 80.0, key="n3_F")
    a1, a2 = Fp / m1, Fp / m2
    e1, e2, e3 = st.columns(3)
    e1.metric("ແຮງທີ່ A ຍູ້ B", f"{Fp:.0f} N")
    e2.metric("ແຮງທີ່ B ຍູ້ A", f"{Fp:.0f} N")
    e3.metric("ອັດຕາສ່ວນ a_A : a_B", f"{a1/a2:.2f}")
    st.write(f"ຄວາມເລັ່ງຂອງ A = **{a1:.2f} m/s²**, ຄວາມເລັ່ງຂອງ B = **{a2:.2f} m/s²** (ແຮງເທົ່າກັນ ແຕ່ຄົນເບົາກວ່າເລັ່ງຫຼາຍກວ່າ)")

st.header("📝 ທົດສອບຄວາມເຂົ້າໃຈ")
quiz("n_q1", "ວັດຖຸ 5 kg ມີແຮງລັບ 20 N ຄວາມເລັ່ງເທົ່າໃດ?",
     ["0.25 m/s²", "4 m/s²", "15 m/s²", "100 m/s²"], 1, "a = ΣF / m = 20 / 5 = 4 m/s²")
quiz("n_q2", "ລົດບັນທຸກຕຳລົດນ້ອຍ ແຮງທີ່ລົດບັນທຸກກະທຳຕໍ່ລົດນ້ອຍ ເປັນແນວໃດກັບແຮງທີ່ລົດນ້ອຍກະທຳຕໍ່ລົດບັນທຸກ?",
     ["ໃຫຍ່ກວ່າ", "ນ້ອຍກວ່າ", "ເທົ່າກັນ", "ຂຶ້ນກັບຄວາມໄວ"], 2, "ກົດຂໍ້ 3: ແຮງກິລິຍາ ແລະ ປະຕິກິລິຍາ ເທົ່າກັນສະເໝີ")
