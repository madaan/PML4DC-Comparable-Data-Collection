  
* [Practical Comparable Data Collection for Low-Resource Languages via Images](#practical-comparable-data-collection-for-low-resource-languages-via-images)
* [Source](#source)
* [Data](#data)
* [Task Instructions](#task-instructions)
* [Citation](#citation)


## Practical Comparable Data Collection for Low-Resource Languages via Images

- Paper: https://arxiv.org/abs/2004.11954

- Slides: https://madaan.github.io/res/artifacts/pml4dc-practical-data-collection.pdf

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


## Task Instructions

 - आपको एक वाक्य के साथ हर छवि का वर्णन करना होगा। 
 - छवि के वर्णन में शुद्ध हिंदी का उपयोग करना ज़रूरी नहीं हे | जैसा ठीक लगे लिखें |  
 - कृपया उन गतिविधियों, लोगों, जानवरों और वस्तुओं का सटीक विवरण प्रदान करें जिन्हें आप चित्र में देख रहे हें |  
 - प्रत्येक विवरण एक ही वाक्य का होना चाहिए। 
 - विवरण हिंदी में लिखा जाना चाहिए। 
 - संक्षिप्त होने का प्रयास करें। 
 - अगर किसी शब्द का हिंदी में मतलब ना पता हो तो उसे इंग्लिश में ही लिख दें | 
 - व्याकरण और वर्तनी पर ध्यान दें।
 
# Citation

If you use our work, please cite:

```
@inproceedings{madaan2020practical,
  title={Practical Comparable Data Collection for Low-Resource Languages via Images},
  author={Madaan, Aman and Rijhwani, Shruti and Anastasopoulos, Antonios and Yang, Yiming and Neubig, Graham},
  booktitle={Proceedings of the Practical ML for Developing Countries Workshop, ICLR 2020},
  year={2020}
}
```
