import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',size='species',data=df,palette='Set2')
plt.show()