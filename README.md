# Gender Dataset 

## Ex

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
