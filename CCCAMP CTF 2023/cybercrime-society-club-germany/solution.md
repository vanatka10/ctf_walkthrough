# Phân tích
Bước đầu truy cập challenge này là 1 trang web chứa các một số chức năng như chính login, register và việc tạo tài khoản không dễ dàng
Có hai file nên quan tâm chủ yếu là  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/498e079d-5aa9-486c-aaa9-1f0cf221add0)
Trong file app.py chứa chứa các hàm thực hiện chức năng và các router xử lý request.

Khi thực hiện việc đăng kí cần phải nhập activation code, mà code ở đâu ra ;v xem file nguồn  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/59f6e11d-703f-42c9-9375-107f35ce66b5)  
- Một hàm khá kì lạ nó thực hiện genarate ra 1 chuỗi 4 số ngẫu nhiên và so sách với activation code mà mình nhập, nếu đúng thì trả về true. Như gợi ý 'no bruteforce' ta không thể brute force được vì mỗi khi ta nhập activation code thì nó lại gen ra 1 chuỗi số khác.
- Ở đây là có 1 lỗi lập trình và sai về mặt logic . Lỗi lập trình là ở đây sử dụng ```in``` thay vì so sánh bằng toán tử vì thế nên nó sẽ chỉ kiểm tra xem chuỗi 4 chữ số đó có ở trong activation code hay không => ta có thể nhập hết tất cả trường hợp của activation code trên cùng 1 dòng là có thể bypass
- Sau khi tạo được tài khoản thì bước tiếp theo là làm thế nào để trở thành admin và thực hiện lệnh để lấy flag
  ![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/176b218e-d2bf-4e7a-9e39-08d43d210958)
- Yêu cầu để trở thành admin là (1) có email admin, (2)userid > 90000000
  (1) việc edit, xóa cũng như dùng email của admin lúc đăng kí đều đã bị chặn, vậy chỗ cần khai thác là chức năng xóa. Ở đây cũng có 1 lỗi
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/98d701cf-1f44-4835-bdfe-fe20ce449e41)
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/81e103f0-b65d-4a29-8aba-621f186ea922)

-> Hàm này sẽ lấy ra tất cả các values của data ngay cả khi ta chèn thêm 1 key:values khác từ đó ta có thể xóa email admin ra khỏi tài khoản khác
(2) Vì nó chỉ kiểm tra bằng len chức không phải kiểm tra bằng giá trị nên ta có thể bypass bằng cách sửa id bằng 1e10 là ta có thể bypass

- Tiếp theo là bypass valid command yêu cầu len là 4 và có lệnh date bên trong ,bằng cách gửi kiểu dữ liệu dạng chuỗi ta có thể bypass nó dễ dàng
  ![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/0a2c569a-09f6-4166-b9b2-07082fac14cb)
  



   


