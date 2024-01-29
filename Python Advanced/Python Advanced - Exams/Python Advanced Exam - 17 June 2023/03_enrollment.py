def gather_credits(credits_needed, *args):
    collected_credits = 0
    result = []
    for course_name, course_credits in args:
        if course_name in result:
            continue

        if credits_needed > collected_credits:
            collected_credits += course_credits
            result.append(course_name)
        else:
            break

    if credits_needed > collected_credits:
        return (f"You need to enroll in more courses! You have to gather"
                f" {credits_needed - collected_credits} credits more.")

    else:
        output = sorted(result)
        return (f"Enrollment finished! Maximum credits: {collected_credits}."
                f"\nCourses: {', '.join([x for x in output])}")
