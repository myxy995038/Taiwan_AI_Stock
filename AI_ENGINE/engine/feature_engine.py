"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Feature Engine
==========================================================
"""




from AI_ENGINE.feature import (
    FeatureResult,
    MarketFeature,
    TrendFeature,
    MomentumFeature,
    InstitutionFeature,
    TradeFeature,
    ThemeFeature,
    RevenueFeature,
)

class FeatureEngine:

    def __init__(self):

        self.market = MarketFeature()

        self.trend = TrendFeature()
        
        self.momentum = MomentumFeature()
        
        self.institution = InstitutionFeature()
        
        self.trade = TradeFeature()
        
        self.theme = ThemeFeature()
        
        self.revenue = RevenueFeature()

    def run(
          
        self,
        latest=None,
        df=None,
        trading_money=None,
        foreign_days=0,
        trust_days=0,
        buy_price=0,
        stop_price=0,
        atr=0,
        themes=None,
        monthly_revenue=0,
        revenue_growth=0,
             
        
    ):

        feature = FeatureResult()

        feature.market = self.market.run(
            trading_money
        )

        if latest is not None and df is not None:

            feature.trend = self.trend.run(
                latest,
                df,
            )
            
        # 動能特徵
        if latest is not None:

            feature.momentum = self.momentum.run(
                latest
            )
            
        feature.institution = self.institution.run(
            foreign_days,
            trust_days,
        )
        
        
        if latest is not None:

            feature.trade = self.trade.run(

                close_price=latest["close"],

                buy_price=buy_price,

                stop_price=stop_price,

                atr=atr,

            )
            
            
            
        if themes is not None:

            feature.theme = self.theme.run(
                themes
            )
            
            
        feature.revenue = self.revenue.run(
            monthly_revenue,
            revenue_growth,
        )
            

        return feature