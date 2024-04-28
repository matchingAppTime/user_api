# DB設計

### テーブル名: USER_INFO
#### カラム
* USER_ID
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