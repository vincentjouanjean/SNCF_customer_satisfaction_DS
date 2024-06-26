from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.models.train import train_model

clf1 = KNeighborsClassifier(
    algorithm='auto',
    leaf_size=5,
    metric='manhattan',
    n_neighbors=5,
    p=1, weights='distance',
    n_jobs=-1
)
clf2 = SVC(
    C=10,
    kernel='rbf',
    gamma=0.1
)
clf3 = LogisticRegression(
    C=0.1,
    multi_class='multinomial',
    penalty='l2'
)
clf4 = DecisionTreeClassifier(
    criterion='gini',
    max_depth=5
)

model = VotingClassifier(
    estimators=[
        ('KNeighborsClassifier', clf1),
        ('SVC', clf2),
        ('LogisticRegression', clf3),
        ('DecisionTreeClassifier', clf4)
    ],
    voting='hard'
)

train_model(model)
