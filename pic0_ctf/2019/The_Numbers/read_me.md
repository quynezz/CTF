**Description:** The numbers... what do they mean? numbers.png

First we open the image file with 

```bash 
xdg-open numbers.png 
```

Then we'll see a combination of non-formatted range of number, but it seem like ascii number but being modify by some math formula 

`real_number = 97 + (current_number - 1)`

[image](./the_numbers.png)

```bash
#!/bin/bash

for i in $(cat the_number.txt); do
        # Check if the input is a number (integer)
        if [[ "$i" =~ ^[0-9]+$ ]]; then
                res=$((97 + i - 1))
                printf "\\$(printf '%03o' "$res")"
        else
                # not a int 
                printf "%s" "$i"
        fi
done
```
run 

`./bash.sh`

 and we have: 

**Flag:** `picoctf{thenumbersmason}`


