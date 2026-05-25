# =========================================
# Topic : Visualization
# =========================================

import pandas as pd
import matplotlib.pyplot as plt

data = {

    "Name": ["Madhav", "Arjun", "Simran"],

    "Marks": [95, 88, 97]
}

df = pd.DataFrame(data)

# Bar chart
df.plot(

    x="Name",

    y="Marks",

    kind="bar"
)

plt.show()