import pandas as pd


"""
feature extraction
"""

df = pd.read_csv("../UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv", sep='\t')

"""
drop blanks ("") or empty data from the data set
"""
blanks=[]

for i, lb, rv in df.itertuples():
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)
df.drop(blanks,inplace=True) #drop indices that point to empty string
df.dropna(inplace=True)

"""
check what's in labels
"""

print(df['label'].value_counts())


"""
split data to train and test sets
"""

from sklearn.model_selection import train_test_split

X = df['review']   # X usually capitalized because larger matrix

y = df['label']     # y usually small, only 1d array of labels, the correct lsbels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


"""
the best way is to use a pipeline to vectorize the model and train the model.
pipeline allows to chain multiple steps into one sequence, makes automation easier.
feature extraction (tfidf) and model training (linearsvc).
"""

from sklearn.pipeline import Pipeline

from sklearn.svm import LinearSVC #classifier

from sklearn.feature_extraction.text import TfidfVectorizer # convert text into numerical data based on importance (tfid) Term Frequency-Inverse Document Frequency

text_clf = Pipeline([('tdif', TfidfVectorizer()), ('clf',LinearSVC())]) # choose what needs to be done, all in one pipelie step, use list of tuples
text_clf.fit(X_train, y_train) # fit into training data

predictions=text_clf.predict(X_test) # try model with test data

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predictions)) # visualize results




