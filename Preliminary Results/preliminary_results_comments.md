# GitHub Comments on Preliminary Results

## [Chemino](https://github.com/macss-uml19/Preliminary-Results/issues/53)
1. It is recommended that to note the demographics of the users on dating sites may not necessarily truly describe themselves, but the character that they want to be / the character that they believe to be most likely to get a date.
1. I think the most important feature for the users on dating sites is their appearance or their numbers of being "liked" (not sure if OkCupid works like Tinder), is it possible to get this kind of demographic data out of the dataset you are mining?

## [arun-131293](https://github.com/macss-uml19/Preliminary-Results/issues/52)
I think it's an interesting decision to aggregate data across genders, given that dating profiles could be highly gendered (and regressively so). It would be interesting in fact to split the analysis based on female/male profiles. It would be shocking if the qualities highlighted (in the sense of the interestingness you are interested in) by both genders are similar. One would expect them to be different, at least as a function of age.

## [SharonShen-UC](https://github.com/macss-uml19/Preliminary-Results/issues/45)
Awesome presentation and really cool topic! Just as a general suggestion on identifying clusters, I think initial variable selection would be important in determining clusterability, as the optimal K may change after you drop certain variables. Another question is that since there are nine essays each theoretically covers one aspect of people's characteristics/interest, I was wondering if your topic modelling were using corpus from all the essays, if that is the case would it be worth it to derive textual pattern for each essay?

## [erika-tyagi](https://github.com/macss-uml19/Preliminary-Results/issues/29)
This is broadly a theme that came up during your presentation, but I think including more ‘human in the loop’ insights might help facilitate more interpretable results. This may include the following –

- Consider limiting your population to a particular subset of individuals (e.g., just straight, single individuals)
- Consider alternative forms of feature engineering
- Consider limiting your features to those that you ex ante thing are most likely to be meaningful (in addition to or in lieu of dimensionality reduction techniques)

More broadly, I also think it would be helpful to explain why the charts / tables that you include are relevant in the context of your project and ultimate goal. Of course, most of them are descriptive / exploratory / diagnostic, but I think it’s easy to fall into the trap of generating visualizations – but then forgetting to explain (1) what’s actually important in what they show, and (2) how that then informs your process.

Overall, I think the project is super cool – I look forward to seeing your results!


## [08wparker](https://github.com/macss-uml19/Preliminary-Results/issues/18)
You have a really rich dataset and I think your clustering approaches could answer some interesting questions. I recommend:

1. Take a step back and better define the aims of the project. Why exactly are you clustering the demographic data? Why are you clustering the text responses? this may help you select a subset of the demographic variables that you think are "important" to cluster
1. Diagnose the clusterabillity of the features you chose before clustering
1. Use a distance metric that can handle categorical variables, like gower's.

## [di-Tong](https://github.com/macss-uml19/Preliminary-Results/issues/17)
Thanks for presenting your rigorous (as well as very entertaining) preliminary explorations. I wonder if the homogeneity of self-introductions has something to do with the OKCUPID app? Does the app encourage or guide people to include certain kinds of contents into their introduction in any way? Or does a learning pattern exist when people start to use the app (e.g. new users might write their introductions according to old users' profiles, so gradually people converge to a similar pattern)? Are there any previous studies that address the same question yet using a different dataset? Maybe by comparing the topics identified from corpus on different dating apps would help you solve the homogeneity puzzle. You may want to check [Elizabeth Bruch](https://mhbsd.net/research/)'s work.

## [yaoxishi](https://github.com/macss-uml19/Preliminary-Results/issues/13)
The dataset looks very fun to play with, but by reading the report, I am not very clear about the research question you are interested in investigating in this project, it would be better to state more clearly at the beginning. Also, it would be very helpful to add explanations to important variables, some variable names look a bit confusing, and also would be good to explain the results of each visualization and how these results guide further analysis. Finally, since many of the variables in the dataset are nearly normally distributed, GMM might be better than K-means. Looking forward to further analysis!
