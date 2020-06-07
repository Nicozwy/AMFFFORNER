# Named Entity Recognition
Named entity recognition (NER) is a fundamental task that aims to identify named entities in raw text and assign them pre-defined categorical tags such as PER (Person), ORG (Organization), LOC (Location), etc.<br>
This is an implementation of the paper: Attention-based Multi-level Feature Fusion for Named Entity Recognition. Intuitively, multi-level features can be helpful when recognizing named entities from complex sentences. This study proposes a novel framework called attention-based multi-level feature fusion (AMFF), which is used to capture the multi-level features from different perspectives to improve NER.

# Requirements
+ Ubuntu 
+ Python 3.6.9+
+ TensorFlow-gpu 1.13.1
+ CUDA 10+
+ pathlib
+ numpy
+ json

# Datasets
+ [CoNLL-2003](https://www.clips.uantwerpen.be/conll2003/ner/)
+ [NCBI-disease](https://pubmed.ncbi.nlm.nih.gov/24393765/)
+ [SciERC](https://arxiv.org/abs/1808.09602)
+ [JNLPBA](https://www.aclweb.org/anthology/W04-1213/)

# Usage
1. Switch to the corresponding virtual environment, and install metrics for NER 
```
    pip install git+https://github.com/guillaumegenthial/tf_metrics.git
```
2. Put the dataset into the corresponding directory and preprocess the datasets to the CONLL format, e.g.,<br>

```
    data/sample
```
3. get pre-trained word embeddings [GloVe](https://nlp.stanford.edu/projects/glove/) and put it into `data/sample`;<br>
> Switch to `../data/sample`:<br>
> Run `preprocess.py` and make sure the first line of the output file is not blank.
```
      python preprocess.py
``` 
> decompress glove:<br>	
```
      unzip glove.840B.300d.zip -d glove.840B.300d.txt
      rm glove.840B.300d.zip
```
> build vocab and glove:<br>    
```
      python build_vocab.py
      python build_glove.py
```
4. Switch to the root directory and get started with `main_amff.py`.<br>
```
      python main_amff.py
```

## References 
* Scibert: A pretrained language model for scientific text， Beltagy et al. [link](https://www.aclweb.org/anthology/D19-1371.pdf)
* Collabonet: collaboration of deep neural networks for biomedical named entity recognition, Yoon, et al. [link](https://arxiv.org/abs/1809.07950)
* Contextual String Embeddings for Sequence Labeling, Akbik et al. [link](https://www.aclweb.org/anthology/C18-1139/)
* Neural architectures for named entity recognition, Lample, et al. [link](https://arxiv.org/abs/1603.01360)
* End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF, Ma et al. [link](https://arxiv.org/pdf/1603.01354.pdf)
* Named Entity Recognition with Bidirectional LSTM-CNNs, JPC Chiu et al. [link](https://arxiv.org/pdf/1511.08308.pdf)
* Bidirectional LSTM-CRF Models for Sequence Tagging, Z Huang et al. [link](https://arxiv.org/pdf/1508.01991.pdf)
* Sequence-tagging-with-tensorflow, guillaumegenthial. [link](https://guillaumegenthial.github.io/sequence-tagging-with-tensorflow.html)<br>
...

# Citation
Please cite:<br>
```
@InProceedings{yang2020AMFF,
  title     = {Attention-based Multi-level Feature Fusion for Named Entity Recognition},
  author    = {Zhiwei Yang, Hechang Chen, Jiawei Zhang, Jing Ma, and Yi Chang},
  booktitle = {IJCAI},  
  year      = {2020},
 }
```

