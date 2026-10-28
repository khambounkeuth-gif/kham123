import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from utils import quiz

st.title("🚗 ບົດທີ 2: ການເຄື່ອນທີ່ດ້ວຍຄວາມເລັ່ງຄົງທີ່")

st.header("🎯 ຈຸດປະສົງການຮຽນ")
st.markdown("""
- ອະທິບາຍຄວາມເລັ່ງ ແລະ ຜົນຕໍ່ຄວາມໄວ
- ໃຊ້ສູດການເຄື່ອນທີ່ຄວາມເລັ່ງຄົງທີ່ແກ້ໂຈດ
- ອ່ານກຣາຟ x–t, v–t ແລະ a–t
""")

st.header("📖 ທິດສະດີ")
st.write("ເມື່ອວັດຖຸມີ **ຄວາມເລັ່ງຄົງທີ່ a** ຄວາມໄວຈະປ່ຽນໄປຢ່າງສະໝໍ່າສະເໝີ")
st.latex(r"v = v_0 + a t")
st.latex(r"x = x_0 + v_0 t + \tfrac{1}{2} a t^2")
st.latex(r"v^2 = v_0^2 + 2a(x - x_0)")
st.markdown("""
- ກຣາຟ **v–t** ເປັນເສັ້ນຊື່ ຄວາມຊັນ = ຄວາມເລັ່ງ
- ກຣາຟ **x–t** ເປັນເສັ້ນໂຄ້ງ (ພາຣາໂບລາ)
- ຖ້າ a ແລະ v ມີທິດກົງກັນຂ້າມ ວັດຖຸຈະ **ຊ້າລົງ**
""")

st.sidebar.header("⚙️ ປັບຄ່າ")
x0 = st.sidebar.number_input("ຕຳແໜ່ງເລີ່ມຕົ້ນ x₀ (m)", value=0.0)
v0 = st.sidebar.slider("ຄວາມໄວຕົ້ນ v₀ (m/s)", -20.0, 20.0, 0.0)
a = st.sidebar.slider("ຄວາມເລັ່ງ a (m/s²)", -10.0, 10.0, 2.0)
t_max = st.sidebar.slider("ເວລາທັງໝົດ (s)", 1.0, 30.0, 10.0)

st.header("🔬 ການຈຳລອງ")
st.write("🤔 **ທຳນາຍ:** ຖ້າ a ເປັນລົບ (ເບຣກ) ກຣາຟ v–t ຈະເປັນແນວໃດ?")
t_now = st.slider("ເວລາປັດຈຸບັນ t (s)", 0.0, float(t_max), 0.0, 0.1)

t = np.linspace(0, t_max, 300)
x = x0 + v0 * t + 0.5 * a * t**2
v = v0 + a * t
x_now = x0 + v0 * t_now + 0.5 * a * t_now**2
v_now = v0 + a * t_now

c1, c2, c3 = st.columns(3)
c1.metric("ຕຳແໜ່ງ x", f"{x_now:.2f} m")
c2.metric("ຄວາມໄວ v", f"{v_now:.2f} m/s")
c3.metric("ຄວາມເລັ່ງ a", f"{a:.2f} m/s²")
if a * v_now < 0:
    st.warning("⚠️ a ແລະ v ມີທິດກົງກັນຂ້າມ: ວັດຖຸກຳລັງຊ້າລົງ")
elif a * v_now > 0:
    st.success("🚀 a ແລະ v ມີທິດດຽວກັນ: ວັດຖຸກຳລັງໄວຂຶ້ນ")

lo, hi = min(x.min(), x0) - 2, max(x.max(), x0) + 2
fig0, ax0 = plt.subplots(figsize=(10, 1.4))
ax0.axhline(0, color="gray")
ax0.plot(x_now, 0, "o", ms=18, color="tab:orange")
ax0.set_xlim(lo, hi)
ax0.set_yticks([])
ax0.set_xlabel("position x (m)")
st.pyplot(fig0)

fig, ax = plt.subplots(1, 3, figsize=(12, 3.6))
ax[0].plot(t, x, color="tab:blue")
ax[0].plot(t_now, x_now, "ro")
ax[0].set(title="x - t", xlabel="t (s)", ylabel="x (m)")
ax[1].plot(t, v, color="tab:red")
ax[1].plot(t_now, v_now, "ko")
ax[1].set(title="v - t", xlabel="t (s)", ylabel="v (m/s)")
ax[2].plot(t, np.full_like(t, a), color="tab:green")
ax[2].plot(t_now, a, "ko")
ax[2].set(title="a - t", xlabel="t (s)", ylabel="a (m/s²)")
for p in ax:
    p.grid(True)
plt.tight_layout()
st.pyplot(fig)

st.header("✏️ ຕົວຢ່າງໂຈດ")
with st.expander("ລົດເລີ່ມຈາກຢຸດ ເລັ່ງ 3 m/s² ເປັນເວລາ 6 s ຄວາມໄວ ແລະ ໄລຍະທາງເທົ່າໃດ?"):
    st.latex(r"v = 0 + 3 \times 6 = 18 \text{ m/s}")
    st.latex(r"x = \tfrac{1}{2}(3)(6^2) = 54 \text{ m}")

st.header("📝 ທົດສອບຄວາມເຂົ້າໃຈ")
quiz("a1", "ວັດຖຸເລີ່ມຈາກຢຸດ ເລັ່ງ 2 m/s² ເປັນເວລາ 5 s ຄວາມໄວສຸດທ້າຍເທົ່າໃດ?",
     ["2 m/s", "5 m/s", "10 m/s", "25 m/s"], 2, "v = v₀ + at = 0 + 2 × 5 = 10 m/s")
