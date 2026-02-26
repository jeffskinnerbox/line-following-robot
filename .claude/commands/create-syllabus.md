
# Create a Course Syllabus

## Step 1 — Load the Skill
Read the file at `.claude/skills/syllabus-generator.md` in full before proceeding.
Follow all instructions and formatting rules defined there.

## Step 2 — Load the Specification File (if provided)
The user may have passed a specification file as an argument: **$ARGUMENTS**

- If `$ARGUMENTS` is not empty, read that file now and extract everything useful:
  course name, audience, duration, format, topics, goals, constraints, or any other
  relevant details. Treat this file as the authoritative starting point.
- If `$ARGUMENTS` is empty, skip this step and proceed with no pre-loaded context.

## Step 3 — Identify Gaps & Ask Only What You Still Need
Based on what you learned from the spec file (or nothing, if none was provided),
determine which of the following are still unknown or unclear. Ask **only** the
questions that remain unanswered — do not ask for information already present in
the spec file.

Questions to consider (ask only if unanswered):
1. What is the course name and subject?
2. Who is the target audience? (age range, background, experience level)
3. How long is the course? (number of weeks, sessions per week, hours per session)
4. What is the delivery format? (in-person, online, hybrid, self-paced)
5. What are the core learning outcomes or skills students should leave with?
6. Are there specific tools, technologies, or materials that must be included?
7. Are there any topics, activities, or formats that must be excluded?
8. Is there a required grading or assessment structure?
9. Any other constraints — budget, room setup, prerequisite courses, accreditation?

If the spec file answered everything, skip this step entirely and move to Step 4.

## Step 4 — Generate & Save the Syllabus
Using the skill's formatting rules, the spec file content, and any answers gathered
above, generate the complete syllabus.

Save it as `syllabus-[course-name].md` in the current directory.

## Step 5 — Confirm
Tell the user:
- The filename where the syllabus was saved
- A 2–3 sentence summary of what was generated
- Any assumptions made that were not explicitly stated in the spec file or answers
