# Draw a lines Art drawing algorithm in [ModernGL](https://moderngl.readthedocs.io/en/latest/)

## General Instructions
- Choose a line drawing algorithm from http://graphx-chlg1.obedmr.com/ and implement your `line(x1, y1, x2, y2)` function in python with modernGL
- Implement your code in the [`linesArt.py`](./linesArt.py) file
- A `line` function must exists with the desired line-drawing algorithm
- A `linesArtDrawing` function is required with the algorithm that generates a patterned lines-only piece of art
- For the line drawing algorithm, you can get some inspiration from 
  - [Google Images](https://www.google.com/search?q=lines+algorithm+art&sca_esv=0938baf10882972d&udm=2&biw=1920&bih=993&sxsrf=ADLYWILRg10N0dgfTO4j3ihiND79LuiwBA%3A1723002820540&ei=xO-yZtXFILXfp84PyN_U-AQ&ved=0ahUKEwjVt8LY_eGHAxW178kDHcgvFU8Q4dUDCBE&uact=5&oq=lines+algorithm+art&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2xpbmVzIGFsZ29yaXRobSBhcnRIxSxQ5glY7ytwA3gAkAEAmAHHAqAB5RCqAQgxMy4zLjEuMbgBA8gBAPgBAZgCCaACpAnCAgQQIxgnwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIGEAAYBRgewgIGEAAYCBgemAMAiAYBkgcFMC43LjKgB_I2&sclient=gws-wiz-serp)
  - [Algorithm Art](https://observablehq.com/collection/@mmansion/algorithmic-art)


## Test cases
Your program will be graded with the following requirements

- Your program must support the following way of execution
  ```
  python linesArt.py --nLines <# of lines> [--color]
  ```
- Below the tests that will be executed by the reviewer
  ```
  # Test 1 - 25 black lines (20 points)
  python linesArt.py --nLines 25

  # Test 2 - 1000 black lines (20 points)
  python linesArt.py --nLines 1000

  # Test 3 - 50 random-color lines (20 points)
  python linesArt.py --nLines 100 --color

  # Test 4 - 50000 black lines (20 points)
  python linesArt.py --nLines 50000

  # Test 5 - 50000 random-color lines (20 points)
  python linesArt.py --nLines 50000 --color
  ```
