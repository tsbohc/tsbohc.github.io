<!--
name: lipu pi wile sona ale
peek: none
tags: draft
date: 1651628474
-->

This document is meant to serve as an informal introduction to the subject of word embedding in the context of my paper.

<!-- And also my supervisor accusing me of being unable to explain my research "in simple words". -->
<!-- So, it's written like a children's book. -->

## table of contents

{{TOC}}

## toki!

<p class='linja-pona'>toki. mi jan pi kili laso.</p>

<p class='linja-pona'>jan lawa sona mi la, mi sona ala e pali mi. mi la, jan lawa sona mi li jan pi sona lili, li ike, li toki utala e pali mi. tan ni la, mi sitelen e lipu ni.</p>

<p class='linja-pona'>tenpo ni la, mi pana e sona pi lipu mi tawa sina. wile mi la, sina ken kama sona e toki lawa mi. sina o lukin e lipu ni. lukin ona li pali suli ala.</p>

<p class='linja-pona'>pona tawa sina a.</p>

# distributional semantics

In a 1957 publication[^[A Synopsis of Linguistic Theory](https://cs.brown.edu/courses/csci2952d/readings/lecture1-firth.pdf) (1957) by J. R. Firth, p.11], J. R. Firth wrote:

<!-- In a 1957 [publication](https://cs.brown.edu/courses/csci2952d/readings/lecture1-firth.pdf) (p.11), J. R. Firth wrote: -->

> The placing of a text as a constituent in a context of situation contributes to the statement of meaning since situations are set up to recognise use. *You shall know a word by the company it keeps!*

Here is an example to illustrate this:

> a. A bottle of *telo nasa* is on the table.\
> b. *telo nasa* makes people drunk.\
> c. Only adult people can drink *telo nasa*.\
> d. *telo nasa* is made out of oranges.

Clearly, *telo nasa* refers to an alcoholic beverage. But how did we arrive at this conclusion?

Let us consider a few words that could replace *telo nasa* in these 4 contexts. When a word is appropriate in a context (a, b, c, or d), we will mark that context with a *y* and with a *.* when it is not.

| word    |a|b|c|d|
|-        |-|-|-|-|
|telo nasa|y|y|y|y
|juice    |y|.|.|y
|pancake  |.|.|.|.
|wine     |y|y|y|.

- *telo nasa* is inherently appropriate in all contexts.
- *juice* is stored in bottles and is made out of oranges, but everyone can drink juice and it does not make people drunk.
- *pancake* fits none of the contexts.
- *wine* fits all of the contexts but the one that specifies the main ingredient[^There are varieties of wine that are made with the inclusion of orange zest or juice, but this is irrelevant to the discussion.].

Because *wine* is the best fit for these contexts, we can assume that *telo nasa* shares some of its properties.

Now, what if it was possible to make a computer do the same thing? That is, to infer meaning from context just like we have.

## word embedding

Let us write a program that will make a computer look through the words in a corpus, one by one. It will also count how many times each of the other words appears in the context of the current word.

For now, let us look at the contexts from the previous example. We will only consider *telo nasa* and its surrounding content words that are less general.

| |telo nasa
|-| :-:
|bottle|1
|table|1
|people|2
|drink|2
|adult|1
|orange|1

What can be said about *telo nasa* based on the data provided by the program?

That it is related to people and drinking, but also the legal age, bottles, and citruses or the colour orange. It is however, not related to quaternions, the printing press, or non-euclidean geometry.

## word vectors

Let us take the above table and divide each value by the total number of the word relationships in it (6):

| |telo nasa
|-| :-:
|bottle|0.16
|table|0.16
|people|0.33
|drink|0.33
|adult|0.16
|orange|0.16

Now *telo nasa* can be represented as a set of numbers: [0.16, 0.16, 0.33, 0.33, 0.16, 0.16]. This is its *word vector*, a numerical description of a word relative to every other word in a corpus. Every single word in a corpus can have one such vector.

Because we are operating on vectors, the principles of linear algebra can be applied to them. We will use *cosine similarity*[^Read more about *cosine similarity* on [wikipedia](https://en.wikipedia.org/wiki/Cosine_similarity).] to determine the degree of similarity between two vectors, that is, to quantify their semantic similarity.

Right now, our corpus is highly specialised, but what if we had more contexts featuring more words?

What if instead of 4 contexts, we had *a quarter of a million*?

# constructed languages

J. R. R. Tolkien wrote books so that his languages had somewhere to live and thrive. Since then, many people have created their own languages. One of them is jan Sonja.

## toki pona

In 2001, jan Sonja created *toki pona*, a philosophical constructed language centered around minimalism. The vocabulary of *toki pona* contains only 120-180 words.

*toki pona* is recognised by the [ISO 639-3](https://iso639-3.sil.org/code_tables/639/data/t?title=tok&field_iso639_cd_st_mmbrshp_639_1_tid=All&name_3=&field_iso639_element_scope_tid=All&field_iso639_language_type_tid=All&items_per_page=200) registry under *tok*. It is the second most spoken[^[ISO 693-3 proposal](https://iso639-3.sil.org/sites/iso639-3/files/change_requests/2021/2021-043_tok.pdf) (2021), p.3] constructed language in the world.

The words *telo nasa* mean *weird liquid*, which is a common way of referring to alcohol.

### grammar

*toki pona* is an uninflected language. Basic sentences have the following structure:

> [context] la [subject] li [predicate] e [d.o.] lon [prep.phrase]

<!-- The vocabulary of toki pona consists of content verbs, grammtical particles, prepositions, and preverbs. Modifiers follow content words. Any content word can be a verb and any verb can be transitive. -->

<!-- #### example sentence -->

Example sentence in *sitelen pona*, the writing system of *toki pona*:

<blockquote><p class='linja-pona'>ilo pi sitelen tawa la kon li tawa suli lon tenpo pimeja ni.</p></blockquote>

Written in latin:

> ilo pi sitelen tawa la kon li tawa suli lon tenpo pimeja ni.

|word|defintion|
|-|
|ilo|tool, instrument|
|pi|[modifier regroup particle]|
|sitelen|picture, symbol|
|tawa|movement|
|la|[context particle]|
|kon|air, spirit, essence|
|li|[predicate particle]|
|tawa|movement|
|suli|big, old, important|
|lon|[prepositional phrase particle]|
|tenpo|time, duration|
|pimeja|black, dark|
|ni|this|

Literal interpretation:

> in the context of a tool of moving pictures, air moves largely at this time of darkness.

Translation:

> TV broadcast reported that there will be strong wind tonight.

# NLP

NLP (Natural Language Processing) is a field at an intersection of computer science, artificial intelligence, and linguistics.

## vector space model

I have compiled a corpus containing *214000* sentences in *toki pona*. Each sentence is preceded by the date of writing. It spans over 10 years, half of the language's existence.

With this corpus, I have constructed a VSM (Vector Space Model) of *toki pona*. That is, I have calculated the *word vector* of every word in the vocabulary of *toki pona*. Meaning that I have the data that shows the semantic relationships between them.

The actual architecture of the model is more far involved than word counting, but this discussion is beyond the scope of this document. It is however the same in principle.

## visualisation

I have also made an interactive visualisation[^[Bokeh](https://bokeh.org/) is a Python library for creating interactive visualizations for modern web browsers.] of the model projected onto 2D space:

<div class="bk-root" id="b32f1451-dea2-4965-b307-b8f556058c66" data-root-id="1003"></div>
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.2.min.js"></script>
<script type="text/javascript">
Bokeh.set_log_level("info");
</script>
<script type="application/json" id="1330">
{"1da6c962-c5d6-46fe-8652-3cb593dc9fbb":{"defs":[],"roots":{"references":[{"attributes":{"coordinates":null,"group":null,"source":{"id":"1002"},"text":{"field":"labels"},"text_align":{"value":"center"},"text_font":{"value":"Regular"},"x":{"field":"x"},"y":{"field":"y"},"y_offset":{"value":5}},"id":"1040","type":"LabelSet"},{"attributes":{},"id":"1045","type":"BasicTickFormatter"},{"attributes":{},"id":"1046","type":"AllLabels"},{"attributes":{"fill_alpha":{"value":0.2},"fill_color":{"field":"cluster"},"hatch_alpha":{"value":0.2},"line_alpha":{"value":0.2},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Scatter"},{"attributes":{},"id":"1017","type":"BasicTicker"},{"attributes":{"coordinates":null,"group":null},"id":"1042","type":"Title"},{"attributes":{"axis":{"id":"1012"},"coordinates":null,"group":null,"ticker":null},"id":"1015","type":"Grid"},{"attributes":{"coordinates":null,"data_source":{"id":"1002"},"glyph":{"id":"1035"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"1037"},"nonselection_glyph":{"id":"1036"},"view":{"id":"1039"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"1026","type":"BoxAnnotation"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"source":{"id":"1002"}},"id":"1039","type":"CDSView"},{"attributes":{"overlay":{"id":"1026"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{"end":-7,"start":-16},"id":"1004","type":"Range1d"},{"attributes":{"coordinates":null,"formatter":{"id":"1048"},"group":null,"major_label_policy":{"id":"1049"},"ticker":{"id":"1013"}},"id":"1012","type":"LinearAxis"},{"attributes":{},"id":"1050","type":"UnionRenderers"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{"active_scroll":{"id":"1021"},"tools":[{"id":"1020"},{"id":"1021"},{"id":"1022"},{"id":"1023"},{"id":"1024"},{"id":"1025"}]},"id":"1027","type":"Toolbar"},{"attributes":{},"id":"1051","type":"Selection"},{"attributes":{"coordinates":null,"formatter":{"id":"1045"},"group":null,"major_label_policy":{"id":"1046"},"ticker":{"id":"1017"}},"id":"1016","type":"LinearAxis"},{"attributes":{},"id":"1049","type":"AllLabels"},{"attributes":{"fill_alpha":{"value":0.9},"fill_color":{"field":"cluster"},"line_alpha":{"value":0},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1035","type":"Scatter"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{"background_fill_color":"#f6f6f6","below":[{"id":"1012"}],"border_fill_color":"#f6f6f6","center":[{"id":"1015"},{"id":"1019"},{"id":"1040"}],"left":[{"id":"1016"}],"renderers":[{"id":"1038"}],"sizing_mode":"scale_width","title":{"id":"1042"},"toolbar":{"id":"1027"},"x_range":{"id":"1004"},"x_scale":{"id":"1008"},"y_range":{"id":"1006"},"y_scale":{"id":"1010"}},"id":"1003","subtype":"Figure","type":"Plot"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"field":"cluster"},"hatch_alpha":{"value":0.1},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Scatter"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{"axis":{"id":"1016"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"1019","type":"Grid"},{"attributes":{"data":{"cluster":["#B53679","#F4685B","#F4685B","#F4685B","#341068","#B53679","#FB8660","#CE4070","#B53679","#B53679","#4F117B","#4F117B","#FB8660","#FB8660","#4F117B","#FB8660","#9A2D7F","#F4685B","#F4685B","#FB8660","#FDA470","#9A2D7F","#F4685B","#CE4070","#CE4070","#9A2D7F","#F4685B","#E55063","#F4685B","#FDA470","#F4685B","#1B1044","#341068","#E55063","#F4685B","#4F117B","#FDA470","#1B1044","#681B80","#812581","#F4685B","#4F117B","#4F117B","#F4685B","#4F117B","#9A2D7F","#341068","#F4685B","#1B1044","#FEC286","#FB8660","#681B80","#4F117B","#F4685B","#681B80","#681B80","#9A2D7F","#4F117B","#9A2D7F","#681B80","#9A2D7F","#CE4070","#4F117B","#FDA470","#341068","#CE4070","#FDA470","#FDA470","#9A2D7F","#CE4070","#681B80","#9A2D7F","#681B80","#1B1044","#B53679","#341068","#9A2D7F","#812581","#FDA470","#CE4070","#341068","#341068","#FEC286","#681B80","#CE4070","#681B80","#E55063","#812581","#1B1044","#CE4070","#FEC286","#341068","#9A2D7F","#812581","#4F117B","#FEC286","#341068","#812581","#FEC286","#341068","#341068","#341068","#FEC286","#CE4070","#341068","#F4685B","#FEC286","#CE4070","#341068","#CE4070","#812581","#341068","#FDA470"],"labels":["mi","ni","toki","pona","tawa","jan","ala","lon","sina","ona","tenpo","mute","sona","wile","kama","ken","pilin","taso","seme","pali","lili","tan","nimi","tomo","ma","ike","kepeken","jo","ale","lukin","sitelen","musi","suli","pana","ante","pini","sama","ilo","telo","moku","ijo","suno","tu","nasin","wan","lawa","anu","lipu","kalama","soweli","sin","sewi","nanpa","kulupu","wawa","lape","nasa","luka","weka","kon","pakala","awen","sike","mama","kasi","poka","meli","olin","utala","insa","seli","moli","pimeja","kute","mani","len","sijelo","suwi","mije","open","linja","kiwen","waso","anpa","poki","lete","esun","kili","uta","supa","mu","kule","jaki","ko","mun","pipi","noka","pan","akesi","loje","palisa","walo","kala","sinpin","nena","pu","alasa","lupa","selo","monsi","jelo","laso","unpa"],"x":["-11.3547535","-11.700243","-12.26973","-11.827016","-11.424689","-10.545621","-11.522168","-11.848974","-11.235615","-10.982602","-14.400184","-11.505433","-12.565788","-11.984659","-12.455359","-11.860193","-9.954526","-11.68808","-11.036486","-12.551102","-11.286631","-10.485082","-12.458322","-12.253875","-11.588774","-10.088989","-13.335131","-13.124921","-10.470868","-12.08924","-13.11029","-14.714038","-11.103747","-12.793467","-11.6979065","-13.666387","-11.22466","-13.956148","-7.928884","-6.7072396","-11.263438","-14.662734","-16.545992","-11.530422","-16.554874","-9.552243","-10.379661","-13.083867","-15.045937","-6.796476","-12.698548","-11.186783","-16.576262","-11.814103","-10.040007","-13.355016","-9.466966","-16.606997","-10.2537155","-9.244922","-10.081073","-11.660459","-15.170188","-7.826397","-7.4662137","-12.122097","-8.086477","-8.975294","-8.858745","-10.077777","-8.314571","-8.497483","-10.356352","-14.931915","-14.231231","-11.444893","-9.554197","-6.5770264","-8.102757","-13.65185","-10.726879","-9.470697","-6.596846","-11.385849","-9.433489","-8.363866","-13.9617605","-7.0356255","-15.609814","-12.526348","-6.5980716","-8.6887245","-9.005751","-7.4312215","-14.93621","-6.7887783","-11.697866","-6.559492","-7.1178284","-8.016626","-9.626873","-8.253977","-6.685755","-11.075792","-10.5851","-12.56368","-12.087563","-12.073214","-9.813381","-11.80368","-7.789886","-8.427357","-8.8695545"],"y":["5.3453007","5.2219567","6.8774433","5.992398","4.072133","5.936585","5.479155","3.1257522","6.3489823","5.160894","3.0757475","4.652384","6.425243","5.83309","3.9933052","6.048485","5.010208","5.3845863","8.292778","5.361781","4.042312","4.626911","8.028114","2.8320785","2.6368928","4.9109306","6.2501593","4.51778","6.20237","4.572963","7.104485","7.1587415","2.8866034","4.820308","6.6386704","3.249191","4.6687365","6.7834935","1.2560792","1.4050095","6.6560917","2.7097425","3.0697422","7.3817205","3.0887754","5.7040663","7.2162046","7.1996665","7.3748684","3.5824313","5.732482","2.1583934","3.1225736","7.185908","3.2845678","1.7416993","4.6260386","3.040425","4.004046","2.4846592","4.1667666","3.5329015","2.5420008","7.5005054","0.10746253","2.6673872","7.41322","7.0098596","5.467712","1.9953845","1.8796984","4.395697","2.2607145","7.2060976","5.100539","-0.41421604","3.6654677","1.5383114","7.4198556","3.219424","0.3907538","0.5462991","3.4327512","1.5859401","1.5697005","2.020668","4.98384","0.437019","6.3414426","0.56802326","4.6538167","-0.798846","3.4483764","1.3201326","2.6880708","3.450085","0.4861469","1.1752446","3.8151903","-0.3596137","0.27744055","0.4311943","3.4818716","0.82103807","0.8684981","8.2479725","4.250719","1.4440607","1.212335","1.1324283","-0.065962866","-0.647846","6.952565"]},"selected":{"id":"1051"},"selection_policy":{"id":"1050"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{"end":-0.5,"start":8.5},"id":"1006","type":"Range1d"},{"attributes":{},"id":"1048","type":"BasicTickFormatter"}],"root_ids":["1003"]},"title":"Bokeh Application","version":"2.4.2"}}
</script>
<script type="text/javascript">
(function() {
const fn = function() {
Bokeh.safely(function() {
(function(root) {
function embed_document(root) {
const docs_json = document.getElementById('1330').textContent;
const render_items = [{"docid":"1da6c962-c5d6-46fe-8652-3cb593dc9fbb","root_ids":["1003"],"roots":{"1003":"b32f1451-dea2-4965-b307-b8f556058c66"}}];
root.Bokeh.embed.embed_items(docs_json, render_items);
}
if (root.Bokeh !== undefined) {
embed_document(root);
} else {
let attempts = 0;
const timer = setInterval(function(root) {
if (root.Bokeh !== undefined) {
clearInterval(timer);
embed_document(root);
} else {
attempts++;
if (attempts > 100) {
clearInterval(timer);
console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
}
}
}, 10, root)
}
})(window);
});
};
if (document.readyState != "loading") fn();
else document.addEventListener("DOMContentLoaded", fn);
})();
</script>

Use your mouse (click and drag) and scroll wheel (zoom) to explore the model. Use the toolbar on the right for extra functionality.

The position of a word is determined by the context it is most commonly used in. Words that are often used together, and thus are semantically related, are placed close to each other. The distance between points is a measurement of semantic similarity between the words they represent.

## using the vsm

With a VSM, we can operate on the semantic relationships between words.

For example, we can ask the model to list words that are closely related to a particular word. Here that word is *utala* (fight):

```python
vsm.most_similar('utala') =>
```

|word|similarity|definition
|-| :-: |-
|lawa|0.551|head, control, rule
|moli|0.536|death, murder
|jan|0.427|person, people
|wawa|0.404|power, strength
|pakala|0.397|break, damage
|palisa|0.360|long hard object

Or even ask the question "if *suno* (sun) is *seli* (hot), then what is something *lete* (cold) that is similar to *suno* (sun)?" using linear algebra operations:

```python
vsm.most_similar(positive=['suno', 'lete'], negative=['seli']) =>
```

|word|similarity|definition
|-| :-: |-
|mun|0.659|moon
|pini|0.595|end, finish
|pimeja|0.469|black, dark

Keep in mind that there are only two words in *toki pona* that can denote celestial bodies. Also, *cosine similarity* ranges from *-1* to *1*, meaning that *0.659* is almost an exact match (83%). 

See further examples in the library[^[Gensim](https://pypi.org/project/gensim/) is a Python library for topic modelling, document indexing and similarity retrieval with large corpora.] documentation [here](https://radimrehurek.com/gensim/models/keyedvectors.html#what-can-i-do-with-word-vectors).

## making observations

The following is just a couple of examples.

Despite *pimeja* (black) being a colour, it is more semantically connected to the word *tenpo* (time). This is because the most common usage of *pimeja* is to specify a time of day.

In contrast, *kasi* (plant) is closely related to the rest of the colours. This is because *toki pona* has one word for blue and green: *laso*. Despite the existence of natural languages that do this, the majority of *toki pona* speakers feel the need to refer to these colours unambiguously.

## argumentation

This research aims to analyse and classify the vocabulary of *toki pona* based on the actual usage patterns of the language via the methodology discussed previously.

Observations like the ones above cannot be made based on the existing dictionaries of the language, nor any other resource. They cannot be made without studying how the language is spoken. The VSM provides us with this data.

There was no VSM of *toki pona* prior to this research. There is no larger corpus of *toki pona*. There is no other dated corpus at all.

With the access to the time of writing of each sentence, changes in the vocabulary can be tracked from 2010 up to the present.

# formalities

**Title.** TOKI PONA: DISTRIBUTIONAL APPROACH TO SEMANTIC ANALYSIS OF A CONSTRUCTED LANGUAGE.

**Subject.** Semantic analysis and classification of vocabulary.

**Object.** *toki pona*, a constructed language.

**Problem.** The publicly available dictionaries do not fully reflect how the language is spoken today.

**Goal.** Perform the semantic analysis and classification of the vocabulary of the language.

**Methodology.** Distributional semantics and natural language processing, namely language modelling (word embedding).

**Objectives.**

* Define distributional semantics and distributional models.
* Discuss modern implementations of distributional models.
* Define and classify constructed languages.
* Describe *toki pona*, its philosophy, history, and unique features.
* Obtain the necessary corpora.
* Normalise the input data.
* Construct a vector space model of the language.
* Make observations on the model.
* Classify the words of the vocabulary based on the observed semantic relationships between them.

**Relevance.**

Constructed language are gaining popularity. With the rise of the internet, these languages now have a space where they can be created, discussed, learnt, taught, and spoken. Despite this, the only constructed language that has seen much representation in scientific writing is Esperanto.

The existing dictionaries of Toki Pona could benefit from the findings of this research. This data can also be used as an aid in teaching the language to new speakers.

The vector space model of Toki Pona developed in the course of this research can find further use in machine translation, topic modelling, text prediction, sentiment analysis, and many other areas.

**Personal reasons.**

I like *toki pona*. I want more people to learn about it. I want to see it grow.

**Source code.**

The paper is a work in progress. The most recent rendered *.pdf* can be viewed [here](https://docs.google.com/viewer?url=https://github.com/tsbohc/lipu-sona/raw/master/latex/lipu.pdf) or [here](https://github.com/tsbohc/lipu-sona/blob/master/latex/lipu.pdf). The direct link to the download is [here](https://github.com/tsbohc/lipu-sona/raw/master/latex/lipu.pdf).

The [tsbohc/lipu-sona](https://github.com/tsbohc/lipu-sona) github repository includes:

- The model in the binary format. The scripts that were used to prepare, normalise, and clean the training data.
- The paper and the bibliography in LaTeX[^[LaTeX](https://www.latex-project.org/) is a typesetting system; it includes features designed for the production of technical and scientific documentation.], as well as a rendered *.pdf*.

<!-- <iframe src="http://docs.google.com/gview?url=https://github.com/tsbohc/lipu-sona/raw/master/latex/lipu.pdf&embedded=true" style="width:718px; height:700px;" frameborder="0"></iframe> -->
