---
layout: default
title: About
permalink: ./about.html
---

## Welcome to Monkstones Experiments with py5

#### Experiments with py5 (by a rubyist)

Here I will document my py5 experiences

#### Warning my python is very rusty

But I hope that my experience with [pyprocessing][pyp], [processing.py][pyde] and as developer of [ruby-processing projects][rp5] may give useful insights.

[Pyprocessing][pyp] is a pure python implementation of processing, based on pyglet (so includes numpy), but performance is a bit wanting. [Processing.py][pyde] is similar to JRubyArt using jython to connect to java-processing, and can be run from processing ide. JRubyArt uses jruby instead of jython to connect to java-processing (but no longer relies on vanilla-processing). Although py5 uses some processing java code, it is a more sophisticated animal than its predecessors. Key points are that you should think python first, so for example it does not support PVector, for matrix and vector operations you should use numpy (its fast and powerful).



[pyp]:https://github.com/monkstone/pyprocessing-experiments
[pyde]:https://github.com/monkstone/processing.py-examples
[rp5]:https://ruby-processing.github.io/
