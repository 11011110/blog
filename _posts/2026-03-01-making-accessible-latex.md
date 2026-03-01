---
layout: post
title: Making accessible LaTeX talk slides with ltx-talk
date: 2026-03-01 14:52
---
US-based academics are being required [by the government](https://www.ada.gov/resources/2024-03-08-web-rule/) and by their universities to make all online content accessible by April 24, and I think many of us have been running around trying to figure out what that means and how to do it. My university has been especially unhelpful, demanding compliance in vague terms but not telling us what standard they're using and pointing only to Microsoft and Google's web sites for guidance on how to improve accessibility for Microsoft and Google products. The relevant standard appears from the government links to be WCAG 2.1 AA. For those of us who have been using the LaTeX beamer package to create mathematical course lecture notes as pdf files, beamer cannot do this. The accessibility standards require tagged pdf and beamer does not have code to generate the tags correctly. But there is a solution: a replacement package, [ltx-talk](https://ctan.org/pkg/ltx-talk), that is mostly compatible with beamer. After some effort, I have succeeded in using ltx-talk to create slide decks that closely resemble my old beamer decks both in appearance and coding and that pass all automated accessibility checks in Acrobat. That makes now a good time to record what I have learned about going from beamer to accessible ltx-talk, before I forget it all again.

Online guides
=============

I have found three helpful guides to accessible LaTeX (not specifically about ltx-talk): "[Using LaTeX to produce accessible PDF](https://latex3.github.io/tagging-project/documentation/usage-instructions)" from the LaTeX tagging project, "[A quick primer on modifying existing LaTeX for digital accessibility](https://richardwong.rice.edu/LaTeX-Accessibility-Primer/)" by Richard Wong at Rice University, and "[Creating accessible PDFs in LaTeX](https://docs.overleaf.com/writing-and-editing/creating-accessible-pdfs)" from Overleaf. If you are using some unusual LaTeX packages or document classes, the LaTeX tagging project also maintains a useful [list of the tagging status of LaTeX packages and classes](https://latex3.github.io/tagging-project/tagging-status/). This includes the information that beamer cannot generate accessible tagged pdf but ltx-talk can. These links got me from a state of having no idea how to generate accessible pdf files from my slides to a state where I thought it might be possible, and helped me start setting up my files. Most of the rest was from carefully reading log files and accessibility reports and then experimenting to figure out what to change in order to make the errors and warnings go away.

This posting is not intended as a substitute for these guides, but rather as a collection of tips and tricks for converting beamer slide decks into accessible ltx-talk slide decks.

Compilation
===========

To compile ltx-talk files and produce accessible tagged pdf files, you need to run lualatex instead of pdflatex. Sometimes you need as many as four runs: one run of lualatex to get an aux file with bibliography items, a run of bibtex, and then three more runs of lualatex before it stabilizes and stops telling you to run again because the labels have changed or because it miscalculated page numbers and added a dummy page. Check the log files for these things.

You also need to be running a very recent version of LaTeX, dated November 2025 or more recent. TeX Live 2025, released in March 2025, will not work. The new [TeX Live 2026 pretest](https://www.tug.org/texlive/pretest.html) will. I use MacOS and have not figured out whether there is any way to access the TeX Live pretest on a Mac. Instead I have been using either Overleaf (through its [Overleaf Labs](https://www.overleaf.com/about/overleaf-labs) feature) or a linux install on some departmental machines accessible to me via ssh. This already includes the ltx-talk package; you do not need to install it separately.

There are apparently [incompatibilities between recent releases of LaTeX and the cleveref package]({{site.baseurl}}{% post_url 2026-02-15-linkage %}). Fortunately, my slide decks do not use cleveref.

Preamble
========
The magic incantation at the start of your file is different, of course, because it's a different package but also because tagged pdf needs a metadata command before the document class to set it up. The old incantation (for, say, a $$16\times 9$$ target aspect ratio) was:

{% highlight latex %}
\documentclass[aspectratio=169]{beamer}
{% endhighlight %}

Instead, now it is:

{% highlight latex %}
\DocumentMetadata{
  lang          = en,
  pdfstandard   = {ua-2,a-4f},
  tagging       = on,
  tagging-setup = {math/setup=mathml-SE} 
}
\documentclass[aspect-ratio=16:9]{ltx-talk}
{% endhighlight %}

Change the `lang = en` line if you are writing in a different language than English. Wong suggests instead `tagging-setup={math/setup=mathml-SE,math/alt/use}`; I have no idea whether that would be an improvement.

The other important change in the LaTeX preamble works around what I think is a bug in ltx-talk. By default, it tags frame titles with an h4-level header tag. But there are no h1, h2, or h3-level header tags that it produces. This causes Acrobat's accessibility checker to complain about header nesting. Maybe the right thing to do is to add some h1, h2, and h3-level tags, for instance on the title page, but I haven't figured out how to do that. Instead, I changed the frame titles to h1, with

{% highlight latex %}
\tagpdfsetup{
  role / new-tag = frametitle / H1
}
{% endhighlight %}

The default appearance produced by ltx-talk is close to beamer with the structure skin, but not quite the same. You can change it in your LaTeX preamble but the documentation for how to change it is somewhat lacking. What worked for me is to look for code like `DeclareTemplateInterface` in ltx-talk.cls and to use `\EditInstance` to change it. For instance I use the code

{% highlight latex %}
\definecolor{ksblue}{RGB}{0,129,205}
\EditInstance{header}{std}{
  color            = ksblue,
  left-hspace      = 0cm plus 1fil,
  right-hspace     = 0cm plus 1fil
}
{% endhighlight %}

to change the color of frame titles and center them. I also use

{% highlight latex %}
\renewcommand{\labelitemi}{ {\footnotesize\color{ksblue}$\blacktriangleright$}}
\renewcommand{\labelitemii}{ {\scriptsize\color{ksblue}$\blacktriangleright$}}
{% endhighlight %}

to make big triangular itemize bullets like beamer, instead of the default little circular ones. (So far I have only converted slides with two levels of itemize nesting.)

Figures
=======

In the article content, the easiest change to explain but the most time-consuming one, for me, is adding alt-text to all images. The syntax is straightforward: `\includegraphics[alt={Alt text goes here}]{filename}`. I have seen big online debates on what alt-text should describe and how detailed it should be. The important thing to remember is that you're not trying to describe the image in vivid-enough detail that an AI image generator could make a copy of it. The purpose of these things is to substitute for the image when people use a screenreader to convert your slides into spoken text. So it should be concise enough that it doesn't interrupt the flow of the text when spoken but informative enough that people using a screenreader don't miss out on the meaning. For complicated mathematical examples that can be a big ask.

I had one figure, created as a pdf file by Adobe Illustrator, that triggered a flate decode error in lualatex. The same image had worked correctly in pdflatex and beamer. The compilation continued with a warning but the figure did not render correctly in the compiled file. I could not figure out why. The only workaround I could find was to save it as a different pdf version in Illustrator.

Environments
============

Getting ltx-talk to run required a few changes elsewhere in my LaTeX files. I was using `\begin{frame}{Title of frame}`, and ltx-talk has an option to make that work, but by default it doesn't. Instead you need to use `\begin{frame}\frametitle{Title of frame}`. Columns need to be delimited by `\begin{column}{size}`...`\end{column}` instead of starting them by `\column`. (Also the spacing between columns is different between beamer and ltx-talk so you may need some reformatting to get them to look good.) And the same thing about using an environment rather than a command applies to some formatting things like `\flushright`: it won't cause a LaTeX error but it will cause the tagging to get mismatched with a warning message at the end of the log. Then you have to work through your file trying to figure out which slide caused the mismatch.

If you use verbatim environments, beamer needed to mark this by `\begin{frame}[fragile]`. This still works in ltx-talk but with a different syntax, `\begin{frame*}`. If you use tabular environments, you need to tell LaTeX which rows of your table are header rows. See the accessibility guides linked above.

Formulas
========

There is lua code somewhere that generates mathml tags for the mathematical formulas (I think this is the main reason that you need to use lualatex). It is not as robust as LaTeX itself. Using code like `\bigl` and `\bigr` will cause a tagging mismatch; use `\left` and `\right` instead and let LaTeX choose for itself how big to make the parentheses. Using `\dots` inside math often does not work at all, and in one case using `$\dots$` inside a tabular environment caused lualatex to crash hard. Use `\ldots` or `\cdots` instead. Also, I think using mathematics inside `\text` inside more mathematics caused a tagging mismatch; don't nest them like that. This code will also generate files with names of the form *-luamml-mathml.html; add that pattern to your .gitignore file.

I had one deck (discussing the Ackermann function) containing the expression $$\approx 2\times 10^{19728}$$. This caused lualatex to freeze. The only hypothesis I can find is that it looks like a formula whose numerical value can be calculated and that the mathml conversion code was trying to calculate it, using a slow exponentiation algorithm.

Sections
========

If your deck has 21 or more slides, Acrobat will complain if it doesn't also have bookmarks for navigation within sections of the deck. I did this using `\pdfbookmark[1]{Bookmark name}{Bookmark name}` at the start of each section. Maybe there is a better way. This would be a good place to put more higher-level header tags than the H4 frame titles, if I knew how.

Many of my slide decks have bibtex bibliography sections. I don't generally show these when speaking but I want them to be part of the pdf files of my slide decks that I distribute. I like to use natbib for this (plus the doi package to make the external links and dois work properly).  But natbib never worked correctly in beamer; I needed to add the code `\newcommand{\newblock}{}` to the preamble to make it work. In ltx-talk, I also needed to add `\newcommand{\thebibliography}{\relax}` before loading natbib. Then you can just put your bibliography within one of the frames. A problem I have not found a good workaround for is that beamer allows multi-frame bibliographies with `\begin{frame}[allowframebreaks]`. However, ltx-talk does not and reading its documentation reveals that its developer is very hostile to long bibliographies (such as would arise in a talk incorporating a literature review). The only workaround I have found is to use a small-enough font size (in some cases `\tiny`) to allow the whole bibliography to fit on one slide. This is mildly problematic with respect to accessibility but better than truncating the bibliography because it overflows the slide.
