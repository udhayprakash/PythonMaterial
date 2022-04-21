from subprocess import check_output


def print_contents_of_cwd():
    return check_output(['ls']).split()
