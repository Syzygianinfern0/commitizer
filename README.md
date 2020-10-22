![alt text](https://github.com/Syzygianinfern0/commitizer/blob/master/docs/Assets/Images/3.png)
---
<p align=center> Generate patterns and keep your GitHub contribution streak going </p>
<p align=center> Project under construction </p>

# Installation
```bash
git clone https://github.com/Syzygianinfern0/commitizer.git
cd commitizer
pip install .
```
# Usage
Available arguments are:

|Argument|Function|
|---|---|
|`-s` or `--start-date`|Start date as dd/mm/YYYY|
|`-e` or `--end-date`|End date as dd/mm/YYYY|
|`-n` or `--number`|Accepts either a single number (constant number every day between the date range) or two comma separated numbers (bounds of random int generator)|
|`-v` or `--verbose`|Verbosity Level 1|
|`--v`|Verbosity Level 2|

## Example Usage
```bash
commitizer -s 15/10/2020 -e 22/10/2020 -n 3,8
```
