import pandas as pd
import pprint
student_dict = {
    "student": ["Ankush","James","Lily"],
    "score": [56,76,98]
}
df = pd.DataFrame(student_dict)
pprint.pprint(df)

for (index,row) in df.iterrows():
    if row.student =="Ankush":
        print(row.score)