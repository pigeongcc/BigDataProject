# Issues Encountered

1. Dataset download links are dynamic (change with time) both on Kaggle and Google Drive. For now, we uploaded the dataset to Yandex Disk. We tested it on May 11th, 18:00. If downloading leads to HTTP error 400, it means the links became outdated. Still, we suppose it is better than upload the dataset into Github. In case of 400 error, we can quickly fix it. You may contact us via telegram: [@pigeon_gcc](https://t.me/pigeon_gcc), [@and_va2](https://t.me/and_va2).
2. We haven't managed to setup the Hive optimization. Although the code in `sql/hive_optimization.hql` seems to be ok, the bucketing jobs are constantly starting to fail at some moment of data inserting process. For both small (10) and large (200-300) number of buckets it throws an error:
```[Error 20004]: Fatal error occurred when node tried to create too many dynamic partitions.```
3. We implemented the grid search and cross-validation. Due to lack of resources and time, we only trained a model on 1x1 grid, and 2-fold cross-validation.
4. We had no success with computing the MAP and NDCG metrics for the model, however we provide the rating RMSE metric.

All the other parts of the project are fully comleted. The code is tested on reproducibility.

# Repository Structure

This repository is a template for the final project of big data course in IU-2023. It contains the following directories:

- `data/` contains the dataset files.
- `models/` contains the Spark ML models.
- `notebooks/` has the Jupyter or Zeppelin notebooks of your project and used just for learning purposes.
- `output/` represents the output directory for storing the results of the project. It can contain `csv` files, text files. images and any other materials you returned as an ouput of the pipeline.
- `scripts/` is a place for storing `.sh` scripts and `.py` scripts of the pipeline.
- `sql/` is a folder for keeping all `.sql` and `.hql` files.

`requirements.txt` lists the Python packages needed for running your Python scripts. Feel free to add more packages when necessary.

`main.sh` is the main script that will run all scripts of the pipeline stages which will execute the full pipeline and store the results in `output/` folder. During checking your project repo, the grader will run only the main script and check the results in `output/` folder.

**Important Note:** You cannot change the content of the script `main.sh` since it will be used for assessment purposes.

**Another Note:** The notebooks in `notebooks/` folder are used only for learning purposes since you need to put all Python scripts of the pipeline in `scripts/` folder. During the assessment, the grader can delete the folder `notebooks/` to check that your pipeline does not depend on its content.
