from freqtrade.strategy import IStrategy
from pandas import DataFrame

class MyStrategy(IStrategy):
    """
    Strategi dummy untuk testing. Tidak beli/sell, hanya buat memastikan bot bisa jalan.
    """

    # Wajib: Timeframe trading
    timeframe = '5m'

    # Tidak pakai indikator khusus
    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    # Tidak pernah beli (buy = 0)
    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['buy'] = 0
        return dataframe

    # Tidak pernah jual (sell = 0)
    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['sell'] = 0
        return dataframe
