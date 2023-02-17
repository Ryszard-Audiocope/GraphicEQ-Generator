
# GraphicEQ Generator

This project is an automatic generator of graphic equalizer filters for Wavelet and possibly other equalizer software. All you need to provide are base and target measurements.

Unlike [AutoEQ](https://github.com/jaakkopasanen/AutoEq), it doesn't convert generated Parametric EQ filters into Graphic EQ filters. Instead, it simply calculates the difference between those two measurements and generates Graphic EQ filters accordingly.
## Authors

- [@Ryszard-Audiocope](https://github.com/Ryszard-Audiocope)
- [@ChatGPT](https://chat.openai.com/chat)


## Installation and usage
This is the step-by-step guide to running a GraphicEQ Generator by Ryszard. 
### Prerequisites
Before running the generator, you need to have Python and NumPy installed on your computer. 	Here are the steps to install them:

1. Install Python: Go to the official Python website and download the latest version of Python. Follow the instructions in the installation wizard to complete the installation.

2. Install NumPy: Once Python is installed, you can install NumPy using the following command in your command prompt or terminal: ```pip install numpy```. This will install the latest version of NumPy.

### Running the program
Once you have installed Python and NumPy, you can follow these steps to run the generator:

1. Prepare two text files: base.txt and target.txt. Make sure these files contain frequency and amplitude data, separated by a space or a tab, with each data point on a separate line. The first line of each file should contain a header that you will skip during loading. They should be basically standard frequency response .txt files.

2. Download codeblock.py provided by Ryszard.

3. Place the codeblock.py file in the same directory as the base.txt and target.txt files. It could be any folder you want.

4. Press the ```Win``` + ```R``` keys on your keyboard to open the "Run" dialog box.

5. In the "Run" dialog box, type ```cmd``` and press ```Enter``` to open the Command Prompt.

6. In the Command Prompt, type ```cd <directory_path>``` to change the current directory to the one you have made in previous steps. Replace ```<directory_path>``` with the actual path of the directory you want to open. For example ```C:\Users\Username\Documents\ProjectX```.

7. Press Enter to execute the command and change the current directory.

8. Run the Python script by typing the command ```python codeblock.py``` in the terminal.

9. Results will be saved in output.txt file in the same directory.

And that's it! If you have any issues or questions, feel free to ask.
## Examples
[base.txt](https://github.com/Ryszard-Audiocope/GraphicEQ-generator/blob/main/examples/base.txt)

[target.txt](https://github.com/Ryszard-Audiocope/GraphicEQ-generator/blob/main/examples/target.txt)

[output.txt](https://github.com/Ryszard-Audiocope/GraphicEQ-generator/blob/main/examples/output.txt)
