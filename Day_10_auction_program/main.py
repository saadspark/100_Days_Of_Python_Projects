from art import logo

print(logo)
start_bidding = True
data = []
while start_bidding :
   
    name = input("What is your name? ")
    price = int(input("What is your Bid price? $ "))
    data.append({'name':name,'price':price})
    
    bidder = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if bidder == 'no':
        price = 0
        name = ''
        for key in data :
            for value in key :
                if price < key['price'] :
                    price = key['price']
                    name = key['name']
                    
        print(f"The winner is {name} with a bid of $ {price}.")            
        start_bidding = False
    
    

