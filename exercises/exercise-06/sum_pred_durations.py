from batch import get_output_path, read_data
import sys


def main(year, month):

    output_file = get_output_path(year, month)
    df = read_data(output_file)

    print(sum(df["predicted_duration"]))
    return


if __name__ == "__main__":
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    main(year, month)
