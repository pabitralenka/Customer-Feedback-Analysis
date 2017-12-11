# Customer Feedback Analysis, IJCNLP'17
* **Our goal is to determine what class(es) the customer feedback sentences should be annotated with five-plus-one-classes       categorization (comment, request, bug, complaint, meaningless and undetermined) as in four languages i.e. English,           French, Japanese and Spanish**.
* This is one of the shared tasks of [**IJCNLP - 2017**](http://ijcnlp2017.org/site/page.aspx?pid=901&sid=1133&lang=en). For more details about the task, please visit [here.](https://sites.google.com/view/customer-feedback-analysis/)
***

### Citing the paper

If you are using this code for any sort of research, please cite our paper 
* [**IITP at IJCNLP-2017 Task 4: Auto Analysis of Customer Feedback using CNN and GRU Network.**](http://aclweb.org/anthology/I17-4031)
***

### Dataset 
#### Training Data samples for CNN (training.tsv) from different languages used
tag  | consumer_complaint_narrative
------------- | -------------
comment  | Rooms and sitting area was always immaculate.
request  | :) Deberían abrir vacantes para beta-testers :)
meaningless | il beug tou le temp
complaint  | シャンプーが泡立たない

#### Test Data samples for CNN (test.tsv) from different languages used
id  | consumer_complaint_narrative
------------- | -------------
en-test-0002  | You can't go wrong!!!
es-test-0004  | La habitación súper grande! muy cómoda..
fr-test-0006  | La salle de bains est splendide.
jp-test-0016  | 日々の忙しさを忘れて、娘が優しくされると優しくなれるね

#### Training Data samples for CNN + RNN (training.tsv) from different languages used
Category  | Descript
------------- | -------------
comment  | Rooms and sitting area was always immaculate.
request  | :) Deberían abrir vacantes para beta-testers :)
meaningless  | il beug tou le temp
complaint  | シャンプーが泡立たない

#### Test Data samples for CNN + RNN (test.tsv) from different languages used
id  | Descript
------------- | -------------
en-test-0002  | You can't go wrong!!!
es-test-0004  | La habitación súper grande! muy cómoda..
fr-test-0006  | La salle de bains est splendide.
jp-test-0016  | 日々の忙しさを忘れて、娘が優しくされると優しくなれるね
***

### Running the Code
#### For CNN
##### Train 
* Command : **`python3 train.py training.tsv parameters.json`**
* A directory will be created during training, and the best model will be saved in this directory.

##### Test
* Provide the model directory (created when running `train.py`) and test data to `predict.py`
* Command : **`python3 predict.py trained_model_1505467324/ test.tsv`**
***

#### For CNN + RNN
##### Train 
* Command : **`python3 train.py training.tsv training_config.json`**
* A directory will be created during training, and the best model will be saved in this directory.

##### Test
* Provide the model directory (created when running `train.py`) and test data to `predict.py`
* Command : **`python3 predict.py trained_results_1505468375/ test.tsv`**
***

### Reporting Doubts and Errors
* For any queries, please drop me an email at pabitra.lenka18@gmail.com.
* Please refer to the publication for detailed results and model performances.

### Credits
* I would like to thank [Jie Zhang](https://github.com/jiegzhan) and [Denny Britz](https://github.com/dennybritz) for sharing their code.
* We have used their code and modified according to our need by incorporating pre-trained `Word2Vec` embedding.
* [Deepak Gupta](https://github.com/deepak1357) has also contributed to this code repository. 
