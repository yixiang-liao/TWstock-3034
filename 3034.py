import twstock
import requests

def get_stock(stock_id):
    return twstock.Stock(stock_id)

def line_notify(stock):
    token = "ZOYXC8nXCsgpIOu5MAO3Xl9pXRA8TzN6BZ1tqjcEeNC"
    message = ""
    message += f'\n今日聯詠(3034)總成交股數(單位:股):{stock.capacity[-1]}'
    message += f'\n今日聯詠(3034)總成交金額(單位:元):{stock.turnover[-1]}'
    message += f'\n今日聯詠(3034)開盤價:{stock.open[-1]}'
    message += f'\n今日聯詠(3034)最高價:{stock.high[-1]}'
    message += f'\n今日聯詠(3034)最低價:{stock.low[-1]}'
    message += f'\n今日聯詠(3034)收盤價:{stock.price[-1]}'
    message += f'\n今日聯詠(3034)漲跌價差:{stock.change[-1]}'
    message += f'\n今日聯詠(3034)成交筆數:{stock.transaction[-1]}'

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    x = requests.post(url=line_url, headers=line_header, data=line_data)
    print(x.status_code)


if __name__ == '__main__':
    stock_id = '3034'
    stock = get_stock(stock_id)
    line_notify(stock)