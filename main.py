from typing import Iterable

from nicegui import ui
import redis


# r = redis.Redis(host='localhost', port=6379, db=0)
# data = r.get('data')
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", "DOGEUSDT", "DOTUSDT", "UNIUSDT", "BCHUSDT", "LTCUSDT"]
positions_opened = [35,31,231,3123,131,23,23,312,57,831]
number_positions = [10.32, 20.54, 30.2, 40, 50, 60, 80, 100, 90, 100]
time_position_opened = ["time", "time", "time", "time", "time", "time", "time", "time", "time", "time"]
time_in_position = ["time", "time", "time", "time", "time", "time", "time", "time", "time", "time"]
time_till_profit = ["not sure","not sure","not sure","not sure","not sure","not sure","not sure","not sure","not sure","not sure"]
profit_loss = [5,-5,10,-20.5, 10, 20, -0.30, 40, 50, 60]
profolio_size = 1000
position_size_percentage = [round((x/profolio_size*100),2) for x in number_positions]

def label_generator(data):
    for _ in data:
        yield ui.label(f'{_}$')
#risk reward  stop loss/ take profit
#suppose to be more like data.get(symbol)
def label(text):
     return ui.label(text)

with ui.element("div").classes('w-full').style(
        "background-color: black; color: white; display:flex; height: max-content;"
):

     with ui.element("div").style("flex:1; display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Symbol")
          symbol_labels = [ui.label(_) for _ in symbols]
          ui.label(len(symbols)).style("font-size: 24px;")


     with ui.element("div").style("flex:1; display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Positions Opened")
          position_open_labels = [ui.label(_) for _ in positions_opened]
          ui.label(sum(positions_opened)).style("font-size: 24px;")

     with ui.element("div").style("flex:1;  display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Position size$")
          list(map(lambda x: ui.label(f'{x}$'), number_positions))
          label_generator(number_positions)
          ui.label(sum(number_positions)).style("font-size: 24px;")


     with ui.element("div").style("flex:1;  display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Position size%")
          list(map(lambda x: ui.label(f"{(x/profolio_size*100)}%"), number_positions))
          ui.label(f"{round((sum(number_positions)/profolio_size*100), 2)}%").style("font-size: 24px;")

     with ui.element("div").style("flex:1;  display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Time in position")
          time_in_position_labels = [ui.label(_) for _ in time_in_position]
          ui.label("average time in position")

     with ui.element("div").style("flex:1;  display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Till till profit")
          till_profit_labels = [ui.label(_) for _ in time_till_profit]
          ui.label("average time till profitable")

     with ui.element("div").style("flex:1;  display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Profit/Loss")
          list(map(lambda x: ui.label(x).style("color: green;") if x > 0 else ui.label(x).style("color: red;"), profit_loss))
          apply_style = lambda x: ui.label(x).style("color: green; font-size: 24px;") if x > 0 else ui.label(x).style("color: red; font-size: 24px;")
          apply_style(sum(profit_loss))

     columns = [
          {'name': 'symbol', 'label': 'Symbol', 'field': 'symbol', 'required': True, 'align': 'left'},
          {'name': 'positions opened', 'label': 'Positions Opened', 'field': 'positions opened', 'sortable': True},
          {'name': 'position size', 'label': 'Position size', 'field': 'position size', 'sortable': True},
          {'name': 'position size%', 'label': 'Position size%', 'field': 'position size%', 'sortable': True},
          {'name': 'time in position', 'label': 'Time in position', 'field': 'time in position', 'sortable': True},
          {'name': 'till till profit', 'label': 'Till till profit', 'field': 'till till profit', 'sortable': True},
          {'name': 'profit/loss', 'label': 'Profit/Loss', 'field': 'profit/loss', 'sortable': True},
     ]
     rows = [{'symbol': symbol,
              'positions opened': opened,
              'position size': size,
              'position size%': percentage,
              'time in position': time,
              'till till profit': till,
              'profit/loss': pl}
             for symbol, opened, size, percentage, time, till, pl in
             zip(symbols, positions_opened, number_positions,position_size_percentage, time_in_position, time_till_profit, profit_loss)]

     # Printing the extracted rows
     for row in rows:
          print(row)
     ui.table(columns=columns, rows=rows, row_key='name')

ui.run()