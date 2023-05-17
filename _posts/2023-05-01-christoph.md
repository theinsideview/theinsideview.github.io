---
layout: post
title: "Christoph Schuhmann on Open Source AI"
category: podcast
permalink: christoph
youtubeId: -Mzfru1r_5s
spotifyId: 1FEl3ZUC9k6GJmEDIqTLm5
---

{% include youtubePlayer.html id=page.youtubeId %}
{% include spotifyPlayer.html id=page.spotifyId %}

Christoph Schuhmann is the co-founder and organizational lead at [LAION](https://laion.ai/), the non-profit who released [LAION-5B](https://laion.ai/blog/laion-5b/), a dataset of 5,85 billion CLIP-filtered image-text pairs, 14x bigger than LAION-400M, previously the biggest openly accessible image-text dataset in the world.

Christoph is being interviewed by [Alan Chan](https://mila.quebec/en/person/alan-chan/), PhD in Machine Learning at Mila, and friend of the podcast, in the context of a NeurIPS "existential risk from AI greater than 10% change my mind" debate in the wild that Christoph joined.

> Disclaimer about this episode: when talking to people in this podcast I try to sometimes invite guests who share different inside views about existential risk from AI so that everyone in the AI community can talk to each other more and coordinate more effectively. This is especially true for this episode, where Christoph is much more optimistic about the potential risks from AI than a lot of people working in AI Alignement research, and I believe his perspective about AI risk is potentially shared by many in the open source community.

<sup><sub><i>(Note: you can click on any sub-topic of your liking in the outline below and then come back to the outline by clicking on the green arrow</i></sub></sup> ⬆<sup><sub><i>)</i></sub></sup>


# Outline

* [LAION](#laion)
    * [How LAION was created](#how-laion-was-created)
    * [Why LAION Decided To Stay Independent, Relying On Volunteer Work](#why-laion-decided-to-stay-independent-relying-on-volunteer-work)
* [What Should We Do About Misuse](#what-should-we-do-about-misuse)
    * [Most People Use Technology To Do Good Things](#most-people-use-technology-to-do-good-things)
    * [Regulating Generative Models Won't Lead Anywhere](#regulating-generative-models-wont-lead-anywhere)
    * [Reinforcement Learning Is No Different, We Should Always Double Check](#reinforcement-learning-is-no-different-we-should-always-double-check)
* [What Should We Do As A Society](#what-should-we-do-as-a-society)
    * [Instead Of Slowing Things Down We Should Be Careful During Deployment](#instead-of-slowing-things-down-we-should-be-careful-during-deployment)
    * [The Solution To Societal Changes Is To Be Open And Flexible To Change](#the-solution-to-societal-changes-is-to-be-open-and-flexible-to-change)
    * [We Should Be Honest And Face The Tsunami](#we-should-be-honest-and-face-the-tsunami)
    * [What Attitude To Keep After We Are Done Educating People](#what-attitude-to-keep-after-we-are-done-educating-people)
* [Existential Risk From AI](#existential-risk-from-ai)

# LAION

## How LAION was created 

**Alan**: What do you do?

**Christoph**: I'm one of the founders and chairman of [LAION](https://laion.ai/), a community of people who just like to do open source AI stuff. <a href="#outline">⬆</a>

**Alan**: What motivated you to start LAION?

**Christoph**: I originally saw the DALLE-1 paper and I was blown away. And I was thinking, "Okay, how could we get a data set to replicate such a model?" And I was at this time on the Eleuther AI Discord server and I was talking to some people and they told me, "Yeah, someone should do it. Maybe I'll do it later." And I was thinking, "Oh, yeah, hopefully they will do it." But they didn't. They had other projects going on. And then I simply began to do it myself, being a high school physics and computer science teacher, on Colab.

**Christoph**: And, yeah, someone else joined me, who later turned out to be a 15-year-old high school student at the time from England. And we got a few million image text pairs from Common Crawl, which is basically something a huge public dump of HTML from several websites. And we used the existing clip model to filter out which images fit to which alternative text that they carry with them. And after a few weeks, we had 3 million image text pairs. And we thought, "Oh, this was easy." And then more and more people joined and just gave us access to virtual machines, to GPUs, and it grew. And after a few months, we had 413 million filtered image text pairs.

**Christoph**: And then, I have a background in supervising alternative education private schools, and I have been making a documentary about this in the past, and I know a lot about non-profit in this area. So I thought, "Okay, let's register a non-profit, not big, just something small where we can open a bank account and get then some funding, maybe not to pay people, but to cover costs." And then, yeah, we did it, and we got an offer from Hugging Face to support us to cover some compute costs.

**Christoph**: And then a few months later, we had 5.8 billion image text pairs, which is by far the biggest publicly available. And then more and more compute came to us, people popped up, like Emad Mostaque, the CEO of Stability. He came to our server and he said, "Oh, I'm a former hedge fund manager. I want to give free GPUs for open source researchers." And I was thinking, "Really?"

**Alan**: Yeah, yeah. And we all know the story from there, right? You're a big name now, LAION. Everybody knows you. <a href="#outline">⬆</a>

## Why LAION Decided To Stay Independent, Relying On Volunteer Work

**Christoph**: Yeah, and it's great, but it's not about LAION. It's about grassroots open source AI, because I'm still a high school teacher by profession. I have been getting some offers. I declined because I have a tenure. Germany is crazy. They give tenure to high school teachers. And so I thought, "It's much better for us to stay independent and to rely completely on volunteer work, because by doing this, we don't open up this box of Pandora, because we have some people working with us who are Google engineers, working at Facebook. And if we would have to pay them, we would have to pay them $10,000, $20,000 a month. But now they are working part-time for free for our projects, because they believe in this dream of truly open AI, making it open source, available as open source. And this is a huge community, and everyone just contributes as much as he wants. <a href="#outline">⬆</a>

# What Should We Do About Misuse
 
**Alan**: Great. Yeah. So open source AI. I'm really interested in learning your thoughts on the interaction between open source AI and possible negative consequences from people using AI, misuse type things. <a href="#outline">⬆</a>

## Most People Use Technology To Do Good Things

**Christoph**: Yeah. I mean, this might sound a little bit cheesy, but we have been in so many discussions about this. And for example, you can take a knife and you can make delicious food with it. You can take a knife, you can do very bad things like killing people with knives, and we still can buy knives. And most people, 99.999999% do nice things with it. The difference is that AI in the future is much more scalable. So it could be that in the future, AI could be used to do far worse things than just me with a knife. But the thing is, if you have a huge network of AIs, then you could have something like an antivirus system where you have agents that make sure that if 99% behave good and 1% behaves bad, the other 1% gets somehow kicked out of the society of AIs.

**Christoph**: And the thing is, if, for example, people right now take a text-to-image model and do, I don't know, something that insults me or someone else, then this is bad. But first, they could already do it with Photoshop right now or with a pen if they really tried hard. Or if AI empowers them to do so, then it's better they do it right now and cause a public discourse about the potential implications of an AI. Then imagine we would keep it closed and other companies like Google and Facebook would keep it closed.

**Christoph**: And then one day, the Russians or the Chinese or some states that are a little bit like, where it's not really obvious what their intentions are, they would just release a very powerful model. And no one in the broad society would know about it. And every normal people, like the people who go to my school, decent, intelligent people, but they have no idea about AI, they would be completely oblivious. They would be completely shocked and the consequences of misuse by bad actors like Russia would be much worse than if we have right now these models open and everyone can talk about it.

**Christoph**: Journalists can bring it into the consciousness of like politicians, decision makers and then we can see as a society all together how we will deal with it. And this is like, so open sourcing AI you can say AI in the future will be something like the ability to do cool stuff, to solve problems. Okay, maybe not all problems can be solved with AI, but in a world that increasingly gets computerized and digitized it will be increasingly... converge to "AI equals the ability to solve problems".

**Christoph**: Not completely but a lot of problems and if you're asking should we open source the ability to solve problems or should we make it exclusively available to nation states and big companies? And if you think about this imagine a future where the ability to solve problems exclusively belongs to big companies or nation states and it's obvious to almost anyone that this is not a good future. I mean we want legal systems that are reliable, that take care of us, that protect us and our rights and we want companies that flourish and that give employment and pay taxes and so we want this.

**Christoph**: But this is in my opinion completely independent from the question should the people who work in these companies, should they have also access to these superpowers? In my imagination, it's more "imagine a future where nation states and companies are flourishing and safe and pay taxes and everything's fine because the people who work there and the citizens they have these abilities to do cool stuff that they wouldn't have to." <a href="#outline">⬆</a>

## Regulating Generative Models Won't Lead Anywhere

**Alan**: So you mentioned something at the beginning about misuse so I think the example was something like "99% of people using AI systems are doing good thingsand like 1% are doing bad things and the idea is that you somehow kick out the 1%". So I think this is a nice ideabut my uncertainty, and the question I guess is, we're in a world right now where we are deploying generative models more and moreto people. We don't have such a system of you know kicking people out or preventing misuse right now like the 1% right?So from the perspective of somebody working onlinehow do you think about you know dealing with for example misinformation or increased bias now?

**Christoph**: I have been thinking a lot about this. I have been contacted by some political advisors and like to talk to them. So my opinion is like, let's be honest, no matter even if you would shut down LAION and even if you would probably shut down some academic research labs working on open source a few years from now, three four or five years, we will be in a position where people can easily generate all kinds of fake content that looks so good. Images, music, songs, videos that a normal person cannot tell the difference to an actual camera recording, and this will happen sooner or later and in a world like this, the idea of prohibiting it would result in a complete surveillance state because you cannot monitor everyone, what everyone is doing at home on his or her GPU, what image or so, 20-30 years ago people maybe thought "oh no the internet is so mean everyone can look up like mean pictures or disgusting pictures on google" and you can do it right now, right?

**Christoph**: For me being a high school teacher of course it's not allowed that people do this but I was in an inner city school where many people, low income kids were. And sometimes they just pulled out their smartphones with their mobile plans and got really ugly pictures. Okay, so they can do it. This is something that's already there and in the future, no matter if you shut down all the open source institutions or not, this will be a possibility you cannot monitor everything one because they are suspect of eventually belonging to the one percent that who does evil stuff. So there will be a flood of fake media and disinformation and the solution will not be by trying to shut down all the fake media The solution will be by putting higher value to trustworthiness and I can imagine this is just an idea. 

**Christoph**: But my imagination is that there will be something like an international blockchain like a like a notebook where people can note down That they consider an individual or a newspaper as trustworthy and let's say we have something like an us centralized State authority that certifies trustworthiness to journalists or to content creators on youtube like you are And there will be maybe such an agency for germany and for france and for russia and maybe even for north Korea. Even though no one would like to want it But it could be. And then later when you're using youtube and you want to see something about the Ukraine war.

**Christoph**: Then you can filter out and say I want only those people who have been checked for trustworthiness Who had been certified by this american institution during the last six months? Or you could say okay now i've watched all the american youtubers Now I want to see all the from the russian side where the russian authorities certified them to make it and like Not just because I believe them but just because i'm curious. I want to see what they are saying and believe, and then I can be Sure that at least within certain information bubbles these people are considered trustworthy and I can build myself an opinion because if I would not have like an instrument able to tell me who I can trust then I would be completely lost and it's already almost there.

**Christoph**: Like I cannot believe every youtuber, every bullshit. So I have to like look up who is this guy? What did he do before? How many followers does he have and it's already hard but it will be much harder in five years No matter if there will be open source AI or not open so they but I think it's good To talk about this openly and frankly and I can really imagine like maybe 10 years from now Really rich people going to a retreat without wi-fi listening to real music watching like real art from real artists and this will give even more value to those things that are provably made by humans because Cheap will be like the cheapest thing that everyone does will be just taking your smartphone and like. Make me a sound like Maria Carey. <a href="#outline">⬆</a>

## Reinforcement Learning Is No Different, We Should Always Double Check

**Alan**: Yeah, totally. Yeah, these are very interesting ideas. So just for the record I'm a machine learning phd student not a youtuber Um, so we've talked a lot about you know possible harms from supervised learning systems One thing i'm interested in getting your thoughts on is do you think about the harms from reinforcement learning systems? So like agents that are trained to achieve some goal or maximize some return over a long time horizon

**Christoph**: Yeah, this is something. In general with machine learning we should be cautious a little bit because it's the same as with humans Yeah, if I don't know someone and I give him a task where he has a huge responsibility. With huge power comes huge Responsibility I should at first observe him a little bit test him a little bit get an opinion a good feeling or maybe some Protocol to test his abilities And the same applies to reinforcement learning even more because we know that this technology is still in an early phase of like being reliable So if I for example I train a summarization model to summarize from human feedback Like what may I did a few days ago and I want to deploy it on a website where I know many business people Will use it. Of course, I should do a proper evaluation of its reliability or I should put a big disclaimer Please don't use. Only with caution. Always double check. <a href="#outline">⬆</a>

# What Should We Do As A Society

## Instead Of Slowing Things Down We Should Be Careful During Deployment

**Alan**: Yeah, yeah, I think that's totally the case. Um, yeah. So I guess one additional worry is there might be cases in which we test and test but it turns out the systems we're building. Just happen to misgeneralize out of distribution. We deploy it and something bad happens. um, so I think one perspective is you know, we kind of want to be in a situation where. That bad thing doesn't happen in the first place whether because one we've funded we fundamentally gain some understanding about how our systems work. Or two, you know, we just decide not to deploy such systems in the first place. So I guess i'm wondering what your stance is on this with respect to you know. Systems over which we have a lot of uncertainty. Should we be slowing things down and try to characterize the properties of such systems more or should we be doing something else?

**Christoph**: I think we should not slow things down. I think we should. Improve the speed of which the general public gets educated about it because the most important the most dangerous thing. Here is now having ordinary people downloading an image generation tool or maybe a language model and deploying it without knowing about the. the. order of the capabilities, the limits, so people need to be aware that ai is growing. exponentially or maybe you can debate about whether the true capability it's not growing exponentially.

**Christoph**: But it's growing fast and the people have to know that this is a thing. Not you not me not the people who watch this channel, but all the other people out there and once they understand. Okay, this is cool. But I cannot yet let my little child use it without parental guidance or so. Then it's already good. And then, you know. If we have a chatbot, imagine we have a gpt, like a super chatbot that people could deploy for call centers. It would be nice to have this for art maybe as a creative writing assistant.

**Christoph**: I can imagine this already being useful for some people. But I can really not imagine to be this deployed in a call center for huge banks or so. so if you deploy it at first in a creative content or in a content where people are allowed to make. Mistakes and learn then maybe after five years or three years people are like "oh, okay. The failure rate gets really low and we have better tools to understand it". <a href="#outline">⬆</a>

## The Solution To Societal Changes Is To Be Open And Flexible To Change

**Alan**: So the question was, you know, we've talked a lot about misuse and ai systems possibly acting out of control. Do you have any thoughts on ai systems that could cause harms in a sort of more diffuse way at the collective level?. So say with labor automation if we automate a lot of labor, um, you know that people in the middle class do this. Seems like this destroys a lot of your social mobility, right? So yeah, what are your thoughts on this?

**Christoph**: Yeah, I actually have lots of thoughts on this and I think. The biggest threat in this context is that no matter if there are certain ai models right now. the change of our society and the change of the labor market will be. Huge and I say really huge and most people cannot anticipate this especially those people who have nothing to do with computers. and. This will change the world completely independent of certain models or companies. And if you're in an environment, like a labor environment education environment that quickly changes. Imagine you have a continuum and you have two extremes on the one hand people. 

**Christoph**: Who embraces change, and who has an open mindset, they learn and they see change or failures as an opportunity. To learn something to expand their skill set and on the other end as a continuum. This is an extreme. Yeah. we have people who are very conservative and. they. laugh if things stay the same as they always had been and they hate change and they feel actually threatened by change because they think. Oh, I have to learn something new. I thought I was done with learning after school. So and if in reality people are between these two extremes and the same person can be in one context be a little bit more. Here and another context a little bit more here, but in general, for example.

**Christoph**: If you consider someone who is more here in the open-minded side, he would say, okay. Yeah, my job is changing. I need to learn new skills. Maybe I will learn about ai maybe I will learn about this or that internet marketing. I don't know whatever and you have this other person who says oh no my job is threatened. The machines are stealing my jobs. The big companies are stealing my jobs. I refuse this and then he would try to refuse it to ignore it and then later maybe he will like say. Oh, these people are really stealing my job. They are bad. We have to destroy them. We have to sue them and there are these tensions on the other hand.

**Christoph**: You have this divide the people who have lots of opportunities. And there you have so many many people who are actually scared and then become angry because they are so scared and this is very bad. And this is not about a certain company or a certain country. This is a global phenomenon and these people here they will look for certainty for people who make clear promises. So say this is a reason we're gonna to bring back the good old time. and of course.

**Christoph**: This is a lie because the compute the society is changing so fast because we'll just look back 20 years, we now have. The internet, we have twitter, we have all these debates about Drake and Trump being on twitter, not being on twitter. We have like a facebook where you can meet all your. School friends, elementary school friends and you can connect with them. 20 years ago it wasn't possible and. This will accelerate even far more than people can imagine right now. And this will lead to this these extremes where people here were scared and afraid of change. They will vote people with simple solutions who promise that everything will be like in the good old days. Regardless of the country or the party or, wheter communist... <a href="#outline">⬆</a>

## We Should Be Honest And Face The Tsunami

**Christoph**: It doesn't matter and this is a really scary thing. I am not so much scared of certain ai systems. Even though they can have dangers and should be, hum closely carefully handled. i'm much more scared by the fact that we have this divide in societies between open-minded people and people who hate change and who have. Feel threatened by change and this is a challenge that we have to meet but I think we cannot solve this problem. By saying okay, we will keep the change. We will pretend as if there was nothing like this because, behind the scenes, nation states and companies will be keep developing this and these models will leak out even if they try to hold them back.

**Christoph**: So this development, this tsunami this information disinformation ai tsunami that's rolling upon our societies. It is coming and no single state or a single company will be able to hold it. To prevent it to keep it stop it from from approaching. The thing is do we close our eyes and say no, there's no tsunami. We are regulating everything trust us. We have trust us incorporate people and politicians or do we say it is there. Let's try to make the best out of it. And let's take openly about it. Let's let's probe this tsunami and let's talk about it in a like in an honest way. Let's be honest. Let's be honest with it. It will be there and like there will be jobs in 10 years that are not there anymore. and it's not about me or LAION or. Any company on the world? So we are not even a company either but like it's it's not about us. It's about the truth that the tsunami is coming and we should educate the people about it. <a href="#outline">⬆</a>

## What Attitude To Keep After We Are Done Educating People

**Alan**: So what do we do beyond education?

**Christoph**: The truth is: I don't know the exact solution. I could promise you I could tell you. Yeah, I know exactly this. Let's do this and everything will be like in the good old way. So everything will be all right. This would be a lie.. And I think if he would be someone else and he would tell you the solution this also would be a lie because everything is. very complex, but I think what. imagine again, imagine. A future where the superpowers we will get we can get from ai. Will be exclusively limited to nation states and big corporations and maybe a few. agencies.

**Christoph**: And then imagine a future where these superpowers made by ai will be accessible to everyone and everyone can make an opinion out of it. And we have a network of many many people and organizations and small companies big companies private people journalists. Countries and they all together can try to organize this new system. If you ask me which I would choose it would be pretty easy for me to make a choice. What do you think about existential risk?. Yeah, I mean it had been there when I was born in 1982. And now with the ukraine war it came a little bit back into my mind that in theory.

**Christoph**: Even though I don't think it's likely but there could be a nuclear war for example. and I think it also like could happen with ai or. Actually, I think far more dangerous is bioweapons with things like CRISPR. So like we have seen this with corona and no one took it seriously. and I mean there only needs to be one mad scientist somewhere in a lab and release something that is as. Cautious as corona but. Far more deadly and this would change everything completely or like imagine like like a certain leader in asia. Deciding to attack a small country that is important for the semiconductors.

**Christoph**: This would be very bad for the whole economy of the whole world. And therefore I hope that these people who can make the decisions are reasonable and don't do it. but um. These are true threats and ai of course can also be such a threat. But it's the same like I mean. There will always be threats. And the thing is about if we have a grim view of human nature and of life like grimmer than it actually is by thinking. Oh my god, there's one person chance that people will take the knife and kill someone with a knife. I mean then your heart and your mind is filled with scare with fear and fear is not a good teacher.

**Christoph**: I mean fear is good if you can recognize it and use it as a basis to elaborate on it like we're doing. It's good. It informs us it motivates us. But if it takes control and it narrows down your your your mind. And you fall back onto these old rigid behaviors that you had been back in the good old days when you were in. Another like fight or flight situation like this then it's a really bad like source of information. So therefore like let's be afraid let's let's say. Yeah, there's a chance that there's an existential risk by ai as well as by bioweapons and other technologies and mad. politicians.

**Christoph**: But let's also remember all the positive aspects of this. Of it like so there was this tweet by joshua bach who told that there should be like a team red with release of every. Ai model that where people would evaluate what are the dangers of releasing this way I model. But it's the same they should be a team green and say what are the dangers of not releasing it?. I mean like by not releasing it we could prevent like lots of progress and wonderful art or like maybe people who can like, discover aspects of their soul because they use ai as a mirror to their own. conscious states so like all these wonderful aspects could be prevented and by not preventing this would also be a loss for the possible future. So, I mean in general i'm a pretty much an optimist, but i'm not a naive optimist.

**Christoph**: I know there are fears. I know bad things can happen bad things have been happening to my life. Even though my life I have been pretty. privileged and i'm very happy in my life, but. The more I experienced bad situations in my life dire situations the more I tried to focus on the thought. How can I make something happen something new so that in the future things will get better again. And I think if we have this inner attitude like realistic optimism like having this image. Maybe having a little bit romanticized image of the future, but realistically making a plan how to get from here to there.

**Christoph**: This is the best attitude, and not saying "oh my god. There could be a something bad happening and therefore we have to kill all the positive aspects of team green like after". Of the streams like we should be bold enough to dream about an utopian future. And not forget about the potential threats by a dystopian future and then we should sit down calmly. And try to make a solid plan with several alternatives. To get to the utopia or at least close. <a href="#outline">⬆</a>

# Existential Risk From AI

**Alan**: Yeah, I really like what you said there about fear about you know. Having it being an important signal for direction your work when having it consumed and like everything we're doing. Um, yeah, so I guess one question is like, you know, um, yeah existential risk might be real. Also, the benefits from ai might be real and important. Um, it seems like it's very hard to like balance these things, right?. So i'm wondering like how do you personally think about balancing?. You know like the possible downsides of ai from like possible upsides and how that informs, you know, you work at LAION and um, yeah.

**Christoph**: I don't even work at LAION. It's my hobby. I'm a computer science teacher and for some reasons, uh, ceos of tech companies. PM me on discord and slack and I I just do it because I believe it. I I don't make any money with this and the thing is i'm doing this I even reject offers for jobs because. I want I believe that it's better to have open source. Abilities to solve problems like open source ai equals abilities to solve problems in the future.

**Christoph**: I really want this because I personally think that I will become really. Really powerful maybe within 10 20 years when my kids will be grown up. And I want to influence it in a positive way and positive. I do not mean i'm not trying to prevent all the threats because I think no one really can. I'm trying to create opportunities for people to do wonderful stuff with this. And then maybe find solutions for the problems that we cannot even think about right now. So great.

**Alan**: Well one last question if you had one thing to say right now to yourself, uh, you know. When you were 10 years old, what would it be?

**Christoph**: Oh, i've recently watched back to the future with my older son who's 10. And I feel like if you change the past maybe maybe there's a reason all the bad things you had been encountering in life. All the hardships they they made me the person i am now. Therefore I would say nothing. I would just say thank you life for giving me all the hardships. I could learn from and all the wonderful moments I can savor in. Retrospective.

**Alan**: All right. Thank you very much. This is Christoph Schuhmann from LAION.
