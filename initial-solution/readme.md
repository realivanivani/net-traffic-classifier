Directory containing my original solution in which I used


Here is the feedback of the team, for which I am very greatful!

A crucial part of the process of developing a classifier is feature engineering. For that you need to understand the data and have some notion of the domain.

When submitting this particular task we expect the candidates to parse the data properly. The header is a list of key-value pairs which. The keys are a great candidates from columns of the initial dataframe. Only with properly parsed data you can then assess meaning and usefulness of individual columns and think how to process them to get more informed features.

If you check out the CSVs you produced you will see that you have misaligned values from different records. There are standard python libraries for parsing headers you could use. Also concatenating two padas DataFrames takes time proportional to their size - they need to be copied. Thus the complexity of the initial loop where you parse the input files is O(n^2).

What we see is that you have a an understanding of ML approaches, however, we see a great gap in SW engineering skills. In our work (and I believe in most of the ML projects which aim for production), SW engineering is a crucial part of the problem solution. We feel that you need to get more hands on programming experience. I would start with learning best practices in python and studying how to write and structure code and maintain codebases. Also, solid knowledge in SQL databases, design patterns and algorithmic complexity would increase your skills significantly.
