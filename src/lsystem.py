class LSystem:
    def __init__(self, axiom: str, rules: dict, num_gen: int) -> None:
        self.sentence = axiom
        self.rules = rules
        self.num_gen = num_gen

    def generate(self) -> str:
        if self.num_gen < 1:
            return self.sentence
        else:
            new_sentence = ""
            for s in self.sentence:
                if s in self.rules:
                    new_sentence += self.rules[s]
                else:
                    new_sentence += s
        
            self.sentence = new_sentence
            self.num_gen -= 1

            return self.generate()