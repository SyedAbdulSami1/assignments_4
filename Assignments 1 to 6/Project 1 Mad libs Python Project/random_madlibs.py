from sample_madlibs import adventure, motivation, programming, school
import random

if __name__ == "__main__":
    m = random.choice([adventure, motivation, programming, school])
    m.madlib()