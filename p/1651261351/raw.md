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

Now, what if it was possible to make a computer do the same thing? That is, infer meaning from context just like we did.

## word embedding

Let us write a program that will make a computer look through the words in a corpus, one by one. It will also count how many times each of the other words appears in the context of the current word.

For now, let us look at the contexts from the previous example. We will only consider *telo nasa* and its contexts. We will only concern ourselves with content words that are less general.

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

Right now, our corpus is very specialised, but what if we had more contexts featuring more words?

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

<div class="bk-root" id="bfabaee6-f4c2-45d0-8b7b-025b700d3fb6" data-root-id="1003"></div>
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.2.min.js"></script>
<script type="text/javascript">
Bokeh.set_log_level("info");
</script>
<script type="application/json" id="1197">
{"9dccfb7e-894f-4c29-bf0a-e85812aab332":{"defs":[],"roots":{"references":[{"attributes":{},"id":"1049","type":"AllLabels"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"source":{"id":"1002"}},"id":"1039","type":"CDSView"},{"attributes":{"fill_alpha":{"value":0.9},"fill_color":{"value":"#DA5A57"},"line_alpha":{"value":0},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1035","type":"Scatter"},{"attributes":{"data":{"labels":["li","mi","ni","la","pona","jan","toki","tawa","ala","pi","lon","sina","ona","tenpo","sona","mute","wile","kama","ken","seme","pali","taso","pilin","lili","tan","tomo","ma","nimi","ike","musi","kepeken","sitelen","lukin","jo","ilo","ale","suli","pini","moku","ante","pana","sama","telo","ijo","suno","anu","nasin","tu","kalama","lawa","lipu","wan","kin","soweli","sin","lape","wawa","nanpa","en","nasa","weka","kulupu","sewi","kon","awen","pakala","luka","mama","sike","kasi","poka","olin","seli","kute","insa","meli","suwi","len","utala","pimeja","open","sijelo","mani","moli","linja","esun","mije","ali","lete","kili","uta","waso","poki","mu","kiwen","supa","jaki","anpa","kule","pan","ko","noka","pipi","pu","mun","loje","akesi","alasa","kala","walo","sinpin","palisa","nena","monsuta","selo","lupa","laso","jelo","monsi","oko","unpa","leko","kipisi","ku","tonsi","namako","misikeke","kijetesantakalu","meso","to","kokosila","linluwi","epiku","isipin","soko","lanpan","majuna","powe","jasima","te","pake","oke","wa","pata","waleja","po","mulapisu","ete","apeja","kiki","kan","tuli","misa","jami","kuntu","unu","yupekosi","san","melome","kapesi","kulijo","usawi","kamalawala","puwa","su","omekapo","taki","ewe","mijomi","kese","soto","teje","natu","sutopatikuna"],"x":[1.3486547,-1.1393044,-1.5720041,-0.38249698,-2.2710347,1.7975209,-3.1358418,1.2617582,-1.3343861,1.8259941,2.500386,-1.2873998,-0.67260605,-2.6114821,-3.2218158,1.0977894,-2.338796,-1.9397383,-2.3715923,-1.6890316,-2.6118054,-1.4154502,-0.371847,1.289328,1.2850772,3.4333413,3.5986688,-1.4442865,-0.13737985,-4.095844,-1.728795,-2.7685974,-1.4875969,0.95621985,-3.1846993,-2.0221148,2.5452545,-2.401174,1.4957461,0.52510387,0.025120322,1.2092049,2.4588406,0.7372529,-2.650996,-1.9527134,1.5064843,-4.703963,-4.218044,2.843264,-2.7152133,-4.710185,-0.88238037,0.3531759,-3.0299003,-0.85121346,1.71347,-4.7283216,1.106221,0.8324366,2.6428747,1.7950042,4.4064302,1.7699559,2.8903997,2.3274336,-4.679999,2.3018837,-3.1676924,3.0665834,3.5154555,1.6312311,2.0138965,-4.0783014,2.9445803,2.4165685,1.2775857,3.1562002,2.790032,-1.537148,-2.4276206,0.6250177,-3.756722,2.5665672,3.9025834,-3.5565283,2.3954515,1.3597451,1.9677153,2.4122329,-2.9489431,0.3714413,2.4578843,-1.7086161,3.681842,4.3674703,1.0481634,4.289725,3.7803977,1.918512,2.646997,4.3389215,0.21798682,-1.6301309,-2.977052,3.4680796,-0.08074489,-1.528182,0.353501,3.4254289,3.7086706,3.7806742,3.7970464,-1.2879957,3.202499,3.7966437,3.592175,3.3436065,3.9473133,0.8063183,1.519453,-0.1628589,-0.13387059,-1.6437308,-0.14704908,1.4940221,0.671744,-1.0352519,-0.6031066,-0.21888901,-1.1336043,-1.354688,-0.73348534,-0.50150144,-0.8901231,-0.7509864,-0.22895344,-0.48945007,-0.5116246,-0.31301895,-0.119534396,-0.77886367,-0.35911262,0.6700997,-0.120781966,0.5845433,0.30793384,0.36645955,-0.51419705,0.30733,-0.43515074,0.46789724,-0.16744474,0.0025528565,-0.3351295,0.47105402,-0.40125257,0.32378298,-0.32320964,0.25254032,-0.32426476,-0.067115955,-0.040247988,0.03577867,-0.3592219,-0.26636425,-0.018406807,0.078108564,-0.07480129,-0.16248938,-0.22983024,-0.19403492,-0.105678946,0.00035136536],"y":[-1.6194587,0.091540664,0.013880752,-0.24738923,-2.1469693,-3.458898,-2.1051152,-1.2633659,-0.6940632,-1.5761495,-1.2804806,-0.01885449,-0.16454135,1.6370367,-1.8465341,-0.7146838,-1.354074,0.80034477,-1.4336692,-1.5894786,-0.7158609,-0.8872366,0.5677124,-0.72075576,-1.9592618,-1.6379726,-1.5748372,-5.113256,0.32466418,-3.272726,-2.521056,-4.2033057,-1.2290186,-2.7907531,-3.706703,-0.16430664,-0.66898036,1.4609884,2.2779295,-3.4482331,-0.20708857,-4.8034067,1.8410627,-3.5576665,1.9316725,-2.7817144,-3.6227875,1.3149072,-3.2893126,-3.5460024,-4.30396,1.3093299,-0.74031305,3.1932538,-0.87673485,1.1312143,-0.27431858,1.2866735,-5.012714,-0.2826188,-2.2174845,-3.5791433,-1.1861067,0.060993396,-1.4045873,-2.398534,1.3310863,-5.4745383,2.122627,2.868148,-1.4783422,-4.888441,1.7347054,-3.2365975,0.066626534,-5.5573316,2.1731818,0.5401592,-3.3878493,2.2370572,1.4171952,0.8097125,-0.6031646,-2.7849262,0.5036407,-0.641934,-5.5496984,-2.4910145,1.6721187,2.8763802,-2.9351091,3.2608004,0.82196045,-3.9078004,1.4946777,-0.41835502,0.8529549,-0.97224593,3.0116124,2.8913603,1.9389071,-0.5530466,3.1611354,-5.247842,2.0197835,2.936544,3.0010295,-1.9228253,3.1503463,2.8098974,0.2947729,1.4827051,0.8004138,-3.7318,0.92564774,-0.3999076,2.9667902,2.9206233,-0.36703673,0.068739645,-4.818571,-5.0460315,-4.904574,-5.216436,-4.188448,1.0860133,0.5861515,-3.6388514,-3.052886,-3.7906208,-3.3352144,-2.1211064,-3.2205286,-2.628678,-3.6098037,-2.8196676,-2.5570753,-2.3316472,-2.8246365,-3.7513275,-2.0318813,-1.8859667,-1.9116253,-2.1943202,-2.3627577,-2.6494517,-0.9112065,-1.7448351,-1.668227,-1.5355413,-1.7365415,-2.239803,-1.9662799,-1.2800547,-1.6481704,-1.2649623,-1.9072429,-1.9689267,-1.4468037,-1.423437,-1.5254948,-1.4080102,-1.3626056,-1.3835872,-1.4134328,-1.2491384,-1.5967892,-1.5720711,-1.2809391,-1.4623657,-1.3629607,-1.4080211,-1.1756572,-1.2071126]},"selected":{"id":"1051"},"selection_policy":{"id":"1050"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{"end":0.5,"start":-3.5},"id":"1006","type":"Range1d"},{"attributes":{"background_fill_color":"#f6f6f6","below":[{"id":"1012"}],"border_fill_color":"#f6f6f6","center":[{"id":"1015"},{"id":"1019"},{"id":"1040"}],"left":[{"id":"1016"}],"renderers":[{"id":"1038"}],"sizing_mode":"scale_width","title":{"id":"1042"},"toolbar":{"id":"1027"},"x_range":{"id":"1004"},"x_scale":{"id":"1008"},"y_range":{"id":"1006"},"y_scale":{"id":"1010"}},"id":"1003","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{},"id":"1048","type":"BasicTickFormatter"},{"attributes":{},"id":"1046","type":"AllLabels"},{"attributes":{},"id":"1045","type":"BasicTickFormatter"},{"attributes":{"active_scroll":{"id":"1021"},"tools":[{"id":"1020"},{"id":"1021"},{"id":"1022"},{"id":"1023"},{"id":"1024"},{"id":"1025"}]},"id":"1027","type":"Toolbar"},{"attributes":{"fill_alpha":{"value":0.2},"fill_color":{"value":"#DA5A57"},"hatch_alpha":{"value":0.2},"line_alpha":{"value":0.2},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Scatter"},{"attributes":{"coordinates":null,"group":null},"id":"1042","type":"Title"},{"attributes":{"coordinates":null,"data_source":{"id":"1002"},"glyph":{"id":"1035"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"1037"},"nonselection_glyph":{"id":"1036"},"view":{"id":"1039"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{},"id":"1050","type":"UnionRenderers"},{"attributes":{"axis":{"id":"1012"},"coordinates":null,"group":null,"ticker":null},"id":"1015","type":"Grid"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"1026","type":"BoxAnnotation"},{"attributes":{"overlay":{"id":"1026"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{"axis":{"id":"1016"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"1019","type":"Grid"},{"attributes":{"coordinates":null,"group":null,"source":{"id":"1002"},"text":{"field":"labels"},"text_align":{"value":"center"},"text_font":{"value":"Regular"},"x":{"field":"x"},"y":{"field":"y"},"y_offset":{"value":5}},"id":"1040","type":"LabelSet"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#DA5A57"},"hatch_alpha":{"value":0.1},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Scatter"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{},"id":"1051","type":"Selection"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{"end":2,"start":-2},"id":"1004","type":"Range1d"},{"attributes":{"coordinates":null,"formatter":{"id":"1045"},"group":null,"major_label_policy":{"id":"1046"},"ticker":{"id":"1017"}},"id":"1016","type":"LinearAxis"},{"attributes":{},"id":"1017","type":"BasicTicker"},{"attributes":{"coordinates":null,"formatter":{"id":"1048"},"group":null,"major_label_policy":{"id":"1049"},"ticker":{"id":"1013"}},"id":"1012","type":"LinearAxis"}],"root_ids":["1003"]},"title":"Bokeh Application","version":"2.4.2"}}
</script>
<script type="text/javascript">
(function() {
const fn = function() {
Bokeh.safely(function() {
(function(root) {
function embed_document(root) {
const docs_json = document.getElementById('1197').textContent;
const render_items = [{"docid":"9dccfb7e-894f-4c29-bf0a-e85812aab332","root_ids":["1003"],"roots":{"1003":"bfabaee6-f4c2-45d0-8b7b-025b700d3fb6"}}];
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

**Title.** TOKI PONA: DATA-DRIVEN VOCABULARY ANALYSIS.

**Subject.** Semantic analysis and classification of vocabulary.

**Object.** *toki pona*, a constructed language.

**Goal.** Perform the semantic analysis and classification of the vocabulary of the language.

- *Problem.* Vocabulary cannot be analysed based on the existing resources. The available dictionaries of the language do not contain enough information.
- *Solution.* Use natural language processing techniques to construct a semantic model of the language and base the analysis on it.

**Methodology.** Distributional semantics and natural language processing, namely language modelling (word embedding).

**Objectives.**

* Define and classify constructed languages.
* Describe *toki pona*, its philosophy, history, and unique features.
* Define distributional semantics.
* Define modern approaches to NLP applicable to the research.
* Obtain the necessary corpora.
* Construct a vector space model of the language.
* Make observations on the model.
* Classify the vocabulary based on the observed semantic relationships between the words of the vocabulary.

**Relevance.**

Constructed language are gaining popularity. With the rise of the internet, these languages now have a space where they can be created, discussed, learnt, taught, and spoken. Despite this, the only constructed language that has seen much representation in scientific writing is Esperanto.

The existing dictionaries of Toki Pona could benefit from the findings of this research. This data can also be used as an aid in teaching the language to new speakers.

The Vector Space Model of Toki Pona can find further use in information retrieval, topic modelling, text prediction, sentiment analysis, and many other areas.

**Personal reasons.**

I like *toki pona*. I want more people to learn about it. I want to see it grow.

**Source code.**

The paper is a work in progress. The most recent rendered *.pdf* can be viewed [here](https://docs.google.com/viewer?url=https://github.com/tsbohc/lipu-sona/raw/master/latex/lipu.pdf). The direct link to a download is [here](https://github.com/tsbohc/lipu-sona/raw/master/latex/lipu.pdf).

The [tsbohc/lipu-sona](https://github.com/tsbohc/lipu-sona) github repository includes:

- The model in the binary format. The scripts that were used to prepare, normalise, and clean the training data.
- The paper and the bibliography in LaTeX[^[LaTeX](https://www.latex-project.org/) is a typesetting system; it includes features designed for the production of technical and scientific documentation.], as well as a rendered *.pdf*.
