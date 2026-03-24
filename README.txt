=============================================================================================
TẠO TIN ĐĂNG BẤT ĐỘNG SẢN TỪ JSON
=============================================================================================


Ứng dụng AI tự động tạo tin đăng bất động sản chuyên nghiệp từ dữ liệu JSON.

TÍNH NĂNG:
- Tạo tin đăng BDS từ dữ liệu JSON
- Tùy chọn thêm emoji và thông tin liên hệ
- Sử dụng model Qwen 2.5 7B qua Ollama

=============================================================================================
CÀI ĐẶT
=============================================================================================

BƯỚC 1: YÊU CẦU HỆ THỐNG

- Python 3.9+
- Ollama (tải tại: https://ollama.com)
- RAM: Tối thiểu 8GB

BƯỚC 2: CÀI ĐẶT OLLAMA VÀ BASE MODEL

Tải Ollama từ: https://ollama.com/download

Tải base model:
ollama pull qwen2.5:7b

Kiểm tra:
ollama list

BƯỚC 3: TẠO CUSTOM MODEL VIẾT TIN

Tạo model viết tin:
ollama create bds-writer -f Modelfile

Kiểm tra:
ollama list

BƯỚC 4: CÀI ĐẶT THƯ VIỆN PYTHON

pip install -r requirements.txt

Hoặc cài thủ công:
pip install streamlit ollama

=============================================================================================
CHẠY ỨNG DỤNG
=============================================================================================

streamlit run app.py

Ứng dụng sẽ mở tại: http://localhost:8501



ĐỊNH DẠNG JSON MẪU:
{
  "so_nha": "123",
  "duong": "Nguyễn Văn Linh",
  "phuong": "Tân Phú",
  "quan": "Quận 7",
  "gia": "15 tỷ",
  "dien_tich": "5x20m",
  "phong_ngu": 4,
  "wc": 5,
  "so_tang": "3 tầng",
  "huong_nha": "Đông",
  "huong_ban_cong": "Nam",
  "phap_ly": "Sổ hồng",
  "co_ban_cong": true,
  "tien_ich": ["Gần chợ", "Gần trường"],
  "sdt": "0901234567"
}


=============================================================================================
GHI CHÚ
=============================================================================================

- Model sử dụng: bds-writer (dựa trên Qwen 2.5 7B)
- Temperature = 0.7 (sáng tạo, tự nhiên)
- Chỉ sử dụng thông tin có trong JSON, không bịa đặt


=============================================================================================
VÍ DỤ KẾT QUẢ
=============================================================================================

Input JSON:
{
  "duong": "Đường số 7",
  "phuong": "Phường Hạnh Thông",
  "quan": "Quận Gò Vấp",
  "gia": "5.79 tỷ thương lượng",
  "dien_tich": "3,5m x 14m",
  "phong_ngu": 3,
  "wc": 4,
  "so_tang": "1 trệt, 1 lầu",
  "phap_ly": "Sổ hồng chính chủ",
  "co_ban_cong": true,
  "tien_ich": ["Gần chợ", "Gần sân bay"],
  "sdt": "0907849789"
}

Output:
BÁN NHÀ GÒ VẤP - 3 PHÒNG NGỦ - SỔ HỒNG - GIÁ CHỈ 5.79 TỶ

VỊ TRÍ:
Đường số 7, Phường Hạnh Thông, Quận Gò Vấp
Gần chợ, gần sân bay - Giao thông thuận lợi

THÔNG SỐ:
- Diện tích: 3.5m x 14m
- Kết cấu: 1 trệt, 1 lầu
- 3 phòng ngủ, 4 toilet
- Có ban công thoáng mát

ƯU ĐIỂM:
- Sổ hồng chính chủ, pháp lý rõ ràng
- Vị trí đẹp, gần đầy đủ tiện ích

GIÁ: 5.79 tỷ (có thương lượng)

LIÊN HỆ: 0907849789


