# ==============================================================================
# CELL 17E: 昨日回測與 AI 因子排行榜 (V7核心)
# ==============================================================================
history_file = "history/performance_history.csv"
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
last_file = f"history/{yesterday}.csv"


from AI_ENGINE.learning.learning_center import LearningCenter

learning = LearningCenter(
    history_file="history/performance_history.xlsx"
)

print(result_df.columns.tolist())

learning.append_today(result_df)






# --- 1. 昨日推薦績效回測 ---
if os.path.exists(last_file) and not result_df.empty:
    yesterday_df = pd.read_csv(last_file)

    # 統一股票代號型別
    yesterday_df["代號"] = yesterday_df["代號"].astype(str)
    result_df["代號"] = result_df["代號"].astype(str)

    # 去除空白（保險）
    yesterday_df["代號"] = yesterday_df["代號"].str.strip()
    result_df["代號"] = result_df["代號"].str.strip()

    # 修正重疊的 merge 語法，精確比對
    compare_df = yesterday_df.merge(
        result_df[[
            "代號", "名稱", "收盤價", "總分", "AI品質(總分)", "RR數值",
            "是否站上MA20", "是否創 60 日新高", "MACD黃金交叉", "KD黃金交叉",
            "RSI區間", "外資連買天數", "投信連買天數"
        ]],
        on=["代號", "名稱"],
        how="left",
        suffixes=("_昨日", "_今日")
    )

    compare_df["漲跌%"] = ((compare_df["收盤價_今日"] - compare_df["收盤價_昨日"]) / compare_df["收盤價_昨日"] * 100).round(2)

    print("\n========================")
    print("昨日推薦績效")
    print("========================")
    display(compare_df[["代號", "名稱", "收盤價_昨日", "收盤價_今日", "漲跌%"]])

    # 寫入/追加績效歷史資料庫
    compare_df.to_csv(history_file, mode="a", header=not os.path.exists(history_file), index=False, encoding="utf-8-sig")
    print("✅ 已更新績效資料庫")
else:
    print("沒有昨日排行榜，或今日無新資料，略過實時回測。")


# --- 2. 歷史總體績效統計 ---
if os.path.exists(history_file):
    perf = pd.read_csv(history_file)

    if "漲跌%" in perf.columns and len(perf) > 0:
        total = len(perf)
        win = (perf["漲跌%"] > 0).sum()
        lose = (perf["漲跌%"] <= 0).sum()
        win_rate = round(win / total * 100, 2)
        avg_return = round(perf["漲跌%"].mean(), 2)

        print("\n========================")
        print("AI 歷史總體績效")
        print("========================")
        print(f"總筆數：{total} | 上漲：{win} | 下跌：{lose}")
        print(f"綜合勝率：{win_rate}% | 平均報酬：{avg_return}%")



        # =========================
        # Enterprise Learning
        # =========================

        weight, factor_df, summary = learning.run()

        print("\n========================")
        print("Enterprise Learning 完成")
        print("========================")

        print(summary)

        display(factor_df)

       