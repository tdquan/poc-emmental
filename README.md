# poc-emmental

Why emmental ? Take a quick look in the code, there are some `*TBW*` holes in the scripts... This is where critical code needs `To Be Written` to make the application working.


## Task 5 : poc-form

Final goal of this challenge is to let people sign and add appearances for a certain claim. First, after making sure that the sandbox database is set, one can sign with the only poctest.user@feedback.news user:

<p align="center">
  <img
    alt="Demo of what to expect with poc-form : sign step"
    src="https://github.com/feedback-news/poc-emmental/blob/poc-form/images/poc-sign.gif"
  />
</p>

Then, the whole user story is like this : a not yet logged user can search for verdicts, but once he/she has clicked on `Add a new appearance`, signin is forced to be required and the user has then access to the withRequiredLogin page `/verdicts/<verdictId>/appearances/creation` :

<p align="center">
  <img
    alt="Demo of what to expect with poc-form : form step"
    src="https://github.com/feedback-news/poc-emmental/blob/poc-form/images/poc-form.gif"
  />
</p>

The challenge is considered ended when we can check at the top of the list an appearance created by the current user.

At that point, optional extra features can be coded : what if the user enters an already recorded appearance ? Imagine how to display the amount of testifiers that recorded the same appearance, etc...
