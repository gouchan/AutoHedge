# Example usage
from loguru import logger
from autohedge.main import AutomatedTradingSystem


if __name__ == "__main__":

    try:
        stocks = ["NVDA"]
        trading_system = AutomatedTradingSystem(stocks)
        print(trading_system.run_trading_cycle(task = "Let's analyze nvidia to see if we should buy it, we have 50k$ in allocation "))

    except Exception as e:
        logger.error(f"Critical error in trading system: {str(e)}")
        raise