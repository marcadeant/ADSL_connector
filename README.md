#ADSL connector

ADSL is french for "Aide aux dirigeants et services aux licenciés". 
It's a web service supplied by ADSL company to tennis club. Thanks to this plateform,
each member of the tennis club can easily booked a tennis court session. For further
information, you can check [official website](https://www.adsltennis.com/).

The main purpose of this project is to create an agent able to connect into the plateform
and booking a tennis court session. I'm a tennis player and i'm using this agent to schedule my tennis sessions 
of the week.

It's an interesting way to discover 'selenium' in Python.
In my case, I'm using `selenium` instead of `mechanize` or `request` because it's best way to
deal with internet browsing. When we use `webdriver` module to start a session with `Safari()`, `Firefox()`
or `Chrome()` and do some requests, a navigator window will pop up and show us what our python script is doing.

Configuration of the agent:

1) Python 3.7.1 is required 
2) Configure a json file `auth.json` with your ADSL login (look at `example.json`)
3) Save `auth.json` in `../ADSL_connector/`
4) Choose `date`, `hour`, `tennis_court_letter`, `player_name` and fill values in the `parameters.json`
5) Run the agent with the linux command `python3 ../ADSL_connector/main.py`





