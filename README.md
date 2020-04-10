# WYSIWYS
What you see is what you say: An alternative method of generating translation data for low resource languages 

## src

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
- The Flicker8k dataset is available here: http://academictorrents.com/details/9dea07ba660a722ae1008c4c8afdd303b6f6e53b

- The captions are located at: data/captions.tsv

