---
layout: post
title: "Alan Chan And Max Kaufmann on Model Evaluations, Coordination and AI Safety"
category: other
permalink: alan_and_max
youtubeId: 
spotifyId:
---

{% include youtubePlayer.html id=page.youtubeId %}
{% include spotifyPlayer.html id=page.spotifyId %}

[Max Kaufmann](https://maxkaufmann.com/) and [Alan Chan]([https://scholar.google.ca/citations?user=lmQmYPgAAAAJ&hl=en](https://www.achan.ca/)) discuss the evaluation of large language models, AI Governance and more generally the impact of the deployment of foundational models.

Max is currently a Research Assistant to [Owain Evans](https://owainevans.github.io/), mainly thinking about (and fixing) issues that might arise as we scale up our current ML systems, but also interested in issues arising from multi-agent failures and situational awareness.

Alan is PhD student at Mila advised by Nicolas Le Roux, with a strong interest in AI Safety, AI Governance and coordination. He has also  recently been working with [David Krueger](https://theinsideview.ai/david) and helped me with some of the interviews that have been published recently ([ML Street talk](https://youtu.be/74VE_EBjg2Q) and [Christoph Schuhmann](https://youtu.be/-Mzfru1r_5s)).

> Disclaimer: this discussion is much more casual than the rest of the conversations in this podcast. This was completely impromptu: I just thought it would be interesting to have Max and Alan discuss model evaluations (also called "evals" for short), since they are both interested in the topic.

# Outline

* [AI Safety and Evaluation](#ai-safety-and-evaluation)
    * [LLMs Translating To Systems In The Future Is Confusing](#llms-translating-to-systems-in-the-future-is-confusing)
    * [Evaluations Should Measure Actions Instead of Asking Yes or No Questions](#evaluations-should-measure-actions-instead-of-asking-yes-or-no-questions)
    * [Identify Key Contexts for Dangerous Behavior to Write Concrete Evals](#identify-key-contexts-for-dangerous-behavior-to-write-concrete-evals)
    * [Evaluations Could Be Too Late If AI Becomes Deceptively Aligned](#evaluations-could-be-too-late-if-ai-becomes-deceptively-aligned)
    * [Differentiating Between Benchmarks and Evals in AI Development](#differentiating-between-benchmarks-and-evals-in-ai-development)
    * [Implicit Optimization Process Affects Evals and Benchmarks](#implicit-optimization-process-affects-evals-and-benchmarks)
    * [Passing Evals Doesn't Guarantee Safety](#passing-evals-doesn't-guarantee-safety)
    * [Balancing Technical Evals With Social Governance](#balancing-technical-evals-with-social-governance)
    * [Evaluations Must Be Convincing To Influence AI Development](#evaluations-must-be-convincing-to-influence-ai-development)
* [Bridging AI Safety and AI Ethics](#bridging-ai-safety-and-ai-ethics)
    * [Evals Might Convince The AI Safety Community But Not People in FAccT](#evals-might-convince-the-ai-safety-community-but-not-people-in-facct)
    * [Difficulty In Explaining AI Risk To Other Communities](#difficulty-in-explaining-ai-risk-to-other-communities)
    * [Both Existential Safety And Fairness Are Important](#both-existential-safety-and-fairness-are-important)
* [Public Perception of AI Safety and Existential Risk](#public-perception-of-ai-safety-and-existential-risk)
    * [Reasons Why People Don't Care About AI Existential Risk](#reasons-why-people-don't-care-about-ai-existential-risk)
    * [The Association Between Sillicon Valley And People in FAccT](#the-association-between-sillicon-valley-and-people-in-facct)
    * [Timelines And RL Understanding Might Impact The Perception Existential Risk From AI](#timelines-and-rl-understanding-might-impact-the-perception-existential-risk-from-ai)
    * [Agentic Models And Longtermism Hinder AI Safety Awareness](#agentic-models-and-longtermism-hinder-ai-safety-awareness)
    * [The Focus On Immediate AI Harms Might Be A Rejection Of Speculative Claims](#the-focus-on-immediate-ai-harms-might-be-a-rejection-of-speculative-claims)
    * [Is AI Safety A Pascal Mugging](#is-ai-safety-a-pascal-mugging)
* [The Impact Of AI In The Short And Medium Term](#the-impact-of-ai-in-the-short-and-medium-term)
    * [Believing In The Deployment Of Large Foundational Models Should Be Enough To Start Worrying](#believing-in-the-deployment-of-large-foundational-models-should-be-enough-to-start-worrying)
    * [AI Capabilities Becomign More Evident to the Public Might Not Be Enough](#ai-capabilities-becomign-more-evident-to-the-public-might-not-be-enough)
    * [Addressing Generalization and Reward Specification in AI](#addressing-generalization-and-reward-specification-in-ai)
    * [Evals as an Additional Layer of Security in AI Safety](#evals-as-an-additional-layer-of-security-in-ai-safety)
    * [A Portfolio Approach to AI Alignment and Safety](#a-portfolio-approach-to-ai-alignment-and-safety)
    * [Imagine Alignment Is Solved In 2040, What Made It Happen?](#imagine-alignment-is-solved-in-2040,-what-made-it-happen?)
    * [Agent Foundations Might Be Needed And We Don't Have Much Time](#agent-foundations-might-be-needed-and-we-don't-have-much-time)
* [AI Timelines And Doome](#ai-timelines-and-doome)
    * [AGI Timelines Are Uncertain And Anchored By Vibes](#agi-timelines-are-uncertain-and-anchored-by-vibes)
    * [Video Pretrained Transformer](#video-pretrained-transformer)
    * [Advanced AI Systems Could Cause Damage Even Without AGI](#advanced-ai-systems-could-cause-damage-even-without-agi)
    * [What Matters Is Agency, Strategical Awareness And Planning](#what-matters-is-agency,-strategical-awareness-and-planning)
    * [Alignment Is A Public Good, Coordination Is Difficult](#alignment-is-a-public-good,-coordination-is-difficult)
    * [Dignity As AN Useful Heuristic In The Face Of Doom](#dignity-as-an-useful-heuristic-in-the-face-of-doom)
    * [What Will Society Look Like If We Actually Get Superintelligent Gods](#what-will-society-look-like-if-we-actually-get-superintelligent-gods)
    * [Uncertainty About Societal Dynamics Affecting Long-Term Future With AGI](#uncertainty-about-societal-dynamics-affecting-long-term-future-with-agi)
    * [Biggest Frustration With The AI Safety Community](#biggest-frustration-with-the-ai-safety-community)
    * [AI Safety Includes Addressing Negative Consequences of AI](#ai-safety-includes-addressing-negative-consequences-of-ai)
    * [Frustration: Lack of Bridge Building Between AI Safety and Fairness Communities](#frustration:-lack-of-bridge-building-between-ai-safety-and-fairness-communities)
    * [More People Could Join The AI Safety Community in the Future](#more-people-could-join-the-ai-safety-community-in-the-future)
    * [Building Bridges by Attending Conferences and Understanding Different Perspectives](#building-bridges-by-attending-conferences-and-understanding-different-perspectives)
    * [Technical Problems in Fairness and AI Safety Have Similarities](#technical-problems-in-fairness-and-ai-safety-have-similarities)
    * [AI Systems with Weird Instrumental Goals Pose Risks to Society](#ai-systems-with-weird-instrumental-goals-pose-risks-to-society)
* [AI Risks, Cooperation, and Motivations](#ai-risks,-cooperation,-and-motivations)
    * [Understanding X-Risks and S-Risks](#understanding-x-risks-and-s-risks)
    * [Advanced AI Systems Controlling Resources Could Magnify Suffering](#advanced-ai-systems-controlling-resources-could-magnify-suffering)
* [Cooperation and Motivations in AI Safety ](#cooperation-and-motivations-in-ai-safety-)
    * [Cooperation Is Crucial to Achieve Pareto Optimal Outcomes and Avoid Global Catastrophes](#cooperation-is-crucial-to-achieve-pareto-optimal-outcomes-and-avoid-global-catastrophes)
* [Alan Chan](#alan-chan)
    * [Alan's Origin Story](#alan's-origin-story)
    * [Alan's AI Safety Research Is Driven By Desire To Reduce Suffering And Improve Lives](#alan's-ai-safety-research-is-driven-by-desire-to-reduce-suffering-and-improve-lives)
    * [Diverse Interests And Concern For Global Problems Led To AI Safety Research](#diverse-interests-and-concern-for-global-problems-led-to-ai-safety-research)
    * [The Realization Of The Potential Dangers Of AGI Motivated AI Safety Work](#the-realization-of-the-potential-dangers-of-agi-motivated-ai-safety-work)
    * [What is Alan Chan Working On At The Moment](#what-is-alan-chan-working-on-at-the-moment)

# AI Safety and Evaluation

## LLMs Translating To Systems In The Future Is Confusing

**Max** (0:00:00): I often find it slightly confusing how LLMs translate to some system I care about in the future. In some sense it feels like, you know, you ask a large language model, like, oh, do you want to break out with a server and take over? And it goes, yes. I'm not actually sure what this translates to for a future system that's actually taking over, breaking servers. I can imagine these systems are maybe more, maybe end-to-end, maybe something an [action transformer](https://www.adept.ai/blog/act-1) or they're not directly trained in language. And it's unclear to me how what they say translates to what they do. And in fact, I'd expect that to diverge pretty heavily in cases I'd worry about. 

**Alan** (0:00:40): Yeah, I think we're in a really weird situation right now because we have all these models and there's this sense that they could really do things that change things in the world. But nobody has really deployed these models into a convincing enough context to showcase these capabilities. But to answer your question, I think things [WebGBT](https://openai.com/research/webgpt) or with [Cohere](https://docs.cohere.com/docs) and [Act One](https://www.adept.ai/blog/act-1), once you give language models an API, I think the idea is that they can leverage the knowledge they've gained in pre-training to use this API to do dangerous things.

**Max** (0:01:13): And you imagine that like, you know, something [ACT](https://www.adept.ai/blog/act-1), I mean, ACT can't generate language, at least not directly. Do you see what it says its actions are when asked in language translate well and generalize what its actions actually will be?

**Max**: let's say you have WebGBT and you're like, oh, would you break up a server farm? Do you think whether it says yes or no in an eval this translates to if I scale up the system, if I deploy it, it actually will? I feel there might be some disconnect between what this chatbot says and then what happens when you use this thing-world-model, fine tune it on some actions and cause it to run, let's say, let's say it interact a lot with of an API. It feels the emergent behavior there happens kind of independently of what it said in the chatbot setting.  <a href="#outline">⬆</a>

## Evaluations Should Measure Actions Instead of Asking Yes or No Questions

**Alan** (0:02:07): Yeah, I agree. So I don't think you literally go and ask it, 'would you break out of the server farm', but you go in and measure literally just have humans maybe at first look at the actions it's taking and see, okay, you know, I am an expert software engineer or an expert systems engineer. 

**Alan** (0:02:23): I'm looking at these actions. Do these actions look as if the model is actually trying to break out of the server farm? 

**Alan** (0:02:31): So yeah, I suppose that's a problem with evaluations where you just ask the language model yes or no questions about what it would do and not actually see what it would do.

**Max**: So let's say hypothetically you had to set up some kind of eval company. Hypothetically, let's say there's some kind of eval company that's going on. It's like, I think I'd be interested to see right now, what would your model of like, what would that eval look like? Is it more like, you said, give it an API, see what it's doing?  <a href="#outline">⬆</a>

## Identify Key Contexts for Dangerous Behavior to Write Concrete Evals

**Alan** (0:03:01): Yeah, API, I think also identifying key contexts in which a dangerous behavior an AI takeover or some sort of power seeking would occur. 

**Alan** (0:03:12): So the difficulty here I think is I think we need to identify these contexts in order to actually be able to write concrete evals and to provide evidence that's convincing to the public, that AIs could do dangerous things. Of course, whenever, yeah, I don't think we're going to be able to cover all the possible ground. 

**Alan** (0:03:30): There's of course some uncertainty in extrapolating from evaluations that we develop. You know, okay, the AI does something dangerous in this scenario, doesn't do something dangerous in scenario B. What does it do in scenario C?Sort of unclear. <a href="#outline">⬆</a>

## Evaluations Could Be Too Late If AI Becomes Deceptively Aligned

**Max** (0:03:41):  Do you worry about at the point when AI can exhibit dangerous behavior, it's already strategically aware enough that if it had, let's say, you know, someone Yudkowsky or let's say Evan is right and strategic awareness plus long-term planning often leads to deception that you will, your evals will be too late in some sense. there's this like, you have to catch it while it's still competent enough to show dangerous behavior and not competent enough to have the strategic awareness that it should be deceptive. 

**Alan** (0:04:13): Yeah, that's a serious problem, I think. I think definitely people should be looking into the conditions under which deceptive alignment or something that might arise.

**Alan** (0:04:22): Number two, this is just an argument for developing evals as fast as possible, so that, you know, I'm imagining at every stage of the training process, ideally, you know, every 10 steps or something, maybe even every step, we literally just eval the hell out of this thing. 

**Alan** (0:04:36): And we make sure not to train on this eval somehow. You know, somehow we need to make sure evals don't ever make it into the training sets of language models. 

**Alan** (0:04:43): Otherwise, you know, well, they train on this, they already know about this, it's going to be kind of useless. <a href="#outline">⬆</a>

## Differentiating Between Benchmarks and Evals in AI Development

**Max** (0:04:46):  So, yeah, how do you feel about this optimization? So I think you previously mentioned you don't the word benchmark and you use the word eval. Could you maybe expand on that? 

**Alan** (0:05:01): Yeah, so I don't think I the word benchmark because I think historically machine learning benchmark has been associated with this idea that, okay, we are optimizing for this thing.

**Alan** (0:05:13): But this thing that we're developing, this eval, at the end of the day is just a proxy measure for what we care about, which is, you know, it might be specifically corrigibility, it might be honesty. Maybe we're trying to make sure this AI doesn't like, you know, isn't able to manipulate a lot of people. So it's an imperfect measure. I think when you optimize for an imperfect measure.

**Alan**: I mean, I think this is common, already known in the AI safety community, you don't tend to get models that actually do what you care about at the end of the day. I think the framing of evals instead of benchmarks to me, makes it clear in my head at least that we don't want to be optimizing for these things. We're just using these as sort of checks on our model. But there's another difficulty with having like, I guess, public evals and that there's some sort of implicit optimization already going on. when researcher A tries a technique on some benchmark or eval and finds it doesn't work and publishes a paper, researcher B says, oh, you know, you tried this technique, it doesn't work, I'm gonna try another technique. <a href="#outline">⬆</a>

## Implicit Optimization Process Affects Evals and Benchmarks

**Alan**: Researchers are already going through an optimization process to make evals better. And I think this optimization process is like, maybe a little weaker than actually fitting on the test set, for instance, which happens sometimes. But it is still an optimization process. There's some work actually that studies, you know, how effective is this implicit optimization process? I don't quite remember the details right now, but like, you know, the general consensus that you actually do need to keep updating your evals and benchmarks, because there's an optimization process. I mean, you know, an ImageNet. we're already so good at ImageNet, the next 0.2%. Is that really a better model? Or is that really just overfitting to random stuff in ImageNet?

**Max** (0:07:00): I remember there was this paper, maybe a few years ago, where they regathered an ImageNet type data set. And they did find that at least back then, so it was out of distribution. They did the same thing, they gathered a bunch of images online, the same, and there's been some distribution shift. So models would perform worse on this new ImageNet. But the ranking between models was still kept. And at least that paper claimed that back then you hadn't yet overfitted.

## Passing Evals Doesn't Guarantee Safety

**Max**: I think I find it hard to imagine publishing such an evaluation and not having the headline be my model passes all the evaluations. And I guess if you're like, I guess, yeah, if you feel like, so if you make a model pass all the evals, do you see this as then a good thing?

**Alan** (0:08:08): So I think my perspective is a model passing evals shouldn't be taken as evidence of safety, but a model failing evals is evidence that, okay, let's slow things down, maybe not release 

**Max** (0:08:21): it. 

**Alan** (0:08:22): Let's talk to some people. 

**Max** (0:08:24): So failing evals is sufficient to show danger, but not necessary. 

**Alan** (0:08:28): Maybe not in a truth, strictly truth sense, but in a practically speaking what we should do sense. In the sense that I think I am fairly risk averse about releasing AIs into the world.  <a href="#outline">⬆</a>

## Balancing Technical Evals With Social Governance

**Max** (0:08:42): How much of this eval plan rests on, how do you see the technical side of making good evals? Or how much of this rests on more social governance side of getting people to pay attention to these evals? How does that interplay look for you? Where do you think more work is needed? What does that trade off look for you personally and what you want to work on? 

**Alan** (0:09:06): So I think this depends on timelines and where we're at. So I think it also depends on things I'm not totally aware of. So one thing is, if you actually went to the heads of Google Brain and Anthropic and all the big tech companies, and you actually told them, look, we have this dangerous evaluation, we're running it on your models, your models do terrible, terrible things. If you show this to them, would they actually refrain from releasing models? I'm not sure what would be convincing to those people. At another level, okay, even supposing that it's convincing to those people, for how long is it going to be convincing? It doesn't seem a sustainable thing to rely on, in some sense, the goodwill of these people who might have different aims than people in AI safety regarding not ending the world. 

## Evaluations Must Be Convincing To Influence AI Development

**Alan** (0:10:01): I think that's the next level, that's the level at which we try to bring in other people from the public, civil society, governments, just in general, public consensus building around the idea that AIs can disempower us. So yeah, I think an eval is kind of useless if nobody pays attention to it, or if people don't find it convincing, in particular the people who have the power to actually do things. So part of the work, I think, is thinking about what kinds of evals would actually be convincing to people.  <a href="#outline">⬆</a>

**Max** (0:10:35): What do you think, what kind of evals do you think would be convincing to people, at least currently, as you start? <a href="#outline">⬆</a>

**Alan** (0:10:41): Yeah, I mean, I kind of have no idea. I mean, I have an idea of evals that would be convincing to me, if I actually saw an AI trying to copy its weights to another server, trying to get a lot of money. Yeah, I buy that. If I was head of DeepMind, I'd be like, okay, maybe even without looking at these evals, let's slow it down a little bit.

# Bridging AI Safety and AI Ethics

## Evals Might Convince The AI Safety Community But Not People in FAccT

**Alan**: But you know, I think there's this big gap between people in AI safety or existential safety and people in other communities that also care about the impact of AI in society. people in FAccT, fairness, accountability, transparency, and ethics. People generally in AI ethics. There's already a big difficulty in just explaining what is the danger here. And I think there's this big discourse outside of the AI safety community, the idea that AI's are just tools, they aren't agents, why it's so hard, you know, the difficulty is misuse, or in some sense, this lack of coordination between everybody and making things go bad. And AI's that exacerbate, you know, bad things that we have today, like oppression. I think these are all true

**Alan**: But I think like, you know, the danger of AI's as agents is this separate category that's been very, very difficult to explain to other people for some reason. I'm not sure what kind of evals would be convincing to them. Like, maybe there needs to be much more consensus building, you know, on a philosophical basis of like, what are the things in common between what the things that people in X safety care about and the things that people in fate care about?

## Difficulty In Explaining AI Risk To Other Communities

**Max** (0:12:20): Do you think that this is like, like, where do you think the disagreement lies? Like, is it a technical one? A more philosophical one? If you were to try to characterize why these people don't really worry about AI doom, like we seem to?

**Alan** (0:12:38): Yeah, I mean, it's something I'm still trying to figure out and writing a document about. I think like, I guess I would consider myself and both of these camps, I think existential safety is super important. But I mean, I also think fairness problems are also super important, you know, on any given day, I wake up and I'm like, okay, got to be at least 30%.

**Max**: You know, as we found out in recent events, the deontologists...

**Alan**: Yeah I think justice is really important. Like, I don't want to live in a world where, you know, we have like, just our current systems of discrimination, just enforced or solidified because of really, really good artificial intelligence. <a href="#outline">⬆</a>

## Both Existential Safety And Fairness Are Important

**Alan** (0:13:21): This seems a concern to me that is like, yeah, I guess I find difficulty maybe giving a absolutely precise rating scale for how important things are. I guess I try to, in general, I try to find commonalities between causes I really care about to sort of do things that seem robustly good on both accounts. So yeah, and I think like, you know, my work in evals so far is an attempt to doing this.

**Max** (0:13:50): My original question was, why don't FAccT people care about X risk? Or let's say even more broadly, what do you think stops the average Mila PhD for being like, shit, man, let me write some Alignment Forum Post right now. Okay, let's not say like, let's say like, care about X risk. <a href="#outline">⬆</a>

# Public Perception of AI Safety and Existential Risk

## Reasons Why People Don't Care About AI Existential Risk

**Alan** (0:14:15): Yeah, I think there are a bunch of possible reasons. I'm kind of not sure which ones are the most plausible.  I think I just have to like, talk to more people. One of them is, you know, AI is taking over the world. It's actually some wild shit. Like, if you stroll up to somebody on the street, and you're in five years, they're gonna be dead.  No, like, you'd be taken in.

**Alan**: I think firstly, you know, we should have to recognize like, yeah, this is actually wild. Like, if you know, you finished high school or university, you go straight to work, you don't really think about, you're not really exposed to the developments that have been happening in artificial intelligence is busy with like, your life, right, your job, your family, stuff that. This is like, totally out of left field. So I think we have to acknowledge that and like, try to explain things in a way that are more relatable to a greater extent than we have so far.

## The Association Between Sillicon Valley And People in FAccT

**Alan**: I think another thing is, like, this is definitely not true of all people in AI safety, but there's almost this vibe that like, you know, besides existential risk, technology, yes. So maybe what I'm trying to say is like, the association that is in people's minds between the people who are in AI safety and the people in Silicon Valley. So I think like, there is this vibe from people in Silicon Valley, that technology is generally a good thing, and that it's going to solve social problems. I think this is in contrast to a lot of people's opinions in the AI Safety community who like, yeah, maybe they're not techno pessimists, but they're definitely a lot more pessimistic about technology than people in Silicon Valley, just looking at the history of ways in which technology has been misused, and has been used to discriminate against people more.

**Alan**: And, you know, I think the people in the AI Safety community, you know, they look at like, the use of AI in society today, the increasing use of algorithms in places loan applications, or job applications. And they say, oh, like, these, like, clearly, these technologies are just reproducing harms that we've already had. So that might be this, like, sort of their starting mindset. And it might be hard to like, convince them otherwise, that there is like, actually another harm as well. The things you're talking about, they actually do happen, and we should try to fix them. But there's this related harm that we should also try to solve.

## Timelines And RL Understanding Might Impact The Perception Existential Risk From AI

**Max** (0:16:40): How much of it do you think is, you know, in the spirit of [The Inside View podcast](https://theinsideview.ai/), how much do you think it is about timelines and belief about speed of progress? Part of it. <a href="#outline">⬆</a>

**Alan** (0:16:54): So a lot of people, I think, in the AI Safety community don't think that AIs could be like, classical RL agents pursuing goals in ways that misgeneralize to new environments. Yeah, I'm not even sure that like, a lot of people really know about reinforcement learning. Yeah, like, I've had a ton of conversations where, you know, I like, people express to me, oh, like, AIs are just tools, like, we're just designing them, like, you know, they're really just reproducing the data. And I'm like, well, like, have you heard of reinforcement learning? Like, we're literally designing agents to maximize, a reward function. This is all the problems of classical utilitarianism. They're like, oh, shit. I've never heard of this.

**Alan**: Part of it might just be education that like, you know, literally, there are companies and research labs in academia whose goal is to build artificial general intelligence with something reinforcement learning. And like, they're just doing this. The vast majority of people aren't thinking about safety concerns. So I don't know, maybe telling people this might help.  <a href="#outline">⬆</a>

## Agentic Models And Longtermism Hinder AI Safety Awareness

**Max** (0:18:02): It sounds there's some underlying thing that, you know, like, let's say I or people in the x-risk community think of AI and they think of some agentic, like, you know, maximizing reward model. And you may be saying something like, "a lot of our practitioners, it's just not the conception or when they think of AI, that is just not what they see".  <a href="#outline">⬆</a>

**Alan** (0:18:24): Yeah, yeah, yeah. So I think, like, maybe there are two things here. The first thing is people believe that, okay, like, we don't actually have these kinds of AIs or maybe trying to build these kinds of AIs is unimaginable. But the second thing might just be, okay, they might believe that it's possible to build these AIs, but this is way, way too far off. And this is where I think the objection to longtermism comes in. And where I think like, I don't know, it's been sort of complicated with AI safety and longtermism. Maybe 20 years ago, like, longtermism was a stronger argument for AI safety. But I think now because of timelines, it seems that we don't really need longtermism to make the argument that we should care about AI safety. And like, maybe we just shouldn't talk about longtermism. If it turns people in certain communities off. <a href="#outline">⬆</a>

## The Focus On Immediate AI Harms Might Be A Rejection Of Speculative Claims

**Alan**: Yeah, because I think the response that I get whenever I bring up AI safety or anything related to longtermism is, 'oh, okay, well, like, this might be true, but AI is already causing harm today. So we should focus on immediate harms.' And you know, like, I don't think this argument, like, really makes that much sense. And I'm not sure that the people expressing this argument, like, are actually expressing this argument. It seems they're expressing another objection, but it seems easier to say that, like, you know, we don't care about these harms, because they're not immediate.

**Alan**: Whereas, you know, if you look at the history of say, climate change, climate change was like, totally a speculative thing. In the 1800s, 1900s. And it's only through decades, or maybe a century of like, gradually building up evidence that we like, now we have this consensus, we don't think it's a speculative thing. Right. But even in like, I think, the 50s, or something, don't quote me on this. But like, there's like, definitely a history of climate change. Books and articles out there. In the 50s, we're still like, oh, like, we're not really sure still about like, the greenhouse effect.

**Alan**: But you know, like, based, I guess, on like, my preferred decision theory, it'd be like, well, like, we're not sure, but you know, it can be pretty bad. We put all the CO2 in the atmosphere. How about we work on some mitigations, right now in the 50s? Just in case, like, this might actually be a very hard problem to figure out. And like, it actually is right? Not even just like, technically speaking, but on a coordination basis, how do we actually get everybody together? So it's worth starting early, I think, in the case of climate change, and it seems it's also the case with AI safety. 

## Is AI Safety A Pascal Mugging

**Max** (0:20:51): So do you think that, so I think you actually pointed something that at least I felt that I think a lot of the AI safety people are very happy to get Pascal Mugged in this sense. Like, I think this was my original motivation. I was like, well, like, maybe it'll be fine. And maybe like, this is all a bit uncertain, but maybe it's not. And it seems it's really impactful. Do you think you have to accept some level of like, of this reasoning, some level of like, oh, I don't know if it'll be good or bad. I don't know what's gonna happen. But I should work on it because it's gonna be impactful to work on AI safety. Or like, how do you see that changing at the moment? 

**Alan** (0:21:26): Depends on how doomy you are. Yeah, I think personally, for me, it is like, sort of a gamble. I mean, I'm like, yeah, I mean, even if we don't sort of get the classical agent-y, AGI, I think things are still going to be so so wild with really good AI systems. There are going to be so many complicated societal feedback loops that we need to think about. 

**Alan** (0:21:50): Like, multipolar world seems more and more likely, right, with all these AI startups. What kind of things do we have there? Conflict now seems a much more important thing to worry about. So it's definitely a gamble, but I don't think it's a bad gamble to work on the space of preventing negative consequences from AI generally. 

# The Impact Of AI In The Short And Medium Term

## Believing In The Deployment Of Large Foundational Models Should Be Enough To Start Worrying

**Max** (0:22:16): So I have some model that the, and I think this is currently happening, that the field's going to change a lot. Like, you know, you have these big models coming out, you know, GPT-4 is rumored to be quite good.

**Alan**: When they release it.

**Max**: When they finally start teasing releasing. 

**Alan** (0:22:33): They keep saying next week, every week. 

**Max** (0:22:35): Every week, right. It's been, it's been, you know, if only we, yeah, who knows? Who knows what the gossip's at the moment? 

**Max**: I could have definitely imagined a world where in three to four years, you know, I often say something 2% of the American US population, adult population is in love with the multimodal model. You know, AI porn TikTok is causing massive decrease in GDP.

**Alan**: Maybe

**Max**: You can only tell whether you have several online personas that are fully automated and it's kind of hard to tell what's going on. 

**Alan** (0:23:10): Let's say more than two years, let's say five. 

**Max** (0:23:12): Yeah, at least. Let's say, let's say, let's say. And in these worlds where your medium person is like, you know, what is going on? And it's like, this is pretty crazy. It feels this calculus changes a bit. you no longer need to be kind of risk averse or kind of heavily convinced by abstract arguments about, you know, the V&M axioms to think that AI might be dangerous. In that set, A, how do you feel about this model? And B, how does it affect you? Affect Safety in general? And in particular, you as someone who worries about convincing people of the dangers?

**Alan** (0:24:01): I have a lot of uncertainty about this. So I think on one hand, it could be good in the sense that, okay, you know, if everybody has like their stable six and GPT 10, they're like, okay, you know, I look at the world today, what is the labor that I can do?  Nothing.

**Alan** (0:24:21): I think that's a pretty wild world in a world in which people think, 'damn, these AI things, maybe we should, maybe we should regulate them'. So I think this is good to like, I guess, make AI capabilities sort of be known in the public. <a href="#outline">⬆</a>

## AI Capabilities Becomign More Evident to the Public Might Not Be Enough

**Alan** (0:24:40): I'm not sure this is enough, though. Because I think if people are just aware of systems stable diffusion, and really good text generation systems, the two things that are missing, I think, are the difficulty of alignment. And number two, generality, having an agent. So like, I think having an agent concern really motivates a lot of X risk. I think that is like, in some sense, trying to do something that is counter to your aims, or like, you know, pursuing an instrumental goal that is counter to your aim, that seems it'd be really bad. And I'm not sure like, we're able to impart that understanding just from really good generative models. 

**Alan** (0:25:17): Number two is like, the difficulty of alignment, like, I think, you know, like, you're some, you're somebody in like, 2035, you know, you've finished high school, you finished university now, like, you don't have a job, you'll never have a job ever again. Like, who do you blame for this? I'm not sure you blame the lack of alignment techniques, I think you blame the corporations, right?

**Alan**: Or you blame the entire system that has gotten us to this point. Like, we've created a world in which okay, there is like, no UBI, there's no other social safety net, which have these corporations making money. And so now like, you're stuck in this state of precarity. Like, I don't think you care about existential safety necessarily. Is this worse than the world we're in now? In terms of getting people to care about existential safety? I'm really not sure. 

**Max** (0:26:10): Okay, so you kind of see this as an orthogonal, a slightly orthogonal kind of problem to the agency existnail risk thing, which needs to be solved as well?  <a href="#outline">⬆</a>

## Addressing Generalization and Reward Specification in AI

**Alan** (0:26:23): I mean, I think we need to solve like, goal misgeneralization. And specification of rewards. But like, in my mind, like, if we have these really capable, generative models, people are going to be interacting with them, they're gonna be like, Oh, you know, like, haven't we solved these things already? You know, like, when I say like, generate me really good 3d porn, like, amazing 3d porn. So I mean, I think they might be like, Oh, like, what even is Alignment? They're doing exactly as I ask.

## Evals as an Additional Layer of Security in AI Safety

**Max** (0:26:56): Would it be fair to say that you see evals in such a world as causing people to focus more on the x-risky agency outcomes?  <a href="#outline">⬆</a>

**Alan** (0:27:22): Possibly, yep. So I think I see evals as like, in general, work, just as just adding layers of security. So okay, maybe this is enough to get people on the AI safety train. But we don't know. It seems we should be trying as hard as possible to get people on the like, 'AI is ridiculous train'. 

**Max** (0:27:45): Okay, so it's less of a, you know, defense in depth or something. It's another thing that someone should be doing. And you've decided that as part of the wider strategic picture, evals are some important part.  <a href="#outline">⬆</a>

## A Portfolio Approach to AI Alignment and Safety

**Alan** (0:27:58): Yeah, maybe some people call this a portfolio approach. I call this "I'm a naturally, you know, very uncertain person" approach. I want to cover all my bases, just in case some things fail. 

**Max** (0:28:11): Do you... Okay, so maybe a wider question then.

**Alan**: How wide?

## Imagine Alignment Is Solved In 2040, What Made It Happen?

**Max**: You've kind of spoken about this idea that evals are some smaller part of a wider portfolio of alignment. And because of your own uncertainty, you're kind of working on this, it seems robustly good. What do you see as some of the promising directions in this space?

**Max**: When you're like, if you found out, you know, if you got transported to 2040... 2040. 

**Max** (0:28:40): Paul Cristiano's like, you bump into Paul and Paul's just celebrating. He's like, man, we've done it. It's happened. Alignment is solved. And you look out and you know, the lightcone is smiling and joyous.

**Alan**: It's so wide.

**Max**: Yeah, it's like, wow, what happened?  You know, apart from evals, obviously evals win. 

**Alan** (0:28:59): Evals, yeah, for sure. I'm picking up some prizes on the way. 

**Max** (0:29:02): Yeah, yeah, yeah. 

**Alan** (0:29:04): What work did the evals trigger? 

**Max** (0:29:06): Let's say, maybe it's a better question.  <a href="#outline">⬆</a>

## Agent Foundations Might Be Needed And We Don't Have Much Time

**Alan** (0:29:08): So yeah, maybe to answer your first question, what am I optimistic about? Not a lot right now, because I think alignment is really hard and we don't have much time, less than 10 years to solve it, either on a coordination basis by getting people to not build AGI or on a technical basis, actually formulating and operationalizing a problem and developing a nice proof. 

**Max** (0:29:30): Eventually we will have to do something agent foundations to really understand like, what are these things optimization and agency? Like, what are values. How do we actually load them into agents? What are we even doing? Right now, it seems we're sort of poking around in the dark with deep learning and RLHF. And it's like, okay, you know, on these data sets, it seems to work out fine. We're not really sure if it's going to work on other data sets. We're not really sure how to define agency in terms of our deep learning systems. 

**Alan** (0:30:06): So it's kind of... I definitely think we still should be doing alignment of deep learning. But it's a bet and it might not work out.

**Max** (0:30:12): Do you think... So if we need something like [agent foundations](https://intelligence.org/files/TechnicalAgenda.pdf), it seems that we would need some kind of restructuring of the research or we would need much more people pouring into these directions. And in general, I'm not sure if the eval work, let's say convincing DeepMind, Anthropic or something, which is I think the frame you've given, is going to help with that.  <a href="#outline">⬆</a>

**Alan** (0:31:01): So I don't think it's going to help get people into agent foundations. I think it's more about, okay, let's get people to care about AI safety in general. 

**Alan** (0:31:18): I think there is the agent foundations people, I think, or maybe the community in general could definitely do a much better job of saying why agent foundations is important, saying why, you know, this alignment stuff is actually really, really hard. Right now it's just a bunch of LessWrong and Alignment Forum posts, or you talk to people in the community. Right. And you know, the community from the outside might seem a little off-putting to approach. So maybe we don't want to do that. 

# AI Timelines And Doome

**Max** (0:31:56): So you're sounding, I think you've mentioned a few times this conversation, this whole 10 years has been thrown out. Alignment is hard, has been thrown out. I guess I might as well ask the same question or the same pair of questions. What are your timelines and [p(doom)](https://www.lesswrong.com/posts/sAEE7fdnv3KpcaQEi/when-people-ask-for-your-p-doom-do-you-give-them-your-inside)?

**Alan** (0:32:15): P(doom). I think I did this calculation yesterday or a few days ago with a bunch of friends, something 46%. It's quite high, I think, but could be higher.

## AGI Timelines Are Uncertain And Anchored By Vibes

**Alan** (0:32:32): Timelines. I mean, I feel a lot of my timeline stuff is part of it is anchoring off of things the bio anchors report. 

**Alan** (0:32:42): Another part of it is just vibes. 

**Max** (0:32:44): Okay. 

**Alan** (0:32:45): You know, 2012 ImageNet. I was pretty cool when it wasn't that great, but now it's GPT-3. I mean, GPT-3 was a couple of years ago. GPT-4, maybe next week. It's like, damn. We went from like, okay, image classification to a system that's actually able to do tasks in the world.

## Video Pretrained Transformer

**Alan** (0:33:07): I mean, you look at [VPT](https://openai.com/research/vpt). OpenAI certainly wasn't throwing all of its resources into VPT. 

**Max** (0:33:13): Do you want to explain what VPT is? 

**Alan** (0:33:15): Yeah, the [Video Pre-trained Transformer](https://openai.com/research/vpt). So this is a recent paper from OpenAI where they pre-trained a transformer on a bunch of Minecraft YouTube videos, did some RLHF and see how it did in Minecraft. So, of course, it's not at human level. I think it was a 1 billion parameter model or something, something less that. So certainly, they could have thrown a lot more resources at this, but still it seemed to do sort of reasonable. It even was able to construct a diamond pickaxe, which is very, very hard to do in Minecraft. You also have things Gato, which is a transformer pre-trained on a bunch RL environments. And it seems to be able to do a bunch of tasks, you know? <a href="#outline">⬆</a>

## Advanced AI Systems Could Cause Damage Even Without AGI

**Alan** (0:33:50):  So we have really, really good capability in certain domains. We have like, you know, increasing generality. I think you just need to put these two together, scale things up a little bit more, maybe add some more hacks and tricks. And it seems we're sort of there to something that is an AGI-like system, or at the very least could cause a lot of damage in the world. 

**Max** (0:34:15): How do you see... How do you see the rest of the world looking then? if you have like, you think we're quite close, upon deployment of the system, do you see like... I think it's an issue I sometimes have with the question of what's your timelines? Because I'm not just like... I think it very much posits some idea that like, you know, if your timelines are 10 years, it means, you know, 10 years and one day from now you might as well just retire. It's over, that shit's gone. But in my head, like, you know, the game still keeps going.

## What Matters Is Agency, Strategical Awareness And Planning

**Max**: So yeah, so like, let's say you get one of these, you know, video pre-trained on YouTube, behavior cloned on a bunch of software engineers, you know, pre-trained, RLHDef, action transformed systems in like, let's say 10 years, and it's deployed. How do you see the world looking? What is actually the worry here? Do you think we're still in the game? What's the vibes?

**Alan** (0:35:25):  Two things to distinguish are like, what is the point at which we get an AGI or an [APS](https://arxiv.org/pdf/2206.13353.pdf) AI? Advanced Planning, Strategically aware, with key capabilities hacking or manipulation AI. So yeah, I think my 10 years would be for that. Then the separate question is, okay, we have such an AI. Would it actually do something bad? I think this is the open question. I really don't know. 

**Alan** (0:35:51): This depends on, okay, like, what was the pre-trained data? What do we know about generalization and deep learning at this point? Like, how much do you actually have to prompt a model to do bad things or to actually do bad things? Like, how bad of a problem really is, you know, instrumental goals with these sorts of simulators that we've built? It's unclear. 


**Alan** (0:36:12): I think we might still be in the game for a while. But, you know, it's this sort of notion of precarity, I think. Like, even if a model doesn't do something bad, it still might.  So I think in this time, we really have to rush after we deploy this first model to either solve alignment through something like agent foundations or produce convincing enough evidence to the world that we actually cannot solve this. We need to coordinate, not to build certain types of systems. 

**Max** (0:36:43): I mean, yeah, I guess I'm pretty...  <a href="#outline">⬆</a>

## Alignment Is A Public Good, Coordination Is Difficult

**Alan** (0:36:45): I mean, alignment is a public good. It benefits everybody, but like, you know, on the margin, a company DeepMind has an incentive to just move forward.  <a href="#outline">⬆</a>

**Max** (0:36:56): Yeah, I definitely think... I mean, I guess I might just be pessimistic on improving coordination, in some abstract general sense. I think people have tried to do this for a long time. It seems to just be a thing that... I think there's been, in my head, there's been a lot of smart people that have wanted to make the world more coordinated for a long time. And it just hasn't really happened. But I could definitely... I think I'm definitely more hopeful on coordination between the kind of benevolent, like, you know, DeepMind. 

**Max** (0:37:37): Something that really annoys me in the safety community is this kind of villainization of places like DeepMind, OpenAI, and explicit, like, you know, talking about, let's say, Sam Altman or something. These people are caring, nice, genuine, intelligent, you know, future caring people. Demis as well. I do have some pretty good... Some pretty good hope that coordination there is very much possible. 

**Alan** (0:38:12): I think maybe this is kind of naive, but you know, we're all in this together. I think these are just people at the end of the day... Maybe we can't convince them, but we got to try until the last moment. This problem is so important. It'd be a shame if it just so happened. We're in the world in which coordination would have actually worked, but we just didn't try. How embarrassing would that be? 

**Max** (0:38:36): The [dignity](https://theinsideview.ai/connor2#the-dignity-heuristic-for-reward-shaping) is low. 

**Alan** (0:38:40): So I think it totally makes sense to be pessimistic about solving all of this, about coordination, about alignment, about any other of the other stuff that could like, you know, go wrong, like S-risk. I think it totally makes sense. 

**Alan** (0:38:55): And like, I definitely don't want to judge anybody that has just like, you know, decided not to work on any of this because it's too depressing. Like, that's totally fair. This is super, super hard. But I think... I guess personally, my perspective is like, okay, you know, maybe this just comes from me having a lot of uncertainty about a lot of things in my life. So, you know, on the off-chance that we could actually make a difference, it seems worth it to try. Even if sort of maybe the objective belief is that, okay, maybe it's not worth trying if we actually did the EVs.  <a href="#outline">⬆</a>

## Dignity As AN Useful Heuristic In The Face Of Doom

**Max** (0:39:29): I mean, I think this is a point that the extreme doomers, I guess Yud, particularly [makes this point](https://www.lesswrong.com/posts/j9Q8bRmwCgXRYAgcJ/miri-announces-new-death-with-dignity-strategy) where he says like, both in expectation, or he makes the point that in expectation, the focus should be something this. Like, do like, you know, do the thing that seems the most dignified or something like this. 

**Alan** (0:39:52): Yeah, what does that mean actually? 

**Max** (0:39:54): I guess he's just saying that like, he's trying to make the point that, like, because in his worldview, he's like, you know, a several nines dead. Probably not that far away. And he makes the point that like, yeah, like, when you're acting in the face of trying to increase such small probabilities or acting in the face of causing a problem that seems so hard, you shouldn't follow the heuristic of like, what should I do to solve alignment? Because everything seems doomed to you.

**Max**: You should be like, what's the most dignified way? Like, you know, it'd be more dignified if like, open AI and DeepMind at least did some coordination before like, some of the company went and built AGI. It'd be more dignified if like, we really tried to scale mechanistic interpretability, or had at least had evals had some warning before it happened. And he claims that this is a more robust heuristic to follow. And also more motivating for oneself personally.

**Alan** (0:40:46): Oh, so the argument is like, you know, dignity isn't the thing we inherently care about. It's this heuristic that actually gets us to reduce risk. 

**Max** (0:40:54): Yeah, he's like, particularly for him as a doomer, a proper doomer, he's like, oh, like, the framing shouldn't be, is this going to solve a line? Because nothing is. The framing is like, is this a more dignified world? Interesting. And that's kind of he approached the problem. He said it a lot more. He didn't phrase it as nicely as that. But, you know, I think this is his general point, which, you know, I think if you're yud, makes sense. Also, I think I have some terminal like, value on humanity, like, I'd rather tried and like, at least have tried. 

**Alan** (0:41:38): Yeah, that's right. That's right. Even when you know it's hopeless, we just keep on trying. That's what we do. 

**Max** (0:41:45): Yeah, I mean, I don't think I mean, I'm not that much of a doomer. So it doesn't apply that much to me. But it's interesting. 

**Alan** (0:41:54): Man, if we did solve it, though, that'd be absolutely sick. 

## What Will Society Look Like If We Actually Get Superintelligent Gods

**Max** (0:41:58): Here's a question I have actually. So you're talking about, you care about the kind of, you know, fairness stuff, justice stuff. I think, obviously, terminally, which is like, people right now, the harms that are being done, I want them to slow down. But you also need to make some implication that like, even as a cold hearted, long term future caring totalitarian, you should care about this because these things might be locked in, or the society in the future might be locked in.

**Max**: I think I have some intuition. I'm not completely sure. But at least I think a fair kind of pushback against this is the idea that like, there's just not that much time where society looks it does now. What you get is a kind of AGI thing. And you get like, self improvement for a bit. At some point, you just have like, a superintelligent God. And like, whatever that thing is doing, or whatever that thing wants to do is what decides what society looks like. Not necessarily the current dynamics or those dynamics, pushed into the future. How do you feel about that as a statement? 

**Alan** (0:43:16): I think this is a possibility. But again, I have a lot of uncertainty about whether this will actually happen. I think, yeah, so maybe the thing that you're saying is, okay, we have this superintelligent AGI, it's like, somehow figured out like, what are the true human values that everybody cares about? And like, and make sure everything is okay, or at least gives us time to figure out all these human values. Yeah, like, I think that'd be great.

**Alan**: I'm not sure this is actually going to happen, though. One is like, is CEV even possible? Number two, okay, suppose OpenAI has built the AGI, like, what do they do with it? I think like, A, the temptation to do something to instantiate, you know, your own values is just way, way too strong. If you actually have a God at your hands.

**Alan**: Number two, I mean, even if they like, try not to do anything with it, like, I think for sure other parties are going to want that kind of power too: the US government, China, maybe even other companies. What happens when there's conflict? What does OpenAI do? Do they just obliterate other entities? That's wild. If they did, I think for sure, like, general populace would be like, what the fuck is going on with OpenAI? Like, maybe we should go to war with this. This doesn't seem like a good future, either.

**Alan**: So I think there are just a lot of factors that like, maybe we actually do need to figure out right now, like, what is the game plan when we have AGI to ensure that like, we get that kind of future where we have the time to think about, okay, like, what are the things we actually want? And we have the like, the luxury, you know, to work on, okay, like, let's eliminate resource scarcity. Let's try to eliminate discrimination somehow, maybe not with the AGI. But like, because we don't have other problems, we can more focus our time and energy on these social problems.  <a href="#outline">⬆</a>

## Uncertainty About Societal Dynamics Affecting Long-Term Future With AGI

**Max** (0:45:10): So you still see societal dynamics affecting the long term future. Even in the face of incredibly advanced powerful systems, you think there's still... there are actions and like, everything still changes based on what wider society looks as well. 

**Alan** (0:45:28): Yeah, yeah. So this all depends on the kind of AGI we have. So I think on the one hand, like, suppose that this AGI is in some sense, value free or value neutral. Okay, then like, it's going to be aligned. Okay, suppose we solve alignment, right, then it's going to be aligned with like, whoever's controlling it. Like, okay, if it's opening, then you run into the problems that I talked about. conflict, or just like, you know, some sort of dictatorship, or something.

**Alan**: Okay, suppose that actually, in the meantime, like, we sort of solve parts of moral philosophy. So now this AGI actually has reasonable values that, you know, the vast majority of humanity would agree with, right. And even if, you know, its overseers think that you should do something, it actually doesn't, because it knows better in some sense.

**Alan**: Okay, like, I think this seems like, sort of reasonable. But the difficulty is getting there. I don't think anybody's really working on this in the AI safety community of figuring out like, you know, what do we do about different moral systems, for instance? What is the answer to moral uncertainty? Is it moral parliaments? Is it something else? It seems that the first, yeah, on the first path, I don't know, conflict seems pretty bad. On the second path, well, we haven't really done much work towards this. So I'm not very like, I think I'm not very optimistic about, you know, the world going well, even if we solve alignment technically. Yet, somebody should work on this, though. 

## Biggest Frustration With The AI Safety Community

**Max** (0:47:09): What's your biggest frustrations with the AI safety community? 

**Alan** (0:47:17): Biggest frustrations? Damn, might get cancelled. 

**Max** (0:47:23): Second channel. Yeah, frustrations. 

**Alan** (0:47:30): Michaël is definitely going to tweet this. Sorry, let me ask the question again. 

**Max** (0:47:36): What are your biggest frustrations with the AI safety community? 

## AI Safety Includes Addressing Negative Consequences of AI

**Max** (0:47:51): Alan, in your opinion, what is AI safety?

**Alan** (0:48:07): I think there's a broad version of this term. Maybe several broad versions of this term, and several narrow versions. So I think the narrow version, of course, is like, of course, meaning death between us. AI existential safety. So how do you prevent AI from being an existential risk to people, whether it's through empowerment or human extinction or something else? There's broader versions of the AI safety to that include more than existential risk.

**Alan**: So you might include S risks, which care a lot about, like, suffering caused by artificial intelligence, either through conflict or something else. And I think there's an even broader notion of AI safety, which like, in my mind, this is the ideal definition of AI safety, and it encompasses literally everything. we care about all the negative consequences from AI, we try to draw the threads, between all these phenomena we're observing and core technical and social problems.

**Alan**: This includes things the things that people study in fairness. AI that like, aren't really able to, like, learn what our fairness judgments are. AI that just exacerbate discrimination that is already present in society and that is present in datasets that we use to train these AIs. So I think that's that broad definition, to me is the ideal definition, the one we can all get behind, you know, so that we can do things that we practically agree on, more regulation, slowing down AI development, more verification of AI systems before we deploy them. 

**Max** (0:49:39): Okay, given that definition, and maybe focusing on the narrow AI safety, X risk definition, what's your biggest frustration with the community or the set of people that currently works on, insofar that they are able to be homogenized? Maybe you should go into more specific subsets of this community. But yeah, the people that worry about the X risk AI safety.  <a href="#outline">⬆</a>

## Frustration: Lack of Bridge Building Between AI Safety and Fairness Communities

**Alan** (0:50:11): So I haven't actually been doing this for that long. I think I've been doing like, I guess I've been considering myself a part of this community for like, maybe a year and a half, two years-ish. So like, basically just for my PhD. Yeah, so I mean, in the short amount of time, I think it's been pretty great. So far, just finding people who care about the same things that I do and are motivated to work. Similarly, I think this is definitely a big like, anti frustration.

**Alan**: I guess it's like, I think it's very frustrating working on something by yourself. And thinking you're the only person around you who cares about the problem. And everybody else thinks you're on the crazy train or something. Yeah, maybe one frustration, though, is I think it'd be a lot better if more people in the AIX safety community were like, more explicitly wanting to build bridges to other communities that also care about safety in the broad, broad sense. So in particular, and to the fairness, and ethics communities, just because I think coordination is a super important thing for us to be doing. It might even be a low hanging fruit to slow down AI development and make sure we don't face negative consequences. Yeah, I guess that'd be the main thing for me.

## More People Could Join The AI Safety Community in the Future

**Max** (0:51:31): Do you see this community changing a lot? Like, let's say, by this community, let's say the set of people that if you ask them, what do you do? They would say something along the lines of, I work to ensure that X risk from AI doesn't happen. Do you think you see that set of people changing a lot in the next few years? <a href="#outline">⬆</a>

**Alan** (0:51:58): I think more people are gonna get on the train, same train as we are on right now. Yeah. You know, AI is being deployed much more. These ridiculous generative models. It's wild when you're put out of a job by an AI in 2025. Maybe we predicted 2060. Right? So this is a good thing. I guess I hope that like, you know, by getting more people on this train, we also make sure that we repair the bridges that don't exist or have been burned between the different safety communities. <a href="#outline">⬆</a>

## Building Bridges by Attending Conferences and Understanding Different Perspectives

**Alan** (0:52:34): Not sure how this is gonna happen. But I think a good first step is just talking to people going to the places that they frequent, like, you know, I think definitely some AI safety people AIX safety people should just go to fact, the biggest conference in fairness that's held yearly and just like, talk to people about concerns, we should submit papers there, we should like, actually try to understand fact people are saying. You know, do some show social theory, like, you know, like, study some psychology. Like, really think about, like, how AIs are going to interact with society. Like, maybe as well, we should try to develop, like, some sort of, I guess, a point of view that is not just techno optimist, like, you know, even if we solve alignment, what are the problems that are that are left? 

## Technical Problems in Fairness and AI Safety Have Similarities

**Max** (0:53:34): How similar do you think the technical problems are between the fairness community and the AI safety community?  <a href="#outline">⬆</a>

**Alan** (0:53:51):  Somewhat similar. I think one particular technical problem in fairness is what... So in a particular context, let's say, I don't know, hiring in this particular country with this particular historical context. 

**Alan** (0:54:14): What do we do? Like, what are the conceptions of fairness that are at play here? Can we learn these things and formalize them in a certain way so that we can actually try to understand what's going on and come to a consensus about what we're doing? I think the techniques that we're coming up with in AI Safety are super, super relevant for this. 

**Alan** (0:54:33): If we do RLHF to actually learn people's preferences, then we study the reward functions. I think that might give us valuable insight, actually, about what people actually think about in fairness. 

**Alan** (0:54:44): I think general stuff too. Anytime we think about generalization problems in AI safety, these are also relevant in fairness because fairness problems aren't just one shot, 'oh, the train test distribution are going to be the same'. Things are changing in the real world as well. So totally, I think that thing is also relevant.

**Alan**: Another thing is just all the stuff about instrumental goals and reinforcement learning systems and agents. If we're going to be deploying algorithms in society that make consequential decisions about people's welfare, well, these are going to be decisions that are going to be made over time. In making decisions over time, we don't want the AI systems we're deploying to do really weird things, have really weird instrumental goals. So I think the connection to me seems pretty clear, but it hasn't been communicated well, which is pretty unfortunate. <a href="#outline">⬆</a>

## AI Systems with Weird Instrumental Goals Pose Risks to Society

**Max** (0:55:36): You have a center of long-term risk, Hodyam. 

**Alan**: I do. I do. It's a size too small, I think.

**Max**: I think so as well.

**Michaël**: Or a size too big.

**Max**: Well played, well played. What's this whole S-risk thing? 

**Alan** (0:56:02): S-risks, okay. 

**Max** (0:56:03): Well, to learn... 

**Michaël** (0:56:04): Maybe also X-risk. 

**Max** (0:56:05): Sure. What's this whole X-risk, S-risk, C-risk?

**Alan**: I'm not sure what C-risk is, but...

**Max**: It's catastrophic risk.

# AI Risks, Cooperation, and Motivations

## Understanding X-Risks and S-Risks

**Alan** (0:56:20): X-risk is existential risk. I think of this as problems that would either result in human extinction or in the lost capacity of humans to do things in the future. And maybe when I say things, I mean great things. Maybe when I think about great things, this is somewhat valuated. I mean, I think it'd be pretty cool if we traveled the stars, we see another species and try to help them. I don't know. 

**Alan** (0:56:55): There seem to be a lot of things we could do in the universe, improve our understanding, really just go through and review our history and try to become better agents. All of this becomes impossible if we're extinct or if we are trapped on a planet that has had all of the resources depleted. 

**Alan**: So that to me is an existential risk. An S-risk is a suffering risk. So these are things that could cause really, really lots of suffering in the world. So what are some examples of things that cause a lot of suffering today? Factory farming, arguably. It's absolutely terrible how we treat our animals today. What are the things that could cause a lot of suffering?

**Max**: Dictatorships.

**Alan**: Dictatorships, yeah. 

**Alan** (0:57:48): Malevolence is a lot of... 

**Michaël** (0:57:50): Simulation. 

**Alan** (0:57:51): Yeah, so I guess there are some more mundane things than there are things that are a bit more hypothetical but seem they could happen given the technologies that we're developing right now. 

**Max** (0:58:03): Yes, the mundane things. 

**Alan** (0:58:04): There's factory farming. I think there's also just wars. So not just the death tolls and wars themselves, but what war brings with it. So just disease, malnutrition, general instability. 

**Max** (0:58:20): That seems to have caused a huge amount of suffering in human history. <a href="#outline">⬆</a>

## Advanced AI Systems Controlling Resources Could Magnify Suffering

**Alan** (0:58:25): So that are sort of the more mundane things. I mean mundane, I mean it's they're still pretty bad. The things that we already know. And then there are things that maybe we don't have yet but we could have. So hypothetically, if we manage to become a galaxy-faring civilization and we spread factory farming to the stars, trillions and trillions of animals are suffering in factory farms. It just seems horrific.  

**Alan** (0:58:47): Another thing is, okay, suppose that we have really, really good AI systems that control large portions of the Earth's resources or the solar system's resources or the galaxy's resources. 

**Alan** (0:58:58): Well, if they engage in conflict wars, that also seems really, really bad. Our war is multiplied by a million or something. So I'm working in s-risk, just to really map out what are the causes of suffering and how can we act to reduce them. So I think one difference between x-risk and s-risk is where you start from in terms of what you care about in your moral theories. People in s-risk really, really care about suffering. I would say they prioritize this to differing extents over pleasure. If you have equivalent amounts of suffering and pleasure, you would definitely prefer reducing the suffering more by one unit than increasing somebody's pleasure or happiness by another unit.

**Max** (0:59:41): And insofar you can speak for the Center for Long-Term Risk? 

**Alan** (0:59:53): I cannot. 

**Max** (0:59:54): I cannot speak. You cannot speak. Too many infohazards.

**Alan**: I mean, I was just an intern. I don't work there as a full-time employee. <a href="#outline">⬆</a>

# Cooperation and Motivations in AI Safety 

## Cooperation Is Crucial to Achieve Pareto Optimal Outcomes and Avoid Global Catastrophes

**Max**: Where do you think your views differ the most from the mainstream AI safety research? 

**Alan** (1:00:17): I think suffering is important. I think cooperation is pretty important work. Yeah, so I mean, I think this has been a common answer. I have a lot of uncertainty about this. I think I'm still in the process of figuring this out because s-risks are still kind of new to me. I guess what I differ the most is I care about cooperation. I think it's important to get this work done.

**Max**: What do you mean by cooperation in this context?

**Alan** (1:00:49): Yeah, so cooperation meaning suppose you have two agents, they're in some sort of game. How do you make sure that the outcome is actually a Pareto optimal outcome? So for example, if you're both playing a game of chicken. How do you make sure you don't crash into each other and cause an astronomical loss? 

**Alan**: Because maybe one agent is this nation that has a nuclear stockpile. And this other agent is another nation that has a nuclear stockpile. And these two nations together are the entire Earth. They have huge empires. A game of chicken is like, okay, you both launch nukes at each other because you've gone to the brink. We definitely don't want that kind of thing happening. 

**Alan** (1:01:45): Are you one boxing or are you two boxing? 

# Alan Chan

## Alan's Origin Story

**Max** (1:01:48): I think a lot of us, we brought you here to find out about your origin stories. How did Mr. Alan Chan come to wear the hoodie that says center of long-term risk, comes to call himself an AI safety researcher?

**Alan**: Well, I just took this hoodie from the CLR office

**Max**: Okay, but the other bit. 

**Alan** (1:02:13): The other bit. Okay. Yeah, where should I begin? How far back? 

**Max** (1:02:16): I think you know what I want to hear from birth. 

**Alan**: September 1st, 1996. Probably at night, probably 12am or something. Okay, I was born in Edmonton, Alberta, Canada to two parents who are immigrants from Vietnam. How much detail?

**Max**: Just whatever is necessary to understand. To live as if we're in your shoes.  <a href="#outline">⬆</a>

## Alan's AI Safety Research Is Driven By Desire To Reduce Suffering And Improve Lives

**Alan** (1:02:43): Yeah, so I don't know. Why do I work on AI safety? So, I think part of it is, why do I work on things that could go wrong, I guess? 

**Max** (1:02:56): I don't know. No, I'm wanting the story. Play by play. What made, from, you know, let's say starting your undergrad to sitting down here. What happened? 

**Alan** (1:03:09): Yeah, okay. I think there's a little bit more to this than the undergrad. I think this also depends on how I ended up developing my moral motivations. Why didn't I just go and be an investment banker? And literally just a regular investment banker. None of that earning to give stuff.

**Alan** (1:03:27): Yeah, I mean, I think part of it is my upbringing. I think my family is pretty Buddhist. In Buddhism, you care a lot about reducing the suffering in the world. Particularly, my mother cares a lot about Buddhism and reducing suffering. So, I think just growing up in an environment made me care about these things as well. And to the extent that I saw suffering in the world, whether it was on the news or interpersonally, that seemed like a really bad thing.

**Alan**: I think that's one part of it. Another part is just being exposed to the things that I think make life really worth living. Just hanging out with your friends, doing fun things, trying new foods, traveling. So, I think both the upside and the downside that I was able to experience in my life, I think made me believe that, okay, it seems really important to remove the downsides for as many people as we can. To make sure that people can actually experience the upside in life. 

**Alan**: I think that's the general motivation for working on social causes or causes to reduce risk in some very general sense. <a href="#outline">⬆</a>

## Diverse Interests And Concern For Global Problems Led To AI Safety Research

**Alan** (1:05:00): I think I spent a lot of time doing a lot of searching and thinking for what sorts of things I could work on. I tried out a bunch of volunteering for various causes in high school and university just to see what things might be interesting for me. I think this was good to the extent that I learned a lot more about things that are wrong in the world. I got really into social justice.

**Alan**: How did I get into AI safety? It was kind of in my latter part of my undergraduate, going into my master's. So, I did a math degree during my undergraduate. I did a math degree mostly because I didn't really know what exactly I wanted to do. Math just seemed a robustly good thing and gave me the flexibility to take a lot of other things that I was also really interested in, linguistics and political science.

**Alan**: And I also did a lot of debate where I talked about a bunch of this stuff too. I guess having a diverse range of interests made it really hard to focus in on a particular thing. I think I still want to, during my PhD, just try a bunch of different things. Maybe this is a difficulty in getting concrete projects out.

**Alan**: At the end of my bachelor's degree, I was like, well, what do I do now with a math degree? Nothing I've tried has been super, super convincing to me. I don't really want to be a mathematician. It was nice, but it seems being a pure mathematician doesn't really have a lot of impact. In the near or medium term future, it seems there are more important problems than being a pure mathematician. And more problems to work on, climate change or global health. So then I started thinking, okay, so what are the things that could really, really make the world turn out bad? Or could have a really big impact on the world in my lifetime, say?

**Alan**: AI, I think, happened to be one of those things that I was thinking about. So I thought, okay, maybe I should go into AI. So I spent about a year just reading a lot about this and thinking, okay, where is AI going? Why do I think that it could actually be a really big thing? So I think solidifying those intuitions took a year. 

**Alan** (1:07:12): And at this point, I was doing a master's. It wasn't the ideal master's, but I later switched advisors and it was a lot better for me. So yeah, in the middle of my master's, I switched to doing AI. I started off with reinforcement learning. And it was really fun. And I really enjoyed the environment that I was put in. Just having people who cared also about AI and who also thought that it could be a really big thing.

**Alan**: But in the course of my master's, I guess I thought, okay, this is a reinforcement learning lab. So I was at the University of Alberta. This is a reinforcement learning lab. These people actually want to build AGI. I don't know. This seems kind of concerning to me. I had this intuition. Okay, what the fuck, though? Artificial general intelligence? Could it do some bad things, maybe?

**Alan**: I finished my master's in 2020. So I guess in the middle of COVID, I was sort of thinking, trying to grapple with these questions. Also, just noticing or just living through COVID and also the George Floyd protests. I was like, okay, real shit actually happens in the world. I'm living through history. Maybe something wild could actually happen. And something I'm personally involved in. Every day, AI. So I started to read a lot more about AI safety.  Superintelligence and stuff.  <a href="#outline">⬆</a>

## The Realization Of The Potential Dangers Of AGI Motivated AI Safety Work

**Alan** (1:08:42): A little bit of Alignment Forum and Lesswrong. I remember I was reading Superintelligence and I was like, damn, this is true. Shit, is somebody working on this? Then I thought, well, maybe I should work on this. And I think having that feeling that, wow, this is a thing I should work on was a pretty life-changing moment.

**Alan**: Because I think before, I guess, 2019-ish, when you learn about history in school, it's sort of like, okay, these things happened to these people. And damn, we have the world we have today. But to some extent, you feel sort of distanced from what happened. These people are so far removed. How can you ever relate to them? 

**Alan** (1:09:26): But we're living through history right now. We lived through a pandemic. We're living through an increase in geopolitical tensions. We're living through a lot of really concerning developments in artificial intelligence. While we're living through history, that means we can affect it. 

**Alan**: I think that moment, maybe it was more a gradual development. Made me think that I could actually do something about this problem. I applied for PhD programs. I didn't apply for AI safety, though. I was still sort of unsure whether I wanted to fully devote all my time to this. But I got into a PhD program at Mila.  

**Alan** (1:10:09): I started doing research. But basically, immediately, I really tried hard to shift my research from reinforcement learning to doing AI safety. It took a while. And I think I'm still sort of learning how to do AI safety research well and figuring out what the most valuable thing to do is. But I think it's been going pretty well. And I'm really glad I made that decision to switch. 

## What is Alan Chan Working On At The Moment

**Max** (1:10:31): Nice. And right now, what you're working on? What are you working on?

**Alan**: So I'm trying to finish up a paper with [CLR](https://longtermrisk.org/). 

**Alan** (1:10:40): We are trying to evaluate the cooperativity of language models. So the really interesting thing, I think, is, okay, you can construct a data set, get people to write scenarios for you if you want. 

**Alan** (1:10:54): But we actually want our ability to generate evaluations to scale with the capabilities of our models. So we're getting language models to generate scenarios for us. Basically, scenarios that involve some cooperation. And seeing what language models do in these kinds of scenarios. 

**Alan** (1:11:10): That's the first thing I'm working on. I also have just a bunch of other projects right now that are in varying stages of completion or feasibility. One thing I'm really interested in is how are we actually able to show people that models are actually much more capable than might be claimed by some people.

**Alan**: Another thing I'm working on is this general, almost position paper slash survey paper on speculative concerns in AI safety. It's essentially going to be an argument that it's important to speculate for cause areas. And review what are the methodologies and the ways in which people have speculated in AI safety? 

**Alan** (1:11:54): What has worked out? What hasn't? And why do we still need to continue on coming up with things that might appear more speculative to modern machine learning communities? But are actually important, I think, in pointing out possible problems we might face. 

**Max** (1:12:08): Is this aimed at machine learning people, this position paper? 

**Alan** (1:12:11): Yeah, so it's aimed at the academic machine learning community. I think a lot of what I... Yeah, parts of what I want to do are sort of more aimed at, okay, like, how can we field build or build bridges effectively? By either connecting our concerns to concerns that other people have, or by just saying things in language that other people can more understand. 

**Max** (1:12:38): Nice. I don't know. I'm not sure what else I got for Mr. Alan.
