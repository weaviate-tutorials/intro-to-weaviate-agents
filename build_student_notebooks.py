# This script will strip sections of cells between
# '# BEGIN_SOLUTION' & '# END_SOLUTION' and
# replace it with '# ADD YOUR CODE HERE'
# to produce student-friendly versions of Jupyter notebooks
import nbformat
import re


def remove_solution_blocks(input_file, output_file):
    with open(input_file, "r") as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.source = re.sub(
                r"# BEGIN_SOLUTION.*?# END_SOLUTION",
                "# ADD YOUR CODE HERE",
                cell.source,
                flags=re.DOTALL,
            )

    with open(output_file, "w") as f:
        nbformat.write(nb, f)


filename_pairs = [
    ("wv-query-agent-finished.ipynb", "wv-query-agent.ipynb")
]

for fname_pair in filename_pairs:
    remove_solution_blocks(*fname_pair)
