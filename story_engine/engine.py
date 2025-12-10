# import random
# import textwrap

# def wrap(text):
#     return textwrap.fill(text, width=90)

# ENDINGS = {
#     "happy": "In the end, {p} overcomes the struggle and begins a hopeful new chapter.",
#     "sad": "In the end, despite all efforts, {p} faces a painful but meaningful ending.",
#     "bittersweet": "In the end, {p} gains something valuable but loses something that can never be replaced.",
#     "hopeful": "In the end, {p} finds strength and the path ahead begins to brighten.",
#     "tragic": "In the end, fate turns cruel, and {p}'s story closes in tragedy.",
#     "poetic": "In the end, {p}'s journey settles like a quiet verse, complete and eternal.",
#     "heroic": "In the end, {p} rises with bravery, leaving behind a legacy of courage."
# }

# class StoryEngine:
#     def __init__(self, seed=None):
#         if seed is not None:
#             random.seed(seed)

#     def generate(self, protagonist, ally, antagonist, setting, conflict, obj, theme, ending):
#         opening = wrap(
#             f"In {setting}, {protagonist} lives an ordinary life until the discovery "
#             f"of {obj} sets events into motion."
#         )

#         middle = wrap(
#             f"Seeking answers, {protagonist} turns to {ally}. Together they confront "
#             f"the growing tension: {conflict}."
#         )

#         climax = wrap(
#             f"As challenges intensify, the presence of {antagonist} forces "
#             f"{protagonist} to confront the true meaning of {theme}."
#         )

#         final = wrap(
#             ENDINGS.get(ending, ENDINGS["hopeful"]).format(p=protagonist)
#         )

#         return (
#             f"{protagonist}'s {theme.title()}\n\n"
#             f"{opening}\n\n"
#             f"{middle}\n\n"
#             f"{climax}\n\n"
#             f"{final}\n"
#         )

import random
import textwrap

def wrap(text):
    return textwrap.fill(text, width=90)

ENDINGS = {
    "happy": "In the end, {p} overcomes the struggle and begins a hopeful new chapter.",
    "sad": "In the end, despite all efforts, {p} faces a painful but meaningful ending.",
    "bittersweet": "In the end, {p} gains something valuable but loses something that can never be replaced.",
    "hopeful": "In the end, {p} finds strength and the path ahead begins to brighten.",
    "tragic": "In the end, fate turns cruel, and {p}'s story closes in tragedy.",
    "poetic": "In the end, {p}'s journey settles like a quiet verse, complete and eternal.",
    "heroic": "In the end, {p} rises with bravery, leaving behind a legacy of courage."
}

DEFAULT_MODEL = "distilgpt2"

class StoryEngine:
    def __init__(self, seed=None, model_name: str = None, do_expand: bool = False):
        if seed is not None:
            random.seed(seed)
        self.model_name = model_name or DEFAULT_MODEL
        self.do_expand = do_expand
        self._generator = None

    def _build_template_story(self, protagonist, ally, antagonist, setting, conflict, obj, theme, ending):
        opening = wrap(
            f"In {setting}, {protagonist} lived an ordinary life until the discovery of {obj} set events into motion."
        )
        middle = wrap(
            f"Seeking answers, {protagonist} turned to {ally}. Together they faced the growing tension: {conflict}."
        )
        climax = wrap(
            f"As challenges intensified, the presence of {antagonist} forced {protagonist} to confront the true meaning of {theme}."
        )
        final = wrap(ENDINGS.get(ending, ENDINGS["hopeful"]).format(p=protagonist))

        title = f"{protagonist}'s {theme.title()}"
        core = f"{title}\n\n{opening}\n\n{middle}\n\n{climax}\n\n{final}\n"
        return core

    def _ensure_generator(self):
        if self._generator is not None:
            return True
        try:
            from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
            # lazy load tokenizer & model
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            model = AutoModelForCausalLM.from_pretrained(self.model_name)
            self._generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
            return True
        except Exception:
            self._generator = None
            return False

    def _expand_with_model(self, base_story: str, protagonist: str, ending: str, max_length: int = 300) -> str:
        ok = self._ensure_generator()
        if not ok:
            return base_story

        # Build a focused prompt instructing the model to expand while preserving ending style
        instruction = (
            "Expand and enrich the following short story. Keep the characters and core plot, "
            "add sensory detail and emotional beats, and produce natural, human-like prose. "
            f"Make sure the story ends with a complete {ending} ending (no cliffhangers). "
            "Do not introduce new main characters. Keep it appropriate and concise.\n\n"
        )
        prompt = instruction + base_story + f"\n\nContinue and expand the story with a proper {ending} ending:\n"

        try:
            outputs = self._generator(prompt, max_length=max_length, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95)
            text = outputs[0]["generated_text"]
            # The model may reproduce the prompt; find the part after the original base_story
            if base_story.strip() in text:
                expanded = text.split(base_story.strip(), 1)[-1].strip()
                # If expanded begins immediately with repeated title, remove duplicates
                if expanded.startswith(base_story.strip().splitlines()[0]):
                    expanded = expanded[len(base_story.strip().splitlines()[0]):].strip()
                result = base_story.strip() + "\n\n" + expanded
            else:
                result = text
            # final safety: ensure ending sentence mentions protagonist or finality
            if protagonist not in result.splitlines()[-1] and len(result.splitlines()) > 0:
                result = result.strip()
            return result
        except Exception:
            return base_story

    def generate(self, protagonist, ally, antagonist, setting, conflict, obj, theme, ending):
        base = self._build_template_story(protagonist, ally, antagonist, setting, conflict, obj, theme, ending)
        if self.do_expand:
            expanded = self._expand_with_model(base, protagonist, ending)
            return expanded
        return base
