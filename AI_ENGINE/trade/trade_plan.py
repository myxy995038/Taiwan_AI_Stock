from dataclasses import dataclass
import pandas as pd


@dataclass
class TradePlan:

    buy_zone: str

    buy_price: float

    stop_price: float

    target1: float

    target2: float

    target3: float
    
    from typing import Union

    rr: Union[float, str]

    
    rr_score: int


class TradePlanEngine:

    @staticmethod
    def build(df, latest):

        price = latest["close"]

        ma20 = latest["MA20"]

        diff = (price - ma20) / ma20 * 100

        # -----------------------
        # 建議買點
        # -----------------------

        if diff <= 3:
            buy_price = price

        elif diff <= 8:
            buy_price = ma20

        else:
            buy_price = ma20 * 1.01

        buy_price = round(min(buy_price, price), 1)

        buy_zone = f"{buy_price*0.99:.1f} ~ {buy_price*1.01:.1f}"

        # -----------------------
        # ATR
        # -----------------------

        atr = latest["ATR"]

        if pd.isna(atr):

            atr = price * 0.03

        recent_low = df["min"].tail(20).min()

        stop_price = min(

            buy_price - atr * 2,

            recent_low * 0.98,

            latest["MA20"] * 0.98,

        )

        stop_price = round(stop_price, 1)

        if stop_price >= buy_price:

            stop_price = round(buy_price * 0.95, 1)

        risk = buy_price - stop_price

        if risk <= 0:

            stop_price = round(buy_price - atr * 2, 1)

            risk = buy_price - stop_price

        target1 = round(min(buy_price + risk * 2, buy_price * 1.25), 1)

        target2 = round(buy_price + risk * 3, 1)

        target3 = round(buy_price + risk * 5, 1)

        reward = target1 - buy_price

        if reward <= 0 or risk <= 0:

            rr = "-"

            rr_score = 0

        else:

            rr = round(reward / risk, 2)

            if rr >= 4:

                rr_score = 20

            elif rr >= 3:

                rr_score = 15

            elif rr >= 2:

                rr_score = 10

            elif rr >= 1.5:

                rr_score = 5

            else:

                rr_score = 0

                rr = "-"

        return TradePlan(

            buy_zone=buy_zone,

            buy_price=buy_price,

            stop_price=stop_price,

            target1=target1,

            target2=target2,

            target3=target3,

            rr=rr,

            rr_score=rr_score,

        )