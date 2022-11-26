def sales(cars, customers) -> int:
    sales = 0
    carsSorted = sorted(cars)
    customersSorted = sorted(customers)
    carsSorted.reverse()
    customersSorted.reverse()
    print(carsSorted)
    print(customersSorted)
    sales = 0
    indexCustomer = 0
    for i in range(len(cars)):
        if carsSorted[i] <= customersSorted[indexCustomer]:
            indexCustomer += 1
            sales += 1
        else:
            pass
        if indexCustomer > len(customers)-1:
            break
    return sales

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5   