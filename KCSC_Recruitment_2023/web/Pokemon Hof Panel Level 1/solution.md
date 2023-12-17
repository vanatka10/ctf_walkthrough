# Task 
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/bcb94ba2-5232-4e60-b07d-9b2bdec7d3c3)  
-Như trên mô ta thì cũng có thể đoán được đây là 1 bài insecure deserialization php và cũng cho sẵn document đọc tham khảo
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/909d4d9c-02ad-41dc-8778-b3544b87df7b)
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/874bba9e-d4e4-4c03-b07f-062d70e9e4b0)  
-Sau khi điền xong thông tin và chọn submit trang web sẽ hiện lên 1 thông báo access denied. Chứng tỏ ta phải leo thang đặc quyền để thành champion
# Solution
-Bài này thì ta cũng không cần đọc file nguồn , đầu tiên ta đi check cookie 
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/90eaa139-b80a-47b0-9ee1-c3244d0b94be)  
-Decode base64 ra thì ta có
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/7c104105-0699-4a49-a8c4-0941948495b9)  
-Đến bước này thì ta chỉ cần sửa giá trị boolean của isChampion thành 1 rồi encode lại dán vô cookie truy cập lại trang web =>flag



