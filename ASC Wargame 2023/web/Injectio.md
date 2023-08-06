# giới thiệu
Cũng không có gì ngoài 1 cái ảnh nhưng được gợi ý ở đây là ngay ở phần tên và tên file trên trang web /xchall.php .
# solution
 Đây là 1 bài php và có thể là command injection  
Bài này cũng phải tìm param như bài trước sau đó thực hiện injection  
Khi thay đổi parameter từ ?name= sang ?name[]= điều đó làm thay đổi parameter từ string sang array điều này gây ra lỗi và thể hiện ra rằng các giá trị của parameter đang được chuyển tới hàm eval()
Tiếp theo sử dụng các công cụ dirscan để tìm ra cờ là flag.php .Sử dụng kĩ thuật **php wrapper** để lấy bài flag
final solution  

```/xchal.php?name=".include($_GET['a']);$name="&a=php://filter/convert.base64-encode/resource=flag.php```  
or
```http://34.18.3.149:8000/xchal.php?name=`%22%26%26+var_dump(`base64%20flag.php`);%23;````
# Lưu ý sau khi giải những bài sau
