#!/usr/bin/python
#hmmmmm....
import argparse

def find_max_profit(prices):
  if len(prices) == 2:
    return prices[1] - prices[0]
  # lowest = prices[0]
  # max_profit = prices[len(prices)] - prices[len(prices) - 1]
  # for i in range(0, len(prices)):
  #   if prices[i] > prices[i + 1]:
  #     prices[i], prices[i + 1] = prices[i + 1], prices[i]
  #   if prices[i + 1] - prices[i] < lowest:
  #     lowest = prices[i + 1] - prices[i]
  #   print(f'Loop: {i}, lowest: {lowest}')
  # lowest = min(prices)
  # highest = max(prices)
  # max_profit = highest - lowest
  # print(f'{max_profit} = {highest} - {lowest}')

  ##### Iterative:
  # buy = prices[0]
  # max_profit = prices[1] - buy
  # for i in range(1, len(prices)):  #<--- start at 1 instead of 0 fixed it?!
  #   current_price = prices[i]
  #   if (current_price - buy) > max_profit:
  #     max_profit = current_price - buy
  #   for j in range(i, len(prices)):
  #     next_price = prices[j]
  #     if (next_price - buy) > max_profit:
  #       max_profit = next_price - buy
  #   buy = prices[i]

  # return max_profit

  ##### Recursive:
  buy = prices[0]
  max_profit = prices[1] - prices[0]
  for i in range(1, len(prices)):
    current_price = prices[i]
    if (current_price - buy) > max_profit:
      max_profit = current_price - buy  #set new max_profit if found
      print(f'max profit: {max_profit}')
  return max(max_profit, find_max_profit(prices[1:])) #compare max of current max_profit vs next_price


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))