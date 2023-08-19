# Phân tích
Bước đầu truy cập challenge này là 1 trang web chứa các một số chức năng như chính login, register và việc tạo tài khoản không dễ dàng
Có hai file nên quan tâm chủ yếu là  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/498e079d-5aa9-486c-aaa9-1f0cf221add0)
Trong file app.py chứa chứa các hàm thực hiện chức năng và các router xử lý request.

Khi thực hiện việc đăng kí cần phải nhập activation code, mà code ở đâu ra ;v xem file nguồn  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/59f6e11d-703f-42c9-9375-107f35ce66b5)  
- Một hàm khá kì lạ nó thực hiện genarate ra 1 chuỗi 4 số ngẫu nhiên và so sách với activation code mà mình nhập, nếu đúng thì trả về true. Như gợi ý 'no bruteforce' ta không thể brute force được vì mỗi khi ta nhập activation code thì nó lại gen ra 1 chuỗi số khác.
- Ở đây là có 1 lỗi lập trình và sai về mặt logic . Lỗi lập trình là ở đây sử dụng ```in``` thay vì so sánh bằng toán tử vì thế nên nó sẽ chỉ kiểm tra xem chuỗi 4 chữ số đó có ở trong activation code hay không => ta có thể nhập hết tất cả trường hợp của activation code trên cùng 1 dòng là có thể bypass

