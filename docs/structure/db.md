# DB設計

## テーブル名: USER_INFO
### 外部利用パラメータ（表示したりする）
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
  * 性別 
    * 1:男
    * 2:女
    * 0:その他
  * デフォルト: 0（非推奨）
  
* BIRTH
  * INT(8)
  * 生年月日　19990203のような8桁
  
* HEIGHT
  * INT
  * 0: 未登録
  
* BODY
  * INT
  * 体型
  * 0: 未登録
    * 1 ~ 7のenum
    * 1: やせている
    * 2: やや痩せている
    * 3: 普通
    * 4: ややぽっちゃり
    * 5: ぽっちゃり
  
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
  
* ABOUT_ME
  * VARCHAR(1000)
  * 自己紹介（1,000文字以内）
  
### 言いにくいパラメータ（基本外に出さないが検索などで利用可能）

* 


### 内部利用パラメータ（外に出さない）

* PREM_STATUS
  * INT(1)
  * プレミアム会員フラグ
    * 0: 通常会員
    * 1: プレミアム会員
    * 2: その他、優遇ユーザーなど
  * デフォルト: 0
  
* IS_DELETE
  * INT(1)
  * 論理削除
    * 0: 会員
    * 1: 退会済み
  * デフォルト: 0
  
* PENALTY_STATUS
  * INT(1)
  * ペナルティ状況
    * 0: ペナルティなし
    * 1: イエローカード
    * 2: レッドカード
  
* FREE_POINT
  * INT
  * アプリ内ポイント
  * 無償配布分
  
* PAID_POINT
  * INT
  * アプリ内ポイント
  * 有料購入分
  
* BAN_STATUS
  * TINYINT(1)
  * BANしているユーザーかどうか、BAN:0 正常:1
  * デフォルト: 1
  

```
+----------------+---------------+------+-----+---------+----------------+
| id             | int           | NO   | PRI | NULL    | auto_increment |
| cognito_id     | varchar(200)  | YES  |     | NULL    |                |
| email          | varchar(200)  | YES  |     | NULL    |                |
| nick_name      | varchar(30)   | YES  |     | NULL    |                |
| sex            | int           | NO   |     | 0       |                |
| birth          | int           | YES  |     | NULL    |                |
| area           | int           | NO   |     | 0       |                |
| income         | int           | NO   |     | 0       |                |
| height         | int           | NO   |     | 0       |                |
| body           | int           | NO   |     | 0       |                |
| about_me       | varchar(1000) | YES  |     | NULL    |                |
| prem_status    | int           | NO   |     | 0       |                |
| is_delete      | int           | NO   |     | 0       |                |
| penalty_status | int           | NO   |     | 0       |                |
| free_point     | int           | NO   |     | 0       |                |
| paid_point     | int           | NO   |     | 0       |                |
| ban_status     | tinyint(1)    | YES  |     | NULL    |                |
+----------------+---------------+------+-----+---------+----------------+
```