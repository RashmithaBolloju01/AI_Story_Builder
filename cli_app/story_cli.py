# from story_engine.engine import StoryEngine

# engine = StoryEngine()

# p = input("Protagonist name: ")
# ally = input("Supporting character: ")
# ant = input("Antagonist: ")
# setting = input("Story setting: ")
# conflict = input("Main conflict: ")
# obj = input("Important object: ")
# theme = input("Story theme: ")
# ending = input("Ending type (happy, sad, bittersweet, hopeful, tragic, poetic, heroic): ").lower()

# story = engine.generate(p, ally, ant, setting, conflict, obj, theme, ending)

# print("\n" + story)

import argparse
from story_engine.engine import StoryEngine

def main():
    parser = argparse.ArgumentParser(description="AI Story Builder - Hybrid Mode")
    parser.add_argument("--model", type=str, help="Transformer model name (optional)", default=None)
    parser.add_argument("--expand", action="store_true", help="Enable model-based expansion")
    args = parser.parse_args()

    p = input("Protagonist name: ").strip()
    ally = input("Supporting character: ").strip() or "a companion"
    ant = input("Antagonist: ").strip() or "an opposing force"
    setting = input("Story setting: ").strip()
    conflict = input("Main conflict: ").strip()
    obj = input("Important object: ").strip()
    theme = input("Story theme: ").strip() or "life"
    ending = input("Ending type (happy, sad, bittersweet, hopeful, tragic, poetic, heroic): ").strip().lower()

    engine = StoryEngine(model_name=args.model, do_expand=args.expand)
    story = engine.generate(p, ally, ant, setting, conflict, obj, theme, ending)
    print("\n" + story + "\n")

if __name__ == "__main__":
    main()
