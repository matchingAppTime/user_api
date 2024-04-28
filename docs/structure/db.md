# DB設計

### テーブル名: USER_INFO
#### カラム
* ID
  * INT
  * user_infoカラムにおける自動採番ID

* COGNITO_ID
  * VARCHAR(100)
  * cognitoで登録されたユーザーのハッシュ
    
* EMAIL
  * VARCHAR(200)
  * cognitoで取得したメアド
    
* NICK_NAME
  * VARCHAR(30)
  * ニックネーム
  
* SEX
  * INT(1)
  * 性別 0:男 1:女 2:その他
  
* BIRTH
  * INT(8)
  * 生年月日　19990203のような8桁
  
* BAN_STATUS
  * TINYINT(1)
  * BANしているかどうか、正常:0 BAN:1
  

```
mysql> DESC USER_INFO;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| cognito_id | varchar(200) | YES  |     | NULL    |                |
| email      | varchar(200) | YES  |     | NULL    |                |
| nick_name  | varchar(30)  | YES  |     | NULL    |                |
| sex        | int          | YES  |     | NULL    |                |
| birth      | int          | YES  |     | NULL    |                |
| ban_status | tinyint(1)   | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
```