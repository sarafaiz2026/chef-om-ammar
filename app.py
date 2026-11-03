import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="منصة الأدوات الذكية للأعمال", page_icon="⚡", layout="centered")

# إعداد مفتاح الـ API الحقيقي
API_KEY = "AIzaSyAh3lB83xCAb-RmpX-E1bAybLaviqilEy4"

if API_KEY:
    genai.configure(api_key=API_KEY)
    # استخدام النموذج القياسي المستقر
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None

# القائمة الجانبية للتنقل
st.sidebar.title("📌 قائمة الأدوات الذكية")
tool_choice = st.sidebar.radio(
    "اختر الأداة التي تريد استخدامها:",
    ["🛍️ مولد أوصاف المنتجات", "📄 ملخص التقارير والمستندات"]
)

st.sidebar.divider()
st.sidebar.caption("© 2026 - منصة الأدوات الذكية للأعمال")

# --- الأداة الأولى: مولد أوصاف المنتجات بالذكاء الاصطناعي ---
if tool_choice == "🛍️ مولد أوصاف المنتجات":
    st.title("🛍️ مولد أوصاف المنتجات الذكي")
    st.write("أداة مخصصة لمساعدة أصحاب المتاجر على توليد أوصاف إبداعية وفريدة بالذكاء الاصطناعي الحقيقي!")
    st.divider()

    st.header("1. أدخل تفاصيل المنتج")
    product_name = st.text_input("اسم المنتج (مثلاً: حقيبة جلدية فاخرة / كعك سوداني أصلي):")
    product_features = st.text_area("أبرز مميزات المنتج:")
    target_audience = st.selectbox(
        "الجمهور المستهدف:",
        ["الشباب والرياضيون", "ربات البيوت وعشاق الحلويات", "الموظفون ورجال الأعمال", "الجميع"]
    )

    st.divider()
    st.header("2. توليد المحتوى التسويقي")
    if st.button("🚀 توليد الوصف بالذكاء الاصطناعي"):
        if not product_name or not product_features:
            st.error("❌ عذراً، يجب إدخال اسم المنتج ومميزاته أولاً!")
        else:
            with st.spinner("جاري التفكير وتوليد النص بواسطة الذكاء الاصطناعي..."):
                if model:
                    prompt = f"""
                    أنت خبير تسويق إلكتروني احترافي. اكتب لي:
                    1. وصف تسويقي جذاب وجاهز للنشر لمنتج: {product_name}
                    2. المميزات الأساسية: {product_features}
                    3. الجمهور المستهدف: {target_audience}
                    4. نص إعلان قصير ومحفز لشبكات التواصل الاجتماعي مع إيموجي مناسبة.
                    """
                    response = model.generate_content(prompt)
                    ai_text = response.text
                else:
                    ai_text = "⚠️ تنبيه: يرجى التحقق من إعدادات المفتاح."

            st.balloons()
            st.success("✨ تم توليد المحتوى الذكي بنجاح!")
            st.code(ai_text, language="markdown")

# --- الأداة الثانية: ملخص التقارير الذكي ---
elif tool_choice == "📄 ملخص التقارير والمستندات":
    st.title("📄 ملخص التقارير والمستندات الذكي")
    st.write("ضع أي نص أو تقرير، وسيقوم الذكاء الاصطناعي بتحليله واستخراج الزبدة فوراً!")
    st.divider()

    input_text = st.text_area("الصق النص أو التقرير هنا:", height=200)
    
    if st.button("⚡ تلخيص بالذكاء الاصطناعي"):
        if not input_text or len(input_text.strip()) < 30:
            st.error("❌ يرجى إدخال نص كافٍ ليتسنى تلخيصه!")
        else:
            with st.spinner("جاري تحليل النص واستخراج النقاط..."):
                if model:
                    prompt = f"قم بتلخيص النص التالي واستخراج أهم النقاط الرئيسية منه بأسلوب تنفيذي واضح:\n\n{input_text}"
                    response = model.generate_content(prompt)
                    summary_text = response.text
                else:
                    summary_text = "⚠️ تنبيه: يرجى التحقق من إعدادات المفتاح."

            st.snow()
            st.success("✨ تم التلخيص بنجاح!")
            st.code(summary_text, language="markdown")
