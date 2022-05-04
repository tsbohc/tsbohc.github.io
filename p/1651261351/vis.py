from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d, HoverTool, WheelZoomTool
from bokeh.plotting import figure, output_file, show, save
from bokeh.embed import components

output_file("vis.html", title="toki pona vsm")

wv = {
    'li': [1.3486547, -1.6194587],
    'mi': [-1.1393044, 0.091540664],
    'ni': [-1.5720041, 0.013880752],
    'la': [-0.38249698, -0.24738923],
    'pona': [-2.2710347, -2.1469693],
    'jan': [1.7975209, -3.458898],
    'toki': [-3.1358418, -2.1051152],
    'tawa': [1.2617582, -1.2633659],
    'ala': [-1.3343861, -0.6940632],
    'pi': [1.8259941, -1.5761495],
    'lon': [2.500386, -1.2804806],
    'sina': [-1.2873998, -0.01885449],
    'ona': [-0.67260605, -0.16454135],
    'tenpo': [-2.6114821, 1.6370367],
    'sona': [-3.2218158, -1.8465341],
    'mute': [1.0977894, -0.7146838],
    'wile': [-2.338796, -1.354074],
    'kama': [-1.9397383, 0.80034477],
    'ken': [-2.3715923, -1.4336692],
    'seme': [-1.6890316, -1.5894786],
    'pali': [-2.6118054, -0.7158609],
    'taso': [-1.4154502, -0.8872366],
    'pilin': [-0.371847, 0.5677124],
    'lili': [1.289328, -0.72075576],
    'tan': [1.2850772, -1.9592618],
    'tomo': [3.4333413, -1.6379726],
    'ma': [3.5986688, -1.5748372],
    'nimi': [-1.4442865, -5.113256],
    'ike': [-0.13737985, 0.32466418],
    'musi': [-4.095844, -3.272726],
    'kepeken': [-1.728795, -2.521056],
    'sitelen': [-2.7685974, -4.2033057],
    'lukin': [-1.4875969, -1.2290186],
    'jo': [0.95621985, -2.7907531],
    'ilo': [-3.1846993, -3.706703],
    'ale': [-2.0221148, -0.16430664],
    'suli': [2.5452545, -0.66898036],
    'pini': [-2.401174, 1.4609884],
    'moku': [1.4957461, 2.2779295],
    'ante': [0.52510387, -3.4482331],
    'pana': [0.025120322, -0.20708857],
    'sama': [1.2092049, -4.8034067],
    'telo': [2.4588406, 1.8410627],
    'ijo': [0.7372529, -3.5576665],
    'suno': [-2.650996, 1.9316725],
    'anu': [-1.9527134, -2.7817144],
    'nasin': [1.5064843, -3.6227875],
    'tu': [-4.703963, 1.3149072],
    'kalama': [-4.218044, -3.2893126],
    'lawa': [2.843264, -3.5460024],
    'lipu': [-2.7152133, -4.30396],
    'wan': [-4.710185, 1.3093299],
    'kin': [-0.88238037, -0.74031305],
    'soweli': [0.3531759, 3.1932538],
    'sin': [-3.0299003, -0.87673485],
    'lape': [-0.85121346, 1.1312143],
    'wawa': [1.71347, -0.27431858],
    'nanpa': [-4.7283216, 1.2866735],
    'en': [1.106221, -5.012714],
    'nasa': [0.8324366, -0.2826188],
    'weka': [2.6428747, -2.2174845],
    'kulupu': [1.7950042, -3.5791433],
    'sewi': [4.4064302, -1.1861067],
    'kon': [1.7699559, 0.060993396],
    'awen': [2.8903997, -1.4045873],
    'pakala': [2.3274336, -2.398534],
    'luka': [-4.679999, 1.3310863],
    'mama': [2.3018837, -5.4745383],
    'sike': [-3.1676924, 2.122627],
    'kasi': [3.0665834, 2.868148],
    'poka': [3.5154555, -1.4783422],
    'olin': [1.6312311, -4.888441],
    'seli': [2.0138965, 1.7347054],
    'kute': [-4.0783014, -3.2365975],
    'insa': [2.9445803, 0.066626534],
    'meli': [2.4165685, -5.5573316],
    'suwi': [1.2775857, 2.1731818],
    'len': [3.1562002, 0.5401592],
    'utala': [2.790032, -3.3878493],
    'pimeja': [-1.537148, 2.2370572],
    'open': [-2.4276206, 1.4171952],
    'sijelo': [0.6250177, 0.8097125],
    'mani': [-3.756722, -0.6031646],
    'moli': [2.5665672, -2.7849262],
    'linja': [3.9025834, 0.5036407],
    'esun': [-3.5565283, -0.641934],
    'mije': [2.3954515, -5.5496984],
    'ali': [1.3597451, -2.4910145],
    'lete': [1.9677153, 1.6721187],
    'kili': [2.4122329, 2.8763802],
    'uta': [-2.9489431, -2.9351091],
    'waso': [0.3714413, 3.2608004],
    'poki': [2.4578843, 0.82196045],
    'mu': [-1.7086161, -3.9078004],
    'kiwen': [3.681842, 1.4946777],
    'supa': [4.3674703, -0.41835502],
    'jaki': [1.0481634, 0.8529549],
    'anpa': [4.289725, -0.97224593],
    'kule': [3.7803977, 3.0116124],
    'pan': [1.918512, 2.8913603],
    'ko': [2.646997, 1.9389071],
    'noka': [4.3389215, -0.5530466],
    'pipi': [0.21798682, 3.1611354],
    'pu': [-1.6301309, -5.247842],
    'mun': [-2.977052, 2.0197835],
    'loje': [3.4680796, 2.936544],
    'akesi': [-0.08074489, 3.0010295],
    'alasa': [-1.528182, -1.9228253],
    'kala': [0.353501, 3.1503463],
    'walo': [3.4254289, 2.8098974],
    'sinpin': [3.7086706, 0.2947729],
    'palisa': [3.7806742, 1.4827051],
    'nena': [3.7970464, 0.8004138],
    'monsuta': [-1.2879957, -3.7318],
    'selo': [3.202499, 0.92564774],
    'lupa': [3.7966437, -0.3999076],
    'laso': [3.592175, 2.9667902],
    'jelo': [3.3436065, 2.9206233],
    'monsi': [3.9473133, -0.36703673],
    'oko': [0.8063183, 0.068739645],
    'unpa': [1.519453, -4.818571],
    'leko': [-0.1628589, -5.0460315],
    'kipisi': [-0.13387059, -4.904574],
    'ku': [-1.6437308, -5.216436],
    'tonsi': [-0.14704908, -4.188448],
    'namako': [1.4940221, 1.0860133],
    'misikeke': [0.671744, 0.5861515],
    'kijetesantakalu': [-1.0352519, -3.6388514],
    'meso': [-0.6031066, -3.052886],
    'to': [-0.21888901, -3.7906208],
    'kokosila': [-1.1336043, -3.3352144],
    'linluwi': [-1.354688, -2.1211064],
    'epiku': [-0.73348534, -3.2205286],
    'isipin': [-0.50150144, -2.628678],
    'soko': [-0.8901231, -3.6098037],
    'lanpan': [-0.7509864, -2.8196676],
    'majuna': [-0.22895344, -2.5570753],
    'powe': [-0.48945007, -2.3316472],
    'jasima': [-0.5116246, -2.8246365],
    'te': [-0.31301895, -3.7513275],
    'pake': [-0.119534396, -2.0318813],
    'oke': [-0.77886367, -1.8859667],
    'wa': [-0.35911262, -1.9116253],
    'pata': [0.6700997, -2.1943202],
    'waleja': [-0.120781966, -2.3627577],
    'po': [0.5845433, -2.6494517],
    'mulapisu': [0.30793384, -0.9112065],
    'ete': [0.36645955, -1.7448351],
    'apeja': [-0.51419705, -1.668227],
    'kiki': [0.30733, -1.5355413],
    'kan': [-0.43515074, -1.7365415],
    'tuli': [0.46789724, -2.239803],
    'misa': [-0.16744474, -1.9662799],
    'jami': [0.0025528565, -1.2800547],
    'kuntu': [-0.3351295, -1.6481704],
    'unu': [0.47105402, -1.2649623],
    'yupekosi': [-0.40125257, -1.9072429],
    'san': [0.32378298, -1.9689267],
    'melome': [-0.32320964, -1.4468037],
    'kapesi': [0.25254032, -1.423437],
    'kulijo': [-0.32426476, -1.5254948],
    'usawi': [-0.067115955, -1.4080102],
    'kamalawala': [-0.040247988, -1.3626056],
    'puwa': [0.03577867, -1.3835872],
    'su': [-0.3592219, -1.4134328],
    'omekapo': [-0.26636425, -1.2491384],
    'taki': [-0.018406807, -1.5967892],
    'ewe': [0.078108564, -1.5720711],
    'mijomi': [-0.07480129, -1.2809391],
    'kese': [-0.16248938, -1.4623657],
    'soto': [-0.22983024, -1.3629607],
    'teje': [-0.19403492, -1.4080211],
    'natu': [-0.105678946, -1.1756572],
    'sutopatikuna': [0.00035136536, -1.2071126]
}

wv_data = {
        'x': [],
        'y': [],
        'labels': []
}

for key in wv:
    wv_data['x'].append(wv[key][0])
    wv_data['y'].append(wv[key][1])
    wv_data['labels'].append(key)

source = ColumnDataSource(data=wv_data)

p = figure(x_range=(-2, 2), y_range=(-3.5, 0.5), sizing_mode='scale_width',
        background_fill_color="#f6f6f6", border_fill_color='#f6f6f6')

p.scatter(x='x', y='y', size=10, source=source, marker='circle', fill_alpha=0.9,
        line_alpha=0, fill_color='#DA5A57')
# p.xaxis[0].axis_label = 'x axis'
# p.yaxis[0].axis_label = 'y axis'

labels = LabelSet(x='x', y='y', text='labels', text_align='center', y_offset=5,
        source=source, render_mode='canvas', text_font = {'value': 'Regular'})

# tooltips = [('token', '@labels')]

p.toolbar.active_scroll = p.select_one(WheelZoomTool)

p.add_layout(labels)

# p.add_tools(HoverTool(tooltips=tooltips))

# show(p)
save(p)
