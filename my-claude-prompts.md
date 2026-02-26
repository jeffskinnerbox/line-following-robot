
# My Claude Code Prompts

## 1st Claude Code Prompt
Read @my-vision.md and create a specification document, reflecting the incrementally development in the Line Following Robot (LFR) course.
I need this this specification document to help prepare me for delivery of the course in about 6 months.
I want all the components implied bellow (both hardware and software) to be built and tested in advance of the course.

I want the software to be built in a modular form, such that, a software subsystem in step N
can be pulled out a replaced with a new subsystem in step N+1 (e.g. PID Controller replaced with Q-Learning Controller)
Make sure you include the Line Track Designer and LFR Simulators software in this specification document.
Think harder about the software architecture and testing of the of this project.

Within the specification document you create (to be called "specification.md"), include this prompt,
all question you ask me, along with my responses.
Place this in an appendix and reference it at the beginning of the development plan
and anywhere else in the text when its a useful reference.

Use the AskUserQuestions tool for all things that require further clarification.

---

Resume this session with:
claude --resume 3867ba3e-b701-4125-bb50-aa242d819955


## 2nd Claude Code Prompt
Read @my-vision.md and @specification.md and create a development plan, to be called "development-plan.md",
describing how & when thing are to be created / build.
The development plan must reflecting the incrementally build approach outline in the Line Following Robot (LFR) course.

Make sure to cover the all major software components and their build order,
key technical decisions to resolve upfront (e.g., which Python GUI library for the simulator),
a rough phasing that mirrors your courses Design Sessions,
and any external dependencies or risks (like CircuitPython library availability for the QTRX sensor).

Produce the plan as a living document it can update as the project evolves,
not just a one-time artifact.
I want it to serves as an ongoing reference rather than going stale after the first few sessions.
Given the scope of this project — firmware, a simulator, a track designer, and incremental design sessions —
I want plan to save significant back-and-forth with Claude Code over the course of development.

Within the development plan document you create (to be called "development-plan.md"), include this prompt,
all question you ask me, along with my responses.
Place this in an appendix and reference it at the beginning of the development plan
and anywhere else in the text when its a useful reference.

Think Hard about what must be done to create a robust plan.
Use the AskUserQuestions tool for all things that require further clarification.


