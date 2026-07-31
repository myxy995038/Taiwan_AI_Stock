from AI_ENGINE.dashboard.dashboard import Dashboard


class DashboardReport:

    def __init__(self):
        self.dashboard = Dashboard()

    def show(self):

        result = self.dashboard.summary()

        if result == {}:
            print("目前沒有歷史資料")
            return

        print("=" * 60)
        print("AI Dashboard")
        print("=" * 60)

        print(f"總交易數：{result['總交易數']}")
        print(f"勝率：{result['勝率']} %")
        print(f"平均報酬：{result['平均報酬']} %")
        print(f"最高報酬：{result['最高報酬']} %")
        print(f"最低報酬：{result['最低報酬']} %")

        print("\n目前 AI 權重：")
        print(result["目前權重"])