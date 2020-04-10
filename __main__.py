import collatz_conjecture as cc

def main():
    current, steps = cc.collatz_conjecture(input('Enter a number greater than 1: '))
    print(f'Result: {current}')
    print(f'Steps to result: {steps}')

if __name__ == '__main__':
    main()
