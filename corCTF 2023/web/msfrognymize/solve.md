# solve
## LFI
trong file docker ta thấy cờ được đặt ở thư mục gốc
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/8bc6c56d-9bfd-4996-ae1f-daab0be0ebdf)  
khi upload ảnh xong ta sẽ được redirect đến /anonymized/<image_file>  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/6e8ae69c-8e01-46d1-99ec-83225c45497b)  
trong route này dựa vào url ta có thể truy cập được các file ảnh . Nhưng có 1 vấn đề ở đây khi sử dụng os.path.join()
Theo document của python:

[os.path.join()](https://docs.python.org/3/library/os.path.html#os.path.join)
**If a segment is an absolute path (which on Windows requires both a drive and a root), then all previous segments are ignored and joining continues from the absolute path segment.**
Điều này xảy ra vì trên hệ điều hành Windows, dấu \ được sử dụng làm ký tự phân tách thư mục trong đường dẫn tuyệt đối. Do đó, khi bạn thêm một dấu / vào đầu của phần tử cuối cùng, nó sẽ được xem như một đường dẫn tuyệt đối bắt đầu từ gốc thư mục của ổ đĩa hệ thống  
ví dụ:
```
>>> import os
>>> os.path.join('uploads/', '/flag.txt')
'/flag.txt'
>>> os.path.join('uploads/', 'flag.txt')
'uploads/flag.txt'
```
## bypass filter
unquote() chỉ decode url 1 lần nên ta encode 2 lần là bypass được
## payload
/anonymized/%252Fflag.txt
