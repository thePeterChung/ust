# Universal Structure Toolkit (UST)

*A generative framework for critical thinking, reasoning and writing built for the age of AI enhanced learning.*

Version: 0.1.0 | License: [CC BY-NC-SA 4.0](/LICENSE.md) | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16898898.svg)](https://doi.org/10.5281/zenodo.16898898)

## Overview

The Universal Structure Toolkit (UST) is a cross disciplinary framework for teaching **structured reasoning, critical thinking and communication** through **film based narrative principles** and **discipline specific structures**.  


---

## 📂 Repository Structure

ust/
    ├── build/         # Obsidian ready and mm format 
    ├── docs/          # White paper & supporting docs
    ├── guides/        # Workflow guides
    ├── src/           # Stage 1–4: scripts, prompts, mm, json
    ├── CITATION.cff
    ├── INSTALL.md
    ├── LICENSE.md
    └── README.md   


---

## Mission

UST transforms learning into **structured inquiry**, where narrative design and disciplinary logic cultivate **creative, critical and AI empowered thinking**. Writing becomes a reflection of thought, not the starting point.  


---

## Why UST?

Traditional writing instruction often emphasizes form over thought, leaving learners unprepared to **analyze, synthesize and reason across contexts**. UST bridges this gap with an **intuitive generative toolkit** that empowers learners to:

- Think critically and adaptively **before writing**.  
- Apply structured reasoning across academic, creative and professional domains.  
- Reframe prompts as **thinking scaffolds** to explore any material or scenario.  
- Integrate AI responsibly to enhance understanding, insight and exploration. 


---

## What It Contains

- **34 structures**: 12 narrative frameworks from film storytelling and 22 discipline specific structures across major academic and professional fields.  
- **4 learning levels**: Beginner, Intermediate, Advanced and Meta/Expert.  
- **1000+ structured concept tagged prompts** designed for reasoning and critical thinking.  
- **Concept based tags** to scaffold thought processes (e.g., Intention, Agency, Focus and Metaphor).  
- **Obsidian ready and Freeplane compatible formats.**  


---

## Who It’s For

- Educators and curriculum designers fostering **critical thinking and structured reasoning**.  
- Students developing **adaptive reasoning, analysis and learning skills**.  
- Writers, researchers and innovators seeking **structured frameworks for thought**.  
- AI developers building tools for **generative reasoning, problem solving and thinking scaffolds**.   


---

## Key Features

- Prompts act as **flexible stems** to analyze, synthesize and reason across **any context**.  
- Supports **thinking first workflows** with writing as a tool to articulate insight.  
- Encourages **transferable reasoning skills** bridging disciplinary silos.  


---

## This Archive Contains

- **[Compiled Vaults](/build/zip)** fully ready for Obsidian  
- **[Full Generation Pipeline (Stages 1–4)](/src)** — scripts and source files to regenerate the release from original `.mm` mind maps. Users may start from Stage 1 for full reproducibility or skip directly to the compiled vaults for immediate use.  


---

## 📄 White Paper

For full methodology, theoretical framework and design principles, see the [White Paper](/docs/white-paper.md).


---

## ⚙️ Installation & Usage

See [INSTALL.md](/INSTALL.md) for setup instructions and workflow.


---

## ⚙️ UST Pipeline Overview

The UST workflow is organized in four stages for clarity and scalability:

1. **[Stage 1](/src/stage1-generation) – Mind Map Generation**  
   Create `.mm` files representing 34 structures and question sets using [Freeplane](https://freeplane.org). Full regeneration takes ~10 hours (AI generation + curation), but most users can skip directly to the compiled vaults.

2. **[Stage 2](/src/stage2-concept-clean) – Cleaning (Optional)**  
   Concept tags from AI generation are mapped to the closest concept in the [concept list](/docs/concept_list.xlsx). Output: clean versions of `.mm` files (~1 hour processing).

3. **[Stage 3](/src/stage3-mm-to-json) – JSON Conversion**  
   Convert mind maps to JSON ready for markdown automation.

4. **[Stage 4](/src/stage4-json-to-markdown) – Obsidian Markdown Integration**  
   Generate linked Markdown notes for use in [Obsidian](https://obsidian.md) (~5 minutes automated).


---

## UST Graph View

### Clean vs Raw

| Clean Graph | Raw Graph |
|-------------|-----------|
| ![Clean Graph](/docs/screenshots/graph-clean.png) | ![Raw Graph](/docs/screenshots/graph-raw.png) |

*The Clean Graph shows the polished curated structures ready for reasoning and critical thinking, while the Raw Graph shows the original AI generated output.* 


---

## 🚀 Quick Start

Follow these steps to begin exploring UST immediately:

1. **Download the [Compiled Vault](/build/zip) or [`.mm` Files](/build/mm)**  

   - For beginners, the `.mm` Freeplane files can be used directly to explore structures and **thinking pathways** without concern for tags or Obsidian integration.  
   - For immediate use with full linking and tagging, download the compiled vault.  
   - Extract the folder to your preferred location.  

2. **Open in Obsidian (Optional)**  

   - Launch [Obsidian](https://obsidian.md).  
   - Open the compiled vault folder as a new vault to take advantage of linked notes, **graph view for reasoning connections** and concept tags.  
   - Beginners can skip this step and explore the [`.mm` Files](/build/mm) directly in Freeplane.  

3. **Explore Structures and Questions**  

   - Navigate through the 34 structures.  
   - Click on individual nodes (in Freeplane) or Markdown notes (in Obsidian) to see **scaffolded reasoning questions**.  

4. **Visualize Relationships**  

   - In Obsidian, use graph view to see connections between **questions, concepts and reasoning pathways**.  
   - In Freeplane, view the structure tree directly to understand **sequence, hierarchy and inquiry flow**.  

5. **Optional: [Regenerate UST from Source](/src)**  

   - For advanced users, follow **Stages 1–4** in the pipeline to regenerate the entire toolkit from `.mm` mind maps.  
   - This allows full reproducibility and experimentation with **modified structures or thinking scaffolds**.  

**Tip:** Beginners can start with a single structure in Freeplane to get familiar with the approach before moving on to Obsidian or advanced workflows.  


---

## License

[CC BY-NC-SA 4.0](/LICENSE.md)

[Universal Structure Toolkit (UST) v0.1.0](https://github.com/thePeterChung/ust) © 2025 by [L. M. Peter Chung](https://www.linkedin.com/in/thepeterchung) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)  
![cc](https://mirrors.creativecommons.org/presskit/icons/cc.svg) ![by](https://mirrors.creativecommons.org/presskit/icons/by.svg) ![nc](https://mirrors.creativecommons.org/presskit/icons/nc.svg) ![sa](https://mirrors.creativecommons.org/presskit/icons/sa.svg)


---

## Citation

If you use the Universal Structure Toolkit (UST) in your research, please cite:

**Chung, L. M. P. (2025). UST: This One Framework Could Change How We Think Forever (0.1.0) [Data set]. Zenodo.**  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16898898.svg)](https://doi.org/10.5281/zenodo.16898898)


---

**BibTeX:**

```
bibtex
@misc{chung2025ust,
  author       = {Chung, L. M. P.},
  title        = {UST: This One Framework Could Change How We Think Forever (0.1.0) [Data set]},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.16898898},
  url          = {https://doi.org/10.5281/zenodo.16898898},
  note         = {Available at https://github.com/thePeterChung/ust}
}
```


---

## 🔗 Additional Resources

- [guides](/guides)
- [build](/build)


---

## Contact

To provide feedback, suggest contributions or explore partnerships:  
📧 peter@essayos.com  
🌐 https:www.linkedin.com/in/thepeterchung

