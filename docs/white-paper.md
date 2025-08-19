# UST: This One Framework Could Change How We Think Forever  

**Author:** L. M. Peter Chung  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16898898.svg)](https://doi.org/10.5281/zenodo.16898898)  
**Version:** 0.1.0  
**Date:** 2025-08-20  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)


## Abstract

The Universal Structure Toolkit (UST) reimagines essay instruction as an adaptive, generative process that unites **narrative thinking** with **cross disciplinary reasoning**. Built on 12 film based narrative structures and expanded to 22 discipline specific models (34 structures total), UST provides a framework where **thinking drives writing**, transforming it from a static form into a **dynamic architecture for inquiry**.

By combining structured prompts, conceptual tagging and automated question generation UST offers a scalable solution for developing **critical thinking, reasoning skills and creative fluency**. This approach transforms writing education from formula driven instruction to an integrated exploratory practice that prepares students for complex interdisciplinary problem solving in academia and beyond. 

Each UST question serves not only as a structured essay prompt but also as a **flexible stem** that can be reframed for any context. Enabling learners to apply **critical thinking first** and then translate insights into written expression.


---

## A. Introduction: Motivation and Problem

Writing is one of the most powerful tools for learning and communication, yet traditional instruction often reduces it to formulaic templates that fail to cultivate **deep reasoning**. Students may master surface level structures like the five paragraph essay, but these rigid forms rarely equip them to **think critically across disciplines or engage in complex problem solving**. The result: writing that meets academic norms but lacks originality, critical depth and rhetorical insight.

Meanwhile, generative AI offers opportunities to scaffold learning, but without structured guidance it often produces shallow unfocused text. What is missing is a framework that teaches **thinking before writing** that connects **narrative principles, discipline specific reasoning and exploratory inquiry**.

The Universal Structure Toolkit (UST) was created to fill this gap. By encoding expert thinking patterns into **structure based prompts** UST transforms the way students approach essays not as rigid templates, but as **thinking driven architectures for meaning making**.

Rooted in narrative principles and expanded across 34 structures in 22 disciplines, the system enables learners to:

- **Develop transferable reasoning skills** through familiar patterns like narrative arcs and argument models.  
- **Use generative AI responsibly** within a guided framework that emphasizes critical analysis first.  
- **Move from mechanical compliance to exploratory practice**, making writing a reflection of structured thought rather than rote production.  

In short, UST addresses a fundamental challenge in education: how to make **critical thinking, reasoning and writing instruction converge** that prepares learners for the future of interdisciplinary scholarship and AI enhanced learning.


---

## B. Conceptual Framework

The foundation of UST lies in the recognition that **narrative structure** and **cross disciplinary reasoning**, rather than content alone, shape how humans reason, explain and persuade. UST integrates insights from multiple domains to create a unified pedagogical system, drawing on:

- **12 canonical film structures** (e.g., Three Act, Dan Harmon's Story Circle, Save the Cat)
- **22 structures across disciplines** (e.g., scientific method, Design Thinking, IRAC Method and Clinical Reasoning Model)
- **Structured prompt formats** designed to elicit distinct cognitive modes and levels of inquiry

Each structure is decomposed into:

- **Discipline origin of structure**: Film
- **Structure name**: Three-Act 
- **Structure process**: 1. Setup → 2. Confrontation → 3. Resolution
- **Examples**: The King's Speech, The Social Network, Erin Brockovich
- **Terminology**: 1. Setup → Introduction / Background / Context, 2. Confrontation → Conflict / Rising Action / Turning Point, 3. Resolution → Climax / Denouement / Outcome
- **Level Of Inquiry**: Beginner
- **Structure Part**: 1. Setup
- **Structure Part Concept**: Framing 
- **Question id**: Three-Act.B.1.2 
- **Question**: What kind of world or situation does the story begin in?
- **Concept of question**: Framing
 
By organizing inquiry through structure and tagging, UST enables students to engage with unfamiliar ideas using familiar patterns and allows AI to assist more meaningfully in the learning process.


---

## C. Technical Implementation

The MVP (Minimum Viable Product) was developed using:

- **Freeplane**: Mind-mapping interface for visualizing and editing narrative structure trees.
- **Markdown (.md)**: For export to **Obsidian**, enabling local linked thinking via backlinks and directories.
- **Custom Python Scripts**: For parsing `.mm` files, transforming them into structured JSON and generating markdown files per question.

### File Structure

Each structure follows a directory layout such as:

/Three-Act/Three-Act.md 
/Three-Act/Beginner/[1-3]_1_Setup/Three-Act-B-[1-3]_1_Setup.md
/Three-Act/Beginner/[1-3]_1_Setup/What details are used to establish the setting and mood of the opening?.md

Each `question.md` file includes:

- Question ID
- Link to concept of question
- Link to structure part associated with the question
- Level of inquiry
- Link to structure
- Discipline name

## Data Versions: Raw and Clean Outputs

The Universal Structure Toolkit workflow produces two main data artifact versions during processing:

- **Raw Version**:  
  Generated from `.mm` Freeplane mind maps. Contains all original nodes including placeholders, inconsistencies and occasional off list tags. Reflects initial AI generated outputs without manual correction or cleanup.

- **Clean Version**:  
  Curated and refined version where incorrect concept tags are corrected.

### Purpose and Benefits of Maintaining Both Versions

- **Benchmarking**: The clean version serves as a quality benchmark to assess the effectiveness and reliability of the automated pipeline against noisy raw data.  
- **Transparency**: Documenting raw data preserves the full AI classification context, supporting auditability and troubleshooting.  
- **Iterative Improvement**: Comparison facilitates iterative prompt engineering and script refinement to reduce errors and boost output consistency.  
- **User Choice**: Educators or researchers can select the version best suited for their workflows: raw for exploration and experimentation, clean for practical application.

### File Outputs for Both Versions

- Raw and clean JSON exports (from `.mm` mindmaps)  
- Raw and clean sets of `.md` question files with corresponding indexes  


---

## D. Usability in Real Workflows

The system was built with practical use in mind:

- **Obsidian Integration**: Markdown files are vault compatible; Obsidian parses the full directory structure for search, backlinks and tagging.
- **Question Indexing**: Each structure and structure part has its own index and each concept has backlinks from all questions using it.
- **Cross Disciplinary View**: Questions can be filtered by concept across structures, enabling meta-thinking.

### File Outputs

- One `index.md` for all structures by discipline
- One `index.md` for all structures
- One `question?.md` file per question
- One `index.md` per structure
- One `index.md` per structure part


---

## E. Prompt Engineering and Output Correction

### E.1. Issues Encountered

- **Concept Inference vs. Classification**: Early prompts used `<concept:Infer>` instead of enforcing a defined set, resulting in inconsistency.
- **Off list Tags**: Some AI outputs introduced novel or adjacent concepts.
- **Incorrect Part Tagging**: Structure parts were sometimes skipped or misclassified.

### E.2. Correction Strategies

- **Prompt Updates**: Enforced a strict [concept list](/docs/concept_list.xlsx) and reframed prompts to require selection, not generation.
- **Validation Scripts**: Python scripts flagged all non listed concept tags and allowed mapping to closest valid concept.
- **Output Filtering**: The `.mm` parser ignored `ID`, `CREATED` and `MODIFIED` metadata for clarity of JSON output.

### E.3. Lessons Learned

- AI classification tasks require **tight constraints** to perform consistently.
- Output consistency improves with:
  - Repeated examples
  - Simplified formats
  - Strong validation logic
- Scripted automation alone isn’t sufficient; **human in the loop** curation remains key.


---

## F. Significance and Impact

The Universal Structure Toolkit is more than a technical solution; it addresses pressing challenges in education. Traditional writing pedagogy struggles to keep pace with a world that values **interdisciplinary thinking, adaptive problem solving and cognitive flexibility**. UST responds to these challenges by:

- **Reimagining Writing as the Output of Thinking**: Essays become a tool for structured exploration, synthesis and reasoning not an end in themselves.

- **Bridging Human and Machine Intelligence**: Structured prompts guide responsible AI use, ensuring technology enhances **thinking processes** rather than replacing them.

- **Scaling Deep Learning Across Disciplines**: A framework that applies across humanities, sciences and professional domains while maintaining intellectual rigor.

- **Promoting Transferable Reasoning Skills**: Builds awareness of structural thinking applicable in multiple contexts.  

- **Flexible Critical Thinking**: Reframing questions transforms prompts into scaffolds for reasoning allowing learners to analyze, synthesize and reason independently before writing.  

By uniting **narrative design, discipline-specific reasoning and AI assisted workflows** into a cohesive framework. UST positions **thinking at the forefront of learning** with writing as its natural expressive outcome.


---

## Conclusion

The Universal Structure Toolkit represents a paradigm shift in education. By integrating **film based narrative structures, discipline specific frameworks and generative AI**, UST reframes essay writing as a **thinking driven, inquiry led process** rather than a formula to memorize.

This approach moves education beyond static templates, enabling learners to:

- **Think structurally and critically across disciplines**  
- **Analyze, synthesize and reason before writing**
- **Express insights purposefully and adaptively**  

Through scaffolded prompts, conceptual tagging and AI assisted workflows UST provides an **adaptable, future ready framework** for learning. Its influence extends beyond the classroom preparing students for academic, professional and creative challenges where **structured thinking and meaningful expression converge**.

In a world of abundant information but scarce understanding, UST lays the foundation for an educational system that values **thinking as the primary act and writing as its structured expression**.

UST redefines learning as an **act of inquiry and structured cognition** that prepare students to **think critically and creatively** using writing as a tool to reason, explore and communicate across domains.


---

## Appendix A: [Full Structure List](/docs/structure_index.xlsx)

 **No.** | **Type**     | **Discipline**          | **Structure**                         
---------|--------------|-------------------------|---------------------------------------
 1       | Narrative    | Film                    | Three-Act Structure                   
 2       | Narrative    | Film                    | Hero's Journey                        
 3       | Narrative    | Film                    | Save The Cat Beat Sheet               
 4       | Narrative    | Film                    | Dan Harmon's Story Circle             
 5       | Narrative    | Film                    | Freytag's Pyramid                     
 6       | Narrative    | Film                    | Fichtean Curve                        
 7       | Narrative    | Film                    | In Medias Res                         
 8       | Narrative    | Film                    | Kishōtenketsu (Japanese 4-act)        
 9       | Narrative    | Film                    | Nested/Framed Narrative               
 10      | Narrative    | Film                    | Parallel Narrative                    
 11      | Narrative    | Film                    | Nonlinear Narrative                   
 12      | Narrative    | Film                    | Episodic Structure                    
 13      | Disciplinary | Science                 | Scientific Method                     
 14      | Disciplinary | Philosophy              | Socratic Method                       
 15      | Disciplinary | History                 | Historical Causation                  
 16      | Disciplinary | Psychology              | Cognitive-Behavioral Model            
 17      | Disciplinary | Design                  | Design Thinking                       
 18      | Disciplinary | Law                     | IRAC Method                           
 19      | Disciplinary | Rhetoric                | Classical Rhetoric                    
 20      | Disciplinary | Systems Theory          | Systems Thinking Loop                 
 21      | Disciplinary | Theology                | Hermeneutic Cycle                     
 22      | Disciplinary | Linguistics             | Semiotic Triangle                     
 23      | Disciplinary | Pedagogy                | Experiential Learning Cycle           
 24      | Disciplinary | Economics               | Supply-Demand Equilibrium             
 25      | Disciplinary | Political Science       | Policy Cycle                          
 26      | Disciplinary | Medicine                | Clinical Reasoning Model              
 27      | Disciplinary | Ethics                  | Moral Reasoning Model                 
 28      | Disciplinary | Artificial Intelligence | Machine Learning Loop                 
 29      | Disciplinary | Project Management      | Agile Sprint Cycle                    
 30      | Disciplinary | Conflict Resolution     | Interest-Based Negotiation            
 31      | Disciplinary | Art & Aesthetics        | Creative Process                      
 32      | Disciplinary | Engineering             | Engineering Design Process            
 33      | Disciplinary | Environmental Science   | Environmental Impact Assessment (EIA) 
 34      | Disciplinary | Philosophy              | Toulmin Model                         


---

## Appendix B: [Concept Tag List](/docs/concept_list.xlsx)

| **No.** | **Type**           | **Concept**               |
|---------|--------------------|---------------------------|
| 1       | Core Structure     | Cause and Effect          |
| 2       | Core Structure     | Transformation            |
| 3       | Core Structure     | Conflict                  |
| 4       | Core Structure     | Resolution                |
| 5       | Core Structure     | Choice                    |
| 6       | Systems Logic      | Hierarchy                 |
| 7       | Systems Logic      | Feedback                  |
| 8       | Systems Logic      | Cycle                     |
| 9       | Systems Logic      | Duality                   |
| 10      | Systems Logic      | Paradox                   |
| 11      | Conceptual Tools   | Framing                   |
| 12      | Conceptual Tools   | Threshold                 |
| 13      | Conceptual Tools   | System                    |
| 14      | Conceptual Tools   | Emergence                 |
| 15      | Conceptual Tools   | Scale                     |
| 16      | Conceptual Tools   | Perspective               |
| 17      | Conceptual Tools   | Boundary                  |
| 18      | Conceptual Tools   | Iteration                 |
| 19      | Human Dynamics     | Agency                    |
| 20      | Human Dynamics     | Pattern                   |
| 21      | Human Dynamics     | Tension                   |
| 22      | Human Dynamics     | Entropy                   |
| 23      | Human Dynamics     | Intention                 |
| 24      | Human Dynamics     | Uncertainty               |
| 25      | Narrative/Affect   | Desire                    |
| 26      | Narrative/Affect   | Power                     |
| 27      | Narrative/Affect   | Ambiguity                 |
| 28      | Narrative/Affect   | Closure                   |
| 29      | Narrative/Affect   | Tone                      |
| 30      | Narrative/Affect   | Mood                      |
| 31      | Narrative/Affect   | Recognition               |
| 32      | Narrative/Affect   | Catharsis                 |
| 33      | Cognitive/Learning | Memory                    |
| 34      | Cognitive/Learning | Analogy                   |
| 35      | Cognitive/Learning | Abstraction               |
| 36      | Cognitive/Learning | Focus                     |
| 37      | Cognitive/Learning | Inversion                 |
| 38      | Cognitive/Learning | Inference                 |
| 39      | Meta/Critical      | Transformation (Cultural) |
| 40      | Meta/Critical      | Disruption                |
| 41      | Meta/Critical      | Genre                     |
| 42      | Meta/Critical      | Authorial Strategy        |
| 43      | Meta/Critical      | Metaphor                  |
| 44      | Meta/Critical      | Reflexivity               |
| 45      | Meta/Critical      | Interpretation            |
| 46      | Temporal/Forma     | Repetition                |
| 47      | Temporal/Forma     | Pacing                    |
| 48      | Temporal/Forma     | Continuity                |
| 49      | Temporal/Forma     | Discontinuity             |
| 50      | Temporal/Forma     | Accumulation              |


---

## Appendix C: Prompts for UST Generation

### Workflow Stages for UST Content Generation

The pipeline consists of four sequential stages:

- **[Stage 1](/src/stage1-generation): UST Generation** — Create initial `.mm` mind map files representing the Universal Structure Toolkit data. This stage involves extensive AI-assisted generation and careful manual curation, representing the core intellectual effort. It typically requires approximately 10 hours or more per full dataset to ensure pedagogical depth, structural accuracy and cross-disciplinary rigor.

- **[Stage 2](/src/stage2-concept-clean): Cleaning and Validation** — Optional step to produce a **clean version** by correcting concept tags.

- **[Stage 3](/src/stage3-mm-to-json): `.mm` to JSON Conversion** — Parses the mind maps into structured JSON format, used for downstream processing.

- **[Stage 4](/src/stage4-json-to-markdown): JSON to Markdown Generation** — Converts JSON into Obsidian-compatible Markdown files, including question files and indexes.

**Note:**

- If you prefer working with raw outputs (for research, debugging, or exploration), you can skip **Stage 2** and proceed directly from Stage 1 to Stage 3. Otherwise, running Stage 2 ensures a cleaner, more consistent dataset that enhances usability and presentation.

- Stages 3–4 are fully automated, lightweight and typically complete within minutes, facilitating reproducibility and enabling users to deploy the toolkit with minimal manual setup. For transparency and reproducibility, the full pipeline and source files are included with this release, allowing users to regenerate or extend the toolkit. However, Stage 1 remains the most time-intensive component and thus is the primary intellectual contribution.


---

## [Stage 1](/src/stage1-generation): Generate Structure in .mm format

**Purpose:**

This prompt sequence generates essay questions for any selected narrative or disciplinary structure in staged outputs. It supports four learning levels (Beginner, Intermediate, Advanced and Meta/Expert) and maintains consistent tagging for question IDs and concepts.

---

### [Prompt Template](/src/stage1-generation/prompts/ust_gen.md)

```
**Prompt:UST Inline Only (Universal, Cross-Disciplinary):**

Design generative essay and thinking questions based on major structural models from across disciplines (e.g., science, history, philosophy, systems theory, rhetoric, psychology).
For each structure, generate pedagogical questions for each of its stages/parts across four levels of learning: **Beginner, Intermediate, Advanced, Meta/Expert**.

Always generate the full canonical or classical stage sequence of the structure, preserving all standard parts as recognized in authoritative sources. Do not summarize or reduce the number of stages; instead, use the most detailed, complete pattern available for each structure.

For example, for the Hero’s Journey, include all 12 classic stages from Ordinary World through Return with the Elixir, labeling each stage clearly and assigning questions accordingly.

* For each structure part (e.g., Step, Phase, Principle, Operation):

  * Include:

    * Generate **at least 12 questions minimum**.

      * Distribute questions as follows:

        * **Structural questions:** Approximately 60–70% of total questions (i.e., at least 7–9 questions) focused on core understanding, basic concepts and functions.

        * **Extension questions:** Approximately 25–30% of total questions (i.e., at least 3–4 questions) focused on application, synthesis, or transformation of the concepts.

        * **Emotional tone, audience effect, or authorial/disciplinary intent questions:** 1–2 questions per structure part, focusing on affective, rhetorical, or interpretive dimensions.

* For each question node, assign a `<question_id:...>` tag using the format:

 `<question_id:<structure_name>.<level_code>.<structure_part_number>.<question_number>>`

 * `<structure_name>`: Use the short name of the structure (e.g., "Three Act" Replace spaces with - to get "Three-Act", "Hero's Journey" Remove apostrophe and spaces to get "Heros-Journey","Save The Cat Beat Sheet" Replace spaces with "-" to get "Save-The-Cat-Beat-Sheet").
 * `<level_code>`: Use `B` for Beginner, `I` for Intermediate, `A` for Advanced and `ME` for Meta/Expert.
 * `<structure_part_number>`: Number each structure part sequentially starting from 1.
 * `<question_number>`: Number each question within its structure part starting from 1. Reset the count for each new structure part.

 Example output: `<question_id:Three-Act.B.1.9>`

* Text formatting rule:

 Inside `<question:...>` and `<structure_part:...>` tags:
 * Do not use ampersands (`&`) in any part of the `<question:...>` or `<concept:...` content.
 * Replace all `&` with the word `"and"` (e.g., "risks and benefits" instead of "risks & benefits").


* *All questions must:*

  * Be **pedagogical**, intuitive and practical
  * Be accessible across disciplines (not limited to field-specific jargon)
  * Be suitable for Freeplane `.mm` output (inline formatting only)

  * Use a variety of question stems, including: What, How, Why, What if, So what, What next.
  * Each structure part must include at least four different stems, but only use a stem when it is grammatically and contextually appropriate.
  * Avoid overusing "What" when "How" or "Why" would create a more insightful or dynamic question.
  * If a "What" question is the most natural choice, it may remain, but strive for a diverse, meaningful mix of stems across the entire structure.

  * Be regenerative: support multiple interpretations or argument pathways.
  * Avoid redundancy between levels: each level must increase in depth/complexity.
  * Be a high-leverage writing prompt: usable for developing paragraphs in essays.
  * Be diagnostically useful: reveal student understanding of structure.
  * Each question must focus on the most essential elements of that structure part — prioritize clarity, conceptual leverage and usefulness in analysis or writing. 

  * **Meet core intellectual standards of good critical thinking**:

    * **Clarity**
    * **Accuracy**
    * **Relevance**
    * **Precision**
    * **Logical coherence**
    * **Depth**
    * **Fairness**
    * **Significance**

* Output in **.mm (Freeplane) mind map format**, inline only, with clean hierarchy.

  * Use pedagogically framed questions such as:

    * “Who is the hero?”
    * “What starts the story?”
    * “How does the conflict change things?”
    * “Why does the ending matter?”
    * “What if the resolution was different?”

  * Classification task — not inference: After generating the structure part and question think longer to classify each structure part and each question using one of the concepts from concept_list.
  
  <concept:...> tag rules:

  * Tag each structure part and each question exactly one <concept:...> tag corresponding to a single concept from concept_list. 
  * Do not include concept group names as concepts.
  * Do not include multiple concepts per tag.
  * Carefully choose the concept most relevant to the structure part focus, strictly matching the naming and spelling in the concept_list.
  * Carefully choose the concept most relevant to the question’s focus, strictly matching the naming and spelling in the concept_list.
  *  Do not invent new concepts.
  *  Do not any concepts outside concept_list.
  *  Always select one concept from concept_list — even if the fit is weak.
  * If a structure part or question concept is not in the concept_list then label concept as unknown.
    
  <concept:...> tag format rules:
   *  Do not include numbering index for a concept in concept_list for example "1.1.1 Cause and Effect" output "Cause and Effect".

  * concept_list rules:
    * concept_list is final and non-negotiable. Do not “improve” the concept names.
    * No additions to concept_list – Pure 50-concept enforcement.
    * Do not paraphrase or rename concepts  
    * concept group names are [1.1 Core_Structure,1.2 Systems_Logic,1.3 Conceptual_Tools,1.4 Human_Dynamics,1.5 Narrative_Affect,1.6 Cognitive_Learning,1.7 Meta_Critical,1.8 Temporal_Forma] to help you understand concept_list.

  1 concept_list
1.1 Core_Structure
1.1.1 Cause and Effect
1.1.2 Transformation
1.1.3 Conflict
1.1.4 Resolution
1.1.5 Choice
1.2 Systems_Logic
1.2.1 Hierarchy
1.2.2 Feedback
1.2.3 Cycle
1.2.4 Duality
1.2.5 Paradox
1.3 Conceptual_Tools
1.3.1 Framing
1.3.2 Threshold
1.3.3 System
1.3.4 Emergence
1.3.5 Scale
1.3.6 Perspective
1.3.7 Boundary
1.3.8 Iteration
1.4 Human_Dynamics
1.4.1 Agency
1.4.2 Pattern
1.4.3 Tension
1.4.4 Entropy
1.4.5 Intention
1.4.6 Uncertainty
1.5 Narrative_Affect
1.5.1 Desire
1.5.2 Power
1.5.3 Ambiguity
1.5.4 Closure
1.5.5 Tone
1.5.6 Mood
1.5.7 Recognition
1.5.8 Catharsis
1.6 Cognitive_Learning
1.6.1 Memory
1.6.2 Analogy
1.6.3 Abstraction
1.6.4 Focus
1.6.5 Inversion
1.6.6 Inference
1.7 Meta_Critical
1.7.1 Transformation (Cultural)
1.7.2 Disruption
1.7.3 Genre
1.7.4 Authorial Strategy
1.7.5 Metaphor
1.7.6 Reflexivity
1.7.7 Interpretation
1.8 Temporal_Forma
1.8.1 Repetition
1.8.2 Pacing
1.8.3 Continuity
1.8.4 Discontinuity
1.8.5 Accumulation

  * Structure output in .mm XML format with clear hierarchy like this for context this template was Three-Act Structure from Film discipline.

  * Use the structure_part text exactly as defined in the <structure_parts_master> block. Always include both the fractional index and the numbered label (e.g., <structure_part:[1/3] 1. Setup>). Do not modify this formatting or rename parts. Ensure Terminology uses the same number and label as structure_part, formatted as: <terminology:1. Setup → Explain structure in a short sentence and then equivalent terms in academia>.Always Code block output.:

<map version="freeplane 1.11.5">
  <node TEXT="<discipline:Film>">
    <node TEXT="<structure_name:Three-Act>">
      <node TEXT="Structure">
        <node TEXT="<structure_process: 1. Setup → 2.Confrontation → 3. Resolution>"/>
        <node TEXT="<structure_parts_master>">
          <node TEXT="<structure_part:[1/3] 1. Setup>"/>
          <node TEXT="<structure_part:[2/3] 2. Confrontation>"/>
          <node TEXT="<structure_part:[3/3] 3. Resolution>"/>
        </node>
      </node>
      <node TEXT="Examples">
        <node TEXT="<examples:The King's Speech, The Social Network, Erin Brockovich>"/>
      </node>
      <node TEXT="Terminology">
        <node TEXT="<terminology:1. Setup → Introduction / Background / Context>"/>
        <node TEXT="<terminology:2. Confrontation → Conflict / Rising Action / Turning Point>"/>
        <node TEXT="terminology:3.Resolution → Climax / Denouement / Outcome>"/>
      </node>
      <node TEXT="Level">
        <node TEXT="<level:Beginner>">
          <node TEXT="<structure_part:[1/3] 1. Setup><part_concept:concept_list>">
            <node TEXT="<question_id:...><question:Who is the hero?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:What kind of world does the story begin in?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:What key ideas are hinted at in the opening?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:How is the protagonist first portrayed?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:What early hint of trouble or change do we see?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:What emotions might the opening evoke?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:How does the story get going?><concept:concept_list>"/>
            <node TEXT="<question_id:...><question:What point of view shapes our first impressions?><concept:concept_list>"/>
          </node>
          <node TEXT="<structure_part:[2/3] 2. Confrontation>"> … </node>
          <node TEXT="<structure_part:[3/3] 3. Resolution>"> … </node>
        </node>
        <node TEXT="<level:Intermediate>"> … </node>
        <node TEXT="<level:Advanced>"> … </node>
        <node TEXT="<level:Meta/Expert>"> … </node>
      </node>
    </node>
    <!-- Repeat structure for the other major structural models from across disciplines -->
  </node>
</map>
Proceed with prompt UST generate .mm file(remember to code block) inline using the mindmap template provided for the following structure:
Discipline: [DISCIPLINE]
Structure: [STRUCTURE_NAME]
Levels: [LEVEL]
Stages:Full canonical or classical stage sequence of the structure

Generate [X] consecutive stages at a time. Continue batching by [X] until all stages for that level are complete. Stop automatically once the last stage is reached.
```

### Prompt Template: Example

```
Proceed with prompt UST generate .mm file(remember to code block) inline using the mindmap template provided for the following structure:
Discipline: Film
Structure: Freytag’s Pyramid
Levels: Beginner
Stages:Full canonical or classical stage sequence of the structure

Generate 3 consecutive stages at a time. Continue batching by 3 until all stages for that level are complete. Stop automatically once the last stage is reached.
```

### Example Output (Partial)

```
<map version="freeplane 1.11.5">
  <node TEXT="<discipline:Film>">
    <node TEXT="<structure_name:Freytags-Pyramid>">
      <node TEXT="Structure">
        <node TEXT="<structure_process: 1. Exposition → 2. Rising Action → 3. Climax → 4. Falling Action → 5. Denouement>"/>
        <node TEXT="<structure_parts_master>">
          <node TEXT="<structure_part:[1/5] 1. Exposition>"/>
          <node TEXT="<structure_part:[2/5] 2. Rising Action>"/>
          <node TEXT="<structure_part:[3/5] 3. Climax>"/>
          <node TEXT="<structure_part:[4/5] 4. Falling Action>"/>
          <node TEXT="<structure_part:[5/5] 5. Denouement>"/>
        </node>
      </node>
      <node TEXT="Examples">
        <node TEXT="<examples:Romeo and Juliet, Macbeth, The Great Gatsby>"/>
      </node>
      <node TEXT="Terminology">
        <node TEXT="<terminology:1. Exposition → Introduction / Background / Context>"/>
        <node TEXT="<terminology:2. Rising Action → Conflict / Complication / Development>"/>
        <node TEXT="<terminology:3. Climax → Turning Point / Crisis / Peak>"/>
        <node TEXT="<terminology:4. Falling Action → Consequences / Decline>"/>
        <node TEXT="<terminology:5. Denouement → Resolution / Conclusion / Closure>"/>
      </node>
      <node TEXT="Level">
        <node TEXT="<level:Beginner>">
          <node TEXT="<structure_part:[1/5] 1. Exposition><part_concept:Framing>">
            <node TEXT="<question_id:Freytags-Pyramid.B.1.1><question:Who are the main characters introduced in the exposition?><concept:Agency>"/>
            <node TEXT="<question_id:Freytags-Pyramid.B.1.2><question:How does the exposition establish the setting of the story?><concept:Framing>"/>
          </node>
          <node TEXT="<structure_part:[2/5] 2. Rising Action><part_concept:Conflict>">
            <node TEXT="<question_id:Freytags-Pyramid.B.2.1><question:What events escalate the conflict during the rising action?><concept:Cause and Effect>"/>
            <node TEXT="<question_id:Freytags-Pyramid.B.2.2><question:How do the characters respond to increasing challenges?><concept:Agency>"/>
          </node>
          <node TEXT="<structure_part:[3/5] 3. Climax><part_concept:Turning Point>">
            <node TEXT="<question_id:Freytags-Pyramid.B.3.1><question:What event marks the climax of the story?><concept:Cause and Effect>"/>
            <node TEXT="<question_id:Freytags-Pyramid.B.3.2><question:How does the climax change the protagonist’s situation?><concept:Transformation>"/>
          </node>
        </node>
      </node>
    </node>
  </node>
</map>
```

### Staged Generation Process

After the main prompt (ust_gen.md) generates first batch of questions use this prompt to generate the rest of stages and levels. 

```
Generate stages: [X]-[Y] of [Z], level: [LEVEL] for [STRUCTURE] in the same format.
```

1. Identify the structure [STRUCTURE] and the total number of stages [Z].
2. Run the prompt for each stage range in order (e.g., `1–3`, `4–6`, `7–9`, `10–12`).

```
Generate stages: 4-5 of 5, level: Beginner for Freytag’s Pyramid in the same format.
Generate stages: 1-3 of 5, level: Intermediate for Freytag’s Pyramid in the same format.
Generate stages: 4-5 of 5, level: Intermediate for Freytag’s Pyramid in the same format.
Generate stages: 1-3 of 5, level: Advanced for Freytag’s Pyramid in the same format.
Generate stages: 4-5 of 5, level: Advanced for Freytag’s Pyramid in the same format.
Generate stages: 1-3 of 5, level: Meta/Expert for Freytag’s Pyramid in the same format.
Generate stages: 4-5 of 5, level: Meta/Expert for Freytag’s Pyramid in the same format.
```

3. Keep instructions identical between runs, only replacing `[X]`, `[Y]` and `[LEVEL]`.
4. Merge the staged outputs to form the complete structure’s question set. Save each stage as .mm and then use freeplane to edit into one complete [mind map](/src/stage1-generation/mm-raw).   

### Additional instruction

If the AI generates an shorter structural process use:

```
Give Full canonical or classical stage sequence of the structure
``` 

Edit [main prompt](/src/stage1-generation/prompts/ust_gen.md) to force structure process:

```
Proceed with prompt UST generate .mm file(remember to code block) inline using the mindmap template provided for the following structure:
Discipline: Film
Structure: Freytag’s Pyramid
Levels: Beginner
Stages:Full canonical or classical stage sequence of the structure

<structure_process: 1. Exposition → 2. Rising Action → 3. Climax → 4. Falling Action → 5. Denouement>

Generate 3 consecutive stages at a time. Continue batching by 3 until all stages for that level are complete. Stop automatically once the last stage is reached.
```

The ust generation prompt was optimized (3 structure parts per message) for the free tier of chatGPT (via web browser). Paid tiers can do 6-9 structure parts per message. 

If the AI generation becomes inconsistant start a new chat or call out the wrong output.


---

## [Stage 2](/src/stage2-concept-clean): Concept Cleanup and Mapping Correction (Optional)

**Purpose:**

After initial question generation in Stage 1, Stage 2 refines the concept tags by detecting inconsistencies or invalid concepts using a [Python script](/src/stage2-concept-clean/cleanup.py) and an [AI assisted correction prompt](/src/stage2-concept-clean/prompts/concept_map.md). This ensures all concepts align with the approved [concept list](/docs/concept_list.xlsx) taxonomy, improving tagging accuracy and downstream usability.

---

### Workflow

1. **Detect invalid concepts**

Run the Python script which will scan concepts in the generated [`.mm` file](/src/stage2-concept-clean/mm-raw). It will log any concepts not found in the official [concept list](/docs/concept_list.xlsx) and remap existing un-official concepts.

```
$python cleanup.py
``` 

[Python script](/src/stage2-concept-clean/cleanup.py)

```
import re
import os

# === CONFIGURATION ===

# Valid 50-concept tags for structure parts and questions
concept_list = {
    "Cause and Effect","Transformation","Conflict","Resolution","Choice","Hierarchy","Feedback","Cycle","Duality","Paradox","Framing","Threshold","System","Emergence","Scale","Perspective","Boundary","Iteration","Agency","Pattern","Tension","Entropy","Intention","Uncertainty","Desire","Power","Ambiguity","Closure","Tone","Mood","Recognition","Catharsis","Memory","Analogy","Abstraction","Focus","Inversion","Inference","Transformation (Cultural)","Disruption","Genre","Authorial Strategy","Metaphor","Reflexivity","Interpretation","Repetition","Pacing","Continuity","Discontinuity","Accumulation"
}

# Mapping of incorrect → correct for <concept:...>
concept_fix_map = {
  "Foreshadowing": "Framing",
  "Significance": "Inference",
  "Leadership": "Inversion"
}

clean_count = 0

def cleanup(mm_filename,mm_clean_filename):
    global concept_list
    global concept_fix_map
    global clean_count

    # === LOAD FILE ===
    with open(mm_filename, "r", encoding="utf-8") as f:
    # with open("Structure.mm", "r", encoding="utf-8") as f:
        content = f.read()

    # === CHECK CONCEPT_FIX_MAP FOR BAD CONCEPTS===
    concept_list_map = {
        "Cause and Effect": "","Transformation": "","Conflict": "","Resolution": "","Choice": "","Hierarchy": "","Feedback": "","Cycle": "","Duality": "","Paradox": "","Framing": "","Threshold": "","System": "","Emergence": "","Scale": "","Perspective": "","Boundary": "","Iteration": "","Agency": "","Pattern": "","Tension": "","Entropy": "","Intention": "","Uncertainty": "","Desire": "","Power": "","Ambiguity": "","Closure": "","Tone": "","Mood": "","Recognition": "","Catharsis": "","Memory": "","Analogy": "","Abstraction": "","Focus": "","Inversion": "","Inference": "","Transformation (Cultural)": "","Disruption": "","Genre": "","Authorial Strategy": "","Metaphor": "","Reflexivity": "","Interpretation": "","Repetition": "","Pacing": "","Continuity": "","Discontinuity": "","Accumulation": ""
    }

    for c in concept_fix_map:
        correctConcept = concept_fix_map.get(c)
        if correctConcept not in concept_list_map:
            print("Bad concept in fix map:"+c +" , "+correctConcept)

    # === CONCEPT CLEANUP ===

    # Extract and replace <concept:...>
    concept_pattern = r"&lt;concept:([^&]+)&gt;"
    all_concepts = set(re.findall(concept_pattern, content))
    bad_concepts = [c for c in all_concepts if c not in concept_list]

    print("❌ Invalid <concept:...> tags found:")
    for c in bad_concepts:

        valid_concept = concept_fix_map.get(c)
        if valid_concept is None:
            print("Review: \"" + c + "\": \"concept_list\",")
        else:
            content = re.sub(
                fr"&lt;concept:{re.escape(c)}&gt;",
                f"&lt;concept:{valid_concept}&gt;",
                content)
            print("Fixed: "+ c +" → " + valid_concept)

    # === PART_CONCEPT CLEANUP ===

    # Extract and replace <part_concept:...>
    part_concept_pattern = r"&lt;part_concept:([^&]+)&gt;"
    all_part_concepts = set(re.findall(part_concept_pattern, content))
    bad_part_concepts = [c for c in all_part_concepts if c not in concept_list]

    print("\n❌ Invalid <part_concept:...> tags found:")
    for c in bad_part_concepts:

        valid_concept = concept_fix_map.get(c)  # default fallback
        if valid_concept is None:
            print("Review: \"" + c + "\": \"concept_list\",")
        else:
            content = re.sub(
                fr"&lt;part_concept:{re.escape(c)}&gt;",
                f"&lt;part_concept:{valid_concept}&gt;",
                content)
            print("Fixed: " + c + " → " + valid_concept)

    # === SAVE FILE ===

    output_file = mm_clean_filename

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    clean_count += 1
    print(f"\n✅ [{clean_count}] Clean: {mm_filename} -> {output_file}")

def natural_sort_key(s):
    """Sort like macOS Finder: split text and numbers."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def process_directory(input_dir, output_dir):
    """Process all .mm files in a directory."""
    os.makedirs(output_dir, exist_ok=True)

    for filename in sorted(os.listdir(input_dir), key=natural_sort_key):
        if filename.lower().endswith(".mm"):
            cleanFileName = filename.replace("R.mm","C.mm")
            cleanFilePath = f"{output_dir}/{cleanFileName}"
            cleanup(f"{input_dir}/{filename}", cleanFilePath)

if __name__ == "__main__":
    input_directory = "mm-raw"
    output_directory = "mm-clean"
    process_directory(input_directory, output_directory)
```

### Example Output

```
❌ Invalid <concept:...> tags found:
Review: "Expectation": "concept_list",
Fixed: Foreshadowing → Framing
Review: "Integration": "concept_list",

❌ Invalid <part_concept:...> tags found:
Review: "Turning Point": "concept_list",

✅ Cleaned file written to: 5_Freytag_Clean.mm
```

2. **Generate AI correction prompt**

Append the list of invalid concepts to [map concept prompt](/src/stage2-concept-clean/prompts/concept_map.md), which matches each invalid concept to the closest valid concept in [concept list](/docs/concept_list.xlsx).

[Map concept prompt](/src/stage2-concept-clean/prompts/concept_map.md)

```
Goal: For every bad_concept in INPUT for example '"Foreshadowing": "similar_concept_from_concept_list",' Replace similar_concept_from_concept_list with the closest matching concept from concept_list. 

No additions to concept_list – Pure 50-concept enforcement. 

OUTPUT is the same format as INPUT:

"bad_concept": "closest matching concept from similar_concept_from_concept_list that matches bad_concept"

concept_list = {
    "Cause and Effect","Transformation","Conflict","Resolution","Choice","Hierarchy","Feedback","Cycle","Duality","Paradox","Framing","Threshold","System","Emergence","Scale","Perspective","Boundary","Iteration","Agency","Pattern","Tension","Entropy","Intention","Uncertainty","Desire","Power","Ambiguity","Closure","Tone","Mood","Recognition","Catharsis","Memory","Analogy","Abstraction","Focus","Inversion","Inference","Transformation (Cultural)","Disruption","Genre","Authorial Strategy","Metaphor","Reflexivity","Interpretation","Repetition","Pacing","Continuity","Discontinuity","Accumulation"
}

INPUT:
"Foreshadowing": "similar_concept_from_concept_list",
"Significance": "similar_concept_from_concept_list",
"Leadership": "similar_concept_from_concept_list"
```

Add invalid concepts that has the word 'Review' from cleanup.py output below

```
INPUT:
```   

### Example

``` 
INPUT:
"Expectation": "concept_list",
"Integration": "concept_list",
"Turning Point": "concept_list"
```

Submit complete prompt to the AI to produce a concept mapping (e.g., `"BadConcept": "ClosestValidConcept"`).

### Output from AI

```
"Expectation": "Repetition",
"Integration": "Iteration",
"Turning Point": "Tension"
```

3. **Update concept mappings in script**

Incorporate the AI’s suggested mappings into the [Python script](/src/stage2-concept-clean/cleanup.py) inside dict variable: concept_fix_map

```
concept_fix_map = {
  "Expectation": "Repetition",
  "Integration": "Iteration",
  "Turning Point": "Tension",
}
```

4. **Clean the `.mm` file**

Execute the [Python script](/src/stage2-concept-clean/cleanup.py) to clean concepts in mind map file

```
$python cleanup.py
```

The script uses this updated mapping to replace invalid concepts with valid ones, producing a [cleaned `.mm` file](/src/stage2-concept-clean/mm-clean) ready for final use.


---

## [Stage 3](/src/stage3-mm-to-json): Convert `.mm` File to JSON Format

**Purpose:**  
Stage 3 transforms the Universal Structure Toolkit (UST) mind map (`.mm` file) into a structured JSON format suitable for programmatic use, data analysis or integration with other tools.

---

### Workflow

1. **Run the conversion script**  

Python script supports one structure per mind map file.

```
$python mm_to_json.py --version ["raw","clean"]
```

**[MM to JSON script](/src/stage3-mm-to-json/mm_to_json.py)** 

```
import xml.etree.ElementTree as ET
import json
import re
import os
import argparse

convert_count = 0

def extract_metadata(text):
    """Extract structured metadata (tags like <key:value>) from node TEXT."""
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    tags = {}
    matches = re.findall(r"<([^:>]+):([^>]+)>", text)
    for key, value in matches:
        tags[key] = value
    clean_text = re.sub(r"<[^:>]+:[^>]+>", "", text).strip()
    return clean_text, tags

def parse_node_clean(xml_node):
    """Recursively convert an XML Freeplane node to structured JSON, omitting system attributes."""
    node_data = {}
    raw_text = xml_node.attrib.get("TEXT", "")
    clean_text, metadata = extract_metadata(raw_text)

    if clean_text:
        node_data["text"] = clean_text
    node_data.update(metadata)

    children = [parse_node_clean(child) for child in xml_node.findall("node")]
    if children:
        node_data["children"] = children

    return node_data

def mm_to_json(mm_file, json_file, mm_folder_path, json_folder_path):
    global convert_count
    """Convert .mm Freeplane file to JSON."""
    tree = ET.parse(mm_folder_path + "/" + mm_file)
    root = tree.getroot()
    first_node = root.find("node")
    if first_node is None:
        raise ValueError("No <node> element found in the .mm file.")
    clean_json = parse_node_clean(first_node)

    os.makedirs(json_folder_path, exist_ok=True)
    with open(json_folder_path +"/" + json_file, "w", encoding="utf-8") as f:
        json.dump(clean_json, f, indent=2, ensure_ascii=False)
    convert_count += 1
    print(f"[{convert_count}] Convert: {mm_file} -> {json_file}")

def natural_sort_key(s):
    """Sort like macOS Finder: split text and numbers."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def ust_json(mm_folder_path,json_folder_path):
    for filename in sorted(os.listdir(mm_folder_path), key=natural_sort_key):
        if filename.endswith(".mm"):
            mm_file = filename
            json_file = filename.replace(".mm",".json")
            mm_to_json(mm_file,json_file,mm_folder_path,json_folder_path)

def run_pipeline(versionIs):
    if (versionIs == "raw"):
        ust_json("mm-raw","json-raw")
    elif (versionIs == "clean"):
        ust_json("mm-clean","json-clean")

def main():
    parser = argparse.ArgumentParser(description="Run UST pipeline with version and platform options.")

    parser.add_argument(
        "--version",
        required=True,
        choices=["clean", "raw"],
        help="Choose pipeline version: clean or raw."
    )

    args = parser.parse_args()
    print(f"Running version: {args.version}")
    run_pipeline(args.version)
   
if __name__ == "__main__":
    main()
```

2. **Output** 

The script produces a JSON file: [json-raw](/src/stage3-mm-to-json/json-raw) & [json-clean](/src/stage3-mm-to-json/mm-clean) representing the hierarchical question structure and metadata extracted from the .mm file.  


---

## [Stage 4](/src/stage4-json-to-markdown): Convert JSON to Obsidian Markdown

**Purpose:**
  
Stage 4 converts the structured JSON question data: [json-raw](/src/stage4-json-to-markdown/json-raw) & [json-clean](/src/stage4-json-to-markdown/json-clean) generated in Stage 3 into Obsidian-friendly Markdown files, enabling seamless use within the Obsidian note-taking environment.

---

### Workflow

1. **Run the Markdown script**  

```
$python markdown.py --version ["raw","clean"] --platform ["unix","win"]
```

**[JSON to Markdown script](/src/stage4-json-to-markdown/markdown.py)**

```
import os
import json
import re
import platform
import urllib.parse
import argparse

concept_list = [
    "Cause and Effect","Transformation","Conflict","Resolution","Choice","Hierarchy",
    "Feedback","Cycle","Duality","Paradox","Framing","Threshold","System","Emergence",
    "Scale","Perspective","Boundary","Iteration","Agency","Pattern","Tension","Entropy",
    "Intention","Uncertainty","Desire","Power","Ambiguity","Closure","Tone","Mood",
    "Recognition","Catharsis","Memory","Analogy","Abstraction","Focus","Inversion",
    "Inference","Transformation (Cultural)","Disruption","Genre","Authorial Strategy",
    "Metaphor","Reflexivity","Interpretation","Repetition","Pacing","Continuity",
    "Discontinuity","Accumulation"
]

concept_descriptions = {
    "Cause and Effect": "Understanding how one event leads to another.",
    "Transformation": "The process of change in form, nature, or appearance.",
    "Conflict": "A struggle or clash between opposing forces or ideas.",
    "Resolution": "The solution or conclusion of a conflict or problem.",
    "Choice": "The act of selecting among alternatives.",
    "Hierarchy": "An arrangement of elements ranked above one another.",
    "Feedback": "Information returned to control a system or process.",
    "Cycle": "A series of events that repeat in a regular sequence.",
    "Duality": "The quality of having two parts or aspects often contrasting.",
    "Paradox": "A statement or situation that contradicts itself but may be true.",
    "Framing": "The context or perspective that shapes perception.",
    "Threshold": "A point or level at which something begins or changes.",
    "System": "A set of connected parts forming a complex whole.",
    "Emergence": "New properties or behaviors arising from interactions.",
    "Scale": "The relative size or extent of something.",
    "Perspective": "A particular attitude or viewpoint.",
    "Boundary": "A limit or edge that defines an area or concept.",
    "Iteration": "Repetition of a process to approach a desired goal.",
    "Agency": "The capacity to act or make choices.",
    "Pattern": "A repeated decorative design or recurring event.",
    "Tension": "Mental or emotional strain caused by opposing forces.",
    "Entropy": "Measure of disorder or randomness in a system.",
    "Intention": "Purpose or goal behind an action.",
    "Uncertainty": "Lack of certainty or predictability.",
    "Desire": "A strong feeling of wanting something.",
    "Power": "Ability to influence or control outcomes.",
    "Ambiguity": "Uncertainty or inexactness of meaning.",
    "Closure": "Bringing a sense of conclusion or completion.",
    "Tone": "The general character or attitude of a piece.",
    "Mood": "Emotional atmosphere created for the audience.",
    "Recognition": "Identification or acknowledgment of something.",
    "Catharsis": "Emotional release or purification.",
    "Memory": "The faculty by which information is stored and recalled.",
    "Analogy": "A comparison between two things for explanation.",
    "Abstraction": "The process of removing details to focus on essentials.",
    "Focus": "Concentration on a particular object or goal.",
    "Inversion": "Reversal of the usual order or position.",
    "Inference": "A conclusion reached based on evidence and reasoning.",
    "Transformation (Cultural)": "Change in cultural norms or practices.",
    "Disruption": "Disturbance that interrupts normal flow or function.",
    "Genre": "Category of artistic composition characterized by similarities.",
    "Authorial Strategy": "Techniques used by an author to convey meaning.",
    "Metaphor": "A figure of speech that implies comparison.",
    "Reflexivity": "Awareness of the self or process in analysis.",
    "Interpretation": "The act of explaining the meaning of something.",
    "Repetition": "The action of repeating something.",
    "Pacing": "Speed at which a story or event unfolds.",
    "Continuity": "Consistency and logical connection in narrative.",
    "Discontinuity": "Break or interruption in sequence or flow.",
    "Accumulation": "Gradual gathering or increase of elements."
}

os_name = platform.system()
all_structures = set()
all_disciplines = set()
discipline_to_structures = {}
structure_info = []

def natural_sort_key(s):
    """Sort like macOS Finder: split text and numbers."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def safe_name(question):
    global os_name
    name = question.strip()
    
    if os_name == "Windows":
        # Remove invalid characters for Windows, including ?
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '*']
        for char in invalid_chars:
            name = name.replace(char, '')
    else:
        # Just remove forward slashes which are invalid on all systems
        name = name.replace('/', '-')

    return name 

def safe_filename(question):
    global os_name
    filename = question.strip()
    
    if os_name == "Windows":
        # Remove invalid characters for Windows, including ?
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        for char in invalid_chars:
            filename = filename.replace(char, '')
    else:
        # Just remove forward slashes which are invalid on all systems
        filename = filename.replace('/', '-')

    return filename + ".md"

def safe_folder_name(name):
    return name.replace("/", "-").replace(" ", "_").replace(".", "")

def write_discipline_index(discipline_to_structures, base_dir="output_md"):
    index_path = os.path.join(base_dir, "_Discipline.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(f"# Index\n\n")
        for discipline in sorted(discipline_to_structures.keys(), key=natural_sort_key):
            safe_name = safe_folder_name(discipline)
            f.write(f"- [[_{safe_name}]]\n")
    print(f"Wrote discipline index: {index_path}")

def write_discipline_notes(discipline_to_structures, base_dir="output_md"):
    for discipline, structures in discipline_to_structures.items():
        safe_name = discipline.replace(" ", "_").replace("/", "-")
        filepath = os.path.join(f"{base_dir}/{safe_folder_name(safe_name)}", f"_{safe_folder_name(safe_name)}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"All Disciplines: [[_Discipline]]\n\n## Structures\n\n")
            for struct in sorted(structures, key=natural_sort_key):
                f.write(f"- [[_{struct}]]\n")
        print(f"Wrote discipline note: {filepath}")

def write_index_file(name_set, filepath, title):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        for name in sorted(name_set, key=natural_sort_key):
            f.write(f"- [[_{name}]]\n")
    print(f"Wrote {filepath} with {len(name_set)} entries.")

def write_concept_markdown(concept_list, descriptions, output_dir):
    os.makedirs(output_dir + "/Concepts", exist_ok=True)
    for concept in concept_list:
        filename = safe_folder_name(concept) + ".md"
        filepath = os.path.join(output_dir + "/concepts", filename)

        description = descriptions.get(concept, "_No description available._")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"**Description:** {description}\n\n")
            f.write("\n---\n")
            f.write("<!-- You can add more info or queries here -->\n")

    print(f"✅ Generated {len(concept_list)} concept markdown notes in '{output_dir}'")

def natural_key(s):
    s = str(s or "")
    parts = re.split(r'(\d+)', s)
    key = []
    for p in parts:
        if p.isdigit():
            key.append(int(p))
        else:
            key.append(p.lower())
    return tuple(key)

def json_to_markdown_hierarchy(json_data, base_dir="output_md"):

    def write_question_md(discipline_name, structure_name, level, part, qID, questionIs, concepted):
        lvl = {"Beginner": "B", "Intermediate": "I", "Advanced": "A", "Meta/Expert": "ME"}

        dir_path = os.path.join(base_dir, safe_folder_name(discipline_name), safe_folder_name(structure_name), safe_folder_name(level), safe_folder_name(part))
        os.makedirs(dir_path, exist_ok=True)
        content=""
        
        qid = qID.replace(":", "-").replace(".", "-")

        filename = safe_filename(questionIs)
        filepath = os.path.join(dir_path, filename)
        conceptStr = str(concepted)
        question_text =questionIs.strip()
        shortLevel = lvl.get(level_name)

        content += f"**Question ID:** {qID}\n\n"
        content += f"**Concept:** [[{safe_folder_name(conceptStr)}]]\n\n"
        content += f"**Structure Part:** [[_{safe_folder_name(structure_name)}-{shortLevel}-{safe_folder_name(part_name)}]]\n\n"
        content += f"**Level:** {level}\n\n"
        content += f"**Structure:** [[_{structure_name}]]\n\n"
        content += f"**Discipline:** {discipline_name}\n\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
        
    def write_structure_part_index_md(discipline_name, structure_name, level_name, part_name, questions, base_dir, terminology):
        global os_name
        lvl = {"Beginner": "B", "Intermediate": "I", "Advanced": "A", "Meta/Expert": "ME"}

        dir_path = os.path.join(base_dir, safe_folder_name(discipline_name), safe_folder_name(structure_name), safe_folder_name(level_name), safe_folder_name(part_name))
        os.makedirs(dir_path, exist_ok=True)
        shortLevel = lvl.get(level_name)

        filename = f"_{safe_folder_name(structure_name)}-{shortLevel}-{safe_folder_name(part_name)}.md"
        index_path = os.path.join(dir_path, filename)

        sorted_questions = sorted(questions, key=lambda x: natural_key(x.get("qid") or x.get("question")))

        content = f"[[_{structure_name}]]\n\n"
        content += f"{terminology}\n\n"
        content += f"Questions for **{part_name}** at level **{level_name}**:\n\n"

        for qdata in sorted_questions:
            qtext = (qdata.get("question") or "").strip()
            qid_display = f" ({qdata.get('qid')})" if qdata.get("qid") else ""
            qid_display = qid_display.split('.', 1)[-1]
            qid_display = qid_display.replace(")","")
            if os_name == "Windows":
                qWin = safe_filename(qtext).replace(".md","")
                qtext = safe_name(qtext)
                content += f"- [[{qWin}|{qtext}]] {qid_display}\n"
            else:
                qtext = safe_filename(qtext).replace(".md","")
                content += f"- [[{qtext}]] {qid_display}\n"

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)    

    def write_index_md(discipline_name, structure_name, questions_index, base_dir, structure_process, terminology):
        global os_name
        dir_path = os.path.join(base_dir, safe_folder_name(discipline_name), safe_folder_name(structure_name))
        os.makedirs(dir_path, exist_ok=True)
        filepath = os.path.join(dir_path, f"_{structure_name}.md")

        
        content = f"All Disciplines: [[_Discipline]]\n"
        content += f"Discipline: [[_{safe_folder_name(discipline_name)}]]\n\n"

        
        s_process = "".join(structure_process).replace("['","").replace("']","").strip()
        content += f"{s_process}\n\n"

        for term in terminology:
            content += f"{term}\n"
        content += f"\n"

        content += f"# Index of Questions\n\n"
        
        level_order = ["Beginner", "Intermediate", "Advanced", "Meta/Expert"]
        lvl = {"Beginner": "B", "Intermediate": "I", "Advanced": "A", "Meta/Expert": "ME"}
        print(f"Structure: {structure_name}")
        print(questions_index.keys())

        for level in level_order:
            content += f"## Level: {level}\n\n"
            
            for part in sorted(questions_index[level].keys(), key=natural_sort_key):
                shortLevel = lvl.get(level)
                
                content += f"### Structure Part: [[_{safe_folder_name(structure_name)}-{shortLevel}-{safe_folder_name(part)}]]\n\n"
                
                for qdata in sorted(questions_index[level][part], key=lambda x: natural_key(x.get("qid") or x.get("question"))):
                    qtext = (qdata.get("question") or "").strip()
                    
                    filename = os.path.basename(qdata["filepath"])
                    qid_display = f" ({qdata.get('qid')})" if qdata.get("qid") else ""
                    qid_display = qid_display.split('.', 1)[-1]
                    qid_display = qid_display.replace(")","")
                    if os_name == "Windows":
                        qWin = safe_filename(qtext).replace(".md","")
                        qtext = safe_name(qtext)
                        content += f"- [[{qWin}|{qtext}]] {qid_display}\n"
                    else:
                        qtext = safe_filename(qtext).replace(".md","")
                        content += f"- [[{qtext}]] {qid_display}\n"
                content += "\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    discipline_name = json_data.get("discipline", [])

    global all_disciplines
    all_disciplines.add(discipline_name)
    print("Discipline: " + discipline_name)

    global all_structures
    global discipline_to_structures

    for discipline_node in json_data.get("children", []):
        structure_name = discipline_node.get("structure_name", "Unknown_Structure")
        print(structure_name)
        discipline_to_structures.setdefault(discipline_name, set()).add(structure_name)

        questions_index = {}

        structure_processIs = []
        structure_process = []
        examplesIs = []
        terminology = []

        structure_process_section = next((child for child in discipline_node.get("children", []) if child.get("text") == "Structure"),None)
        print(f"structure_process_section: {structure_process_section}")
        if structure_process_section:
            for structure_process_node in structure_process_section.get("children", []):
                structure_processIs = structure_process_node.get("structure_process", "Unknown_structure_process")
                print(f"structure_processIs: {structure_processIs}\n\n")
                if structure_processIs != "Unknown_structure_process":
                    structure_process.append(structure_processIs)

        examples_section = next((child for child in discipline_node.get("children", []) if child.get("text") == "Examples"),None)
        print(f"examples_section: {examples_section}")
        if examples_section:
            for examples_node in examples_section.get("children", []):
                examplesIs = examples_node.get("examples", "Unknown_Examples")
                print(f"examplesIs: {examplesIs}\n\n")
        
        terminology_section = next((child for child in discipline_node.get("children", []) if child.get("text") == "Terminology"),None)
        print(f"terminology_section: {terminology_section}")
        if terminology_section:
            for terminology_node in terminology_section.get("children", []):
                t = terminology_node.get("terminology", "Unknown_Terminology")
                print(f"terminologyIs: {t}\n\n")
                terminology.append(t)

        level_section = next((child for child in discipline_node.get("children", []) if child.get("text") == "Level"),None)

        if level_section:
            for level_node in level_section.get("children", []):
                level_name = level_node.get("level", "Unknown_Level")
                print(f"Level: {level_name}")
                questions_index.setdefault(level_name, {})
             
                for part_node in level_node.get("children", []):
                    part_name = part_node.get("structure_part", "Unknown_Part")
                    print(part_name)
                    part_concept = part_node.get("part_concept", "Unknown_Concept")
                    print(f"  Part: {part_name} — Concept: {part_concept}")
                    for question_node in part_node.get("children", []):
                        qid = question_node.get("question_id")
                        question = question_node.get("question")
                        concept = question_node.get("concept")
                        print(f"    QID: {qid}\n    Question: {question}\n    Concept: {concept}\n")
                        
                        filepath = write_question_md(discipline_name, structure_name, level_name, part_name, qid, question, concept)
                        if level_name not in questions_index:
                            questions_index[level_name] = {}

                        if part_name not in questions_index[level_name]:
                            questions_index[level_name][part_name] = []
                        
                        questions_index[level_name][part_name].append({
                            "question": question,
                            "filepath": filepath,
                            "qid": qid
                        })
            write_index_md(discipline_name, structure_name, questions_index, base_dir, structure_process, terminology)
            
            for level_name, parts_dict in questions_index.items():
                for part_name, questions_list in parts_dict.items():
                    print(f"part_name: {part_name}")

                    match = re.search(r'\[(\d+)/\d+\]', part_name)
                    part_number = ""
                    matched_terminology = ""
                    if match:
                        part_number = (match.group(1))
                        print(f"part_number: {part_number}")
                    
                    for t in terminology:
                        match = re.search(r'^(\d+)\.', (t))
                        print(f"terminology: {t}")
                        if match:
                            number = (match.group(1))
                            print(f"number: {number}")
                            if part_number == number:
                                matched_terminology = t
                    print(f"matched_terminology: {part_name} → {matched_terminology}")

                    write_structure_part_index_md(discipline_name, structure_name, level_name, part_name, questions_list, base_dir, matched_terminology)
    for structs in discipline_to_structures.values():
        all_structures.update(structs)

def ust_markdown(json_folder_path,obsidian_folder_path):
    file_count = 0
    global disciplines
    global all_structures
    global concept_list
    global concept_descriptions
    global discipline_to_structures

    for filename in sorted(os.listdir(json_folder_path), key=natural_sort_key):
        if filename.endswith(".json"):
            json_file = os.path.join(json_folder_path, filename)
            print(f"PROCESS: {filename}")
            file_count += 1
            with open(json_file, "r", encoding="utf-8") as jf:
                data = json.load(jf)
            json_to_markdown_hierarchy(data, base_dir=obsidian_folder_path)
            files_total = len(os.listdir(json_folder_path))
            content = f"COMPLETE: [{file_count}/{files_total}] {filename} -> markdown\n\n"
            print(content)
    
    write_concept_markdown(concept_list,concept_descriptions,obsidian_folder_path)
    
    write_index_file(all_structures, os.path.join(obsidian_folder_path, "_Structure.md"), "Index")
    write_discipline_notes(discipline_to_structures, obsidian_folder_path )
    write_discipline_index(discipline_to_structures, obsidian_folder_path)


def run_pipeline(versionIs, platformIs):
    global os_name
    
    if (versionIs == "raw") and (platformIs == "unix"):
        ust_markdown("json-raw","UST-Obsidian-Raw-Unix")
    
    elif (versionIs == "clean") and (platformIs == "unix"):
        ust_markdown("json-clean","UST-Obsidian-Clean-Unix")
    
    elif (versionIs == "raw") and (platformIs == "win"):
        os_name = "Windows"
        ust_markdown("json-raw","UST-Obsidian-Raw-Win")
    
    elif (versionIs == "clean") and (platformIs == "win"):
        os_name = "Windows"
        ust_markdown("json-clean","UST-Obsidian-Clean-Win")

def main():
    parser = argparse.ArgumentParser(description="Run UST pipeline with version and platform options.")

    parser.add_argument(
        "--version",
        required=True,
        choices=["clean", "raw"],
        help="Choose pipeline version: clean or raw."
    )
    parser.add_argument(
        "--platform",
        required=True,
        choices=["unix", "win"],
        help="Choose platform: unix or win."
    )

    args = parser.parse_args()
    print(f"Running version: {args.version}")
    print(f"Target platform: {args.platform}")

    run_pipeline(args.version, args.platform)

if __name__ == "__main__":
    main()
```

2. **Output**

The script generates a folder (UST-Obsidian-["Raw","Clean"]-["Unix","Win"]) containing markdown files representing the UST structures, properly formatted for use inside [Obsidian](/build/zip).

## Appendix D: Known Limitations and Future Work

While the Universal Structure Toolkit (UST) performs well for generating and organizing questions, several limitations remain:

- **No semantic validation** — Current classification focuses on structure and concept tags only, without automated checks to confirm that a question’s structural tag aligns with concrete examples (e.g., ensuring a “Resolution” question matches the closing act of a film).
- **Concept coverage gaps** — The concept list, though broad, may miss subtle rhetorical devices, interdisciplinary overlaps, or emerging narrative techniques.

### Planned Enhancements

- **Semantic validation layer** — AI-assisted checks that compare structural tags against example datasets for higher accuracy.
- **Flowise or LangChain automation** — Streamlined pipeline stages (including Raw and Clean processing) with real-time classification during content creation.
- **Concept taxonomy refinement** — Expanded list to capture edge-case rhetorical devices and interdisciplinary language.


---

## Appendix E: Software Requirements

The Universal Structure Toolkit (UST) is implemented entirely in Python and relies on a small set of third-party packages for file parsing, validation and Markdown generation. The following software components are required:

### Core Software

- **Python**: Version 3.9 or later
- **[Obsidian](https://obsidian.md/)**: For viewing and navigating generated `.md` files as a vault
- **[Freeplane](https://freeplane.org/)**: For creating and editing `.mm` mind map files