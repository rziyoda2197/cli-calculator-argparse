import argparse

def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mul':
        return num1 * num2
    elif operation == 'div':
        if num2 != 0:
            return num1 / num2
        else:
            return "Bo'lishda 0 ga bo'lish qilmaslik kerak!"
    else:
        return "Noto'g'ri amal kiritildi!"

def main():
    parser = argparse.ArgumentParser(description='CLI kalkulyator')
    parser.add_argument('--operation', type=str, help='Amal (add/sub/mul/div)')
    parser.add_argument('--num1', type=float, help='Birinchi son')
    parser.add_argument('--num2', type=float, help='Ikkinchi son')
    args = parser.parse_args()

    if args.operation and args.num1 and args.num2:
        print(calculator(args.num1, args.num2, args.operation))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

Kodni ishga tushirish uchun quyidagicha buyruqlarni bosingiz:

```bash
python calculator.py --operation add --num1 10 --num2 5
python calculator.py --operation sub --num1 10 --num2 5
python calculator.py --operation mul --num1 10 --num2 5
python calculator.py --operation div --num1 10 --num2 5
python calculator.py --operation div --num1 10 --num2 0
python calculator.py --operation add
