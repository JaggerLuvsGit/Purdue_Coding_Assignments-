 

#function to capture input from a user, with error correction to stop the user from inputing a negative amount of numbers <0
def order_capture():
  order = int(input("Enter the number of Shamwowzers sold: "))
  while True:
    try:
      if order < 0:
        print("Check for negative balances")
      else:
        break
    except ValueError:
      print("verify that the number is an actual number")
  return order

# function to caluculate total, if order is less than 10, subtotal is 13 per each, if order is 10 or more, subtotal is 10 per each.
def subtotal(order):
  if order <= 9:
    subtotal = order * 13
  elif order >= 10:
    subtotal = order * 10
  return subtotal

# function to calculate shipping and handling.
def ship_hand(order):
  cost = order * 3
  return cost

# function calculating total of customer's order.
def total(ship_hand,subtotal):
  num = subtotal + ship_hand
  return num


# main function
def main():

  print("Welcome to Shamwowzer, the worlds most absorbent shammy!")
  ordered = order_capture()
  the_subtotal = float(subtotal(ordered))
  the_ship_hand = float(ship_hand(ordered))
  total_amount = float(total(the_subtotal,the_ship_hand))
  print(f"You ordered {ordered}. Your subtotal is ${the_subtotal}, shipping and handling is ${the_ship_hand}, and total amount due is ${total_amount}")


if __name__ == "__main__":

  main()

