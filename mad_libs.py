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


get_story_response = get_story()
if get_story_response != -1:
    story_index_in_file = -1
    try:
        story_template = str(get_story_response[0][0])
        blank_hints = str(get_story_response[0][1]).replace(" ", "").split(";")
        story_index_in_file = get_story_response[1]
        print(story_index_in_file)
        blank_values = []
        print("Enter the following inputs respective to each instructions:")
        for hint in blank_hints:
            blank_values.append(input(hint + " : "))
            # TODO make a function in nimesh_app_basics input_non_empty_string
        print(story_template.format(*blank_values))
    except ValueError:
        pass
        # TODO print an error message and exit message
    except IndexError:
        if story_index_in_file != -1:
            print("A problem occurred. Please check the blank hints in file for story no. {0}.".format(story_index_in_file))
else:
    pass
    # TODO print an error message and the exit message