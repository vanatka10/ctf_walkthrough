**Magic shop**

Mở đầu là 1 form login, mở source:
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/e193728d-cd4d-4f79-a928-534b98ea9903)

-Trong đoạn code trên trang web sẽ lấy username và password bị hash bằng sha256 và kiểm tra điều kiện pasword phải bằng 0 thì mới login được. Mặc dù password đã bị hash nhưng ta vẫn có thể login được. Bởi vì trang web sử dụng sử dụng `==` để so sánh 1 chuỗi với 1 interger nên nó có thể bị 1 lỗ hổng là Type Juggling  
-Khi so sánh một string với một số interger trong PHP, nếu như string bắt đầu bằng một ký tự không phải là số, nó sẽ mặc định là int(0) hoặc các strings bắt đầu với các ký tự là 0e, khi đó các chuỗi được chuyển thành các lũy thừa tương đương đương với int(0)   
-Bên cạnh đó ta có 1 lỗ hổng khác là magic hashes nó xuất hiện do một lỗi trong cách PHP xử lý kiểu dữ liệu khi so sánh chuỗi băm với số nguyên. Nếu một chuỗi băm bắt đầu bằng “0e” . Thế nên ta có thể dễ dàng tìm thấy payload trên mạng   
https://github.com/spaze/hashes
=> Mục tiêu của chúng ta là

