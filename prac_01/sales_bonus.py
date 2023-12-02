# 2. Debugging
#
# TEN PERCENT BONUS = 0.1
# FIFTEEN PERCENT BONUS = 0.15
#
# get sales
# while sales >= 0
#     if sales < 1000
#         bonus = sales * TEN PERCENT BONUS
#     else
#         bonus = sales * FIFTEEN PERCENT BONUS
#
#     display bonus
# get sales

TEN_PERCENT_BONUS = 0.1
FIFTEEN_PERCENT_BONUS = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * TEN_PERCENT_BONUS
    else:
        bonus = sales * FIFTEEN_PERCENT_BONUS

    print(f"Bonus: ${bonus:.2f}")
sales = float(input("Enter sales: $"))
