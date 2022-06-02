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

Wiki 
```
https://dumps.wikimedia.org/jawiki/
```




``
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

## 2. 
