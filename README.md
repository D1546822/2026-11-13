# 2026-11-13
# 飲料價格
price = {
    "珍奶": 60,
    "紅茶": 30,
    "冬瓜茶": 25
}

# 初始庫存
stock = {
    "珍奶": 5,
    "紅茶": 3,
    "冬瓜茶": 6
}

# 訂單資料：編號、客人、飲料、數量
orders = [
    [1, "小美", "珍奶", 2],
    [2, "阿明", "紅茶", 2],
    [3, "小華", "珍奶", 3],
    [4, "小美", "紅茶", 2],
    [5, "阿明", "冬瓜茶", 4],
    [6, "小華", "紅茶", 1],
    [7, "小美", "珍奶", 1]
]

# 每位客人的消費金額
customer_spending = {}

# 每種飲料的訂單紀錄
drink_orders = {
    "珍奶": [],
    "紅茶": [],
    "冬瓜茶": []
}

# 被拒絕的訂單
rejected = []

# 總收入
total = 0

# 開始處理訂單
for no, name, drink, qty in orders:

    if stock[drink] >= qty:

        # 扣除庫存
        stock[drink] -= qty

        # 計算金額
        money = price[drink] * qty
        total += money

        # 記錄客人消費
        if name not in customer_spending:
            customer_spending[name] = 0

        customer_spending[name] += money

        # 記錄飲料訂單
        drink_orders[drink].append(name)

        print(f"訂單{no}：{name} {drink} {qty}杯，成功，{money}元")

    else:
        # 庫存不足，拒絕整筆訂單
        rejected.append(name + "-" + drink)

        print(f"訂單{no}：{name} {drink} {qty}杯，庫存不足，拒絕")

# 找出消費最高的客人
top_name = ""
top_money = 0

for name, money in customer_spending.items():
    if money > top_money:
        top_money = money
        top_name = name

# 輸出結果
print("\n===== 今日結帳結果 =====")

print("剩餘庫存：", stock)

print("今日總收入：", total, "元")

print("每位客人消費：", customer_spending)

print("各飲料訂單：", drink_orders)

print("被拒絕的訂單：", rejected)

print("今晚消費最高：", top_name, top_money, "元")
