"""
==========================================================
Taiwan AI Stock System
V10 Ultimate Enterprise

Statistics Engine
==========================================================
"""

from dataclasses import asdict

import pandas as pd

from AI_ENGINE.constants import FACTOR_COLUMNS


class StatisticsEngine:

    def __init__(self, records):

        self.records = records

        self.df = pd.DataFrame(

            [asdict(r) for r in records]

        )

    # -------------------------------------------------
    # Basic
    # -------------------------------------------------

    def count(self):

        return len(self.df)

    def success_count(self):

        if self.df.empty:

            return 0

        return int(

            self.df["success"].sum()

        )

    def failure_count(self):

        return self.count() - self.success_count()

    def win_rate(self):

        if self.count() == 0:

            return 0

        return round(

            self.success_count() / self.count(),

            4,

        )

    # -------------------------------------------------
    # Return
    # -------------------------------------------------

    def average_return(self):

        if self.df.empty:

            return 0.0

        return float(

            round(

                self.df["return_rate"].mean(),

                2,

            )

        )

    def best_return(self):

        if self.df.empty:

            return 0.0

        return float(

            self.df["return_rate"].max()

        )

    def worst_return(self):

        if self.df.empty:

            return 0.0

        return float(

            self.df["return_rate"].min()

        )

    # -------------------------------------------------
    # Theme Statistics
    # -------------------------------------------------

    def theme_statistics(self):

        if self.df.empty:

            return pd.DataFrame()

        return (

            self.df

            .groupby("theme")

            .agg(

                Count=("theme", "count"),

                WinRate=("success", "mean"),

                AvgReturn=("return_rate", "mean"),

            )

            .reset_index()

        )

    # -------------------------------------------------
    # Factor Statistics (V3)
    # -------------------------------------------------

    def factor_statistics(self):

        if self.df.empty:

            return pd.DataFrame()

        rows = []

        success_df = self.df[

            self.df["success"] == True

        ]

        failure_df = self.df[

            self.df["success"] == False

        ]

        total_samples = len(self.df)

        success_count = len(success_df)

        failure_count = len(failure_df)

        avg_return = float(

            self.df["return_rate"].mean()

        )

        for factor in FACTOR_COLUMNS:

            average = float(

                self.df[factor].mean()

            )

            success_avg = (

                float(success_df[factor].mean())

                if success_count > 0

                else 0.0

            )

            failure_avg = (

                float(failure_df[factor].mean())

                if failure_count > 0

                else 0.0

            )

            rows.append(

                {

                    "Factor": factor,

                    "Samples": total_samples,

                    "SuccessCount": success_count,

                    "FailureCount": failure_count,

                    "SuccessRate": (

                        success_count / total_samples

                        if total_samples > 0

                        else 0.0

                    ),

                    "Average": average,

                    "SuccessAvg": success_avg,

                    "FailureAvg": failure_avg,
                    
                    "FactorPower": success_avg - failure_avg,

                    "AvgReturn": avg_return,

                }

            )

        return pd.DataFrame(rows)

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    def summary(self):

        return {

            "count": self.count(),

            "success": self.success_count(),

            "failure": self.failure_count(),

            "win_rate": self.win_rate(),

            "average_return": self.average_return(),

            "best_return": self.best_return(),

            "worst_return": self.worst_return(),

        }