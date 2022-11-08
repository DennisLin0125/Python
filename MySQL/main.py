import pymysql

# 連結 SQL
connect_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', charset='utf8', db='pydb')

with connect_db.cursor() as cursor:
    sql = """
    DELETE FROM Test WHERE Name='John'
    """

    # 執行 SQL 指令
    cursor.execute(sql)

    # 提交至 SQL
    connect_db.commit()

    # ----------

    sql = """
    SELECT * FROM Member
    """

    # 執行 SQL 指令
    cursor.execute(sql)

    # 取出全部資料
    data = cursor.fetchall()
    print(data)

# 關閉 SQL 連線
connect_db.close()