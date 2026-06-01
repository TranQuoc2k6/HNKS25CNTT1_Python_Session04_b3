list_bill = []
input_quantity_bill = int(input("Nhập số lượng hóa đơn trong ca: "))

for i in range(input_quantity_bill):
    bill_price = float(input(f"Nhập giá trị hóa đơn thứ {i+1}: "))
    list_bill.append(bill_price)    

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print(f"Hoá đơn có giá trị cao nhất: {max(list_bill)} VND")
print(f"Hóa đơn có giá trị thấp nhất: {min(list_bill)} VND")