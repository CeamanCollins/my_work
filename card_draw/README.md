# Card Draw

## Overview

This **Card Draw** script was created as part of the *Programming and Scripting* module as part of the Higher Diploma in Science in Computing (Data Analytics) at Atlantic Technological University (ATU). 

The script uses an API to draw a hand of 5 cards and display them to the user. It also checks for special poker hands, such as pairs, triples, straights, or flushes, and congratulates the user if any are drawn.

The goal of this project was to demonstrate knowledge of APIs in Python and handling structured data with dictionaries, sets, and lists.

---

## Features

- Draws 5 cards from a virtual deck using the [Deck of Cards API](https://deckofcardsapi.com/).
- Detects special poker hands, including:
  - Pairs
  - Triples
  - Straights
  - Flushes
  - Full houses
  - Four of a kind
- Provides congratulatory messages based on the detected hand.

---

## How to Run

### Running in GitHub CodeSpaces:
1. Open the repository in [GitHub CodeSpaces](https://github.com/features/codespaces).
2. Navigate to the **card_draw** folder.
3. Execute the program by running:
   ```bash
   python carddraw.py
   ```

### Running Locally:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CeamanCollins/my_work.git
   cd my_work/card_draw
   ```
2. Ensure Python is installed on your machine.
3. Install all required dependencies via the `requirements.txt` file:

   Using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   Using `conda`:
   Alternatively, create a Conda environment and install the required dependencies:

   ```bash
   conda create --name <environment-name> --file requirements.txt
   ```

5. Run the program:
   ```bash
   python carddraw.py
   ```
   On Windows:
   ```bash
   [path-to-python]\python.exe carddraw.py
   ```

You can view the script [here](./carddraw.py).

---

## Technologies Used

- **Python**: The core programming language used for the script.
- **API Integration**: Utilized the [Deck of Cards API](https://deckofcardsapi.com/) to simulate card drawing.
- **Requests**: Python package that simplifies making HTTP requests, such as GET and POST, and interacting with web services.
- **GitHub CodeSpaces**: Used for testing and running the script in the cloud-based development environment.

---

## References

The following resources were used during development:
- [Deck of Cards API Documentation](https://deckofcardsapi.com/)
- [Creating an Empty Set in Python](https://stackoverflow.com/questions/17663299/creating-an-empty-set)
- [Python String Methods: capitalize()](https://www.w3schools.com/python/ref_string_capitalize.asp)
- [Python Reference: Sets](https://www.w3schools.com/python/python_ref_set.asp)
- [Converting Strings in a List to Integers](https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-integers)
- [Python Reference: Dictionaries](https://www.w3schools.com/python/python_ref_dictionary.asp)

---

## Future Enhancements

- Adding more poker hand rankings such as straight flushes and royal flushes.
- Creating a GUI-based interface for an optimized user experience.
- Allowing players to input their own cards to check for poker hands.
- Implementing a "high card" detection as a fallback for no special hands.

---

## Contact

If you have any questions, issues, or suggestions related to this project, feel free to contact **Céaman Collins** via [GitHub](https://github.com/CeamanCollins).
