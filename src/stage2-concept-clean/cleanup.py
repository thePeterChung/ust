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
  "Leadership": "Inversion",
  "Dual Function": "Resolution",
  "Meta_Critical": "Metaphor",
  "Leverage Points": "Uncertainty",
  "Critique": "Continuity",
  "Risk": "Catharsis",
  "Signal": "Scale",
  "Materialization": "Iteration",
  "Cognitive Learning": "Continuity",
  "Communication": "Recognition",
  "Moral Motivation": "Transformation",
  "Precision": "Tension",
  "Evaluation": "Resolution",
  "Interdisciplinarity": "Inversion",
  "Action": "Abstraction",
  "Leverage": "Emergence",
  "Resistance": "Resolution",
  "Reduction": "Resolution",
  "Embodied Cognition": "Recognition",
  "Learning": "Pacing",
  "Contrast": "Continuity",
  "Constructive Friction": "Abstraction",
  "Balance": "Scale",
  "Connection": "Intention",
  "Feedback Loop": "Feedback",
  "Depth": "Metaphor",
  "Resilience": "Resolution",
  "Holism": "Conflict",
  "Cognitive Leverage": "Recognition",
  "Character": "Choice",
  "Dialogue": "Closure",
  "Information": "Transformation",
  "Moral Character": "Authorial Strategy",
  "Listening": "Intention",
  "Pressure": "Desire",
  "Clarity": "Duality",
  "Constraint": "Continuity",
  "Divergence": "Emergence",
  "Evidence": "Emergence",
  "Moral Judgment": "Framing",
  "Relativity": "Reflexivity",
  "Negotiation": "Repetition",
  "Bounded Creativity": "Boundary",
  "Temporal Scale": "Scale",
  "Robustness": "Tone",
  "Systems_Logic": "System",
  "Verification": "Iteration",
  "Trade-off": "Paradox",
  "Credibility": "Ambiguity",
  "Materiality": "Duality",
  "Preparation": "Iteration",
  "Temporal": "Memory",
  "Discrimination": "Disruption",
  "History": "Hierarchy",
  "Emotion": "Resolution",
  "Semantics": "Iteration",
  "Cognitive_Learning": "Continuity",
  "Justice": "System",
  "Fairness": "Catharsis",
  "Contextualization": "Interpretation",
  "Critical Thinking": "Framing",
  "Moral Sensitivity": "Continuity",
  "Emotional-Intelligence": "Emergence",
  "Surprise": "System",
  "Structure": "Scale",
  "Tacit Knowledge": "Pacing",
  "Application": "Accumulation",
  "Invisible Work": "Inversion",
  "Measurement": "Desire",
  "Society": "Scale",
  "Translation": "Transformation",
  "Synthesis": "Catharsis",
  "Anticipation": "Interpretation",
  "Context": "Continuity",
  "Trust": "Threshold",
  "Reflection": "Resolution",
  "Multimodality": "Duality",
  "Causality": "Duality",
  "Adaptability": "Ambiguity",
  "Awareness": "Inference",
  "Collaboration": "Transformation",
  "Rhetoric": "Choice",
  "Flexibility": "Reflexivity",
  "Core_Structure": "Closure",
  "Control": "Entropy",
  "Strategy": "Authorial Strategy",
  "Audience": "Agency",
  "Analysis": "Analogy",
  "Absence": "Agency",
  "Process": "Power",
  "Delay": "Duality",
  "Risk and Benefit": "Cause and Effect",
  "Impact": "Perspective",
  "Distinction": "Disruption",
  "Logical coherence": "Inference",
  "Continuation": "Continuity",
  "Assumption": "Disruption",
  "Barrier": "Pattern",
  "Limitations": "Iteration",
  "Multi-Criteria Decision-Making": "Iteration",
  "Systems Thinking": "System",
  "Care": "Closure",
  "Style": "Scale",
  "Stability": "Duality",
  "Change": "Pacing",
  "Visual Communication": "Accumulation",
  "Escalation": "Accumulation",
  "Exploration": "Iteration",
  "Vision": "Disruption",
  "Technology": "Analogy",
  "Culture": "Closure",
  "Reframing": "Framing",
  "Authority": "Authorial Strategy",
  "Serendipity": "Reflexivity",
  "Transition": "Transformation",
  "Inquiry": "Continuity",
  "Emotional-Regulation": "Accumulation",
  "Theme": "Tone",
  "Emotional_Intelligence": "Emergence",
  "Metacognition": "Recognition",
  "Sustainability": "Duality",
  "Consequence": "Inference",
  "Relationship": "Resolution",
  "Conceptual_Tools": "Continuity",
  "Temporal_Forma": "Transformation",
  "Accountability": "Discontinuity",
  "Safety": "Scale",
  "Inclusivity": "Reflexivity",
  "Integration": "Iteration",
  "Systems": "System",
  "Disappointment": "Discontinuity",
  "Innovation": "Intention",
  "Judgment": "Agency",
  "Form": "Framing",
  "Accuracy": "Accumulation",
  "Adaptation": "Abstraction",
  "Relevance": "Inference",
  "Loss": "Focus",
  "Limitation": "Iteration",
  "Binary Thinking": "Boundary",
  "Narrative": "Perspective",
  "Value Alignment": "Cause and Effect",
  "Interpretability": "Interpretation",
  "Methodology": "Metaphor",
  "Ethics": "Choice",
  "Inclusion": "Inversion",
  "Bias": "Boundary",
  "Critical Theory": "Authorial Strategy",
  "Philosophy": "Entropy",
  "Expectation": "Repetition",
  "Integrity": "Iteration",
  "Complexity": "Reflexivity",
  "Logical Coherence": "Inference",
  "Equity": "Duality",
  "Ritual": "Duality",
  "Comparison": "Catharsis",
  "Insight": "Inversion",
  "Climax": "Conflict",
  "Turning Point": "Tension",
  "Return": "Resolution",
  "Data Justice": "Power",
  "Symbolic Practice": "Metaphor",
  "Coloniality": "Power",
  "Standards": "System",
  "Interdependence": "Cycle",
  "Affective Labor": "Desire",
  "Value Conflict": "Conflict",
  "Representation": "Interpretation",
  "Pathos in Policy": "Tone",
  "Emotional Framing": "Tone",
  "Justification": "Intention",
  "Epistemology": "Interpretation",
  "Surveillance Ethics": "Power",
  "Visual Rhetoric": "Framing",
  "Ethical Integrity": "Intention",
  "Temporality": "Scale",
  "Materiality Politics": "Boundary",
  "Narrative Framing": "Framing",
  "Linguistics": "Abstraction",
  "Independent Oversight": "Agency",
  "Burnout": "Entropy",
  "Narrative Baselines": "Pattern",
  "Compliance Psychology": "Feedback",
  "Narrative Bias": "Perspective",
  "Structural Omission": "Discontinuity",
  "Deliberative Integrity": "Closure",
  "Exclusion": "Boundary",
  "Linguistic Justice": "Interpretation",
  "Pre-Authorial Power": "Authorial Strategy",
  "Trust Breakdown": "Conflict",
  "Temporal Framing": "Framing",
  "Ecological Limits": "Boundary",
  "Justice Frameworks": "System",
  "Narrative Power": "Power",
  "Civic Co-Creation": "Agency",
  "Accessibility": "Boundary",
  "Responsibility": "Agency",
  "Reflexive Governance": "Reflexivity",
  "Ontological Framing": "Framing",
  "Epistemic Expansion": "Emergence",
  "Normativity": "Intention",
  "Value Systems": "System",
  "Future-Sensing": "Inference",
  "Visual Framing": "Framing",
  "Historical Amnesia": "Memory",
  "Temporal Erasure": "Memory",
  "Automation Ethics": "Disruption",
  "Performative Participation": "Agency",
  "Crisis": "Disruption",
  "Greenwashing": "Ambiguity",
  "Testimonial Justice": "Recognition",
  "Moral Psychology": "Intention",
  "Quantification": "Abstraction",
  "Uncertainty Ethics": "Uncertainty",
  "Sacred Ecology": "System",
  "Feasibility": "Scale",
  "Risk Ethics": "Uncertainty",
  "Data Absence": "Entropy",
  "Temporal Ethics": "Uncertainty",
  "Linguistic Framing": "Framing",
  "Relational Repair": "Repetition",
  "Adaptive Learning": "Iteration",
  "Affective Data": "Tone",
  "Emotive Feedback": "Feedback",
  "Ecological Mourning": "Catharsis",
  "Engagement": "Agency",
  "Algorithmic Bias": "Pattern",
  "Scope Colonialism": "Scale",
  "Care Knowledge": "Desire",
  "Creative Expression": "Authorial Strategy",
  "Genealogy of Impact": "Accumulation",
  "Long-Term Ethics": "Continuity",
  "Temporal Politics": "Perspective",
  "Deliberative Ethics": "Intention",
  "Burden of Proof": "Inference",
  "Foresight": "Inference",
  "Governance Architecture": "System",
  "Geo-Temporal Ethics": "Scale",
  "Institutional Memory": "Memory",
  "Ethical Benchmarks": "Hierarchy",
  "Risk Shifting": "Disruption",
  "Epistemic Pluralism": "Ambiguity",
  "Baselining Fallacy": "Pattern",
  "Bias by Default": "Perspective",
  "Attachment": "Desire",
  "Pluralism": "Ambiguity",
  "Iterative Policy": "Iteration",
  "Institutional Credibility": "Recognition",
  "Dual Role": "Duality",
  "Affective Exclusion": "Boundary",
  "Epistemic Stratification": "Hierarchy",
  "System Complexity": "System",
  "Threshold Politics": "Threshold",
  "Ontological Inversion": "Inversion",
  "Epistemic Equity": "Closure",
  "Relational Metrics": "Pattern",
  "Structural Blindness": "Discontinuity",
  "Knowledge Systems": "System",
  "Ethics of Attention": "Focus",
  "Cognitive Jurisdiction": "Boundary",
  "Sequence": "Cycle",
  "Time Horizon": "Scale",
  "Ethical Comparison": "Inference",
  "Ideological Scope": "Perspective",
  "Intangible Impacts": "Emergence",
  "Enforcement Ethics": "Power",
  "Collaborative Design": "Agency",
  "Ethical Pluralism": "Ambiguity",
  "Reconciliation": "Resolution",
  "Restorative Justice": "Closure",
  "Voice": "Agency",
  "Cultural Relativism": "Perspective",
  "Techno-Responsibility": "Power",
  "Learning Culture": "Iteration",
  "Participation": "Agency",
  "Emotional Topography": "Mood",
  "Compliance Design": "System",
  "Affective Intelligence": "Intention",
  "Ecological Normativity": "System",
  "Substitution Ethics": "Inversion",
  "Plural Screening": "Ambiguity",
  "Ethical Pedagogy": "Interpretation",
  "Boundary-Setting": "Boundary",
  "Eligibility": "Threshold",
  "Knowledge Formation": "Emergence",
  "Pre-Legibility": "Inference",
  "Democracy": "Agency",
  "Forecasting": "Inference",
  "Development": "Transformation",
  "Setup": "Threshold",
  "Interrelationships": "Cycle"
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