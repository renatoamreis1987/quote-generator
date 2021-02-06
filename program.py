investment = input("Please insert your investment amount: ")
investment = float(investment)
rate = input("Interest rate: ")
rate = float(rate) * .01


for i in range(10):
    investment = investment + (investment * rate)
    print("In the {} year your earnings: {:.2f}".format(i, investment))
