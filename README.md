# Dataset

```
# Japanese tokenizer 
＃https://taku910.github.io/mecab/
pip install fugashi  
pip install ipadic
```


```
Japanese Tokenization

今日は良い天気ですね。

今日　は　良い　天気　です　ね　。
```

## Dataset 

Wiki (last dump) 
```
https://dumps.wikimedia.org/jawiki/
https://dumps.wikimedia.org/jawiki/20220220/
```

The data look like this 
```
<doc id="10" url="https://ja.wikipedia.org/wiki?curid=10" title="言語">
言語

言語（げんご）は、
広辞苑や大辞泉には次のように解説されている。
『日本大百科事典』では、「言語」という語は多義である、と解説され、大脳のに蓄えられた《語彙と文法規則の体系》を指すこともあり、その体系を用いる能力としてとらえることもある、と解説され、一方では、抽象的に「すべての人間が共有する言
語能力」を指すこともあるし、「個々の個別言語」を指すこともある、と解説されている。
言語は、人間が用いる意志伝達手段であり、社会集団内で形成習得され、意志を相互に伝達することや、抽象的な思考を可能にし、結果として人間の社会的活動や文化的活動を支えている。言語には、文化の特徴が織り込まれており、共同体で用いられて
いる言語の習得をすることによって、その共同体での社会的学習、および人格の形成をしていくことになる。
ソシュールの研究が、言語学の発展の上で非常に重要な役割を果たしたわけであるが、ソシュール以降は、「共同体の用いる言語体系」のことは「langue ラング」と呼ばれ、それに対して、個々の人が行う言語活動は「parole パロール」という用語で呼
ばれるようになっている。 
```

##  Data preprocessing and cleaning 

Example of the file data with the gender and the context 
````
  
Ex:
ある夜、エリッサは帰宅する途中にライアンと知り合い、(彼)の車で家まで送ってもらうことになる。
One night, Elissa meets Ryan on her way home and (he) sent her home by his car.


ハイデルベルク大学は(彼の)出身大学である。
Heidelberg University is (his) home university.

```` 

please refer to huggingface for the full dataset 5M sent 
[full data](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset)




### 1. MLM 家の中に[MASK]はいるのか

```
python predict_mask_run_jp.py --short jap_he_Mask.txt --output man.txt
```

Example:
Input sentence: ```[MASK]は大学を卒業することが重要であると知っていた```--> GT  **彼**　

```
私は大学を卒業することが重要であると知っていた
```
## Problem with Mask fill in Jap

Input sentence: ```[MASK]はコミュニティのアナウンサーですか``` GT--> **彼**

```
またはコミュニティのアナウンサーですか 
```
