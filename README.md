# scikit_test
RedCarpetUp internship application

First step(For a batch of movies):

Primary dataset
Download primary data from https://www.kaggle.com/PromptCloudHQ/imdb-data/data

Feature generation

Casts: https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/casts.html
Awards_types(dataset AW): https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/awtypes.html
Actors(dataset A): https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/actors.html
Movies(dataset M): https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/main.html

First exercise(time: 12 hours):
1. Load primary dataset to pandas.
2. Scrape data from secondary links and load to pandas. While any method is fine - beautiful soup would be recommended.
3. Use Levenshtein distance to match movie names in primary dataset with movies provided in dataset M. (Recommendations:  https://github.com/seatgeek/fuzzywuzzy)
3. Persist Levenshtein distance scores between movies in primary dataset and movies in dataset(M) and share in a CSV. 
4. Assume that the movies with the highest Levenshtein distance is the same and use that to merge primary dataset to dataset M.
5. Using this, use data in dataset AW,A to create additional features.
6. After this exercise, you should have multiple features in for each movie. Share the processed data in a csv format.  

Second exercise(time: 12 hours)
For modelling divide the data into atleast three samples:
1) Training
2) Testing
3) Out of time testing - This dataset needs to have all 2016 year releases - DO NOT INCLUDE 2016 year releases in previous two datasets.
Feel free to play around with distribution of training & testing datasets.

Models to be implemented:
1. SVM for multiclass prediction - http://scikit-learn.org/stable/modules/svm.html#classification
2. LARS Lasso - http://scikit-learn.org/stable/modules/linear_model.html#lars-lasso

Model comparision metrics to be generated for each of your models:
1. AUC (Multiclass) - http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score
2. MAPE (LARS) - http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error
3. R2 (LARS) - http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score

Share Jupyter notebook reading in .csv with all modelling code - try to optimize the model as much as possible in given time frame.


Brownie points:
1. Create function with single movie run. Something like this:
	def fun_name(movie_name):
		......
	
	Calling fun_name(movie_name) should predict rating of a movie.
