all_presentation = 0
counter  = 0
jury_count = int(input())
while jury_count != 'Finish':
    presentation_name = input()
    if presentation_name == 'Finish':
        print(f"Student's final assessment is {all_presentation / counter:.2f}.")
        break
    counter += 1
    average_per_presentation = 0
    total_per_presentation = 0


    for grades in range(jury_count):

        grade = float(input())
        total_per_presentation += grade
        average_per_presentation = total_per_presentation / jury_count

    all_presentation += average_per_presentation
    print(f'{presentation_name} - {average_per_presentation:.2f}.')