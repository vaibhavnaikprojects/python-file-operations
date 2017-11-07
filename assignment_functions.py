STARTING_YEAR=1993
ENDING_YEAR=2013
STARTING_MONTH=1
ENDING_MONTH=12
def get_year(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])

def get_month(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[0])

def get_price(str):
    items = str.split(':')
    return float(items[1])

def get_average_yearly(gas_list,year):
    total=0
    count=0
    for line in gas_list:
        if  get_year(line)== year:
            total += get_price(line)
            count += 1
    return total / count

def get_average_monthly(gas_list,month):
    total=0
    count=0
    for line in gas_list:
        if  get_month(line)== month:
            total += get_price(line)
            count += 1
    return total / count

def get_lowest_price_yearly(gas_list,year):
    minimum_value=99
    for line in gas_list:
        if  get_year(line)== year:
            if get_price(line)<minimum_value:
                minimum_value=get_price(line)
    return minimum_value
    
def get_highest_price_yearly(gas_list,year):
    max_value=0
    for line in gas_list:
        if  get_year(line)== year:
            if get_price(line)>max_value:
                max_value=get_price(line)
    return max_value

def sorted_lowest_highest(gas_list):
    price_dict = {}
    for line in gas_list:
        date,price=line.rstrip().split(":")
        price_dict[date] = price
    outfile = open('LowestToHighest.txt','w')
    sorted_values=sorted(price_dict.items(), key=get_value,reverse=False)
    for date, price in sorted_values:
            outfile.write(date+ ': '+price +'\n')
    outfile.close()
    print('file created LowestToHighest.txt')
    
def sorted_highest_lowest(gas_list):
    price_dict = {}
    for line in gas_list:
        date,price=line.rstrip().split(":")
        price_dict[date] = price
    outfile = open('HighestToLowest.txt','w')
    sorted_values=sorted(price_dict.items(), key=get_value,reverse=True)
    for date, price in sorted_values:
            outfile.write(date+ ': '+price +'\n')
    outfile.close()
    print('file created HighestToLowest.txt')        
        
def get_value(x):
    return x[1]
        
def main():
    gas_file = open('GasPrices.txt', 'r')
    gas_list = gas_file.readlines()
    gas_file.close()
    print('Average prices per month')
    for i in range(STARTING_MONTH, ENDING_MONTH + 1):
        print('The average price in month ', i,' was $', format(get_average_monthly(gas_list, i), '.2f'),sep = '')
    
    print('Lowest/Average/Highest price per year')
    for i in range(STARTING_YEAR, ENDING_YEAR + 1):
        print('The lowest price in ', i,' was $', get_lowest_price_yearly(gas_list, i))
        print('The average price in ', i,' was $', format(get_average_yearly(gas_list, i), '.2f'),sep = '')
        print('The highest price in ', i,' was $', get_highest_price_yearly(gas_list, i))
    sorted_lowest_highest(gas_list)
    sorted_highest_lowest(gas_list)

main()