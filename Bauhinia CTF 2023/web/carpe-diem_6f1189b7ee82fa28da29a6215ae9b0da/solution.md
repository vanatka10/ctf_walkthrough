```
const idx = Math.floor(Math.random() * flag_content.length);
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


