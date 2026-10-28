import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from utils import quiz

st.title("🍎 ບົດທີ 3: ການຕົກຕາມລຳພັງ")

st.header("🎯 ຈຸດປະສົງການຮຽນ")
st.markdown("""
- ອະທິບາຍການຕົກຕາມລຳພັງ ແລະ ຄວາມເລັ່ງໂນ້ມຖ່ວງ g
- ຄິດໄລ່ເວລາຕົກ ແລະ ຄວາມໄວກ່ອນກະທົບພື້ນ
- ປຽບທຽບການຕົກຢູ່ດາວຕ່າງໆ
""")

st.header("📖 ທິດສະດີ")
st.write("ການຕົກຕາມລຳພັງ ຄື ການເຄື່ອນທີ່ທີ່ມີ **ແຮງໂນ້ມຖ່ວງ** ເປັນແຮງດຽວ (ບໍ່ນັບແຮງຕ້ານອາກາດ) ຄວາມເລັ່ງ = g")
st.latex(r"v = v_0 + g t")
st.latex(r"h = h_0 - v_0 t - \tfrac{1}{2} g t^2")
st.latex(r"t_{fall} = \sqrt{\frac{2h_0}{g}} \quad (v_0 = 0)")
st.latex(r"v_{final} = \sqrt{2 g h_0}")
st.info("ເວລາຕົກບໍ່ຂຶ້ນກັບມວນ! ວັດຖຸໜັກ ແລະ ເບົາ ຕົກເຖິງພື້ນພ້ອມກັນ (ຖ້າບໍ່ມີອາກາດ)")

planets = {"ໂລກ (9.8)": 9.8, "ດວງຈັນ (1.62)": 1.62, "ດາວອັງຄານ (3.71)": 3.71, "ດາວພະຫັດ (24.8)": 24.8}

st.sidebar.header("⚙️ ປັບຄ່າ")
planet = st.sidebar.selectbox("ສະຖານທີ່ (g ເປັນ m/s²)", list(planets.keys()))
g = planets[planet]
h0 = st.sidebar.slider("ຄວາມສູງເລີ່ມຕົ້ນ h₀ (m)", 1.0, 200.0, 50.0)
v0 = st.sidebar.slider("ຄວາມໄວຕົ້ນລົງລຸ່ມ v₀ (m/s)", 0.0, 30.0, 0.0)

t_fall = (-v0 + np.sqrt(v0**2 + 2 * g * h0)) / g
v_final = v0 + g * t_fall

st.header("🔬 ການຈຳລອງ")
st.write("🤔 **ທຳນາຍ:** ຖ້າຕົກຢູ່ດວງຈັນ ຈະໃຊ້ເວລາຕົກນານກວ່າ ຫຼື ໄວກວ່າໂລກ?")

c1, c2, c3 = st.columns(3)
c1.metric("ເວລາຕົກທັງໝົດ", f"{t_fall:.2f} s")
c2.metric("ຄວາມໄວກ່ອນກະທົບພື້ນ", f"{v_final:.2f} m/s")
c3.metric("ຄວາມເລັ່ງໂນ້ມຖ່ວງ g", f"{g} m/s²")

t_now = st.slider("ເວລາປັດຈຸບັນ t (s)", 0.0, float(round(t_fall, 2)), 0.0, 0.01)
h_now = max(h0 - v0 * t_now - 0.5 * g * t_now**2, 0.0)
v_now = v0 + g * t_now

left, right = st.columns([1, 3])
with left:
    figb, axb = plt.subplots(figsize=(2.2, 4.5))
    axb.axhline(0, color="saddlebrown", lw=4)
    axb.plot(0, h_now, "o", ms=22, color="tab:red")
    axb.set_xlim(-1, 1)
    axb.set_ylim(-h0 * 0.03, h0 * 1.08)
    axb.set_xticks([])
    axb.set_ylabel("height h (m)")
    st.pyplot(figb)
    st.caption(f"h = {h_now:.2f} m, v = {v_now:.2f} m/s")
with right:
    t = np.linspace(0, t_fall, 200)
    h = h0 - v0 * t - 0.5 * g * t**2
    v = v0 + g * t
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].plot(t, h, color="tab:blue")
    ax[0].plot(t_now, h_now, "ro")
    ax[0].set(title="Height - Time", xlabel="t (s)", ylabel="h (m)")
    ax[1].plot(t, v, color="tab:red")
    ax[1].plot(t_now, v_now, "ko")
    ax[1].set(title="Speed - Time", xlabel="t (s)", ylabel="v (m/s)")
    for a in ax:
        a.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

st.header("✏️ ຕົວຢ່າງໂຈດ")
with st.expander("ປ່ອຍກ້ອນຫີນຈາກສະພານສູງ 80 m (g = 10 m/s²) ຕົກໃຊ້ເວລາເທົ່າໃດ?"):
    st.latex(r"t = \sqrt{\frac{2 \times 80}{10}} = 4 \text{ s}")

st.header("📝 ທົດສອບຄວາມເຂົ້າໃຈ")
quiz("f1", "ປ່ອຍວັດຖຸຈາກຫຼັງຄາສູງ 45 m (ໃຊ້ g = 10 m/s²) ໃຊ້ເວລາຕົກເທົ່າໃດ?",
     ["2 s", "3 s", "4.5 s", "9 s"], 1, "t = √(2h/g) = √(90/10) = 3 s")
