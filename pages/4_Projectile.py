import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from utils import quiz

st.title("🎯 ບົດທີ 4: ການເຄື່ອນທີ່ແບບໂປຣເຈັກໄທລ໌")

st.header("🎯 ຈຸດປະສົງການຮຽນ")
st.markdown("""
- ແຍກການເຄື່ອນທີ່ເປັນແນວນອນ ແລະ ແນວຕັ້ງ
- ຄິດໄລ່ເວລາບິນ, ຄວາມສູງສູງສຸດ ແລະ ໄລຍະຕົກ
- ເຂົ້າໃຈຜົນຂອງມຸມຍິງຕໍ່ໄລຍະໄປໄກ
""")

st.header("📖 ທິດສະດີ")
st.write("ວັດຖຸທີ່ຖືກຖິ້ມເປັນມຸມ θ ເຄື່ອນທີ່ສອງທິດ **ແຍກກັນ**:")
st.latex(r"v_{0x} = v_0\cos\theta,\quad v_{0y} = v_0\sin\theta")
st.latex(r"x = v_{0x}\, t")
st.latex(r"y = h_0 + v_{0y}\, t - \tfrac{1}{2} g t^2")
st.latex(r"R = \frac{v_0^2 \sin 2\theta}{g} \quad (h_0 = 0)")
st.markdown("""
- ແນວນອນ: ຄວາມໄວຄົງທີ່ (ບໍ່ມີຄວາມເລັ່ງ)
- ແນວຕັ້ງ: ຄວາມເລັ່ງ = −g (ຄືການຕົກຕາມລຳພັງ)
""")

st.sidebar.header("⚙️ ປັບຄ່າ")
v0 = st.sidebar.slider("ຄວາມໄວຕົ້ນ v₀ (m/s)", 1.0, 60.0, 20.0)
angle = st.sidebar.slider("ມຸມຍິງ θ (ອົງສາ)", 0, 90, 45)
h0 = st.sidebar.slider("ຄວາມສູງເລີ່ມຕົ້ນ h₀ (m)", 0.0, 50.0, 0.0)
g = st.sidebar.slider("ຄວາມເລັ່ງໂນ້ມຖ່ວງ g (m/s²)", 1.0, 25.0, 9.8)

th = np.radians(angle)
v0x, v0y = v0 * np.cos(th), v0 * np.sin(th)
T = (v0y + np.sqrt(v0y**2 + 2 * g * h0)) / g
R = v0x * T
H = h0 + (v0y**2 / (2 * g) if v0y > 0 else 0)

st.header("🔬 ການຈຳລອງ")
st.write("🤔 **ທຳນາຍ:** ມຸມໃດຈະຍິງໄປໄດ້ໄກທີ່ສຸດ? ລອງປັບມຸມເພື່ອກວດ!")

c1, c2, c3 = st.columns(3)
c1.metric("ເວລາບິນ", f"{T:.2f} s")
c2.metric("ໄລຍະຕົກ (R)", f"{R:.2f} m")
c3.metric("ຄວາມສູງສູງສຸດ (H)", f"{H:.2f} m")

t_now = st.slider("ເວລາປັດຈຸບັນ t (s)", 0.0, float(round(T, 2)), 0.0, 0.01)

t = np.linspace(0, T, 300)
x = v0x * t
y = h0 + v0y * t - 0.5 * g * t**2
x_now = v0x * t_now
y_now = max(h0 + v0y * t_now - 0.5 * g * t_now**2, 0.0)
vy_now = v0y - g * t_now

fig, ax = plt.subplots(figsize=(10, 4.2))
ax.plot(x, y, "--", color="tab:blue", label="trajectory")
ax.plot(x_now, y_now, "o", ms=14, color="tab:red")
ax.axhline(0, color="saddlebrown", lw=3)
ax.set(xlabel="x (m)", ylabel="y (m)", title="Projectile Trajectory")
ax.set_xlim(-1, max(R, 1) * 1.1)
ax.set_ylim(-0.05 * max(H, 1), max(H, 1) * 1.2)
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.caption(f"ຕອນນີ້: x = {x_now:.2f} m, y = {y_now:.2f} m, vₓ = {v0x:.2f} m/s, v_y = {vy_now:.2f} m/s")

with st.expander("📊 ເບິ່ງຜົນຂອງມຸມຕໍ່ໄລຍະຕົກ (ເປັນຄ່າ v₀, h₀ ປັດຈຸບັນ)"):
    angs = np.arange(1, 90)
    ths = np.radians(angs)
    vy = v0 * np.sin(ths)
    Ts = (vy + np.sqrt(vy**2 + 2 * g * h0)) / g
    Rs = v0 * np.cos(ths) * Ts
    best = int(angs[np.argmax(Rs)])
    f2, a2 = plt.subplots(figsize=(8, 3.5))
    a2.plot(angs, Rs, color="tab:green")
    a2.plot(angle if 0 < angle < 90 else best, R if 0 < angle < 90 else Rs.max(), "ro")
    a2.set(xlabel="angle (deg)", ylabel="Range (m)", title="Range vs Launch Angle")
    a2.grid(True)
    st.pyplot(f2)
    st.write(f"ມຸມທີ່ໄດ້ໄລຍະໄກສຸດ ≈ **{best}°** (ຖ້າ h₀ = 0 ຈະເປັນ 45° ພໍດີ)")

st.header("✏️ ຕົວຢ່າງໂຈດ")
with st.expander("ເຕະບານດ້ວຍຄວາມໄວ 20 m/s ມຸມ 30° (g = 10) ບານຕົກໄກເທົ່າໃດ?"):
    st.latex(r"R = \frac{20^2 \sin 60^\circ}{10} = \frac{400 \times 0.866}{10} \approx 34.6 \text{ m}")

st.header("📝 ທົດສອບຄວາມເຂົ້າໃຈ")
quiz("p1", "ເມື່ອ h₀ = 0 ແລະ ຄວາມໄວຕົ້ນຄືກັນ ມຸມໃດຍິງໄດ້ໄກທີ່ສຸດ?",
     ["30°", "45°", "60°", "90°"], 1, "R ∝ sin2θ ມີຄ່າສູງສຸດເມື່ອ 2θ = 90° ຫຼື θ = 45°")
