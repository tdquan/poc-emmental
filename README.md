# poc-emmental

Why emmental ? Take a quick look in the code, there are some `*TBW*` holes in the scripts... This is where critical code needs `To Be Written` to make the application working.


## Task 4 : poc-search

Goal of this task is to build a small navigation into the Science Feedback verdict data :

<p align="center">
  <img
    alt="Demo of what to expect with poc-search"
    src="https://github.com/feedback-news/poc-emmental/blob/poc-search/images/poc-search.gif"
  />
</p>


The webapp should begin with a `/` landing page, allowing to enter some keywords.
Pressing Enter or clicking to the search button leads to a `/verdicts?keywords=<keywords>` page. It is possible there to change the keywords or do some a filter by tag to the verdicts. Each item is clickable and should lead to
a special `/verdicts/<verdictId>` verdict template page inside of which all the appearances of this claim are shown and can be visited.
