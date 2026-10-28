"""ຟັງຊັນຊ່ວຍທີ່ໃຊ້ຮ່ວມກັນທຸກໜ້າ"""
import streamlit as st


def quiz(key, question, options, answer, explanation):
    """ແບບທົດສອບແບບເລືອກຄຳຕອບ
    key        : ຊື່ບໍ່ຊ້ຳກັນ
    options    : ລາຍການຕົວເລືອກ
    answer     : ລຳດັບຄຳຕອບທີ່ຖືກ (ເລີ່ມຈາກ 0)
    explanation: ຄຳອະທິບາຍຫຼັງຕອບຖືກ
    """
    st.markdown(f"**{question}**")
    choice = st.radio("ເລືອກຄຳຕອບ:", options, index=None, key=f"{key}_radio")
    if st.button("ກວດຄຳຕອບ", key=f"{key}_btn"):
        if choice is None:
            st.warning("ກະລຸນາເລືອກຄຳຕອບກ່ອນ")
        elif options.index(choice) == answer:
            st.success("✅ ຖືກຕ້ອງ!")
            st.info(explanation)
        else:
            st.error("❌ ຍັງບໍ່ຖືກ ລອງຄິດໃໝ່ອີກຄັ້ງ")
