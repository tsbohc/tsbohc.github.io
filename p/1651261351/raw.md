<!--
name: toki pona vsm
peek: An elevator pitch for a thesis.
tags: tokipona languages
date: 1651628474
-->

## distributional semantics

In a 1957 publication^[[A Synopsis of Linguistic Theory](https://cs.brown.edu/courses/csci2952d/readings/lecture1-firth.pdf) (1957) by J. R. Firth, p.11], J. R. Firth wrote:

> The placing of a text as a constituent in a context of situation contributes to the statement of meaning since situations are set up to recognise use. *You shall know a word by the company it keeps!*

Here's an example to illustrate this:

> a. A bottle of *telo nasa* is on the table.\
> b. *telo nasa* makes people drunk.\
> c. Only adult people can drink *telo nasa*.\
> d. *telo nasa* is made out of oranges.

Clearly, *telo nasa* refers to an alcoholic beverage.

Now, let's consider a few words that could replace *telo nasa* in these contexts. When a word is appropriate in a context (a, b, c, or d), we will mark that context with a *y* and with a *.* when it is not.

| word      | a | b | c | d
| --------- | - | - | - | -
| telo nasa | y | y | y | y
| juice     | y | . | . | y
| pancake   | . | . | . | .
| wine      | y | y | y | .

- *juice* is stored in bottles and is made out of oranges, but everyone can drink juice and it does not make people drunk.
- *pancake* fits none of the contexts.
- *wine* fits all of the contexts but the one that specifies the main ingredient^[There are varieties of wine that are made with the inclusion of orange zest or juice, but this is irrelevant to the discussion.].

Because *wine* makes the most sense as a replacement, we can assume that *telo nasa* shares some of its properties.

Now, what if it was possible to make a computer to infer meaning from context just like we have?

## word embedding

Let's write a program that will look through the words in our corpus, one by one. It will also count how many times each of the other words appears in the context of the current word. We will only consider *telo nasa* and the less general content words surrounding it.

|        | telo nasa
| ------ | :-:
| bottle | 1
| table  | 1
| people | 2
| drink  | 2
| adult  | 1
| orange | 1

What can be said about *telo nasa* based on the data provided by the program?

That it is related to people and drinking, but also the legal age, bottles, and citruses or the colour orange. It is however, not related to quaternions, the printing press, or non-euclidean geometry.

## word vectors

Let's take the above table and divide each value by the total number of the word relationships in it (6):

|        | telo nasa
| ------ | :-:
| bottle | 0.16
| table  | 0.16
| people | 0.33
| drink  | 0.33
| adult  | 0.16
| orange | 0.16

Now *telo nasa* can be represented as a set of numbers: [0.16, 0.16, 0.33, 0.33, 0.16, 0.16]. This is its *word vector*, a numerical description of a word relative to other words in a corpus. Every single word in a corpus can have one such vector.

Because we are operating on vectors, the principles of linear algebra can be applied to them. We will use *cosine similarity*^[Read more about *cosine similarity* on [wikipedia](https://en.wikipedia.org/wiki/Cosine_similarity).] to determine the degree of similarity between two vectors, that is, to quantify their semantic similarity.

Right now, our corpus is highly specialised, but what if we had more contexts featuring more words?

What if instead of 4 contexts, we had *a quarter of a million*?

# constructed languages

J. R. R. Tolkien wrote books so that his languages had somewhere to live and thrive. Since then, many people have created their own languages. One of them is jan Sonja.

## toki pona

In 2001, jan Sonja created *toki pona*, a philosophical constructed language centered around minimalism. The vocabulary of *toki pona* contains only 120-180 words.

*toki pona* is recognised by the [ISO 639-3](https://iso639-3.sil.org/code_tables/639/data/t?title=tok&field_iso639_cd_st_mmbrshp_639_1_tid=All&name_3=&field_iso639_element_scope_tid=All&field_iso639_language_type_tid=All&items_per_page=200) registry under *tok*. It is the second most spoken^[[ISO 693-3 proposal](https://iso639-3.sil.org/sites/iso639-3/files/change_requests/2021/2021-043_tok.pdf) (2021), p.3.] constructed language in the world.

The words *telo nasa* mean *weird liquid*, which is a common way of referring to alcohol.

### grammar

*toki pona* is an uninflected language. Basic sentences have the following structure:

> [context] la [subject] li [predicate] e [d.o.] lon [prep.phrase]

Example sentence in *sitelen pona*, the writing system of *toki pona*:

<blockquote><p class='linja-pona'>ilo pi sitelen tawa la kon li tawa suli lon tenpo pimeja ni.</p></blockquote>

Written in latin:

> ilo pi sitelen tawa la kon li tawa suli lon tenpo pimeja ni.

| word    | defintion
| ------- | -
| ilo     | tool, instrument
| pi      | [modifier regroup particle]
| sitelen | picture, symbol
| tawa    | movement
| la      | [context particle]
| kon     | air, spirit, essence
| li      | [predicate particle]
| tawa    | movement
| suli    | big, old, important
| lon     | [prepositional phrase particle]
| tenpo   | time, duration
| pimeja  | black, dark
| ni      | this

Literal interpretation:

> in the context of a tool of moving pictures, air moves largely at this time of darkness.

Translation:

> TV broadcast reported that there will be strong wind tonight.

# NLP

NLP (Natural Language Processing) is a field at an intersection of computer science, artificial intelligence, and linguistics.

## vector space model

I have compiled a corpus containing *270903* sentences in *toki pona*.

With this corpus, I have constructed a VSM (Vector Space Model) of *toki pona*. That is, I have calculated the *word vector* of every word in the vocabulary of *toki pona*. Meaning that I have the data that shows the semantic relationships between them.

The actual architecture of the model is more far involved than word counting, but this discussion is beyond the scope of this document. It is however the same in principle.

## visualisation

I have also made an interactive visualisation^[[Bokeh](https://bokeh.org/) is a Python library for creating interactive visualizations for modern web browsers.] of the model projected onto 2D space:

<div class="bk-root" id="b2752458-6f7d-42e9-ae53-b1d2f8947c05" data-root-id="1003"></div>
<script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.2.min.js"></script>
<script type="text/javascript">
Bokeh.set_log_level("info");
</script>
<script type="application/json" id="1330">
{"335f97ec-7432-4c23-bcea-6434f26a3cda":{"defs":[],"roots":{"references":[{"attributes":{"coordinates":null,"group":null,"source":{"id":"1002"},"text":{"field":"labels"},"text_align":{"value":"center"},"text_font":{"value":"Regular"},"x":{"field":"x"},"y":{"field":"y"},"y_offset":{"value":5}},"id":"1040","type":"LabelSet"},{"attributes":{},"id":"1021","type":"WheelZoomTool"},{"attributes":{},"id":"1020","type":"PanTool"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{},"id":"1024","type":"ResetTool"},{"attributes":{},"id":"1045","type":"BasicTickFormatter"},{"attributes":{"data":{"cluster":["#F4685B","#B53679","#B53679","#B53679","#681B80","#681B80","#F4685B","#812581","#B53679","#FEC286","#812581","#9A2D7F","#B53679","#B53679","#F4685B","#B53679","#E55063","#F4685B","#B53679","#B53679","#FEC286","#E55063","#B53679","#9A2D7F","#9A2D7F","#E55063","#1B1044","#FB8660","#681B80","#812581","#1B1044","#1B1044","#9A2D7F","#FB8660","#B53679","#812581","#FEC286","#1B1044","#4F117B","#4F117B","#B53679","#812581","#341068","#B53679","#341068","#9A2D7F","#FB8660","#B53679","#1B1044","#CE4070","#B53679","#681B80","#341068","#B53679","#681B80","#FDA470","#E55063","#341068","#E55063","#4F117B","#E55063","#FDA470","#341068","#FEC286","#4F117B","#681B80","#FEC286","#FEC286","#9A2D7F","#FB8660","#4F117B","#CE4070","#4F117B","#1B1044","#FB8660","#FDA470","#E55063","#4F117B","#FEC286","#812581","#CE4070","#4F117B","#CE4070","#681B80","#FB8660","#4F117B","#FB8660","#4F117B","#4F117B","#FDA470","#CE4070","#9A2D7F","#E55063","#4F117B","#341068","#CE4070","#FDA470","#4F117B","#CE4070","#4F117B","#9A2D7F","#4F117B","#CE4070","#FDA470","#9A2D7F","#B53679","#CE4070","#812581","#4F117B","#FDA470","#4F117B","#4F117B","#FEC286"],"labels":["mi","ni","toki","pona","tawa","jan","ala","lon","sina","ona","tenpo","mute","sona","wile","kama","ken","pilin","taso","seme","pali","lili","tan","nimi","tomo","ma","ike","kepeken","jo","ale","lukin","sitelen","musi","suli","pana","ante","pini","sama","ilo","telo","moku","ijo","suno","tu","nasin","wan","lawa","anu","lipu","kalama","soweli","sin","sewi","nanpa","kulupu","wawa","lape","nasa","luka","weka","kon","pakala","awen","sike","mama","kasi","poka","meli","olin","utala","insa","seli","moli","pimeja","kute","mani","len","sijelo","suwi","mije","open","linja","kiwen","waso","anpa","poki","lete","esun","kili","uta","supa","mu","kule","jaki","ko","mun","pipi","noka","pan","akesi","loje","palisa","walo","kala","sinpin","nena","pu","alasa","lupa","selo","monsi","jelo","laso","unpa"],"x":["-38.46138","-49.086624","-99.00636","-58.667393","-8.771955","-43.024986","-62.138508","7.242768","-78.21611","-29.247143","-79.30121","-23.27711","-98.3818","-70.47139","-31.342113","-79.33582","-16.632399","-36.77186","-67.15863","-53.248337","-15.711523","-11.368229","-125.469246","25.008928","37.096184","-7.692999","-119.6851","-27.19215","-50.873642","-72.61352","-86.57548","-75.52867","47.630287","-19.279793","-84.80182","-77.211845","-1.9857606","-83.896065","158.72025","180.11363","-83.828064","-91.803734","-150.5586","-102.60458","-143.63055","-29.497173","-86.87668","-95.93122","-79.07836","23.987474","-47.866905","59.004173","-156.03564","-60.733685","29.675","5.4288163","11.767666","-144.4474","-3.920557","128.95091","4.4824243","13.161805","-108.03374","71.757774","166.25067","23.588581","45.969475","75.11381","26.326038","113.49866","150.70589","13.623503","129.82455","-68.30175","-44.525017","92.34796","18.304438","186.86093","61.15081","-69.57891","79.684395","119.43521","36.512653","62.61963","125.09696","149.66139","-44.083015","177.77144","-47.985744","66.875404","9.622954","157.3572","7.4458714","179.0609","-96.53182","43.364716","75.2546","188.75877","36.90584","167.43755","118.49258","148.2888","28.833618","81.20126","98.30371","-127.390625","5.027292","90.69532","115.81453","74.40682","164.97054","161.46935","65.85321"],"y":["-32.587513","-10.004149","-21.736603","-17.44885","-3.8755012","-50.93943","-0.5384171","-1.583028","8.998784","-37.714638","-130.07822","-13.83381","-9.312426","-8.290521","-1.3832902","-12.562335","-81.64465","-17.581322","-28.94123","18.404955","-23.533228","-52.374294","3.0319748","17.09239","3.3120933","-76.88944","-27.409245","20.307804","-67.041725","47.806953","50.032524","96.94696","-3.4051857","42.640068","-32.237972","-108.25725","-27.583746","83.320244","-16.50349","-1.7199332","-49.422253","-117.79013","-123.76898","-40.840042","-116.52415","-58.165707","18.778606","47.91142","110.79748","124.68304","5.456404","-17.905056","-114.84189","-49.199955","-40.054893","22.766996","-43.152836","-133.3552","-96.70302","-25.614548","-81.85062","7.894014","-125.527725","-86.54845","20.747412","-3.826006","27.631401","-57.02747","-70.5439","17.00881","-28.947872","-71.5396","-58.541683","102.36837","44.80407","-13.351269","-95.59469","-7.8251133","-71.23125","-114.2952","48.74398","42.327477","107.99596","-6.070653","11.052632","-38.356388","33.708218","23.113983","106.82388","12.014231","122.34713","70.81828","-109.565186","-22.27569","-127.013725","120.12992","-3.5307174","9.019223","129.99672","49.905094","52.762894","38.599068","114.463264","36.11547","38.35858","12.734093","88.38919","16.62199","29.895851","28.670984","40.212578","62.08009","-54.500393"]},"selected":{"id":"1051"},"selection_policy":{"id":"1050"}},"id":"1002","type":"ColumnDataSource"},{"attributes":{"fill_alpha":{"value":0.9},"fill_color":{"field":"cluster"},"line_alpha":{"value":0},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1035","type":"Scatter"},{"attributes":{"background_fill_color":"#f6f6f6","below":[{"id":"1012"}],"border_fill_color":"#f6f6f6","center":[{"id":"1015"},{"id":"1019"},{"id":"1040"}],"left":[{"id":"1016"}],"renderers":[{"id":"1038"}],"sizing_mode":"scale_width","title":{"id":"1042"},"toolbar":{"id":"1027"},"x_range":{"id":"1004"},"x_scale":{"id":"1008"},"y_range":{"id":"1006"},"y_scale":{"id":"1010"}},"id":"1003","subtype":"Figure","type":"Plot"},{"attributes":{"bottom_units":"screen","coordinates":null,"fill_alpha":0.5,"fill_color":"lightgrey","group":null,"left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"right_units":"screen","syncable":false,"top_units":"screen"},"id":"1026","type":"BoxAnnotation"},{"attributes":{},"id":"1008","type":"LinearScale"},{"attributes":{},"id":"1049","type":"AllLabels"},{"attributes":{},"id":"1025","type":"HelpTool"},{"attributes":{"overlay":{"id":"1026"}},"id":"1022","type":"BoxZoomTool"},{"attributes":{"end":150,"start":-150},"id":"1004","type":"Range1d"},{"attributes":{},"id":"1023","type":"SaveTool"},{"attributes":{"coordinates":null,"formatter":{"id":"1045"},"group":null,"major_label_policy":{"id":"1046"},"ticker":{"id":"1017"}},"id":"1016","type":"LinearAxis"},{"attributes":{"coordinates":null,"formatter":{"id":"1048"},"group":null,"major_label_policy":{"id":"1049"},"ticker":{"id":"1013"}},"id":"1012","type":"LinearAxis"},{"attributes":{},"id":"1013","type":"BasicTicker"},{"attributes":{"axis":{"id":"1012"},"coordinates":null,"group":null,"ticker":null},"id":"1015","type":"Grid"},{"attributes":{"active_scroll":{"id":"1021"},"tools":[{"id":"1020"},{"id":"1021"},{"id":"1022"},{"id":"1023"},{"id":"1024"},{"id":"1025"}]},"id":"1027","type":"Toolbar"},{"attributes":{"source":{"id":"1002"}},"id":"1039","type":"CDSView"},{"attributes":{"end":150,"start":-150},"id":"1006","type":"Range1d"},{"attributes":{},"id":"1051","type":"Selection"},{"attributes":{"coordinates":null,"group":null},"id":"1042","type":"Title"},{"attributes":{},"id":"1046","type":"AllLabels"},{"attributes":{"coordinates":null,"data_source":{"id":"1002"},"glyph":{"id":"1035"},"group":null,"hover_glyph":null,"muted_glyph":{"id":"1037"},"nonselection_glyph":{"id":"1036"},"view":{"id":"1039"}},"id":"1038","type":"GlyphRenderer"},{"attributes":{},"id":"1048","type":"BasicTickFormatter"},{"attributes":{},"id":"1050","type":"UnionRenderers"},{"attributes":{"axis":{"id":"1016"},"coordinates":null,"dimension":1,"group":null,"ticker":null},"id":"1019","type":"Grid"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"field":"cluster"},"hatch_alpha":{"value":0.1},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1036","type":"Scatter"},{"attributes":{"fill_alpha":{"value":0.2},"fill_color":{"field":"cluster"},"hatch_alpha":{"value":0.2},"line_alpha":{"value":0.2},"line_color":{"value":"#1f77b4"},"size":{"value":10},"x":{"field":"x"},"y":{"field":"y"}},"id":"1037","type":"Scatter"},{"attributes":{},"id":"1017","type":"BasicTicker"}],"root_ids":["1003"]},"title":"Bokeh Application","version":"2.4.2"}}
</script>
<script type="text/javascript">
(function() {
const fn = function() {
Bokeh.safely(function() {
(function(root) {
function embed_document(root) {
const docs_json = document.getElementById('1330').textContent;
const render_items = [{"docid":"335f97ec-7432-4c23-bcea-6434f26a3cda","root_ids":["1003"],"roots":{"1003":"b2752458-6f7d-42e9-ae53-b1d2f8947c05"}}];
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

| word   | similarity | definition
| -      | :-:        | -
| lawa   | 0.551      | head, control, rule
| moli   | 0.536      | death, murder
| jan    | 0.427      | person, people
| wawa   | 0.404      | power, strength
| pakala | 0.397      | break, damage
| palisa | 0.360      | long hard object

Or even ask the question "if *suno* (sun) is *seli* (hot), then what is something *lete* (cold) that is similar to *suno* (sun)?" using linear algebra operations:

```python
vsm.most_similar(positive=['suno', 'lete'], negative=['seli']) =>
```

| word   | similarity | definition
| -      | :-:        | -
| mun    | 0.659      | moon
| pini   | 0.595      | end, finish
| pimeja | 0.469      | black, dark

Keep in mind that there are only two words in *toki pona* that can denote celestial bodies. Also, *cosine similarity* ranges from *-1* to *+1*, meaning that *0.659* is an *83%* match.

See further examples in the library^[[Gensim](https://pypi.org/project/gensim/) is a Python library for topic modelling, document indexing and similarity retrieval with large corpora.] documentation [here](https://radimrehurek.com/gensim/models/keyedvectors.html#what-can-i-do-with-word-vectors).

## making observations

The following is just a couple of examples.

Despite *pimeja* (black) being a colour, it is more semantically connected to the word *tenpo* (time). This is because the most common usage of *pimeja* is to specify a time of day.

In contrast, *kasi* (plant) is closely related to the rest of the colours. This is because *toki pona* has one word for blue and green: *laso*. Despite the existence of natural languages that do this, the majority of *toki pona* speakers feel the need to refer to these colours unambiguously.

## argumentation

This research aims to analyse and classify the vocabulary of *toki pona* based on the actual usage patterns of the language via the methodology discussed previously.
