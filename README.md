# Agents-Based-TradingCompany

Crew AI Agents Based Trading Company





<u>Running these agents,</u>

As LLMs become better, their understanding of language and
thus their ability to perform NLP tasks such as Sentiment Analysis,
Summarisation, Question Answering and much more improves, the capabilities of
these agents also improve.

To capitalise on this new technology, this project
introduces the use of these agents to work towards a goal of analysing specific
stocks, inspiration from

[Stock Analysis with AI Agents, using CrewAI 🚣 - YouTube](https://www.youtube.com/watch?v=e0Uj4yWdaAg)

[GitHub - joaomdmoura/crewAI-examples](https://github.com/joaomdmoura/crewAI-examples/tree/main)

In order to better understand how these agents work as well
as have knowledge in Agent Communication & LangChain in order to perform
better.



This chain of agents will work together to take news from various places, perform sentiment, and various critical analysis of the data. The final goal is to give positions that should be performed at the start of the day to start.



Two sentiment models are used in this project, these include:

- [ProsusAI/finbert · Hugging Face](https://huggingface.co/ProsusAI/finbert)

- [EleutherAI/pythia-1.4b · Hugging Face](https://huggingface.co/EleutherAI/pythia-1.4b)



We will be using Pythia-1.4B model, this is because unlike FinBERT, it understands language much better. This is because when testing both models on this comment below, 

`I love chicken, its tastes so nice but it's the worst industry to invest in.`

FinBert obtained a nuetral sentiment, and Pythia gave a Negative sentiment, which states it understands this context.


<img title="" src="https://github.com/makiisthenes/Agents-Based-TradingCompany/assets/52138450/0b3b36f9-e828-4c81-b93e-62e9ce0a4b3c" alt="" data-align="center" width="477">


------

I recently came across an interesting video about Agents,
linked below: [Video Link](https://www.youtube.com/watch?v=kJvXT25LkwA)

-----

<u>What is an agent and the reasoning behind this?</u>

All AI LLM models currently run on system 1 thinking, in
which predictions of next words, LLMs are large generative models, that are
able to understand language and produce sentences responses with great language
understanding.

<img title="" src="https://github.com/makiisthenes/Agents-Based-TradingCompany/assets/52138450/609961f3-ada1-4a1b-bec8-5b7835a6c521" alt="" data-align="center">

Current LLMs are just auto-predict on steroids, no LLMs are able to process a
request for 40 mins, look at the request from multiple angles, and then offer a
very rationale solution from a complex problem.

<img title="" src="https://github.com/makiisthenes/Agents-Based-TradingCompany/assets/52138450/4d4808ae-3fbf-49c4-b35e-b68985092cfd" alt="" data-align="center" width="477">


A way to work around this is the use of:

- Tree of thought, forcing the LLM from multiple
  perspectives from different “experts” and these experts form a decision by
  respecting each expert’s position.

- Agents’ systems such as CrewAI, make experts that can collaborate which each other and there by solving complex tasks.





Also we could run language models locally, this is done by reducing the models parameters memory requirements such as quantization from float64 or float32 to reduced float8, which may work less accurately, but perform on lower capable hardware with lower VRAM.

**LLaMA** (**Large Language Model Meta AI**) is a family of autoregressive large language models (LLMs)





<u>How do we make these agents smarter?</u>

This can be done by giving these agents access to tools,
this is by the agent generating commands that can be processed by these tools
to further the development of them.

Two ways to for agents to use tools:

-          Built in tools that are part of Langchain, these are tools for different tasks available to the agent to use

-        Custom made tools.





------
