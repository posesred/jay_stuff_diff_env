from nicegui import ui
import redis


# r = redis.Redis(host='localhost', port=6379, db=0)
# data = r.get('data')
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", "DOGEUSDT", "DOTUSDT", "UNIUSDT", "BCHUSDT", "LTCUSDT"]
positions_opened = [35,31,231,3123,131,23,23,312,57,831]
number_positions = [10.32, 20.54, 30.2, 40, 50, 60, 80, 100, 90, 100]
time_position_opened = ["time", "time", "time", "time", "time", "time", "time", "time", "time", "time"]
time_in_position = ["time", "time", "time", "time", "time", "time", "time", "time", "time", "time"]
unknown = ["not sure","not sure","not sure","not sure","not sure","not sure","not sure","not sure","not sure","not sure"]
profit_loss = [5,-5,10,-20.5, 10, 20, -0.30, 40, 50, 60]
profolio_size = 1000
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
          till_profit_labels = [ui.label(_) for _ in unknown]
          ui.label("average time till profitable")


     with ui.element("div").style("flex:1;  display: flex; flex-direction: column; gap: 5px;"):
          ui.label("Profit/Loss")
          list(map(lambda x: ui.label(x).style("color: green;") if x > 0 else ui.label(x).style("color: red;"), profit_loss))
          apply_style = lambda x: ui.label(x).style("color: green; font-size: 24px;") if x > 0 else ui.label(x).style("color: red; font-size: 24px;")
          apply_style(sum(profit_loss))

ui.run()