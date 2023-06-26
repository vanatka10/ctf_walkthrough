đây là 1 bài web đơn giản , file nguồn sẽ có 2 loại đó là flash (của python) là php . Mục tiêu chính là cấp tier gold cho tài khoản ở trang flash và đăng nhập nó ở web php để lấy flag. Bởi vì có đặt điều kiện tier khiến cho ta không thể tạo tài khoản tier gold được, nên ta cần tìm cách khai thác.
có điều khá kì lạ ở đây
```
def signup_post():
    raw_request = request.get_data()
    username = request.form.get('username')
    password = request.form.get('password')
    tier = models.Tier(request.form.get('tier'))

    if(tier == models.Tier.GOLD):
        flash('GOLD tier only allowed for the CEO')
        return redirect(url_for('authorized.signup'))

    if(len(username) > 15 or len(username) < 4):
        flash('Username length must be between 4 and 15')
        return redirect(url_for('authorized.signup'))

    user = models.User.query.filter_by(username=username).first()

    if user:
        flash('Username address already exists')
        return redirect(url_for('authorized.signup'))

    new_user = models.User(username=username, 
        password=generate_password_hash(password, method='sha256'), tier=tier.name)

    db.session.add(new_user)
    db.session.commit()

    requests.post(f"http://{PHP_HOST}:1337/account_migrator.php", 
        headers={"token": TOKEN, "content-type": request.headers.get("content-type")}, data=raw_request)
    return redirect(url_for('authorized.login'))
```
trong đoạn code trên ở raw_request nó không có bảo mật xác thực nên ta có thể thêm 1 lần biến tier nữa chẳng hạn
ví dụ data request 
```
username=vanatka1&password321123&tier=blue&tier=gold
```
tạo xong tài khoản thì qua trang php lấy cờ thôi
![image](https://github.com/vanatka10/ctf_walkthrough/assets/126310360/b79ad39c-00f6-46f3-b0b3-243090480c83)
