"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Feature Data Models
==========================================================
"""

from dataclasses import dataclass, field


# ----------------------------------------------------------
# Market
# ----------------------------------------------------------

@dataclass
class MarketFeatureResult:

    money: float = 0

    liquidity: float = 0


# ----------------------------------------------------------
# Trend
# ----------------------------------------------------------

@dataclass
class TrendFeatureResult:

    ma20: float = 0

    ma60: float = 0

    above_ma20: bool = False

    above_ma60: bool = False

    breakout20: bool = False

    breakout60: bool = False


# ----------------------------------------------------------
# Momentum
# ----------------------------------------------------------

@dataclass
class MomentumFeatureResult:

    
    rsi: float = 0

    macd: float = 0

    macd_signal: float = 0

    macd_golden: bool = False

    k: float = 0

    d: float = 0

    kd_golden: bool = False


# ----------------------------------------------------------
# Institution
# ----------------------------------------------------------

@dataclass
class InstitutionFeatureResult:

    foreign_days: int = 0

    trust_days: int = 0

    foreign_buy: bool = False

    trust_buy: bool = False


# ----------------------------------------------------------
# Revenue
# ----------------------------------------------------------

   
    
    
@dataclass
class RevenueFeatureResult:

 
    monthly_revenue: float = 0

    revenue_growth: float = 0

    growth_type: str = ""

    positive_growth: bool = False

    score: float = 0


# ----------------------------------------------------------
# Risk
# ----------------------------------------------------------

@dataclass
class TradeFeatureResult:

    buy_price: float = 0

    stop_price: float = 0

    atr: float = 0

    reward: float = 0

    risk: float = 0

    rr: float = 0

    can_trade: bool = False


# ----------------------------------------------------------
# Theme
# ----------------------------------------------------------

from dataclasses import field

@dataclass
class ThemeFeatureResult:

    names: list[str] = field(default_factory=list)

    primary: str = ""

    score: float = 0


# ----------------------------------------------------------
# Feature Container
# ----------------------------------------------------------

@dataclass
class FeatureResult:

    market: MarketFeatureResult = field(default_factory=MarketFeatureResult)

    trend: TrendFeatureResult = field(default_factory=TrendFeatureResult)

    momentum: MomentumFeatureResult = field(default_factory=MomentumFeatureResult)

    institution: InstitutionFeatureResult = field(default_factory=InstitutionFeatureResult)

    revenue: RevenueFeatureResult = field(default_factory=RevenueFeatureResult)

    trade: TradeFeatureResult = field(default_factory=TradeFeatureResult)

    theme: ThemeFeatureResult = field(default_factory=ThemeFeatureResult)