import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(page_title="مطبخ الشيف أم عمار", page_icon="👩‍🍳", layout="centered")

# عنوان التطبيق
st.title("👩‍🍳 مطبخ الشيف أم عمار - Chef Om Ammar's Kitchen")
st.write("مرحباً بك في التطبيق التفاعلي لإعداد أشهى كيكة شوكولاتة!")

# حفظ حالة المطبخ في الـ Session State
if 'ingredients_ready' not in st.session_state:
    st.session_state.ingredients_ready = False
if 'cake_baked' not in st.session_state:
    st.session_state.cake_baked = False

st.divider()

# الخطوة 1: تجهيز المكونات
st.header("1. تجهيز المكونات (Prepare Ingredients)")
if st.button("👩‍🍳 تجهيز المكونات الآن"):
    st.session_state.ingredients_ready = True
    st.success("✔️ تم تجهيز المكونات: [الدقيق، السكر، الكاكاو، البيكنج بودر، البيض، الحليب، الزبدة]")

st.divider()

# الخطوة 2: خبز الكيكة
st.header("2. خبز الكيكة (Bake Cake)")
temp = st.slider("اختر درجة حرارة الفرن (°C):", min_value=100, max_value=300, value=180)
time = st.number_input("اختر وقت الخبز بالدقائق:", min_value=10, max_value=60, value=35)

if st.button("🔥 ابدأ الخبز"):
    if not st.session_state.ingredients_ready:
        st.error("❌ عذراً، يجب تجهيز المكونات أولاً بالضغط على زر الخطوة 1!")
    else:
        if temp < 150:
            st.warning("❄️ درجة الحرارة منخفضة جداً! الكيكة نية وليست ناضجة.")
            st.session_state.cake_baked = False
        elif temp > 220:
            st.error("💥 درجة الحرارة مرتفعة جداً! الكيكة احترقت بالكامل!")
            st.session_state.cake_baked = False
        else:
            st.success("🎂 ممتازة! خرجت الكيكة من الفرن ذهبية وهشة وبدرجة حرارة مثالية!")
            st.session_state.cake_baked = True

st.divider()

# الخطوة 3: تزيين الكيكة
st.header("3. تزيين الكيكة (Decorate Cake)")
if st.button("🍫 تزيين الكيكة بصوص الجناش"):
    if not st.session_state.cake_baked:
        st.error("❌ لا يمكنك تزيين الكيكة قبل خبزها بنجاح!")
    else:
        st.balloons()  # تأثير احتفالي عند النجاح!
        st.success("✨ قمتِ بتزيين الكيكة بصوص الشوكولاتة الفاخر!")
        st.markdown("### 🌟 النتيجة النهائية: كيكة شوكولاتة ملكية جاهزة للتقديم! 🍰🎉")
