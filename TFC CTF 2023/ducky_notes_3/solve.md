# Solve:
# 1. Register user
# 2. Login
# 3. Create post with empty title and XSS payload in content
# 4. Create path traversal username
# 5. Login as path traversal user
# 6. Report username's posts
# 7. Admin is rediect to /posts
# 8. Error occurs when trying to load post with empty title
# 9. XSS payload is executed

## Giải thích: 

payload xss: 
-đoạn script có tác dụng gửi dữ liệu từ máy chủ cục bộ ra bên ngoài
-hàm fetch để gửi một yêu cầu đến URL http://localhost:1337/posts/view/admin. Phản hồi từ yêu cầu này sau đó được chuyển thành văn bản và truyền cho một hàm fetch khác, gửi một yêu cầu đến URL https://requestinspector.com/inspect/01h6qa9edbmw2xv4f9ra1wkny7 với văn bản phản hồi từ yêu cầu đầu tiên được thêm vào dưới dạng tham số truy vấn.

Bài đăng tải trọng của chúng tôi sẽ không có khóa “tiêu đề” trong đối tượng kết quả của nó nên một Ngoại lệ được đưa ra. Điều này dẫn đến một trang lỗi 500 với nội dung của chúng tôi dưới dạng tải trọng XSS

## flag:
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/a820585f-8618-405e-9652-72c4298bc5ad)
