######/ __ \######
# GMP RoboticsXD #
######\ ‾‾ /######

# Technic Hub as RC car setup with various control options from
# the BT Remote


# Import Libraries
from pybricks.tools import wait
from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Port, Direction, Stop, Button, Color

# Initialize Hardware
hub = TechnicHub()
remote = Remote()

# Rename remote
remote.name("TECHubRemote")

# Apply visual effects, to inform user about pairing hub with the remote
print("TECHubRemote paired with TECHub01")
