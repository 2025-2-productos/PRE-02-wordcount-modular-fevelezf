# obtain a list of files in the input directory
import os

from homework.src._internals.write_count_words import write_count_words


def main():
    ### read all lines
    # all_lines = read_all_lines()
    all_lines = []
    input_files_list = os.listdir("data/input/")

    for filename in input_files_list:
        file_path = os.path.join("data/input/", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    ### preprocess lines
    all_lines = [line.strip().lower() for line in all_lines]

    ### split in words
    words = []
    for line in all_lines:
        words.extend(words.strip(", .!?") for words in line.split())
    ### count words
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    ### write count words
    write_count_words(counter)


if __name__ == "__main__":
    main()
