# Zesty Zomato: The Zomato Chronicles
import json;

arr = '';

try:
    with open('item.json', 'r') as json_content:
        arr = json.load(json_content);

except FileNotFoundError:
    print('File not Found');
    

def updateJsonFile(): # This function is used to update data in JSON file
    try:
        with open('item.json', 'w') as json_content:
            json.dump(arr, json_content);
        return True
    except:
        return False;

def displayMenu(): # This function is used to display Items that are present in the menu
    print('============================================\n')
    print('MENU');
    print('************************************');
    for i in range(len(arr['items'])):
        print(f'{arr["items"][i]["id"]}: {arr["items"][i]["name"]} Rs.{arr["items"][i]["price"]}');
    print('************************************');
    print('\n============================================')

def addItem(): # This function is used to Add a new Item in the menu
    itemDict = {};
    name = input('Enter a name for the Item: ');
    price = int(input('Enter a price for the Item: '));
    qty = int(input('Enter the quantity: '));
    itemDict['name'] = name;
    itemDict['price'] = price;
    itemDict['qty'] = qty;
    itemDict['id'] = id(name);
    arr['items'].append(itemDict);
    check = updateJsonFile();
    if check:
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        print('Snack Added Successfully');
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    else: 
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        print('Something went wrong while adding a new item in the menu');
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');


def addOrder(): # This function is used to place an order
    cus = input("Enter a customer's name: ");
    itemId = None;
    try:
        itemId = list(map(int, input("Enter Item Id [use ',' to separate muliple ids]: ").split(', ')));
    except ValueError:
        print('Please enter valid Ids');
        return addOrder();
    totalPrice = 0;
    itemEl = [];
    count = 0;
    for i in range(len(arr["items"])):
        for j in itemId: 
            if j == arr["items"][i]["id"]:
                count += 1;
                if(arr["items"][i]["qty"]==0):
                    print('\n#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#\n')
                    print(f'Item with id: {j} is not Available right now.');
                    print('\n#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#\n')
                    return;
                arr["items"][i]["qty"] = arr["items"][i]["qty"] - 1;
                itemEl.append(arr["items"][i]["name"]);
                totalPrice += arr["items"][i]["price"];
    if count == 0:
        print('Wrong Ids provided.');
        return;
    orderDict = {};
    orderDict["customer"] = cus;
    orderDict["orderId"] = id(cus);
    orderDict["items"] = itemEl;
    orderDict["totalPrice"] = totalPrice;
    orderDict["status"] = 'received';
    arr["orders"].append(orderDict);
    arr["totalSales"] = arr["totalSales"]+totalPrice;
    check = updateJsonFile();
    if check:
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        print('Order Confirmed.');
        print('\n#########################################\n');
        print('Order Details: ');
        for i in orderDict:
            if i=='totalPrice':
                print(f"{i}: Rs.{orderDict[i]}");
                continue;
            elif i=='items':
                print(f"{i}: {', '.join(orderDict[i])}");
                continue;
            print(f"{i}: {orderDict[i]}");
        print('\n#########################################');
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    else:
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        print('Something went while taking your order.');
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');


def displaySales(): # This function is used to display Total Sales
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    print(f'Total Sales: Rs.{arr["totalSales"]}')
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');

def removeItem(): # This function is used to remove an Item from the Menu
    _id = int(input('Enter the id of the element which has to be removed: '));
    index = None;
    for i in range(len(arr["items"])):
        if arr["items"][i]["id"] == _id:
            index = i;
            break;
    print(index);
    arr["items"].pop(index);
    check = updateJsonFile();
    if check:
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        print('Item Removed from the Menu');
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    else:
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        print('Something went wrong while updating the new Menu');
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
        
        

def updateAvailability(): # This function is used to update the quantity of an item
    _id = int(input('Enter the id of the product whose availability has to be changed: '));
    newQty = int(input('Enter quantity: '));
    for i in range(len(arr["items"])):
        if _id == arr["items"][i]["id"]:
            arr["items"][i]["qty"] = newQty;
            check = updateJsonFile();
            if check:
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
                print("Availability changed");
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
            else:
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
                print('Something went wrong while updating the new Menu');
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
            return;
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    print('No Product Found');
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');

def updateOrder(): # This function is used to update status of an order
    _id = int(input('Enter Order Id: '));
    status = input('Enter status of the order: ');
    for i in range(len(arr['orders'])):
        # print(arr["orders"][i]);
        if arr["orders"][i]['orderId'] == _id:
            arr["orders"][i]["status"] = status;
            check = updateJsonFile();
            if check:
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
                print("Status changed");
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
            else:
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
                print('Something went wrong while updating the status of an order');
                print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
            return;
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    print('No Product Found');
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');


def displayAllOrders(): # This function is used to display all orders
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');
    for j in arr['orders']:
        print('\n#########################################\n');
        for i in j:
            if i=='totalPrice':
                print(f"{i}: Rs.{j[i]}");
                continue;
            elif i=='items':
                print(f"{i}: {', '.join(j[i])}");
                continue;
            print(f"{i}: {j[i]}");
        print('\n#########################################\n');
    print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n');


def main(): # This is the main function
    while True: 
        print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*= //** //** //** //** //** //** //** // //=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
        print('1. To See the Menu');
        print('2. To Add a Snack');
        print('3. To Add an Order');
        print('4. To Remove a Snack from the Menu');
        print('5. To Update availablity of an Item');
        print('6. To Display Total Sales');
        print('7. To Update an order');
        print('8. To Display all Orders');
        print('9. To Close the application');
        print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*= //** //** //** //** //** //** //** // //=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')

        choice = input('Enter a valid options between 1-9: ');

        if choice == '1':
            displayMenu();
        elif choice == '2':
            addItem();
        elif choice == '3':
            addOrder();
        elif choice == '4':
            removeItem();
        elif choice == '5':
            updateAvailability();
        elif choice == '6':
            displaySales();
        elif choice == '7':
            updateOrder();
        elif choice == '8':
            displayAllOrders();
        elif choice == '9':
            print('Thank you for coming to Zesty Zomato.');
            break;
        else:
            print('Please Enter a valid option');

if __name__ == "__main__": 
    print('Welcome to Zesty Zomato');
    main();