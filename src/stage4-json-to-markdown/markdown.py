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

