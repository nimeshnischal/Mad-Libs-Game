from xlrd import open_workbook
import nimesh_app_basics


def get_story():
    try:
        wb = open_workbook('story_templates.xlsx')
    except FileNotFoundError:
        print("Stories not found. Please check if the file containing the stories exists or not.")
        return -1
    number_of_stories = wb.sheet_by_index(0).nrows
    if number_of_stories == 1:
        print("No story template found in the file. Please populate the file first.")
        return -1
    random_story_row_index = nimesh_app_basics.get_random_int_in_range(1, number_of_stories-1)
    # TODO devise a mechanism to not repeat last attempted story
    sheet = wb.sheet_by_index(0)
    try:
        return [sheet.cell(random_story_row_index, 1).value,
                sheet.cell(random_story_row_index, 2).value], random_story_row_index
    except ValueError:
        print("There's some problem with story no. {0}. Please check the file for any problem."
              .format(random_story_row_index))
        return -1


def play_game():
    get_story_response = get_story()
    if get_story_response != -1:
        story_index_in_file = -1
        try:
            story_template = str(get_story_response[0][0])
            blank_hints = str(get_story_response[0][1]).split(";")
            story_index_in_file = get_story_response[1]
            blank_values = []
            print("Input according to respective instructions: (Have fun with utterly nonsensical words!)")
            for hint in blank_hints:
                hint.strip()
                blank_values.append(nimesh_app_basics.get_non_empty_string_input(hint + " : ", "Need a word!"))

            nimesh_app_basics.clear_screen()
            nimesh_app_basics.print_welcome_message(app_name)

            print(story_template.format(*blank_values) + "\n")
        except IndexError:
            if story_index_in_file != -1:
                print("A problem occurred. Please check the blank hints in file for story no. {0}.".format(story_index_in_file))


# ------------------ Main program ------------------ #
app_name = "Mad Libs"

while True:
    nimesh_app_basics.clear_screen()
    nimesh_app_basics.print_welcome_message(app_name)
    play_game()
    play_again_boolean = nimesh_app_basics.get_valid_y_n_opinion("Play again? ( y / n ): ")
    if play_again_boolean:
        continue
    else:
        break

nimesh_app_basics.print_exit_message(app_name)