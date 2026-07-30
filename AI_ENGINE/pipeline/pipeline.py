"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Pipeline Builder
==========================================================
"""

class Pipeline:

    @staticmethod
    def build_result(
        stock_id,
        stock_name,
        theme,
        latest,
        trade_plan,
        score_result,
        score,
        extra_scores,
    ):
        """
        統一建立排行榜輸出格式
        """

        result = {
            "代號": stock_id,
            "名稱": stock_name,
            "題材": theme,

            "目前型態": extra_scores["pattern"],

            "收盤價": round(latest["close"], 2),

            "建議買進區": trade_plan.buy_zone,
            "建議買進價": trade_plan.buy_price,
            "停損價": trade_plan.stop_price,

            "第一目標價": trade_plan.target1,
            "第二目標價": trade_plan.target2,
            "第三目標價": trade_plan.target3,

            "風險報酬比(RR)": trade_plan.rr,

            "建議持股天數": score_result.holding_days,
            "AI建議": score_result.action,
            "AI品質(總分)": score_result.quality,
            "總分": score,

            "AI風險": score_result.risk,
            "AI進場時機": score_result.entry_timing,
            "AI評論": score_result.comment,
        }

        # 合併其餘欄位
        result.update(extra_scores)

        return result