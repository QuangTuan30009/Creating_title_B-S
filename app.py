import streamlit as st
import ollama
import json
from datetime import datetime

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="Tạo tin đăng BDS",
    page_icon="📝",
    layout="wide"
)

# =========================
# Header
# =========================
st.title("📝 Tạo tin đăng Bất động sản (AI Powered)")
st.markdown("Ứng dụng sử dụng AI để tạo tin đăng bất động sản chuyên nghiệp từ dữ liệu JSON")
st.markdown("---")

# =========================
# Main Content
# =========================
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Nhập dữ liệu JSON")
    
    input_method = st.radio(
        "Chọn cách nhập:",
        ["✍️ Nhập thủ công", "📁 Upload file JSON"],
        horizontal=True
    )
    
    json_data = None
    
    if input_method == "✍️ Nhập thủ công":
        json_input = st.text_area(
            "Nhập JSON:",
            height=400,
            placeholder="""{
  "so_nha": "123",
  "duong": "Nguyễn Văn Linh",
  "phuong": "Tân Phú",
  "quan": "Quận 7",
  "gia": "15 tỷ",
  "dien_tich": "5x20m",
  "phong_ngu": 4,
  "wc": 5,
  "so_tang": "3 tầng",
  "sdt": "0901234567"
}"""
        )
        
        if st.button("📋 Dùng JSON mẫu"):
            st.session_state.sample_json = """{
  "so_nha": null,
  "duong": "Đường số 7",
  "phuong": "Phường Hạnh Thông (cũ, nay là Phường 7)",
  "quan": "Quận Gò Vấp",
  "gia": "5.79 tỷ thương lượng",
  "dien_tich": "3,5m x 14m (CN 48m2)",
  "sdt": "0907849789",
  "phong_ngu": 3,
  "wc": 4,
  "so_tang": "1 trệt, 1 lầu",
  "huong_nha": null,
  "huong_ban_cong": null,
  "phap_ly": "Sổ hồng chính chủ",
  "co_ban_cong": true,
  "tien_ich": ["Gần chợ Gò Vấp", "Đại học CN4", "BV 175", "Ra sân bay 10p"]
}"""
            st.rerun()
        
        if 'sample_json' in st.session_state:
            json_input = st.session_state.sample_json
            del st.session_state.sample_json
        
        if json_input:
            try:
                json_data = json.loads(json_input)
            except:
                st.error("❌ JSON không hợp lệ!")
    
    else:  # Upload file
        uploaded_file = st.file_uploader(
            "Chọn file JSON:",
            type=['json']
        )
        
        if uploaded_file:
            try:
                json_data = json.load(uploaded_file)
                st.success("✅ Đã tải file JSON thành công!")
                with st.expander("Xem nội dung"):
                    st.json(json_data)
            except:
                st.error("❌ File JSON không hợp lệ!")
    
    st.markdown("---")
    
    # Settings
    with st.expander("⚙️ Tùy chỉnh tin đăng"):
        tone = st.selectbox(
            "Giọng điệu:",
            ["Chuyên nghiệp", "Thân thiện", "Hấp dẫn", "Ngắn gọn"]
        )
        
        include_emoji = st.checkbox("Thêm emoji", value=False)
        include_contact = st.checkbox("Thêm thông tin liên hệ", value=True)
    
    create_button = st.button(
        "✍️ Tạo tin đăng",
        type="primary",
        use_container_width=True,
        disabled=json_data is None
    )

with col2:
    st.subheader("📝 Tin đăng")
    result_container = st.container()

# Processing
if create_button and json_data:
    with st.spinner("✍️ Đang viết tin đăng..."):
        try:
            prompt = f"""Dựa vào dữ liệu JSON sau, hãy viết một tin đăng bất động sản hấp dẫn, chuyên nghiệp:

{json.dumps(json_data, ensure_ascii=False, indent=2)}

Yêu cầu:
- Viết bằng tiếng Việt tự nhiên, dễ đọc
- Giọng điệu: {tone}
- {'KHÔNG SỬ DỤNG emoji hay icon' if not include_emoji else 'Có thể dùng emoji phù hợp'}
- {'Có thông tin liên hệ cuối bài' if include_contact else 'Không cần thông tin liên hệ'}
- Cấu trúc: Tiêu đề → Vị trí → Thông tin chi tiết → Ưu điểm → Liên hệ
- Làm nổi bật các điểm mạnh của bất động sản
- Viết ngắn gọn, rõ ràng, dễ hiểu
"""

            summary_response = ollama.chat(
                model="bds-writer",
                messages=[{"role": "user", "content": prompt}]
            )

            summary_text = summary_response["message"]["content"].strip()

            with result_container:
                st.success("✅ Đã tạo tin đăng!")
                
                st.text_area(
                    label="",
                    value=summary_text,
                    height=450,
                    label_visibility="collapsed"
                )
                
                col_btn1, col_btn2 = st.columns(2)
                
                with col_btn1:
                    st.download_button(
                        "📥 Tải tin đăng (.txt)",
                        data=summary_text,
                        file_name=f"tin_dang_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col_btn2:
                    if st.button("🔄 Tạo lại", use_container_width=True):
                        st.rerun()

        except Exception as e:
            st.error(f"❌ Lỗi: {str(e)}")

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.header("ℹ️ Thông tin")
    
    st.markdown("**Model:**")
    st.info("🔹 Viết tin: `bds-writer`")
    
    st.markdown("---")
    
    st.markdown("**Giọng điệu:**")
    items = [
        "Chuyên nghiệp",
        "Thân thiện",
        "Hấp dẫn",
        "Ngắn gọn"
    ]
    for item in items:
        st.markdown(f"• {item}")
    
    st.markdown("---")
    st.caption("**Powered by:** Ollama AI")

# =========================
# Footer
# =========================
st.markdown("---")
with st.expander("ℹ️ Hướng dẫn"):
    st.markdown("""
    ### 📝 Cách sử dụng:
    1. Nhập JSON thủ công hoặc upload file .json
    2. Tùy chỉnh giọng điệu, emoji (nếu cần)
    3. Nhấn "Tạo tin đăng"
    4. Tải xuống file .txt
    
    ### 🔄 Luồng:
    - **JSON → bds-writer → Tin đăng**
    
    ### 📋 Yêu cầu:
    - Ollama đang chạy
    - Model `bds-writer` đã được cài đặt
    - Chạy lệnh: `ollama create bds-writer -f Modelfile`
    """)

st.caption("📝 Powered by Ollama AI • Tạo tin đăng tự động")
