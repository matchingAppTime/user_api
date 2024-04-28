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
  * デフォルト: 2（非推奨）
  
* BIRTH
  * INT(8)
  * 生年月日　19990203のような8桁
  
* AREA
  * INT
  * 0: その他、未登録  
  * 1 ~ 48: 都道府県
    * この通りの並びでenum列挙 https://gist.github.com/Mo3g4u/c114db05a1646318bb8155415470675b
  * 48: 海外
  * デフォルト: 0
  
* INCOME
  * INT
  * 💰年収
  * 0 ~ 7のenum列挙
    * 0: 未設定、ひみつ
    * 1: 200万未満
    * 2: 200万 ~ 250万
    * 3: 250万 ~ 400万
    * 4: 400万 ~ 600万
    * 5: 600万 ~ 800万
    * 6: 800万 ~ 1000万
    * 7: 1000万以上
  * デフォルト: 0
  
* BAN_STATUS
  * TINYINT(1)
  * BANしているユーザーかどうか、正常:0 BAN:1
  * デフォルト: 0
  

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