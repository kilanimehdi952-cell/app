import streamlit as st
import urllib.parse

# إعدادات الواجهة المتوافقة مع الهاتف
st.set_page_config(page_title="المنصة الذكية الشاملة", page_icon="🧠", layout="centered")

# عنوان المنصة الرئيسي المفتوح للجمهور
st.title("🧠 منصة المساعد الذكي الشاملة")
st.write("مرحباً بك! تصفح خدماتنا المجانية للتسويق والتعليم بالذكاء الاصطناعي.")

FACEBOOK_PAGE_URL = "https://facebook.com"
MESSENGER_BOT_URL = "https://m.me"

# تبويبات مفتوحة للعامة والناس بدون أي كلمة مرور
tab1, tab2 = st.tabs(["💼 كاتب الإعلانات للتجار", "🎓 المساعد التعليمي للطلاب"])

with tab1:
    st.subheader("📝 ولد منشورك الإعلاني وانشره تلقائياً:")
    biz_name = st.text_input("اسم عملك أو منتجك:")
    biz_type = st.selectbox("مجال التخصص:", ["ملابس وموضة", "مطاعم ومأكولات", "عقارات وسيارات", "إلكترونيات وهواتف"])
    target_audience = st.text_input("من هو جمهورك المستهدف؟")

    if biz_name:
        generated_text = f"✨ إعلان مميز لـ {biz_name} ✨\n\nإلى كل عملائنا من {target_audience}، نرحب بكم في أفضل عروضنا المتخصصة في {biz_type}! 🎯\n🌟 جودة عالية وضمان حقيقي وأسعار منافسة جداً.\n📬 تواصلوا معنا الآن فوراً عبر الرسائل للحجز أو الاستفسار!"
        st.text_area("المنشور الجاهز للنسخ:", generated_text, height=140)
        
        encoded_text = urllib.parse.quote(generated_text)
        fb_share_url = f"https://facebook.com{urllib.parse.quote(FACEBOOK_PAGE_URL)}&quote={encoded_text}"
        
        st.markdown(f'<a href="{fb_share_url}" target="_blank" style="text-decoration: none;"><button style="background-color: #1877F2; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: bold;">🚀 انشر الإعلان تلقائياً على فيسبوك الآن</button></a>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.info("الرجاء كتابة اسم عملك أو منتجك أولاً.")

with tab2:
    st.subheader("🤖 خادم المساعد التعليمي الذكي")
    st.write("هل تواجه صعوبة في حل التمارين أو تلخيص الدروس؟ اذهب إلى البوت فوراً!")
    st.info("📚 مميزات البوت: حل مسائل الرياضيات، شرح الدروس، تلخيص النصوص مجاناً!")
    st.markdown(f'<a href="{MESSENGER_BOT_URL}" target="_blank" style="text-decoration: none;"><button style="background-color: #0084FF; color: white; border: none; padding: 14px 24px; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: bold;">💬 ابدأ التحدث مع المساعد التعليمي على ميسنجر الآن</button></a>', unsafe_allow_html=True)

st.markdown("---")

# الحماية المشددة فقط على لوحة الإيرادات في الأسفل
with st.expander("🔐 لوحة إدارة الأرباح (خاصة بصاحب الموقع فقط)"):
    password = st.text_input("أدخل كلمة المرور السرية لرؤية البيانات الحساسة:", type="password")
    if password == "12344321":
        st.success("✅ أهلاً بك يا مدير! تم التحقق من الهوية بنجاح.")
        st.metric(label="💰 الأرباح الإجمالية المستحقة من الإعلانات", value="$284.50")
    elif password != "":
        st.error("❌ كلمة المرور خاطئة! البيانات محجوبة.")


