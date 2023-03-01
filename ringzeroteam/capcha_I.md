capcha I
-Có vẻ capcha I->IV đều ở trong trang web này, có điều mục tiêu chính hôm nay thì ta sẽ cùng giải quyết bài capcha I.
-Ta cần phải capcha 1000 lần mới có flag. Mỗi lần capcha sai thì phải ghi lại từ đầu thế nên việc viết capcha bằng tay không là điều dường như không thể(trừ khi mấy ông rảnh)
![image](https://user-images.githubusercontent.com/126310360/222168624-ad987a01-2b9a-4796-afc5-6bdb7f34e175.png)
- Sau một hồi không tìm ra được lỗ hổng trên trang web, mình bắt đầu tìm kiếm trên mạng về cách vượt qua. hmm... Có vẻ phải dùng bot rồi ;V.
- Một số bài tương tự cũng phải viết code để đọc text từ ảnh -> post capcha.
- Tôi có tìm thấy đoạn code py chuyển lấy text từ img.
```
- from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"csv\sample_text.png"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

# Displaying the extracted text
print(text[:-1])

```
link file tesseract.exe: https://github.com/UB-Mannheim/tesseract/wiki
Rồi bắt tay vào việc thôi
