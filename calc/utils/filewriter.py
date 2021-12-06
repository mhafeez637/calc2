"""File writer using Pandas"""

import pandas as pd
from calc.history.calculation import Calculations

class Export:
    """Data export class"""
    @staticmethod
    def export_resultfile():
        """Export result"""
        result = Calculations.history
        df_result = pd.DataFrame(result, columns=['result'])
        with pd.ExcelWriter('../../tests/test_data/addition_values.xlsx', mode='a', if_sheet_exists='replace') as writer:
            df_result.to_excel(writer, sheet_name='output_logs', index=False)
            writer.save()
