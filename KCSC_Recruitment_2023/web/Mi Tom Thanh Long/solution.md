# Task
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/eaa64910-4fad-4308-b2e6-bcc9ef260d16)

-Mô tả....
# Exploit
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/3a3d79f6-c6b2-4292-99c7-65d17ab6530a)

-Một trang web khá là không bình thường, đập vào mắt là cái flag chình ình    
-Khi truy cập vô thì không có flag chỉ có 1 vài cái meme , nhưng mà điều đáng chú ý là cái url có chứa param là page nên rất có khả năng là 1  bài LFI  

![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/416798a7-661c-4cf2-a0ba-a4a4a3d4a89b)

-Ye đó là LFI
-Sử dụng wrapper php://filter ta có thể đọc được nội dung của file bên phía server 
-Payload 
```
?page=php://filter/convert.base64-encode/resource=pages/flag.php
```
=>Decode ra là ta có flag



