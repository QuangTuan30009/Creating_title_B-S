# Tạo tin đăng Bất động sản từ JSON (AI + Ollama)

Ứng dụng Streamlit giúp tạo tin đăng bất động sản chuyên nghiệp từ dữ liệu JSON bằng mô hình chạy local qua Ollama.

## Tính năng

- Nhập dữ liệu bằng cách dán JSON hoặc upload file `.json`
- Tùy chỉnh giọng điệu tin đăng: Chuyên nghiệp / Thân thiện / Hấp dẫn / Ngắn gọn
- Tùy chọn thêm emoji và thông tin liên hệ
- Sinh nội dung tự động với model `bds-writer`
- Tải kết quả về file `.txt`

## Yêu cầu hệ thống

- Python 3.9+
- Ollama đã cài và đang chạy
- Model base: `qwen2.5:7b`

## Cài đặt

### 1) Clone project

```bash
git clone https://github.com/QuangTuan30009/Creating_title_B-S.git
cd Creating_title_B-S
```

### 2) Cài thư viện Python

```bash
pip install -r requirements.txt
```

### 3) Cài Ollama và tạo model viết tin

```bash
ollama pull qwen2.5:7b
ollama create bds-writer -f Modelfile
```

> Lưu ý: cần chạy dịch vụ Ollama trước khi dùng ứng dụng.

## Chạy ứng dụng

```bash
streamlit run app.py
```

Mặc định ứng dụng mở tại: `http://localhost:8501`

## Cấu trúc dữ liệu JSON mẫu

```json
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
```

## Luồng xử lý

`JSON đầu vào -> Prompt theo cấu hình người dùng -> Ollama (bds-writer) -> Tin đăng hoàn chỉnh`

## Ghi chú

- Ứng dụng ưu tiên viết ngắn gọn, tự nhiên, dễ đọc
- Nội dung phụ thuộc chất lượng dữ liệu JSON đầu vào
- Nếu lỗi kết nối model, kiểm tra lại Ollama và model `bds-writer`