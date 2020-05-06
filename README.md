## Practical Comparable Data Collection for Low-Resource Languages via Images

- Paper: https://arxiv.org/abs/2004.11954

- We propose a method of curating high-quality comparable training data for low-resource languages without requiring that the annotators are bilingual. Our method involves using a carefully selected set of images as a pivot between the source and target languages by getting captions for such images in both languages independently. Human evaluations on the English-Hindi comparable corpora created with our method show that 81.1\% of the pairs are acceptable translations, and only 2.47% of the pairs are not a translation at all. We further establish the potential of dataset collected through our approach by experimenting on two downstream tasks -- machine translation and dictionary extraction. 

- Joint work with Shruti Rijhwani, Antonios Anastasopoulos, Yiming Yang, and Graham Neubig.

- Work to be presented as a poster at Practical ML for Developing Countries Workshop at ICLR 2020.


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
| Captions in both English and Hindi, as well as image ids 	| data/captions.tsv                                                            	|
| Flickr8k                           	| http://academictorrents.com/details/9dea07ba660a722ae1008c4c8afdd303b6f6e53b 	|
| Generated Dictionary               	| data/dict.hin-eng.txt                                                        	|
| Fastalign input/output             	| data/alignments/                                                             	|
