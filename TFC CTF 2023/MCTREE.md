![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/4e608feb-8bf2-4072-ae1a-1059a8e874a7)
Bài này đặt medium nhưng thực ra khá dễ dàng

Bài này chỉ có chức năng chính là regsister và login  và không có bất kì gợi ý nào khác 
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/e86c1726-9363-4363-8698-7be75c63c3c4)

Mình thử đăng kí bằng admin xem thử và nó hiện về l username đẵ được sử dụng cho nên mình nghĩ là sqli nhưng không thành công nên mình nghĩ có thể là ssti vì khi mình đăng nhập xong nó sẽ hiện lời chào "get out of here" có lẽ thế ;v và tên đăng nhập  

![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/c9f26d34-6710-4907-a437-b59c5fac6b08)

Xong mình thử regsister bằng 1 vài payload kí tự đặc biệt xem sao và trả về tên tài khoản bị mất 1 số kí tự đặc biệt đi nhưng tên đăng nhập sẽ được giữ nguyên và không báo lỗi . Điều này khá là lạ 

Từ đó mình nghĩ nếu ta thêm kí tự đặc biệt đó để có thể register bằng username admin thì sao tiến hành luôn
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/5703d494-60a5-4b7b-b28c-f076227cfa5b)

ngon, giờ chỉ cần đăng nhập vào lấy flag là xong
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/40b767aa-c04c-495f-aea4-acc3f51b80b3)
