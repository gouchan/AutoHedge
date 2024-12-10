# Example usage
from autohedge.main import AutomatedTradingSystem

# Define the stocks to analyze
stocks = ["NVDA"]

# Initialize the trading system with the specified stocks
trading_system = AutomatedTradingSystem(stocks)

# Define the task for the trading cycle
task = "Let's analyze nvidia to see if we should buy it, we have 50k$ in allocation"

# Run the trading cycle and print the results
print(trading_system.run_trading_cycle(task=task))
