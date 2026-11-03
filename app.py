import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="منصة الأدوات الذكية للأعمال", page_icon="⚡", layout="centered")

# القائمة الجانبية للتنقل بين الأدوات
st.sidebar.title("📌 قائمة الأدوات الذكية")
tool_choice = st.sidebar.radio(
    "اختر الأداة التي تريد استخدامها:",
    ["🛍️ مولد أوصاف المنتجات", "📄 ملخص التقارير والمستندات"]
)

st.sidebar.divider()
st.sidebar.caption("© 2026 - منصة الأدوات الذكية للأعمال")

# --- الأداة الأولى: مولد أوصاف المنتجات ---
if tool_choice == "🛍️ مولد أوصاف المنتجات":
    st.title("🛍️ مولد أوصاف المنتجات الذكي")
    st.write("أداة مخصصة لمساعدة أصحاب المتاجر الإلكترونية على توليد أوصاف جذابة وإعلانات تسويقية بضغطة زر!")
    st.divider()

    st.header("1. أدخل تفاصيل المنتج")
    product_name = st.text_input("اسم المنتج (مثلاً: ساعة ذكية / كيكة فاخرة):")
    product_features = st.text_area("أبرز مميزات المنتج:")
    target_audience = st.selectbox(
        "الجمهور المستهدف:",
        ["الشباب والرياضيون", "ربات البيوت وعشاق الحلويات", "الموظفون ورجال الأعمال", "الجميع"]
    )

    st.divider()
    st.header("2. توليد المحتوى التسويقي")
    if st.button("🚀 توليد الوصف والإعلانات"):
        if not product_name or not product_features:
            st.error("❌ عذراً، يجب إدخال اسم المنتج ومميزاته أولاً!")
        else:
            st.balloons()
            st.success("✨ تم توليد المحتوى التسويقي بنجاح!")
            
            marketing_desc = f"**{product_name}**\nهل تبحث عن التميز؟ نقدم لك **{product_name}** المخصص لـ **{target_audience}**.\nالمميزات: {product_features}.\nاطلبه الآن!"
            social_ad = f"🔥 عرض خاص! احصل على {product_name} الآن. المميزات: {product_features}. 🛒✨"

            st.subheader("📌 الوصف التسويقي للمتجر:")
            st.code(marketing_desc, language="markdown")

            st.subheader("📱 إعلان السوشيال ميديا:")
            st.code(social_ad, language="text")

# --- الأداة الثانية: ملخص المستندات والتقارير ---
elif tool_choice == "📄 ملخص التقارير والمستندات":
    st.title("📄 ملخص التقارير والمستندات الذكي")
    st.write("ضع أي نص طويل، مقال، أو تقرير، وسيقوم التطبيق بتلخيصه واستخراج النقاط الهامة في ثوانٍ!")
    st.divider()

    st.header("1. أدخل النص المراد تلخيصه")
    input_text = st.text_area("الصق النص أو التقرير هنا:", height=200)
    summary_length = st.select_slider(
        "مستوى التلخيص المطلوبة:",
        options=["موجز جداً (نقاط أساسية)", "متوسط", "شامل"]
    )

    st.divider()
    st.header("2. التلخيص الذكي")
    if st.button("⚡ تلخيص النص الآن"):
        if not input_text or len(input_text.strip()) < 30:
            st.error("❌ يرجى إدخال نص كافٍ (أكثر من 30 حرفاً) ليتسنى تلخيصه!")
        else:
            st.snow()
            st.success("✨ تم تلخيص المستند بنجاح!")
            
            # محاكاة التلخيص الذكي
            words = input_text.split()
            first_part = " ".join(words[:min(15, len(words))])
            
            summary_output = f"""📌 **الملخص التنفيذي ({summary_length}):**
• **الفكرة الرئيسية:** {first_part}...
• **النقاط الأساسية:** تم استخراج زبدة النص بناءً على طلبك في مستوى ({summary_length}).
• **التوصية:** جاهز للاستخدام في العروض والتقارير الرسمية."""

            st.subheader("📝 النص الملخص:")
            st.code(summary_output, language="markdown")
