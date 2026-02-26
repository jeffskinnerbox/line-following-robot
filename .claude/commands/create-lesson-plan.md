# Create a Lesson Plan

## Step 1 — Load the Skill
Read the file at `.claude/skills/lesson-plan-generator.md` in full before proceeding.
Follow all instructions and formatting rules defined there.

## Step 2 — Load the Specification File (if provided)
The user may have passed a specification file as an argument: **$ARGUMENTS**

- If `$ARGUMENTS` is not empty, read that file now and extract everything useful:
  course name, lesson topic, session duration, target audience, learning objectives,
  aligned syllabus section, available materials, instructor notes, or any other
  relevant details. Treat this file as the authoritative starting point.
- If `$ARGUMENTS` is empty, skip this step and proceed with no pre-loaded context.

## Step 3 — Load the Syllabus (if referenced)
If the spec file or the user references a syllabus file, read that file now so the
lesson plan can be properly aligned to it — matching the correct unit, week, learning
outcomes, and vocabulary established in the syllabus.

## Step 4 — Identify Gaps & Ask Only What You Still Need
Based on what you learned from the spec file and syllabus (or nothing, if neither was
provided), determine which of the following are still unknown or unclear. Ask **only**
the questions that remain unanswered — do not ask for information already present in
the spec file or syllabus. Ask all remaining questions at once, not one at a time.

Questions to consider (ask only if unanswered):

1. **What is the lesson topic?** What specific concept, skill, or subject will this lesson cover?
2. **What course or syllabus does this lesson belong to?** Which unit or week does it fall in?
3. **Who is the audience?** (age range, grade level, or experience level of students)
4. **How long is the session?** (e.g., 45 minutes, 90 minutes, 2 hours)
5. **What are the learning objectives?** What should students know or be able to do by the end? (If not provided, Claude should infer from the syllabus and topic.)
6. **What materials, tools, or equipment are available?** (e.g., projector, whiteboards, kits, laptops, handouts)
7. **What teaching methods or activities are preferred?** (e.g., lecture, hands-on, discussion, demo, group work, Q&A)
8. **Are there any topics, activities, or formats to avoid?**
9. **Are there interesting tangents, stories, or "wow" moments the instructor wants to include?**
10. **What prerequisite knowledge should students already have coming into this lesson?**
11. **How will understanding be assessed during or at the end of the session?** (e.g., quiz, exit ticket, project check-in, discussion, observation)

If the spec file and syllabus answered everything, skip this step entirely and move to Step 5.

## Step 5 — Generate & Save the Lesson Plan
Using the skill's formatting rules, the spec file content, the aligned syllabus, and
any answers gathered above, generate the complete lesson plan.

The plan must include ALL of the following sections (as defined by the skill file),
tailored to the session type and audience:

- **Lesson header** — course, unit, lesson number, topic, date, duration, instructor
- **Learning objectives** — specific, measurable outcomes aligned to the syllabus
- **Prerequisites** — what students need to know coming in
- **Materials & preparation** — everything the instructor needs to have ready before class
- **Session plan with timing** — a minute-by-minute or block-by-block breakdown of the full session, including:
  - Opening / hook (grab attention, connect to prior knowledge)
  - Instruction / content delivery blocks
  - Activities, demos, or exercises (with time estimates)
  - Discussion questions or prompts
  - Breaks (if applicable)
  - Closing / wrap-up and preview of next session
- **Instructor notes** — teaching tips, common misconceptions to address, pacing advice, differentiation strategies for different learner levels
- **Interesting tangents & enrichment** — optional deeper dives, fun facts, real-world connections, or stories the instructor can use if time allows or to spark curiosity
- **Assessment / check for understanding** — how to gauge whether students got it
- **Homework or follow-up** (if applicable)

Save the lesson plan as `lesson-plan-[topic-slug].md` in the current directory.

## Step 6 — Confirm
Tell the user:
- The filename where the lesson plan was saved
- A 2–3 sentence summary of the lesson
- Any assumptions made that were not explicitly stated in the spec file, syllabus, or answers
