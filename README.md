# poc-emmental

Why emmental ? Take a quick look in the code, there are some `*TBW*` holes in the scripts... This is where critical code needs `To Be Written` to make the application working.


## Task 2 : poc-data

Let's import real data into the project. Starting from the code written in task 1, you need essentially to go to the api/models folders in order to define the science feedback ORM (See schemas below): Appearance, Claim, Content, Verdict... Before anything, you need first to ask for the .env secret file to put at the top of your repository. This will give you credentials to make your sandbox script allowed to pull science feedback entities from airtable. The task is achieved once you have a /verdicts API with opportunities to explore the dataset thanks to keywords:

  1. `./poc start` making the docker containers run and the Flask Api to be available at localhost:80,

  2. `./poc sandbox` making the app write import airtable science feedback entities,

  4. again, `curl localhost:80/verdicts\?keywords=covid` returns filtered verdicts with claims related to this specified keywords.

<p align="center">
  <img
    alt="Demo of what to expect with poc-docker"
    src="https://github.com/feedback-news/poc-emmental/blob/poc-data/images/poc-data.gif"
  />
</p>


## Object Relational Mapping

All starts with Claim and Content: a claim is a piece of text saying something, and a content is for example an article on internet using this claim to justify its opinion. Appearance is the joining model helping for a user to testify that he saw a claim (or a content)
being quoted by another content :
<p align="center">
  <kbd>
    <img
      alt="orm claim and content"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/poc-data/images/ontology_1.png"
    />
  </kbd>
</p>


The core of the Feedback News is based on the Review/Verdict models. A review is a comment and an evaluation made over a claim (or a content) by a specific user in the platform, a reviewer, ie a scientific for whom peer publishing qualification was already proven in the past. On the top of that, a verdict is an aggregation of several reviews made on a same content or claim and repackaged as a one-single summary by an editor. In the end some tags are associated with the verdict to qualify the evaluated claim or content :
<p align="center">
  <kbd>
    <img
      alt="orm review and verdict"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/poc-data/images/ontology_2.png"
    />
  </kbd>
</p>


Finally the knowledge graph of Feedback News is completed with satellite entities helping us to make connections between communities of contents and claims. In this approach, a content is possibly attached to a medium, ie a platform publishing this content and possibly other contents, and this medium itself can be owned by an organization:
<p align="center">
  <kbd>
    <img
      alt="orm medium and organization"
      src="https://raw.githubusercontent.com/feedback-news/poc-emmental/poc-data/images/ontology_3.png"
    />
  </kbd>
</p>
