# French-flash-cards
This program is a tool for learning new words in French by showing flash cards.

## Use
After running the program, screen displays flash card with a french word, which "turns" after 4 seconds to reveal english translation. If the user guessed the translation right, green button should be clicked to denote right answer, or red button to denote wrong answer. 
List of unknown words is created at the end of the program, and, at next use of the program, those words will be displayed first. If they are guessed correctly, they will be removed from the unknown list.

## Modules and functions
The program uses `tkinter` for GUI, `random` for random word choosing and `pandas` module to read and write to csv files.
From `tkinter`module, we used `Tk()` to draw program window, `after()` function to flip the card, `Canvas()` to display flash cards and `Button()` to display two buttons with different images and commands.
From `pandas` module, we used `read_csv()` to read file containing used words, and `to_dict()` to convert data into dictionary to be used in the program.
```python
next_card()
```
The function takes global variables `current_card` (empty dictionary) and `flip_timer`, randomly chooses a word from `word_dict` and displays it on the canvas.

```python
flip_card()
```
The function configures canvas to display english translation of the word.

```python
is_known()
```
The function takes the word and puts it, using `pandas.DateFrame().to_csv()`, to file called `words_to_learn.csv` to be accessed next time the program is being run, and runs `next_card()` funtion.

## Program engine
The program runs as a part of `Tk()` `Tk.mainloop()` loop.

## Running the game
This game is intended to be run by Python IDE or other Python interpeter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
