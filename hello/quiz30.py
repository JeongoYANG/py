import pandas as pd
from icecream import ic


#a = [i if i==0 or i==0 else i for i in range(1)]
#b = [i if i ==0 or i==0 else i for i in[]]
#c = [(i,j) for i,j in enumerate([])]
#d = {i:j for i,j in zip(ls1,ls2)}
#e = [i + j for i,j in zip(ls1,ls2)]
class Quiz30:
    def quiz30_df_4_by_3(self) -> str:
        df = pd.DataFrame([1,2,3]
                          [4,5,6]
                          [7,8,9]
                          [10,11,12], index=range(1,5), columns=['A', 'B', 'C'])
        ic(df)
        return None

    def quiz31(self) -> str: return None

    def quiz32(self) -> str: return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None