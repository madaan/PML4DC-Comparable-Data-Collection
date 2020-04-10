## Practical Comparable Data Collection for Low-Resource Languages via Images

- Work presented as a poster at Practical ML for Developing Countries Workshop at ICLR 2020
- Talk/presentation/pre-print coming soon.

## Source

* Translation Downstream Task - (Paul Michel's Baseline NMT Implementation)[https://github.com/pmichel31415/11731-assignment-2-baseline]

* Unsupervised Dictionary Extraction
```
python src/make_dict.py -i data/alignments/wys.fastalign.input -a data/alignments/symmetric.align -l1 hin -l2 eng 
```

* Extracting Counts
```
python src/find_token_alignments.py data/alignments/wys.fastalign.input data/alignments/symmetric.align output_path
```
## 

## Data
```
data/
├── alignments
│   ├── forward.align
│   ├── reverse.align
│   ├── symmetric.align
│   └── wys.fastalign.input
├── captions.tsv
└── dict.hin-eng.txt
```

| Contents                           	| Path                                                                         	|
|------------------------------------	|------------------------------------------------------------------------------	|
| Captions in both English and Hindi 	| data/captions.tsv                                                            	|
| Flickr8k                           	| http://academictorrents.com/details/9dea07ba660a722ae1008c4c8afdd303b6f6e53b 	|
| Generated Dictionary               	| data/dict.hin-eng.txt                                                        	|
| Fastalign input/output             	| data/alignments/                                                             	|