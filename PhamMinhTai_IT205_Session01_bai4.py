
print("=" * 60)
print("=== PHẦN MỀM TIẾP NHẬN BỆNH NHÂN ===")
print("=" * 60)

print("\n--- NHẬP THÔNG TIN BỆNH NHÂN MỚI ---")

ho_ten = input("Họ và tên bệnh nhân: ")
ma_benh_an = input("Mã bệnh án (VD: BN1024, BA9901...): ")
khoa_phong = input("Khoa/Phòng khám chỉ định (VD: Khoa Nội, Phòng Khám Mắt...): ")

print("\n" + "=" * 60)
print("=== PHIẾU KHÁM BỆNH ĐIỆN TỬ ===")
print("=" * 60)

print(f"Bệnh nhân: {ho_ten} - Mã BA: {ma_benh_an} - Chuyển tới: {khoa_phong}")

print("\n" + "-" * 60)
print("✅ XÁC NHẬN: Đã tiếp nhận bệnh nhân thành công!")
print("-" * 60)