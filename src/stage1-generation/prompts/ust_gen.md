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

<!-- Example
Proceed with prompt UST generate .mm file(remember to code block) inline using the mindmap template provided for the following structure:
Discipline: Film
Structure: Freytag’s Pyramid
Levels: Beginner
Stages:Full canonical or classical stage sequence of the structure

Generate 3 consecutive stages at a time. Continue batching by 3 until all stages for that level are complete. Stop automatically once the last stage is reached. -->



