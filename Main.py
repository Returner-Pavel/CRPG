import yaml
from tools.Debug import ClassG_Debug

with (open("data/config.yml", "r") as file):
    config = yaml.safe_load(file)
    debug = config["config"].get("debug", False)
    player_id = config["config"].get("player_id", 0)

classG_log = ClassG_Debug(debug)

if "__main__" == __name__:
    classG_log.noneG_LogInfo("Start Main.py")