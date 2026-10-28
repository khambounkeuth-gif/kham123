import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from utils import quiz

st.title("📏 ບົດທີ 1: ການເຄື່ອນທີ່ສະໝໍ່າສະເໝີ")

st.header("🎯 ຈຸດປະສົງການຮຽນ")
st.markdown("""
- ອະທິບາຍການເຄື່ອນທີ່ດ້ວຍຄວາມໄວຄົງທີ່
- ໃຊ້ສູດ x = x₀ + vt ແກ້ໂຈດ
- ອ່ານກຣາຟ x–t ແລະ v–t ໄດ້
""")

st.header("📖 ທິດສະດີ")
st.write("ການເຄື່ອນທີ່ສະໝໍ່າສະເໝີ ຄື ການເຄື່ອນທີ່ເປັນເສັ້ນຊື່ດ້ວຍ **ຄວາມໄວຄົງທີ່** (ຄວາມເລັ່ງ = 0)")
st.latex(r"x = x_0 + v\,t")
st.markdown("""
- **x₀** = ຕຳແໜ່ງເລີ່ມຕົ້ນ (m), **v** = ຄວາມໄວ (m/s), **t** = ເວລາ (s)
- ກຣາຟ **x–t** ເປັນເສັ້ນຊື່ ຄວາມຊັນ = ຄວາມໄວ
- ກຣາຟ **v–t** ເປັນເສັ້ນຂະໜານແກນ t
""")

# ---- ຕົວຄວບຄຸມ ----
st.sidebar.header("⚙️ ປັບຄ່າ")
x0 = st.sidebar.number_input("ຕຳແໜ່ງເລີ່ມຕົ້ນ x₀ (m)", value=0.0)
v = st.sidebar.slider("ຄວາມໄວ v (m/s)", -20.0, 20.0, 5.0)
t_max = st.sidebar.slider("ເວລາທັງໝົດ (s)", 1.0, 60.0, 10.0)

st.header("🔬 ການຈຳລອງ")
st.write("🤔 **ທຳນາຍ:** ຖ້າເພີ່ມຄວາມໄວເປັນສອງເທົ່າ ກຣາຟ x–t ຈະປ່ຽນແນວໃດ?")
t_now = st.slider("ເວລາປັດຈຸບັນ t (s)", 0.0, float(t_max), 0.0, 0.1)

t = np.linspace(0, t_max, 200)
x = x0 + v * t
x_now = x0 + v * t_now

c1, c2, c3 = st.columns(3)
c1.metric("ຕຳແໜ່ງຕອນນີ້", f"{x_now:.2f} m")
c2.metric("ໄລຍະທາງທີ່ຜ່ານມາ", f"{abs(v * t_now):.2f} m")
c3.metric("ຄວາມໄວ", f"{v:.2f} m/s")

# ວັດຖຸເຄື່ອນທີ່ເທິງເສັ້ນທາງ
lo, hi = min(x.min(), x0) - 2, max(x.max(), x0) + 2
fig0, ax0 = plt.subplots(figsize=(10, 1.4))
ax0.axhline(0, color="gray")
ax0.plot(x_now, 0, "o", ms=18, color="tab:orange")
ax0.set_xlim(lo, hi)
ax0.set_yticks([])
ax0.set_xlabel("position x (m)")
st.pyplot(fig0)

fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
ax[0].plot(t, x, color="tab:blue")
ax[0].plot(t_now, x_now, "ro")
ax[0].set(title="Position - Time (x-t)", xlabel="t (s)", ylabel="x (m)")
ax[1].plot(t, np.full_like(t, v), color="tab:red")
ax[1].plot(t_now, v, "ko")
ax[1].set(title="Velocity - Time (v-t)", xlabel="t (s)", ylabel="v (m/s)")
for a in ax:
    a.grid(True)
plt.tight_layout()
st.pyplot(fig)

st.header("✏️ ຕົວຢ່າງໂຈດ")
with st.expander("ລົດແລ່ນດ້ວຍຄວາມໄວ 15 m/s ເລີ່ມຈາກ x₀ = 10 m ຫຼັງ 8 s ຢູ່ຕຳແໜ່ງໃດ?"):
    st.latex(r"x = 10 + 15 \times 8 = 130 \text{ m}")

st.header("📝 ທົດສອບຄວາມເຂົ້າໃຈ")
quiz("u1", "ລົດແລ່ນດ້ວຍຄວາມໄວຄົງທີ່ 20 m/s ໃນເວລາ 5 s ໄດ້ໄລຍະທາງເທົ່າໃດ?",
     ["4 m", "25 m", "100 m", "400 m"], 2, "ໄລຍະທາງ = v × t = 20 × 5 = 100 m")
