import pandas as pd

dic = {
    "col 1": [1, 2, 3],
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}
df = pd.DataFrame(dic)

print("使用字典來建立df：")


df.insert(2, column="經度", value=[88, 72, 74])
df.at[1, "math"] = 55  #修改索引值為1的math欄位資料
df.iat[1, 0] = "Larry"  #修改索引值為1的第一個欄位資料
print(df.head())
print(df['經度'][2])

