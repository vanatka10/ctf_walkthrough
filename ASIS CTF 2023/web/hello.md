![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/733f65ba-b5e5-4004-97d7-a25d190a08a1)
trong file nguồn có 2 hàm cần lưu ý là basename() and readFileSync():  cả hai đều có chức năng đọc tên tệp nhưng
+basename() vẫn sẽ đọc tiếp nếu gặp null byte  
+readFileSync() sẽ kết thúc việc đọc nếu gặp null bype đó còn được gọi là string terminator.  
