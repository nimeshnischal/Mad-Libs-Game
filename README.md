# Mad-Libs-Game
A Mad Libs replica game based on Python including my custom module and an excel file.

Enter words according to the instructions and uncover a strange and unexpected story everytime!

#### The excel file contains story templates in the following format:
1. **Story no.**: Contains integer values indexing the stories.
2. **Story Template**: Contains the template of the story to be displayed.
  Rules for writing story template:
    * Use correctly numbered curly braces instead of blanks starting with 0. e.g. {0}
    * Use alt+Enter for a new line wherever necessary. Do not add '\n' for new lines or any special characters.
3. **Blank Hints**: Contains the hints to be displayed while taking the input.
  Rules for writing story template:
    * Write all hints in a single line, no need of special characters. Can use spaces
    * Separate each hint with a semi-colon "**;**"
    
## Uses nimesh_app_basics module

The module nimesh_app_basics is a custom module made by me to help me in the development of basic commad window based apps.
