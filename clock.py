#main.py
import time, os
from botstrategy import BotStrategy
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
	strategy = BotStrategy()
	#implementation starts
	strategy.tick()
	strategy.evaluatePositions()
	#graphing EMAs and MACD indicator:
	strategy.output.macdrsiplot(strategy.graphdataPoints, strategy.EMA9, strategy.MACD, strategy.cumulatedProfits)

if __name__ == "__main__":
	scheduler = BlockingScheduler()
	scheduler.add_executor('processpool')
	scheduler.add_job(main, 'interval', seconds=60)
	print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		pass