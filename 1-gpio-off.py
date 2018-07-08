import RPi.GPIO as SHARD
SHARD.setwarnings(0)
SHARD.setmode(SHARD.BCM)
SHARD.setup(17,SHARD.OUT)
SHARD.setup(27,SHARD.OUT)
SHARD.setup(22,SHARD.OUT)
SHARD.setup(24,SHARD.OUT)

SHARD.output(17,0)
SHARD.output(27,0)
SHARD.output(24,0)
SHARD.output(22,1)
