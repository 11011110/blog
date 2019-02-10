---
layout: post
title: LIPIcs autoref lemma
date: 2018-05-25 22:28
---
Many computer science conferences these days are being published open-source in the [LIPIcs](https://www.dagstuhl.de/en/publications/lipics) online book series, and that's a good thing.

If you've formatted your papers for LIPIcs, you might know that it automatically includes the [hyperref package](https://ctan.org/pkg/hyperref), which has at least three benefits:

1. It automatically produces hyperlinks from one part of your paper to another whenever you refer to a numbered entity like the name of a theorem.

2. It also produces hyperlinks from within your paper to web resources (like the papers you reference) as long as you include those links as urls or dois in your bibliography files.

3. Instead of writing <code>Theorem~\ref{thm:its-label}</code> you can use a shorthand macro, <code>\autoref{thm:its-label}</code>. If you do this, it will fill in the "Theorem" part itself. But it will also hyperlink the word "Theorem", as well as the theorem number, making it easier for people who want to follow the link to click on it.

Alternatively, you might know that LIPIcs automatically includes the [amsthm package](https://ctan.org/pkg/amsthm). Again, this has some benefits:

1. You can use <code>\qedhere</code> to control where the end-of-proof marker goes.

2. It allows theorems, lemmas, definitions, etc., all to be numbered within a single sequence (and LIPIcs does this), making it easier for readers to search for them in the text and harder for them to get confused about multiple things with the same number.

3. If you prefer, you can set LIPIcs' "numberwithinsects" option to <s>insert lots of bugs into your theorems</s> make the numbering include the section number, again to make it easier for readers to find things.

However, if you've tried to use all of these nice features, you might have noticed that they don't all play nicely together. In particular, you can't use <code>\autoref</code> on lemmas, because it will call them theorems instead and then (despite the nice numbering) your readers will be confused. "Where's Theorem 5.3?" "Oh, that's actually a lemma."

It's too late to save a couple of my papers that this bug bit, but in case anyone else runs into this, here's the fix. It involves undefining the lemma, corollary, etc. environments, and then using some magic involving the [aliascnt package](https://ctan.org/pkg/aliascnt) to redefine them in a way that works with both amsthm and hyperref autoref. I forget where I learned this technique but it might have been from [this stackexchange thread](https://tex.stackexchange.com/questions/187388/amsthm-with-shared-counters-messes-up-autoref-references/187395) or something similar. Anyway, just copy this into your paper's header:

{% highlight latex %}
%%% Fix bug in lipics-v2018 with \autoref{lemma} and corollary
\usepackage{aliascnt}
\makeatletter
\let\corollary\@undefined
\let\endcorollary\@undefined
\let\lemma\@undefined
\let\endlemma\@undefined
\makeatother
\theoremstyle{theorem}
\newaliascnt{lemma}{theorem}
\newtheorem{lemma}[lemma]{Lemma}
\aliascntresetthe{lemma}
\newcommand{\lemmaautorefname}{Lemma}
\newaliascnt{corollary}{theorem}
\newtheorem{corollary}[corollary]{Corollary}
\aliascntresetthe{corollary}
\newcommand\corollaryautorefname{Corollary}
%%% End fix bug
{% endhighlight %}

I also [wrote about this in 2014]({{site.baseurl}}{% post_url 2014-11-25-lipics-formatting-tricks %}), for an older version of the LIPIcs formatting macros. My recommendation then was to remember not to use autoref in LIPIcs, but then I failed to follow this advice myself in some of my later papers. I think this method is more robust and produces better results.

([G+](https://web.archive.org/web/20190210061616/https://plus.google.com/100003628603413742554/posts/BuitS1FyXuJ))