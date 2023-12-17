# Task
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/c2f0dcdb-dc25-41ca-92d4-0092ce6898c4)
# Exploit
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/17051bb6-ffa8-4fba-9050-b68bd40bf4d3)  
-Trong trang web có 1 chức năng đáng lưu ý là upload file, vậy nên mình đã thử upload 1 file webshell thử xem 
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/2965cffd-10b0-4839-921a-e7e35209c218)

-Hmmm chỉ cho phép file pdf và có kích cỡ 1 mb trở xuống 
- Bởi vì mình chỉ dùng loại simple webshell nên điều kiện 1mb có thể dễ dàng thông qua, nhưng về còn định dạng file pdf vì không có file source để biết trang web kiểm tra extension kiểu gì nên mình chỉ có thể tự tìm cách bypass extension. sau một hồi thử 1 số cách mình thấy chỉ cần thêm .php đằng sau file đuôi pdf hoặc ngược lại mình ko nhớ rõ nữa. Sau khi hết giải mình có vô để làm writeup nhưng hình như điều kiện kích thứơc bị giảm thành 0 mb nên mình chỉ có file null mới upload được ;vvvv
 FLAG:
 ![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/2c5238db-d2da-4a50-8e14-517350cacacf)
 
