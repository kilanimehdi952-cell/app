# كود البرنامج المبتكر الخاص بنا
import streamlit as st
import webbrowser

st.title("🛡️ برنامج المساعد الذكي للمبيعات الآمنة")
st.write("هذا البرنامج مصمم لمساعدتك في فحص وتجارة السلع بأمان")

# 1. واجهة رفع الصورة لفحصها عبر ياندكس
st.subheader("1. فحص أمان الصورة (منع النصب)")
uploaded_file = st.file_uploader("ارفع صورة المنتج هنا لفحصها عالمياً:", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='جاري تجهيز الصورة للفحص...', use_column_width=True)
    # رابط فحص الصور العكسي من ياندكس
    yandex_url = "https://yandex.com"
    if st.button("ابحث عن مصدر الصورة الأصلي في Yandex"):
        webbrowser.open_new_tab(yandex_url)
        st.success("تم فتح بوابة ياندكس الذكية لفحص الصورة ومقارنتها!")

# 2. واجهة كتابة المنشور التلقائي لفيسبوك
st.subheader("2. كاتب منشورات الفيسبوك الذكي")
product_name = st.text_input("ما هو اسم المنتج؟ (مثال: آيفون 13 مستعمل)")
product_cond = st.selectbox("حالة المنتج:", ["ممتاز كأنه جديد", "مستعمل خفيف", "متوسط، به بعض الخدوش"])
price = st.text_input("السعر المتوقع (بالعملة المحلية):")

if st.button("توليد منشور احترافي للفيسبوك"):
    post_text = f"📢 للبيع: {product_name} \n✨ الحالة: {product_cond} \n💰 السعر: {price} \n📬 للتواصل والاستفسار، يرجى مراسلتي على الخاص. الجادين فقط!"
    st.text_area("انسخ هذا النص وانشره فوراً على فيسبوك:", post_text, height=150)
    st.balloons()
