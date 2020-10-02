## Motivation
This research was conducted as part of my Master's Thesis for the MA Computational Social Science at the University of Chicago. I am linguist who speaks 12 languages and has been interested in studying language computationally. I am also a social scientist who loves how weird we humans are, and tries to study their psychology. So this project provided the perfect confluence of my interests- using topic models on dating profiles to understand the social norms around online dating. 

The primary research question is whether men who may have faced some disadvantages in dating in the real life (due to their height, weight, race or low education) find ways to strategically market themselves on their dating profiles. In what ways are they different form normal profiles? What is a 'normal' profile anyway? Luckily, we finally have the tools of data science to begin answering some age-old questions on love and romance. 

### Installations
This codes runs on Python 3.6 for the majority of the analysis, and then switches to R for the final component of STMs (Structural Topic Models). So the required libraries/ packages are listed below for ease of understanding. You can install of the Python modules using

```pip install -r requirements.txt```

The cleaning of the core text essays is far from a trivial task. Splitting the conjoined words required a total of 79 hours on a 4 Ghz processor for the 20,000+ profiles. I would strongly recommend doing this task in parallel, since none of the individual profiles' results depend on previous profiles. For this purpose, I have leveraged the mrjob framework in conjunction with AWS, which parallelizes and thus completes the task much faster. 

#### Python
* scikit-learn
* gensim
* wordninja
* pyspellchecker
* beautifulsoup
* spacy
* textacy
* tqdm
* nltk
* mrjob

#### R
* stm
* quanteda
* tidyverse

### File Descriptions
The repository contains a mix of .py files for utilies, Jupyter notebooks for easy visualization, and an R notebook for the component of the analysis that only exists in R libraries. These files are:

#### Python Modules (.py)

* split_utils.py: Contains functions to help split conjoined words in the dating profile essays
* filter_utils.py: Contains functions to standardize some of the categorical variables of interest
* text_complexity_utils.py: Contains functions mainly developed from the SpaCy library to analyze the difficulty level of vocabulary and sentence construction
* nmf_visuals_utils.py: Contains functions required in conjunction with sklearn to generate the visualizations of topics under the Non-Negative Matrix Factorization topic model. This code largely builds off the seminal work of Shishido et al (2016) and the Computational Social Science workshop at the University of Michigan (See references)

#### Jupyter Notebooks
* data_filter.ipynb- Inputs data, drops missing values and irrelevant variables. Removes unwanted characters from essays, as well as fixing the problem of conjoined words (using split_utils.py) Filters for the population of interest (using filter_utils.py). Also calculates new  variables using text_complexity.py
* profile_length_analysis.ipynb- Checks for the influence of the 4 categorical variables on profile length
* doc2vec_model.ipynb- Converts filtered essay data into vector space representation. Then attempts to find clusters using K-Means and DBScan on data after its dimensionality has been reduced with Principal Components Analysis and t-SNE. 
* nmf_visualize.ipynb- Calculates an NMF model and then visualizes differences in the proportions of profiles using the generated topics

#### R Notebooks

* quant_eda_stm.rmd- Contains code to perform Latent Dirichlet Analysis (LDA) and build a Structural Topic Model over it

#### sav files

* nmf.sav - The Jupyter notebooks provide all the necessary code to generate the tables and analyses in the blogpost. However, you can skip a few steps and load the model directly from this file.

### Data sets: [OkCupid Data](https://github.com/rudeboybert/JSE_OkCupid/blob/master/profiles.csv.zip)

### How to Interact With the Project

* You can install the necessary libraries as shown above, and download the raw data using the link in the next section. 
* The full dataset is not very large (compared to other datasets frequently being used in text analysis). Make sure you unzip the folder with the folder name unchanged 'profiles.csv', and unzip it to one step back in your directory (not the same folder as your main analysis). This will ensure compatibility with the code posted in the notebooks. 
You will need to run the Data_Filter.ipynb file first, but are free to run the other analyses in any order. 

### Licensing, Authors, Acknowledgements, etc.
This project owes significant debts to previous work. These may be found in the work of the following authors, whose contributions
have been duly referenced:

* [Juan Shishido](https://github.com/juanshishido/okcupid)
* [Computational Social Science Workshop, University of Michigan](https://github.com/UM-CSS/CSSLabs-NLP)

It also builds off the initial explorations conducted in Fall 2019 as a team project with my classmates, which can be accessed at its own repository here: [Unsupervised Dating](https://github.com/tonofshell/unsupervised-dating)

### Key Findings:
* On the whole, single heterosexual men in the data write profiles of about the same length, with roughly the same use of language, spread over same 5 topics, with the first 3 (the area, hobbies and sociability) taking up most (82%) of it. The differences that emerge for different backgrounds (race, education, fitness and height) only start emerging in the remaining18%.
* There does exist some group of men whose choice of words varies significantly from everyone else. But we can't explain this group purely in terms of the four variables
* Height and fitness level have the least impact on differences of topic choice, while black ethnicity has the highest affect across all topics
* One's love for novelty appears to be the topic most affected by the categories of our chosen variable.

Explore the full analysis either in this fun [Medium blogpost](https://medium.com/@abhishekpandit/does-online-dating-level-the-playing-field-for-disadvantaged-dudes-the-data-decides-11ac57242163?postPublishedType=repub) or for a more rigorous, academic approach that draws on a variety of related research, you can [dig into the thesis here](https://www.academia.edu/44171812/Strategic_Self_Representation_by_Heterosexual_Male_Users_on_American_Online_Dating_Platforms_Converging_Towards_or_Diverging_From_Emergent_Norms)

### Future Directions
Based on this experience of porting across Python and R to implement structural models, I resolved to build in the capability of Structural Topic Models into gensim itself. I will soon be submitting a pull request specifically towards its topic modelling classes. 

