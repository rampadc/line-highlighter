# Purpose

This project highlights specific lines of interest in a code snippet. The result can be copy/pasted back into a Powerpoint slide with the resulting highlight.

![Demo](docs/demo.gif)

## How it works

When copying code from VSCode, you're copying the text as well as the formatting. This carries inside the clipboard data as HTML data. The two GIFs below show the format of this HTML data. Have a look through `dimUnwantedText()` in `index.html`. The code goes over each token of a unwanted line and reduce the opacity by 0.5. Since Powerpoint won't accept reduced opacity of texts, the code is changing the text's colour to an equivalent color that resembles the same color at 0.5 opacity. Copying from the website copies the text as HTML on modern browsers. This project has been tested on the latest version of Chrome, Edge and Firefox as of 20/Dec/2020.

The corresponding GIFs mentioned are as below:

**1.gif**: Lines in code are grouped in DIVs.

![1.gif](docs/1.gif)

**2.gif**: Tokens in code are grouped in spans with inline CSS colour.

![2.gif](docs/2.gif)

