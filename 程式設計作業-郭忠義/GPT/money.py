import datetime

def parse_prize_period(period_str):
    year, months = period_str.split('-')
    start_month, end_month = map(int, months.split(','))
    year = int(year)
    start_date = datetime.date(year, start_month, 1)
    end_date = datetime.date(year, end_month, 1) + datetime.timedelta(days=31)
    end_date = datetime.date(end_date.year, end_date.month, 1) - datetime.timedelta(days=1)
    return start_date, end_date

def validate_invoice(invoice_number, date, prize_period):
    if len(invoice_number) != 8 or not int(invoice_number) % 1 == 0:
        return "invalid format"
    try:
        invoice_date = datetime.date.fromisoformat(date)
    except ValueError:
        return "invalid format"
    if not (prize_period[0] <= invoice_date <= prize_period[1]):
        return "outside prize period"
    return "valid"

def check_prizes(invoice_number, prize_numbers):
    special_prize, grand_prize, *first_prizes = prize_numbers
    prize_levels = [
        ("Special Prize", 10_000_000, special_prize),
        ("Grand Prize", 2_000_000, grand_prize),
        ("1st Prize", 200_000, first_prizes),
        ("2nd Prize", 40_000, [num[-7:] for num in first_prizes]),
        ("3rd Prize", 10_000, [num[-6:] for num in first_prizes]),
        ("4th Prize", 4_000, [num[-5:] for num in first_prizes]),
        ("5th Prize", 1_000, [num[-4:] for num in first_prizes]),
        ("6th Prize", 200, [num[-3:] for num in first_prizes]),
    ]
    for prize_name, prize_value, prize_number in prize_levels:
        if isinstance(prize_number, list):
            if any(invoice_number.endswith(num) for num in prize_number):
                return prize_name, prize_value
        else:
            if invoice_number == prize_number:
                return prize_name, prize_value
    return None, 0

def main():
    s = input().strip().split()
    prize_numbers = s[:5]
    prize_period = parse_prize_period(s[5])
    n = int(input().strip())
    
    invoices = [input().strip().split() for _ in range(n)]
    store_wins = {}
    max_profit_invoice = None
    results = []
    has_winner = False

    for invoice in invoices:
        invoice_number, store_id, date, amount = invoice
        amount = int(amount)
        validation_result = validate_invoice(invoice_number, date, prize_period)
        
        if validation_result == "invalid format":
            results.append(f"{invoice_number} has an invalid format.")
        elif validation_result == "outside prize period":
            results.append(f"{invoice_number} is outside the prize period.")
        else:
            prize_name, prize_value = check_prizes(invoice_number, prize_numbers)
            if prize_value > 0:
                has_winner = True
                profit = prize_value - amount
                results.append(f"{invoice_number} won: {prize_name}: {prize_value} TWD Profit: {profit} TWD")
                
                # 記錄店家中獎數量
                store_wins[store_id] = store_wins.get(store_id, 0) + 1
                
                # 找出最高獲利發票
                if not max_profit_invoice or profit > max_profit_invoice["profit"]:
                    max_profit_invoice = {
                        "invoice_number": invoice_number,
                        "store_id": store_id,
                        "date": date,
                        "prize_value": prize_value,
                        "profit": profit
                    }
            else:
                results.append(f"{invoice_number} did not win anything.")

    # 結果輸出
    print("\n".join(results))
    if not has_winner:
        print("No invoices won any prize.")
    else:
        most_winning_store = max(store_wins.items(), key=lambda x: x[1])
        print(f"Store {most_winning_store[0]} opened the most winning invoices: {most_winning_store[1]}")
        max_invoice = max_profit_invoice
        print(f"Invoice with the highest profit: {max_invoice['invoice_number']}, from store {max_invoice['store_id']}, purchase date {max_invoice['date']}, total prize {max_invoice['prize_value']} TWD, profit {max_invoice['profit']} TWD")

if __name__ == "__main__":
    main()
