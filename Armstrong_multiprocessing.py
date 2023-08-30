
#Armstrong using multiprocessing an experiment 

from multiprocessing import Pool, cpu_count #not sure so much it is a demo

def checkNumber(number):
    convert = str(number)
    len_number = len(convert)
    sum_numbers = 0
    for i in range(len_number):     
        sum_numbers += int(convert[i]) ** len(convert)

    return number if number == sum_numbers else None

def main():
    pool_size = cpu_count()  # Number of cores available
    with Pool(pool_size) as p:
        # Using a generator expression to iterate from 0 to 14000000
        results = p.map(checkNumber, (i for i in range(0, 84000000)))

    # filter results 
    for result in filter(None, results):
        print(result)

if __name__ == '__main__':
    main()
