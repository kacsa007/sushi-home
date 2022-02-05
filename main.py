import sys
from utils import get_bills_from_input, print_bill

# This can be optimized and using a test module instead pytest or unittest ->
# had no time to develop it, although I started it


def main(): 
    
    try:
        input_txt_path = sys.argv[1]
    except IndexError:
        raise Exception('\nProblem with input argument. \nRead README.MD '
                        'to know about the expected input argument.\nUsage: %s <inputs.txt>' % sys.argv[0])

    bills = get_bills_from_input(input_txt_path)
    print_bill(bills)
    
    return 0


if __name__ == '__main__':
    import time

    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
