import math

def main():
    mode = int(input("Mode (enter without parentheses)\n(1) Rate\n(2) Time\n")) % 2
    experiment_c = int(input("Number of experiments:\n"))
    master_table = []

    for i in range(3):
        print(f"Compound #{i}" * (i < 2) + "Rates" * (mode) * (i == 2) + "Times" * (not mode) * (i == 2))
        col = []
        for j in range(experiment_c):
            col.append(float(input()))
        master_table.append(col)

    orders = []
    order_total = 0
    for i in range(2):
        other_col = not i
        row_1, row_2 = find_matching(master_table[other_col])
        if mode:
            orders.append(round(math.log(master_table[2][row_1]/master_table[2][row_2], master_table[i][row_1]/master_table[i][row_2])))
        else:
            orders.append(round(math.log(master_table[2][row_2]/master_table[2][row_1], master_table[i][row_1]/master_table[i][row_2])))
        order_total += orders[i]
        print(f"Order of compound #{i}: {orders[i]}")
    print(f"Total order of reaction: {order_total}")
    constant = master_table[2][0]/(master_table[0][0] ** orders[0] * master_table[1][0] ** orders[1])
    print(f"Reaction rate constant: {constant}")
    
def find_matching(col):
    unique_values = []
    for y, x in enumerate(col):
        if x not in unique_values:
            unique_values.append(x)
        else:
            return [b for b, a in enumerate(col) if a == x][0:2]

if __name__ == "__main__":
    main()
