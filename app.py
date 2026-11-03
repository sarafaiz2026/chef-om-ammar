import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="منصة الشيف ونسخ المنتجات", page_icon="🛍️", layout="centered")

st.title("🛍️ مولد أوصاف المنتجات الذكي للمتاجر الإلكترونية")
st.write("أداة مخصصة لمساعدة أصحاب المتاجر الإلكترونية على توليد أوصاف جذابة وإعلانات تسويقية لمنتجاتهم بضغطة زر!")

st.divider()

# مدخلات المستخدم (التاجر)
st.header("1. أدخل تفاصيل المنتج")
product_name = st.text_input("اسم المنتج (مثلاً: ساعة ذكية أنيقة / كيكة شوكولاتة فاخرة):")
product_features = st.text_area("أبرز مميزات المنتج (مثلاً: مقاومة للماء، بطارية تدوم طويلاً، تصميم عصرى):")
target_audience = st.selectbox(
    "الجمهور المستهدف:",
    ["الشباب والرياضيون", "ربات البيوت وعشاق الحلويات", "الموظفون ورجال الأعمال", "الجميع"]
)

st.divider()

# زر التوليد والنتيجة
st.header("2. توليد المحتوى التسويقي")
if st.button("🚀 توليد الوصف والإعلانات الآن"):
    if not product_name or not product_features:
        st.error("❌ عذراً، يجب إدخال اسم المنتج ومميزاته أولاً!")
    else:
        # تأثير تفاعلي
        st.balloons()
        
        st.success("✨ تم توليد المحتوى التسويقي بنجاح!")
        
        # تجهيز النصوص لكي يتم عرضها مع خيار النسخ
        marketing_description = f"""**{product_name}**
هل تبحث عن التميز والراحة؟ نقدم لك **{product_name}** المصمم خصيصاً ليناسب احتياجات **{target_audience}**.
المميزات الرئيسية: {product_features}.
لا تفوت الفرصة واطلبه الآن لتعيش تجربة استثنائية!"""

        social_ad = f"🔥 عرض خاص لفترة محدودة! احصل على {product_name} الآن. المميزات: {product_features}. اطلبه اليوم واستمتع بالجودة العالية! 🛒✨"

        # عرض النتائج بطريقة منسقة مع ميزة النسخ المدمجة في Streamlit
        st.subheader("📌 الوصف التسويقي للمتجر:")
        st.markdown(marketing_description)
        # ميزة النسخ المباشر من Streamlit
        st.code(marketing_description, language="markdown")

        st.subheader("📱 إعلان مقترح لوسائل التواصل الاجتماعي (سناب/إنستغرام):")
        st.code(social_ad, language="text")

st.divider()
st.caption("© 2026 - منصة الأدوات الذكية للمتاجر الإلكترونية | تطوير: رائد الأعمال الذكي")
